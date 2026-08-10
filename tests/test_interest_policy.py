import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest
from pydantic import ValidationError
from rich.console import Console

from src.ai.prompting.analysis import analysis_system_prompt
from src.models import (
    CategoryGroupConfig,
    ClassificationResult,
    ContentAnalysis,
    ContentArtifact,
    ContentBlock,
    ContentItem,
    DigestConfig,
    InterestBucketConfig,
    InterestConfig,
    ProcessingConfig,
    ProcessingResult,
    SourceType,
    VideoConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.processing import ProfileRegistry
from src.video.pipeline import HorizonVideoPipeline


PROFILES = ProfileRegistry.load(
    Path(__file__).resolve().parents[1] / "profiles", "tech-news"
)


def interests() -> InterestConfig:
    return InterestConfig(
        enabled=True,
        audience="A practical AI builder",
        include_topics=["AI applications"],
        exclude_topics=["Claude Code"],
        hard_reject_rules=["Reject pure benchmarks"],
        min_relevance_score=7,
        min_actionability_score=6,
        buckets={
            "applied-ai": InterestBucketConfig(
                name="Applied AI",
                target_count=1,
                description="Things to try",
            ),
            "builder-stack": InterestBucketConfig(
                name="Builder stack",
                target_count=1,
                description="Things to build with",
            ),
        },
    )


def item(
    item_id: str,
    *,
    bucket: str,
    score: float = 8,
    relevance: float = 8,
    actionability: float = 8,
    video: float = 8,
    rejection: str | None = None,
) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=item_id,
        url=f"https://example.com/{item_id}",
        author="Example",
        published_at=datetime.now(timezone.utc),
        profile="tech-news",
        processing=ProcessingResult(
            classification=ClassificationResult(
                profile="tech-news",
                method="source_override",
            ),
            analysis=ContentAnalysis(
                score=score,
                reason="Useful",
                summary="A practical release.",
                interest_bucket=bucket,
                relevance_score=relevance,
                actionability_score=actionability,
                video_score=video,
                rejection_reason=rejection,
            ),
            artifacts={
                "zh": ContentArtifact(
                    language="zh",
                    title=f"{item_id} 中文标题",
                    blocks=[
                        ContentBlock(
                            id="summary",
                            title="摘要",
                            content="这是一个可以直接试用的工具。它减少了重复配置。",
                            primary=True,
                        ),
                        ContentBlock(
                            id="next_step",
                            title="下一步",
                            content="先在测试项目中验证安装流程。",
                        ),
                    ],
                )
            },
        ),
    )


def orchestrator() -> HorizonOrchestrator:
    instance = HorizonOrchestrator.__new__(HorizonOrchestrator)
    instance.config = SimpleNamespace(
        digest=DigestConfig(
            max_items=5,
            category_groups={
                "applied-ai": CategoryGroupConfig(
                    limit=5,
                    categories=["applied-ai"],
                ),
                "builder-stack": CategoryGroupConfig(
                    limit=5,
                    categories=["builder-stack"],
                ),
            },
        ),
        interests=interests(),
        processing=ProcessingConfig(),
        sources=SimpleNamespace(twitter=None),
    )
    instance.console = Console(record=True)
    return instance


def exact_orchestrator(
    *,
    max_items: int = 4,
    require_unique_items: bool = False,
) -> HorizonOrchestrator:
    instance = orchestrator()
    instance.config.digest = DigestConfig(
        max_items=max_items,
        require_exact_count=True,
        require_unique_items=require_unique_items,
        category_groups={
            "applied-ai": CategoryGroupConfig(
                limit=max_items // 2,
                categories=["applied-ai"],
            ),
            "builder-stack": CategoryGroupConfig(
                limit=max_items // 2,
                categories=["builder-stack"],
            ),
        },
    )
    instance.config.interests = InterestConfig(
        **{
            **interests().model_dump(),
            "buckets": {
                "applied-ai": InterestBucketConfig(
                    name="Applied AI",
                    target_count=max_items // 2,
                    description="Things to try",
                ),
                "builder-stack": InterestBucketConfig(
                    name="Builder stack",
                    target_count=max_items // 2,
                    description="Things to build with",
                ),
            },
        }
    )
    return instance


def test_interest_prompt_contains_policy_and_valid_contract_shape() -> None:
    prompt = analysis_system_prompt(PROFILES.get("tech-news"), interests())

    assert "Claude Code" in prompt
    assert "Reject pure benchmarks" in prompt
    assert '"interest_bucket": "<configured bucket ID or null when rejected>"' in prompt
    assert '"rejection_reason": "<reason or null>"\n}' in prompt
    assert '"rejection_reason": "<reason or null>",\n}' not in prompt


