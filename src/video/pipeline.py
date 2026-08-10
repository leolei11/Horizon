"""Build a deterministic Remotion manifest and optional landscape MP4."""

from __future__ import annotations

import asyncio
import html
import json
import logging
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import urlsplit

import edge_tts

from .._file_utils import _atomic_write_text
from ..models import ContentBlock, ContentItem, VideoConfig


logger = logging.getLogger(__name__)

_SENTENCE_SPLIT = re.compile(r"(?<=[。！？!?；;])\s*")
_MARKDOWN = re.compile(r"[`*_>#\[\]]")
_WHITESPACE = re.compile(r"\s+")
_CJK = r"[\u3400-\u4dbf\u4e00-\u9fff]"
_ASCII = r"[A-Za-z0-9]"


@dataclass(frozen=True)
class VideoBuildResult:
    """Paths and degradations produced by one video build."""

    manifest_path: Path
    output_path: Path | None
    selected_count: int
    warnings: list[str] = field(default_factory=list)


class HorizonVideoPipeline:
    """Create a short, story-driven video without depending on an editor app."""

    def __init__(
        self,
        config: VideoConfig,
        *,
        project_root: Path | None = None,
    ):
        self.config = config
        self.project_root = (project_root or Path.cwd()).resolve()
        self.renderer_dir = (self.project_root / config.renderer_dir).resolve()
        self.output_dir = (self.project_root / config.output_dir).resolve()

    @staticmethod
    def _analysis(item: ContentItem):
        return item.processing.analysis if item.processing else None

    def select_items(self, items: Iterable[ContentItem]) -> list[ContentItem]:
        """Select the small video edition by visual/story utility."""
        eligible = []
        for item in items:
            analysis = self._analysis(item)
            if (
                analysis is None
                or analysis.rejection_reason
                or analysis.video_score is None
                or analysis.video_score < self.config.min_video_score
            ):
                continue
            eligible.append(item)

        eligible.sort(
            key=lambda item: (
                self._analysis(item).video_score or 0.0,
                self._analysis(item).relevance_score or 0.0,
                self._analysis(item).actionability_score or 0.0,
                self._analysis(item).score or 0.0,
            ),
            reverse=True,
        )
        return eligible[: self.config.max_items]

    @staticmethod
    def _clean_text(value: str) -> str:
        value = html.unescape(value)
        value = re.sub(r"<[^>]+>", " ", value)
        value = _MARKDOWN.sub("", value)
        value = _WHITESPACE.sub(" ", value).strip()
        value = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", value)
        return re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", value)

    @classmethod
    def _sentences(cls, value: str, *, limit: int = 3) -> list[str]:
        cleaned = cls._clean_text(value)
        if not cleaned:
            return []
        sentences = [part.strip() for part in _SENTENCE_SPLIT.split(cleaned)]
        return [sentence for sentence in sentences if sentence][:limit]

    @staticmethod
    def _block(
        item: ContentItem,
        language: str,
        block_ids: tuple[str, ...],
    ) -> ContentBlock | None:
        artifact = item.processing.artifacts.get(language) if item.processing else None
        if artifact is None:
            return None
        return next((block for block in artifact.blocks if block.id in block_ids), None)

    @classmethod
    def _story_copy(
        cls,
        item: ContentItem,
        language: str,
    ) -> tuple[str, list[str], str, str]:
        artifact = item.processing.artifacts.get(language) if item.processing else None
        analysis = cls._analysis(item)
        title = cls._clean_text(artifact.title if artifact else item.title)

        primary = None
        if artifact:
            primary = next((block for block in artifact.blocks if block.primary), None)
        primary = primary or cls._block(
            item,
            language,
            ("summary", "solution", "background"),
        )
        primary_text = primary.content if primary else (analysis.summary if analysis else "")
        captions = cls._sentences(primary_text)

        action_block = cls._block(item, language, ("next_step",))
        action_label = "NEXT MOVE"
        if action_block is None:
            action_block = cls._block(item, language, ("takeaway",))
            action_label = "TAKEAWAY"
        if action_block is None:
            action_block = cls._block(item, language, ("impact",))
            action_label = "WHY IT MATTERS"
        action = cls._clean_text(action_block.content) if action_block else ""
        return title, captions, action, action_label

    @staticmethod
    def _source_label(item: ContentItem) -> str:
        feed_name = item.metadata.get("feed_name")
        if isinstance(feed_name, str) and feed_name.strip():
            return feed_name.strip()
        if item.author:
            return item.author
        return urlsplit(str(item.url)).hostname or item.source_type.value

    async def _synthesize(self, narration: str, output_path: Path) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        await edge_tts.Communicate(narration, self.config.voice).save(str(output_path))

    @staticmethod
    async def _audio_duration(path: Path) -> float:
        process = await asyncio.create_subprocess_exec(
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            raise RuntimeError(stderr.decode("utf-8", errors="replace").strip())
        return float(stdout.decode().strip())

    async def prepare_manifest(
        self,
        items: Iterable[ContentItem],
        *,
        date: str,
        language: str = "zh",
        synthesize_audio: bool = True,
        bucket_names: dict[str, str] | None = None,
    ) -> VideoBuildResult:
        """Write a self-contained render manifest and narration assets."""
        localized_items = [
            item
            for item in items
            if item.processing and language in item.processing.artifacts
        ]
        selected = self.select_items(localized_items)
        if not selected:
            raise ValueError(
                "No localized items met video.min_video_score; "
                "the video edition was withheld instead of mixing languages"
            )

        bucket_names = bucket_names or {}
        manifest_dir = self.output_dir / "manifests"
        public_run_dir = self.renderer_dir / "public" / "generated" / f"{date}-{language}"
        manifest_dir.mkdir(parents=True, exist_ok=True)
        public_run_dir.mkdir(parents=True, exist_ok=True)

        intro_frames = round(self.config.fps * 1.5)
        outro_frames = round(self.config.fps * 1.2)
        cursor = intro_frames
        stories = []
        warnings: list[str] = []

        for index, item in enumerate(selected, start=1):
            analysis = self._analysis(item)
            title, captions, action, action_label = self._story_copy(item, language)
            if not captions:
                captions = [title]

            narration_parts = [f"第{index}条，{title}。", *captions]
            if action and action not in captions:
                narration_parts.append(action)
            narration = "".join(narration_parts)

            audio_src = None
            estimated_seconds = max(7.0, len(narration) / 4.2)
            audio_path = public_run_dir / f"story-{index:02d}.mp3"
            if synthesize_audio:
                try:
                    await self._synthesize(narration, audio_path)
                    estimated_seconds = await self._audio_duration(audio_path)
                    audio_src = f"generated/{date}-{language}/{audio_path.name}"
                except Exception as exc:
                    warning = f"Story {index} narration unavailable: {exc}"
                    warnings.append(warning)
                    logger.warning(warning)

            duration_frames = max(
                round(self.config.fps * 7),
                math.ceil((estimated_seconds + 0.7) * self.config.fps),
            )
            bucket_id = analysis.interest_bucket or "signal"
            stories.append(
                {
                    "id": item.id,
                    "index": index,
                    "title": title,
                    "captions": captions,
                    "action": action,
                    "actionLabel": action_label,
                    "source": self._source_label(item),
                    "url": str(item.url),
                    "bucket": bucket_names.get(bucket_id, bucket_id),
                    "videoScore": analysis.video_score,
                    "relevanceScore": analysis.relevance_score,
                    "audioSrc": audio_src,
                    "startFrame": cursor,
                    "durationFrames": duration_frames,
                }
            )
            cursor += duration_frames

        manifest = {
            "title": "HORIZON / DAILY SIGNAL",
            "date": date,
            "language": language,
            "width": self.config.width,
            "height": self.config.height,
            "fps": self.config.fps,
            "introFrames": intro_frames,
            "outroFrames": outro_frames,
            "totalFrames": cursor + outro_frames,
            "stories": stories,
        }
        manifest_path = manifest_dir / f"horizon-{date}-{language}.json"
        _atomic_write_text(
            manifest_path,
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        )
        return VideoBuildResult(
            manifest_path=manifest_path,
            output_path=None,
            selected_count=len(stories),
            warnings=warnings,
        )

    async def render_manifest(
        self,
        manifest_path: Path,
        *,
        output_path: Path | None = None,
    ) -> Path:
        """Render one manifest with the pinned Remotion project."""
        render_script = self.renderer_dir / "render.mjs"
        if not render_script.exists():
            raise FileNotFoundError(f"Remotion renderer not found: {render_script}")
        if not (self.renderer_dir / "node_modules" / "remotion").exists():
            raise RuntimeError(
                f"Video dependencies are not installed; run npm install in {self.renderer_dir}"
            )

        destination = output_path or (
            self.output_dir / "renders" / f"{manifest_path.stem}.mp4"
        )
        destination.parent.mkdir(parents=True, exist_ok=True)
        process = await asyncio.create_subprocess_exec(
            "node",
            str(render_script),
            str(manifest_path.resolve()),
            str(destination.resolve()),
            cwd=str(self.renderer_dir),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )
        stdout, _ = await process.communicate()
        output = stdout.decode("utf-8", errors="replace")
        if process.returncode != 0:
            raise RuntimeError(f"Remotion render failed:\n{output[-4000:]}")
        if not destination.exists() or destination.stat().st_size == 0:
            raise RuntimeError("Remotion completed without a usable MP4")
        logger.info("Rendered Horizon video: %s", destination)
        return destination

    async def build_daily_video(
        self,
        items: Iterable[ContentItem],
        *,
        date: str,
        language: str = "zh",
        bucket_names: dict[str, str] | None = None,
    ) -> VideoBuildResult:
        """Prepare the video edition and render it when auto_render is enabled."""
        prepared = await self.prepare_manifest(
            items,
            date=date,
            language=language,
            bucket_names=bucket_names,
        )
        if not self.config.auto_render:
            return prepared
        output_path = await self.render_manifest(prepared.manifest_path)
        return VideoBuildResult(
            manifest_path=prepared.manifest_path,
            output_path=output_path,
            selected_count=prepared.selected_count,
            warnings=prepared.warnings,
        )
