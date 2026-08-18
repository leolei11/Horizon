import asyncio
import json
import re
from datetime import UTC, datetime
from pathlib import Path
from types import SimpleNamespace

import pytest

from src.ai.quota_digest import QuotaDigestBuilder
from src.models import ContentItem, InterestConfig, SourceType
from src.processing import ProfileRegistry

PROFILES = ProfileRegistry.load(
    Path(__file__).resolve().parents[1] / "profiles", "tech-news"
)
CANDIDATE_COUNT = 64


def _make_item(index: int) -> ContentItem:
    return ContentItem(
        id=f"rss:test:{index}",
        source_type=SourceType.RSS,
        title=f"Candidate {index}",
        url=f"https://example.com/{index}",
        content=(f"Source content for candidate {index}. " * 400),
        published_at=datetime(2026, 8, 18, tzinfo=UTC),
        profile="tech-news",
    )


def _analysis_entry(index: int) -> dict:
    return {
        "id": f"rss:test:{index}",
        "score": 8.5,
        "reason": "与读者目标直接相关。",
        "summary": "这是一个可直接试用的项目。",
        "tags": ["AI", "开源"],
        "interest_bucket": "applied-ai" if index < 10 else "builder-stack",
        "relevance_score": 8.5,
        "actionability_score": 8.0,
        "video_score": 7.5,
        "rejection_reason": None,
    }


def _analysis_response(indices: list[int]) -> str:
    return json.dumps(
        {"items": [_analysis_entry(index) for index in indices]},
        ensure_ascii=False,
    )


def _selection_response(*, duplicate: bool = False) -> str:
    items = [
        {
            "id": f"rss:test:{index}",
            "interest_bucket": "applied-ai" if index < 10 else "builder-stack",
        }
        for index in range(20)
    ]
    if duplicate:
        items[-1] = items[0]
    return json.dumps({"items": items}, ensure_ascii=False)


def _enrichment_response(indices: list[int]) -> str:
    return json.dumps(
        {
            "items": [
                {
                    "id": f"rss:test:{index}",
                    "title": f"候选资讯 {index}",
                    "summary": (
                        "这是一个可直接试用的项目，能够解决具体开发问题。"
                        "它提供了清晰的使用路径和可验证的功能。"
                        "读者可以先运行最小示例。"
                    ),
                    "background": "它建立在成熟的开源工具链之上。",
                    "impact": "开发者可以减少重复配置工作。",
                    "next_step": "查看项目文档并运行最小示例。",
                    "community_discussion": "",
                }
                for index in indices
            ]
        },
        ensure_ascii=False,
    )


def _interests() -> InterestConfig:
    return InterestConfig.model_validate(
        {
            "enabled": True,
            "audience": "实操导向的开发者",
            "include_topics": ["AI 应用", "开源项目"],
            "exclude_topics": [],
            "hard_reject_rules": [],
            "min_relevance_score": 7,
            "min_actionability_score": 6,
            "buckets": {
                "applied-ai": {
                    "name": "AI 落地与提效",
                    "target_count": 10,
                    "description": "可直接试用或集成的 AI 项目。",
                    "priority_topics": ["AI 应用"],
                },
                "builder-stack": {
                    "name": "开发与 SaaS 实战",
                    "target_count": 10,
                    "description": "可复用的工程与开源实践。",
                    "priority_topics": ["开源项目"],
                },
            },
        }
    )


class FakeClient:
    def __init__(self, responses: list[str]):
        self.responses = iter(responses)
        self.calls = []
        self.config = SimpleNamespace()

    async def complete(self, **kwargs):
        self.calls.append(kwargs)
        return next(self.responses)


def _base_responses() -> list[str]:
    partitions = QuotaDigestBuilder.partition_indices(CANDIDATE_COUNT, 12)
    return [
        *[_analysis_response(indices) for indices in partitions],
        _selection_response(),
        _enrichment_response(list(range(10))),
        _enrichment_response(list(range(10, 20))),
    ]