def test_interest_filter_enforces_personal_quality_floor() -> None:
    instance = orchestrator()

    assert instance.passes_profile_filter(item("accepted", bucket="applied-ai"))
    assert not instance.passes_profile_filter(
        item("low-fit", bucket="applied-ai", relevance=6.9)
    )
    assert not instance.passes_profile_filter(
        item("excluded", bucket="applied-ai", rejection="Excluded topic")
    )
    assert not instance.passes_profile_filter(item("unknown", bucket="unknown"))


def test_interest_bucket_targets_are_real_caps() -> None:
    instance = orchestrator()
    result = instance.apply_balanced_digest(
        [
            item("ai-top", bucket="applied-ai", relevance=10),
            item("ai-second", bucket="applied-ai", relevance=9),
            item("stack", bucket="builder-stack", relevance=8),
        ],
        log=False,
    )

    assert [entry.id for entry in result.items] == ["ai-top", "stack"]
    assert result.group_limits["applied-ai"] == 1
    assert result.group_limits["builder-stack"] == 1


def test_interest_caps_apply_without_legacy_digest_groups() -> None:
    instance = orchestrator()
    instance.config.digest = DigestConfig()

    result = instance.apply_balanced_digest(
        [
            item("ai-top", bucket="applied-ai", relevance=10),
            item("ai-second", bucket="applied-ai", relevance=9),
            item("stack", bucket="builder-stack", relevance=8),
        ],
        log=False,
    )

    assert [entry.id for entry in result.items] == ["ai-top", "stack"]


def test_exact_digest_uses_quality_floor_as_priority_then_backfills() -> None:
    instance = exact_orchestrator()

    result = asyncio.run(
        instance.select_digest_items(
            [
                item("primary-ai", bucket="applied-ai", relevance=10),
                item("primary-stack", bucket="builder-stack", relevance=9),
                item(
                    "reserve-ai",
                    bucket="applied-ai",
                    relevance=6.5,
                    actionability=5.5,
                ),
                item(
                    "reserve-stack",
                    bucket="builder-stack",
                    relevance=6,
                    actionability=5,
                ),
            ],
            topic_dedup=False,
            log=False,
        )
    )

    assert [entry.id for entry in result.items] == [
        "primary-ai",
        "primary-stack",
        "reserve-ai",
        "reserve-stack",
    ]


def test_exact_digest_cross_fills_when_one_interest_bucket_is_short() -> None:
    instance = exact_orchestrator()

    result = asyncio.run(
        instance.select_digest_items(
            [
                item("only-ai", bucket="applied-ai", relevance=10),
                item("stack-1", bucket="builder-stack", relevance=9),
                item("stack-2", bucket="builder-stack", relevance=8),
                item("stack-3", bucket="builder-stack", relevance=7),
            ],
            topic_dedup=False,
            log=False,
        )
    )

    assert len(result.items) == 4
    assert {entry.id for entry in result.items} == {
        "only-ai",
        "stack-1",
        "stack-2",
        "stack-3",
    }


def test_exact_digest_refuses_to_return_too_few_items() -> None:
    instance = exact_orchestrator()

    with pytest.raises(RuntimeError, match="requires exactly 4 unique items"):
        asyncio.run(
            instance.select_digest_items(
                [
                    item("ai", bucket="applied-ai"),
                    item("stack", bucket="builder-stack"),
                ],
                topic_dedup=False,
                log=False,
            )
        )


def test_exact_digest_runs_strict_duplicate_audit_and_refills(monkeypatch) -> None:
    instance = exact_orchestrator(require_unique_items=True)
    audited = False

    async def audit(input_items, *, log=True, strict=False):  # type: ignore[no-untyped-def]
        nonlocal audited
        audited = True
        assert strict is True
        return [entry for entry in input_items if entry.id != "duplicate"]

    monkeypatch.setattr(instance, "merge_topic_duplicates", audit)
    result = asyncio.run(
        instance.select_digest_items(
            [
                item("ai-1", bucket="applied-ai", relevance=10),
                item("duplicate", bucket="applied-ai", relevance=9.5),
                item("ai-2", bucket="applied-ai", relevance=9),
                item("stack-1", bucket="builder-stack", relevance=8),
                item("stack-2", bucket="builder-stack", relevance=7),
            ],
            log=False,
        )
    )

    assert audited
    assert len(result.items) == 4
    assert "duplicate" not in {entry.id for entry in result.items}


def test_exact_digest_duplicate_audit_failure_blocks_publication(monkeypatch) -> None:
    instance = exact_orchestrator(require_unique_items=True)

    async def failed_audit(input_items, *, log=True, strict=False):  # type: ignore[no-untyped-def]
        raise RuntimeError("Final duplicate audit failed")

    monkeypatch.setattr(instance, "merge_topic_duplicates", failed_audit)

    with pytest.raises(RuntimeError, match="Final duplicate audit failed"):
        asyncio.run(
            instance.select_digest_items(
                [
                    item(f"item-{index}", bucket="applied-ai")
                    for index in range(4)
                ],
                log=False,
            )
        )


