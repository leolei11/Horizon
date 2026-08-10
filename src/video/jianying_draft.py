"""Automated Jianying (CapCut) Draft Exporter for Horizon Daily Digest.

Architected as a Senior Video Editor and Software Architect pipeline to generate
production-ready Jianying Pro draft projects with multi-track audio, dynamic subtitles,
official brand logos, and stock video background clips.
"""

import os
import re
import json
import shutil
import asyncio
import logging
import hashlib
from pathlib import Path
from typing import List, Dict, Optional
import httpx
import edge_tts
from dotenv import load_dotenv

from pyJianYingDraft import (
    ScriptFile,
    DraftFolder,
    TextSegment,
    TextStyle,
    TextShadow,
    TextBorder,
    TextBackground,
    VideoSegment,
    AudioSegment,
    VideoMaterial,
    AudioMaterial,
    TrackSpec,
    TrackType,
    trange,
    SEC,
)

load_dotenv()
logger = logging.getLogger(__name__)

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")
DEFAULT_VOICE = "zh-CN-YunxiNeural"
DEFAULT_JIANYING_DIR = os.path.expanduser("~/Movies/JianyingPro/User Data/Projects/com.lveditor.draft/")


class JianyingDraftGenerator:
    """Automated Jianying (CapCut) project draft builder."""

    def __init__(
        self,
        jianying_draft_dir: str | None = None,
        voice: str = DEFAULT_VOICE,
        pexels_key: str | None = None,
    ):
        self.draft_base_dir = jianying_draft_dir or DEFAULT_JIANYING_DIR
        self.output_dir = Path("data/videos")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir = self.output_dir / "temp"
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.voice = voice
        self.pexels_key = pexels_key or PEXELS_API_KEY
        self.draft_folder = DraftFolder(self.draft_base_dir)

    async def fetch_background_video(self, query: str) -> Path | None:
        """Fetch stock background video clip from Pexels API."""
        if not self.pexels_key:
            return None

        headers = {"Authorization": self.pexels_key}
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=3&orientation=landscape"

        q_hash = hashlib.md5(query.encode()).hexdigest()[:8]
        out_file = self.temp_dir / f"bg_{q_hash}.mp4"
        if out_file.exists() and out_file.stat().st_size > 100000:
            return out_file

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                res = await client.get(url, headers=headers)
                if res.status_code == 200:
                    videos = res.json().get("videos", [])
                    if videos:
                        vfiles = videos[0].get("video_files", [])
                        hd_files = [f for f in vfiles if f.get("width", 0) >= 1280] or vfiles
                        if hd_files:
                            v_url = hd_files[0]["link"]
                            v_res = await client.get(v_url, follow_redirects=True)
                            if v_res.status_code == 200:
                                with open(out_file, "wb") as f:
                                    f.write(v_res.content)
                                return out_file
        except Exception as e:
            logger.warning("Could not fetch background video for '%s': %s", query, e)
        return None

    async def fetch_brand_logo(self, title: str, url: str) -> Path | None:
        """Fetch official brand logo or GitHub organization avatar."""
        out_hash = hashlib.md5((title + url).encode()).hexdigest()[:8]
        out_file = self.temp_dir / f"logo_{out_hash}.png"

        if out_file.exists() and out_file.stat().st_size > 1000:
            return out_file

        logo_url = None
        gh_match = re.search(r"github\.com/([^/]+)", url)
        if not gh_match:
            gh_match = re.search(r"github\.com/([^/]+)", title, re.IGNORECASE)

        if gh_match:
            owner = gh_match.group(1)
            if owner.lower() not in ["trending", "topics", "features"]:
                logo_url = f"https://github.com/{owner}.png"

        if not logo_url:
            domain = None
            t_lower = (title + " " + url).lower()
            if "nvidia" in t_lower:
                domain = "nvidia.com"
            elif "openai" in t_lower:
                domain = "openai.com"
            elif "microsoft" in t_lower:
                domain = "microsoft.com"
            elif "google" in t_lower:
                domain = "google.com"
            elif "meta" in t_lower or "facebook" in t_lower:
                domain = "meta.com"
            elif "huggingface" in t_lower or "hugging face" in t_lower:
                domain = "huggingface.co"
            elif "anthropic" in t_lower or "claude" in t_lower:
                domain = "anthropic.com"
            elif "apple" in t_lower:
                domain = "apple.com"
            elif "amd" in t_lower:
                domain = "amd.com"
            elif "reddit" in t_lower:
                domain = "reddit.com"
            else:
                d_match = re.search(r"https?://(?:www\.)?([^/]+)", url)
                if d_match:
                    domain = d_match.group(1)

            if domain:
                logo_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=256"

        if logo_url:
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    res = await client.get(logo_url, follow_redirects=True)
                    if res.status_code == 200 and len(res.content) > 300:
                        with open(out_file, "wb") as f:
                            f.write(res.content)
                        return out_file
            except Exception as e:
                logger.warning("Failed to fetch brand logo from %s: %s", logo_url, e)

        return None

    async def generate_speech(self, text: str, output_path: Path) -> Path:
        """Synthesize TTS audio using Edge-TTS."""
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(str(output_path))
        return output_path

    @staticmethod
    def _strip_date_strings(text: str) -> str:
        """Strip all date and time patterns from text."""
        text = re.sub(r"\d{1,4}年\d{1,2}月\d{1,2}日(\s+\d{1,2}:\d{2})?", "", text)
        text = re.sub(r"\d{1,2}月\d{1,2}日(\s+\d{1,2}:\d{2})?", "", text)
        text = re.sub(r"\d{4}-\d{2}-\d{2}", "", text)
        text = re.sub(r"\b\d{1,2}:\d{2}\b", "", text)
        text = re.sub(r"telegram\s*·\s*\w+\s*·?", "", text, flags=re.IGNORECASE)
        text = re.sub(r"rss\s*·\s*[\w\s\(\)]+·?", "", text, flags=re.IGNORECASE)
        text = re.sub(r"hackernews\s*·\s*\w+\s*·?", "", text, flags=re.IGNORECASE)
        text = re.sub(r"reddit\s*·\s*[\w\/]+\s*·?", "", text, flags=re.IGNORECASE)
        text = re.sub(r"·\s*·", "·", text)
        return text.strip()

    @staticmethod
    def _parse_summary_items(md_content: str, max_items: int = 5) -> List[Dict[str, str]]:
        """Parse top items from summary markdown with clean dry-goods explanations."""
        items = []
        pattern = r"###\s+\[(.*?)\]\((.*?)\)(?:.*?)\n\n(.*?)(?=\n---|$$)"
        matches = re.findall(pattern, md_content, re.DOTALL)

        for title, url, text_block in matches[:max_items]:
            clean_title = JianyingDraftGenerator._strip_date_strings(title)
            clean_text = re.sub(r"\*\*「.*?」\*\*", "", text_block)
            clean_text = re.sub(r"\[.*?\]\(.*?\)", "", clean_text)
            clean_text = re.sub(r"\*\*标签\*\*.*", "", clean_text)
            clean_text = re.sub(r"<details>.*?</details>", "", clean_text, flags=re.DOTALL)
            clean_text = JianyingDraftGenerator._strip_date_strings(clean_text)
            clean_text = clean_text.strip()

            sentences = [s.strip() for s in re.split(r"[。！!？?]", clean_text) if s.strip()]
            voiceover = "。".join(sentences[:4]) + "。" if sentences else clean_title

            items.append({
                "title": clean_title,
                "url": url.strip(),
                "voiceover": voiceover,
                "sentences": sentences[:4],
                "text": clean_text[:400],
            })
        return items

    @staticmethod
    def _get_audio_duration_us(audio_path: Path) -> int:
        """Estimate audio duration in microseconds (us)."""
        try:
            import subprocess
            cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            dur_sec = float(res.stdout.strip())
            return int(dur_sec * 1_000_000)
        except Exception:
            # Fallback estimation based on mp3 size (~16KB per sec)
            st_size = audio_path.stat().st_size
            sec = max(3.0, st_size / 16000.0)
            return int(sec * 1_000_000)

    async def build_draft_project(self, summary_md_path: Path, draft_name: str = "HORIZON_AI_DIGEST") -> str:
        """Build full Jianying Pro draft project with multi-track alignment."""
        if not summary_md_path.exists():
            raise FileNotFoundError(f"Summary markdown not found: {summary_md_path}")

        with open(summary_md_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        items = self._parse_summary_items(md_content, max_items=5)
        if not items:
            raise ValueError(f"No parseable summary items in {summary_md_path}")

        # Initialize Jianying ScriptFile (1920x1080 16:9 30fps)
        script = self.draft_folder.create_draft(draft_name, 1920, 1080, fps=30, allow_replace=True)
        script.content["platform"] = {"app_id": 3704, "app_source": "mac", "app_version": "6.0.0", "os": "mac"}
        script.content["last_modified_platform"] = {"app_id": 3704, "app_source": "mac", "app_version": "6.0.0", "os": "mac"}

        # Append multi-tracks with distinct track names
        track_bg_video = script.append_track(TrackSpec(TrackType.video, name="bg_video"))
        track_logo = script.append_track(TrackSpec(TrackType.video, name="logo"))
        track_audio = script.append_track(TrackSpec(TrackType.audio, name="audio"))
        track_title = script.append_track(TrackSpec(TrackType.text, name="title"))
        track_subtitle = script.append_track(TrackSpec(TrackType.text, name="subtitle"))

        current_time_us = 0

        for idx, item in enumerate(items, start=1):
            logger.info("Building draft scene %d/%d: %s", idx, len(items), item["title"])

            # 1. Audio Generation
            audio_path = self.temp_dir / f"jy_audio_{idx}.mp3"
            full_text = f"第{idx}条。{item['title']}。{item['voiceover']}"
            await self.generate_speech(full_text, audio_path)
            duration_us = self._get_audio_duration_us(audio_path)

            time_range = trange(current_time_us, duration_us)

            # 2. Add Audio Segment to Audio Track
            audio_mat = AudioMaterial(str(audio_path.resolve()))
            audio_seg = AudioSegment(audio_mat, time_range)
            script.add_segment(audio_seg, track_audio)

            # 3. Background Stock Video Segment
            bg_query = "technology AI code"
            t_lower = item["title"].lower()
            if "python" in t_lower or "code" in t_lower:
                bg_query = "programming code computer"
            elif "chip" in t_lower or "amd" in t_lower or "nvidia" in t_lower:
                bg_query = "semiconductor microchip"
            elif "model" in t_lower or "robot" in t_lower:
                bg_query = "artificial intelligence robot"

            bg_video_path = await self.fetch_background_video(bg_query)
            if bg_video_path and bg_video_path.exists():
                v_mat = VideoMaterial(str(bg_video_path.resolve()))
                bg_dur = min(v_mat.duration, duration_us)
                v_seg = VideoSegment(v_mat, trange(current_time_us, bg_dur), source_timerange=trange(0, bg_dur))
                script.add_segment(v_seg, track_bg_video)

            # 4. Brand / GitHub Logo Segment
            logo_path = await self.fetch_brand_logo(item["title"], item["url"])
            if logo_path and logo_path.exists():
                l_mat = VideoMaterial(str(logo_path.resolve()))
                l_seg = VideoSegment(l_mat, time_range, source_timerange=trange(0, duration_us))
                script.add_segment(l_seg, track_logo)

            # 5. Title Text Segment (High Impact Gold/White Style)
            title_text = f"【第{idx}条】{item['title']}"
            title_seg = TextSegment(
                title_text,
                time_range,
                style=TextStyle(color=(1.0, 0.84, 0.0), size=14.0),
                shadow=TextShadow(color=(0.0, 0.0, 0.0), alpha=0.8, distance=4.0),
                background=TextBackground(color="#0f172a", alpha=0.85, round_radius=0.2)
            )
            script.add_segment(title_seg, track_title)

            # 6. Subtitle Sentence Segments (Split for readability)
            sentences = item.get("sentences", [item["voiceover"]])
            sub_dur_us = duration_us // max(1, len(sentences))
            sub_time_us = current_time_us

            for sent in sentences:
                sent_range = trange(sub_time_us, sub_dur_us)
                sub_seg = TextSegment(
                    sent,
                    sent_range,
                    style=TextStyle(color=(1.0, 1.0, 1.0), size=10.0),
                    border=TextBorder(color="#000000", width=2.0),
                    shadow=TextShadow(color=(0.0, 0.0, 0.0), alpha=0.6, distance=3.0)
                )
                script.add_segment(sub_seg, track_subtitle)
                sub_time_us += sub_dur_us

            current_time_us += duration_us

        # Save draft JSON into user CapCut & Jianying Projects folders
        target_base_dirs = [
            self.draft_base_dir,
            os.path.expanduser("~/Library/Containers/com.lemon.lvoverseas/Data/Movies/CapCut/User Data/Projects/com.lveditor.draft/"),
            os.path.expanduser("~/Movies/CapCut/User Data/Projects/com.lveditor.draft/"),
            os.path.expanduser("~/Movies/JianyingPro/User Data/Projects/com.lveditor.draft/")
        ]

        main_draft_dir = None

        for b_dir in target_base_dirs:
            try:
                os.makedirs(b_dir, exist_ok=True)
                d_dir = os.path.join(b_dir, draft_name)
                os.makedirs(d_dir, exist_ok=True)
                if not main_draft_dir:
                    main_draft_dir = d_dir

                # 1. Standard draft_content.json (CapCut native format)
                d_json_file = os.path.join(d_dir, "draft_content.json")
                script.dump(d_json_file)

                is_capcut = "CapCut" in b_dir
                target_json_file = d_json_file if is_capcut else os.path.join(d_dir, "draft_info.json")

                # If JianyingPro, create draft_info.json
                if not is_capcut:
                    import shutil
                    shutil.copyfile(d_json_file, target_json_file)
                else:
                    # Clean up draft_info.json for CapCut so it doesn't flag as Jianying draft
                    if os.path.exists(os.path.join(d_dir, "draft_info.json")):
                        os.remove(os.path.join(d_dir, "draft_info.json"))

                # 3. Subdirectories & Configs
                for sd in ["Resources", "Timelines", "common_attachment", "subdraft", "matting", "adjust_mask"]:
                    os.makedirs(os.path.join(d_dir, sd), exist_ok=True)

                default_configs = {
                    "draft_virtual_store.json": '{"draft_materials":[],"draft_virtual_store":[]}',
                    "draft_agency_config.json": '{"is_auto_agency_enabled":false}',
                    "draft_biz_config.json": '{\n    "timeline_settings": {\n        "resolution": "1080P"\n    }\n}',
                    "attachment_editing.json": '{"editing_draft":{}}',
                    "timeline_layout.json": '{"activeTimeline":""}'
                }
                for cfg_name, cfg_val in default_configs.items():
                    cfg_p = os.path.join(d_dir, cfg_name)
                    if not os.path.exists(cfg_p):
                        with open(cfg_p, "w", encoding="utf-8") as f:
                            f.write(cfg_val)

                # 4. Subfolder draft_meta_info.json
                meta_json_file = os.path.join(d_dir, "draft_meta_info.json")
                if os.path.exists(meta_json_file):
                    with open(meta_json_file, "r", encoding="utf-8") as f:
                        meta_data = json.load(f)
                    meta_data["tm_duration"] = current_time_us
                    meta_data["draft_timeline_materials_size_"] = 25000000
                    with open(meta_json_file, "w", encoding="utf-8") as f:
                        json.dump(meta_data, f, indent=2, ensure_ascii=False)

                # 5. Root root_meta_info.json
                root_meta_file = os.path.join(b_dir, "root_meta_info.json")
                if os.path.exists(root_meta_file):
                    with open(root_meta_file, "r", encoding="utf-8") as f:
                        root_meta = json.load(f)
                    for item in root_meta.get("all_draft_store", []):
                        if item.get("draft_name") == draft_name or item.get("draft_fold_path") == d_dir:
                            item["tm_duration"] = current_time_us
                            item["draft_timeline_materials_size"] = 25000000
                            item["draft_json_file"] = target_json_file
                    with open(root_meta_file, "w", encoding="utf-8") as f:
                        json.dump(root_meta, f, indent=2, ensure_ascii=False)

            except Exception as ex:
                logger.warning("Could not sync draft to %s: %s", b_dir, ex)

        logger.info("Successfully exported CapCut & Jianying draft project: %s", main_draft_dir)
        return main_draft_dir
