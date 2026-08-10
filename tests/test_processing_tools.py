import asyncio

from src.processing.tools import WebSearchTool


def test_web_search_timeout_degrades_to_empty_results(monkeypatch) -> None:
    async def blocked_call(*args, **kwargs):  # type: ignore[no-untyped-def]
        await asyncio.sleep(1)
        return [{"href": "https://example.com"}]

    monkeypatch.setattr("src.processing.tools.asyncio.to_thread", blocked_call)

    result = asyncio.run(
        WebSearchTool(timeout_sec=0.01).execute({"query": "Horizon"})
    )

    assert result == []