def _builder(client: FakeClient, **overrides) -> QuotaDigestBuilder:
    settings = {
        "client": client,
        "profiles": PROFILES,
        "interests": _interests(),
        "exact_count": 20,
        "language": "zh",
        "max_requests": 20,
        "analysis_batches": 12,
        "enrichment_batches": 2,
    }
    settings.update(overrides)
    return QuotaDigestBuilder(**settings)


def test_quota_digest_uses_fifteen_requests_with_bounded_batch_context():
    client = FakeClient(_base_responses())
    result = asyncio.run(
        _builder(client).build([_make_item(index) for index in range(CANDIDATE_COUNT)])
    )

    assert result.request_count == 15
    assert len(result.items) == 20
    assert len({item.id for item in result.items}) == 20
    buckets = [item.processing.analysis.interest_bucket for item in result.items]
    assert buckets.count("applied-ai") == 10
    assert buckets.count("builder-stack") == 10
    assert all(item.processing.artifacts["zh"].blocks for item in result.items)

    analysis_calls = client.calls[:12]
    assert all("[Stage: analyze]" in call["system"] for call in analysis_calls)
    assert all(
        len(set(re.findall(r"rss:test:\d+", call["user"]))) <= 6
        for call in analysis_calls
    )
    assert max(len(call["user"]) for call in analysis_calls) < 25_000
    assert "[Stage: select]" in client.calls[12]["system"]
    assert len(client.calls[12]["user"]) < 40_000
    assert all("[Stage: enrich]" in call["system"] for call in client.calls[13:])
    assert max(len(call["user"]) for call in client.calls[13:]) < 50_000


def test_quota_digest_uses_one_reserved_request_to_repair_a_batch():
    partitions = QuotaDigestBuilder.partition_indices(CANDIDATE_COUNT, 12)
    responses = [
        json.dumps({"items": []}),
        _analysis_response(partitions[0]),
        *[_analysis_response(indices) for indices in partitions[1:]],
        _selection_response(),
        _enrichment_response(list(range(10))),
        _enrichment_response(list(range(10, 20))),
    ]
    client = FakeClient(responses)

    result = asyncio.run(
        _builder(client).build([_make_item(index) for index in range(CANDIDATE_COUNT)])
    )

    assert result.request_count == 16
    assert len(result.items) == 20
    assert "previous response failed validation" in client.calls[1]["user"]


def test_quota_digest_rejects_duplicate_selection_after_one_repair():
    partitions = QuotaDigestBuilder.partition_indices(CANDIDATE_COUNT, 12)
    responses = [
        *[_analysis_response(indices) for indices in partitions],
        _selection_response(duplicate=True),
        _selection_response(duplicate=True),
    ]
    client = FakeClient(responses)

    with pytest.raises(RuntimeError, match="unique item IDs"):
        asyncio.run(
            _builder(client).build(
                [_make_item(index) for index in range(CANDIDATE_COUNT)]
            )
        )
    assert len(client.calls) == 14


def test_quota_digest_rejects_a_base_plan_above_the_request_budget():
    client = FakeClient([])
    with pytest.raises(ValueError, match="base request plan"):
        _builder(
            client,
            max_requests=20,
            analysis_batches=18,
            enrichment_batches=2,
        )
    assert client.calls == []


def test_quota_digest_never_sends_a_twenty_first_request():
    client = FakeClient(["{}"] * 20)
    builder = _builder(client)

    async def consume_budget() -> None:
        for _ in range(20):
            await builder._complete(
                stage="test",
                system="system",
                user="user",
                max_tokens=1,
            )
        with pytest.raises(RuntimeError, match="before exceeding the 20-request"):
            await builder._complete(
                stage="test",
                system="system",
                user="user",
                max_tokens=1,
            )

    asyncio.run(consume_budget())
    assert len(client.calls) == 20