def test_digest_identity_dedup_ignores_tracking_and_normalizes_titles() -> None:
    instance = exact_orchestrator(max_items=2)
    same_url = item("url-copy", bucket="applied-ai", relevance=9)
    same_url.url = "https://example.com/original/?utm_source=rss"
    original = item("original", bucket="applied-ai", relevance=10)
    original.url = "http://example.com/original"
    same_title = item("title-copy", bucket="builder-stack", relevance=8)
    same_title.title = "  OpenAI：发布 Agent SDK！ "
    title_original = item("title-original", bucket="builder-stack", relevance=9)
    title_original.title = "OpenAI 发布 Agent SDK"

    result = instance.merge_digest_identity_duplicates(
        [original, same_url, title_original, same_title]
    )

    assert [entry.id for entry in result] == ["original", "title-original"]


def test_strict_duplicate_audit_rejects_invalid_indices(monkeypatch) -> None:
    instance = exact_orchestrator(max_items=2)
    instance.config.ai = SimpleNamespace()

    class InvalidAuditClient:
        async def complete(self, **kwargs):  # type: ignore[no-untyped-def]
            return '{"duplicates": [[0, 99]]}'

    monkeypatch.setattr(
        "src.orchestrator.create_ai_client",
        lambda config: InvalidAuditClient(),
    )

    with pytest.raises(RuntimeError, match="invalid duplicate group"):
        asyncio.run(
            instance.merge_topic_duplicates(
                [
                    item("one", bucket="applied-ai"),
                    item("two", bucket="builder-stack"),
                ],
                log=False,
                strict=True,
            )
        )


def test_strict_duplicate_audit_retries_transient_api_failures(monkeypatch) -> None:
    instance = exact_orchestrator(max_items=2)
    instance.config.ai = SimpleNamespace()
    calls = 0

    class FlakyAuditClient:
        async def complete(self, **kwargs):  # type: ignore[no-untyped-def]
            nonlocal calls
            calls += 1
            if calls < 3:
                raise TimeoutError("temporary timeout")
            return '{"duplicates": []}'

    client = FlakyAuditClient()
    monkeypatch.setattr(
        "src.orchestrator.create_ai_client",
        lambda config: client,
    )

    result = asyncio.run(
        instance.merge_topic_duplicates(
            [
                item("one", bucket="applied-ai"),
                item("two", bucket="builder-stack"),
            ],
            log=False,
            strict=True,
        )
    )

    assert len(result) == 2
    assert calls == 3


def test_video_config_rejects_portrait_output() -> None:
    with pytest.raises(ValidationError, match="landscape"):
        VideoConfig(width=1920, height=1920)


def test_video_manifest_uses_separate_video_ranking(tmp_path: Path) -> None:
    pipeline = HorizonVideoPipeline(
        VideoConfig(
            enabled=True,
            max_items=2,
            min_video_score=7,
            renderer_dir="renderer",
            output_dir="output",
        ),
        project_root=tmp_path,
    )
    result = asyncio.run(
        pipeline.prepare_manifest(
            [
                item("daily-top", bucket="builder-stack", relevance=10, video=7),
                item("video-top", bucket="applied-ai", relevance=8, video=10),
                item("below-video-floor", bucket="applied-ai", video=6.9),
            ],
            date="2026-08-10",
            language="zh",
            synthesize_audio=False,
            bucket_names={
                "applied-ai": "AI 落地",
                "builder-stack": "开发实战",
            },
        )
    )

    manifest = json.loads(result.manifest_path.read_text(encoding="utf-8"))
    assert result.selected_count == 2
    assert [story["id"] for story in manifest["stories"]] == [
        "video-top",
        "daily-top",
    ]
    assert manifest["stories"][0]["bucket"] == "AI 落地"
    assert manifest["stories"][0]["action"] == "先在测试项目中验证安装流程。"
    assert manifest["stories"][0]["actionLabel"] == "NEXT MOVE"
    assert manifest["width"] == 1920
    assert manifest["height"] == 1080
    assert manifest["fps"] == 30


def test_video_localization_filter_runs_before_top_k(tmp_path: Path) -> None:
    pipeline = HorizonVideoPipeline(
        VideoConfig(
            enabled=True,
            max_items=1,
            min_video_score=7,
            renderer_dir="renderer",
            output_dir="output",
        ),
        project_root=tmp_path,
    )
    untranslated = item("untranslated", bucket="applied-ai", video=10)
    untranslated.processing.artifacts = {}

    result = asyncio.run(
        pipeline.prepare_manifest(
            [
                untranslated,
                item("localized", bucket="builder-stack", video=9),
            ],
            date="2026-08-10",
            language="zh",
            synthesize_audio=False,
        )
    )

    manifest = json.loads(result.manifest_path.read_text(encoding="utf-8"))
    assert result.selected_count == 1
    assert [story["id"] for story in manifest["stories"]] == ["localized"]
