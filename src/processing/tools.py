"""Built-in tools available to enrichment blocks."""

import asyncio
from dataclasses import dataclass
import logging
from typing import Any

from ddgs import DDGS

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ToolResult:
    request_id: str
    block_id: str
    tool: str
    results: list[dict[str, str]]


class WebSearchTool:
    name = "web_search"

    def __init__(self, timeout_sec: float = 15.0):
        self.timeout_sec = timeout_sec

    async def execute(self, arguments: dict[str, Any]) -> list[dict[str, str]]:
        query = arguments.get("query")
        if not isinstance(query, str) or not query.strip():
            raise ValueError("web_search requires a non-empty query")
        try:
            raw = await asyncio.wait_for(
                asyncio.to_thread(
                    DDGS(timeout=self.timeout_sec).text,
                    query.strip(),
                    max_results=3,
                ),
                timeout=self.timeout_sec,
            )
        except TimeoutError:
            logger.warning("web_search timed out for %r", query)
            return []
        except Exception as exc:
            logger.warning("web_search failed for %r: %s", query, exc)
            return []
        return [
            {
                "title": str(result.get("title", "")),
                "url": str(result.get("href", "")),
                "text": str(result.get("body", "")),
            }
            for result in (raw or [])
            if result.get("href")
        ]


class ToolRegistry:
    """Small allowlisted registry for executable profile tools."""

    def __init__(self):
        self._tools = {WebSearchTool.name: WebSearchTool()}

    @property
    def names(self) -> set[str]:
        return set(self._tools)

    async def execute(
        self,
        request_id: str,
        block_id: str,
        tool: str,
        arguments: dict[str, Any],
    ) -> ToolResult:
        try:
            implementation = self._tools[tool]
        except KeyError as exc:
            raise ValueError(f"Unknown enrichment tool: {tool}") from exc
        return ToolResult(
            request_id=request_id,
            block_id=block_id,
            tool=tool,
            results=await implementation.execute(arguments),
        )
