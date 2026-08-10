"""GitHub scraper implementation."""

import logging
import os
from datetime import datetime
from typing import List, Optional
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, GitHubSourceConfig

logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    """Scraper for GitHub events and releases."""

    def __init__(self, sources: List[GitHubSourceConfig], http_client: httpx.AsyncClient):
        """Initialize GitHub scraper.

        Args:
            sources: List of GitHub source configurations
            http_client: Shared async HTTP client
        """
        super().__init__({"sources": sources}, http_client)
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"

    async def _fetch_readme(self, owner: str, repo: str) -> str:
        """Fetch raw README excerpt from main or master branch."""
        branches = ["main", "master"]
        for branch in branches:
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md"
            try:
                response = await self.client.get(url, follow_redirects=True, timeout=5.0)
                if response.status_code == 200 and len(response.text.strip()) > 30:
                    return response.text.strip()[:1200]
            except Exception:
                continue
        return ""

    def _get_headers(self) -> dict:
        """Get request headers with optional authentication.

        Returns:
            dict: HTTP headers
        """
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Horizon-Aggregator"
        }
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch GitHub content items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        sources = self.config["sources"]

        for source in sources:
            if not source.enabled:
                continue

            if source.type == "user_events" and source.username:
                user_items = await self._fetch_user_events(source, since)
                items.extend(user_items)
            elif source.type == "repo_releases" and source.owner and source.repo:
                release_items = await self._fetch_repo_releases(source, since)
                items.extend(release_items)
            elif source.type in ("trending_curriculum", "trending"):
                trending_items = await self._fetch_trending_curriculum(source, since)
                items.extend(trending_items)

        return items

    async def _fetch_user_events(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Fetch public events for a user.

        Args:
            source: GitHub source configuration
            since: Only fetch events after this time

        Returns:
            List[ContentItem]: Event content items
        """
        url = f"{self.base_url}/users/{source.username}/events/public"
        items = []

        try:
            response = await self.client.get(url, headers=self._get_headers(), follow_redirects=True)
            response.raise_for_status()
            events = response.json()

            for event in events:
                created_at = datetime.fromisoformat(
                    event["created_at"].replace("Z", "+00:00")
                )

                if created_at < since:
                    continue

                # Filter interesting event types
                event_type = event["type"]
                if event_type not in [
                    "PushEvent", "CreateEvent", "ReleaseEvent",
                    "PublicEvent", "WatchEvent"
                ]:
                    continue

                item = self._parse_event(event, source)
                if item:
                    items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching GitHub events for %s: %s", source.username, e)

        return items

    def _parse_event(self, event: dict, source: GitHubSourceConfig) -> Optional[ContentItem]:
        """Parse GitHub event into ContentItem.

        Args:
            event: GitHub event data
            username: GitHub username

        Returns:
            Optional[ContentItem]: Parsed content item or None
        """
        event_type = event["type"]
        event_id = event["id"]
        created_at = datetime.fromisoformat(event["created_at"].replace("Z", "+00:00"))
        username = source.username

        repo_name = event["repo"]["name"]
        repo_url = f"https://github.com/{repo_name}"

        # Generate title and content based on event type
        if event_type == "PushEvent":
            commits = event["payload"].get("commits", [])
            title = f"{username} pushed {len(commits)} commit(s) to {repo_name}"
            content = "\n".join([c.get("message", "") for c in commits[:3]])
        elif event_type == "CreateEvent":
            ref_type = event["payload"].get("ref_type", "repository")
            title = f"{username} created {ref_type} in {repo_name}"
            content = event["payload"].get("description", "")
        elif event_type == "ReleaseEvent":
            release = event["payload"].get("release", {})
            title = f"{username} released {release.get('tag_name', '')} in {repo_name}"
            content = release.get("body", "")
            repo_url = release.get("html_url", repo_url)
        elif event_type == "PublicEvent":
            title = f"{username} made {repo_name} public"
            content = ""
        elif event_type == "WatchEvent":
            title = f"{username} starred {repo_name}"
            content = ""
        else:
            return None

        return ContentItem(
            id=self._generate_id("github", "event", event_id),
            source_type=SourceType.GITHUB,
            title=title,
            url=repo_url,
            content=content,
            author=username,
            published_at=created_at,
            profile=source.profile,
            metadata={
                "event_type": event_type,
                "repo": repo_name,
                "category": source.category,
            }
        )

    async def _fetch_repo_releases(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Fetch releases for a repository.

        Args:
            source: GitHub source configuration
            since: Only fetch releases after this time

        Returns:
            List[ContentItem]: Release content items
        """
        owner, repo = source.owner, source.repo
        url = f"{self.base_url}/repos/{owner}/{repo}/releases"
        items = []

        try:
            response = await self.client.get(url, headers=self._get_headers(), follow_redirects=True)
            response.raise_for_status()
            releases = response.json()

            for release in releases:
                published_at = datetime.fromisoformat(
                    release["published_at"].replace("Z", "+00:00")
                )

                if published_at < since:
                    continue

                item = ContentItem(
                    id=self._generate_id("github", "release", str(release["id"])),
                    source_type=SourceType.GITHUB,
                    title=f"{owner}/{repo} released {release['tag_name']}",
                    url=release["html_url"],
                    content=release.get("body", ""),
                    author=release["author"]["login"],
                    published_at=published_at,
                    profile=source.profile,
                    metadata={
                        "repo": f"{owner}/{repo}",
                        "tag": release["tag_name"],
                        "prerelease": release.get("prerelease", False),
                        "category": source.category,
                    }
                )
                items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching releases for %s/%s: %s", owner, repo, e)

        return items

    async def _fetch_trending_curriculum(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Fetch trending & curriculum GitHub repositories."""
        items: List[ContentItem] = []
        since_str = since.strftime("%Y-%m-%d")

        # 1. Search for trending repositories created or updated recently
        limit = source.trending_limit
        url = f"{self.base_url}/search/repositories?q=pushed:>{since_str}&sort=stars&order=desc&per_page={limit}"
        try:
            response = await self.client.get(url, headers=self._get_headers(), follow_redirects=True)
            if response.status_code == 200:
                data = response.json()
                for repo in data.get("items", []):
                    pushed_at_str = repo.get("pushed_at") or repo.get("created_at")
                    published_at = (
                        datetime.fromisoformat(pushed_at_str.replace("Z", "+00:00"))
                        if pushed_at_str
                        else since
                    )
                    description = repo.get("description") or "GitHub Trending Repository"
                    lang = repo.get("language") or "General"
                    stars = repo.get("stargazers_count", 0)

                    owner_login = repo["owner"]["login"]
                    repo_name_only = repo["name"]
                    readme_text = await self._fetch_readme(owner_login, repo_name_only)
                    
                    content_parts = [description, f"Language: {lang} | Stars: {stars} | Owner: {owner_login}"]
                    if readme_text:
                        content_parts.append(f"\n--- README Excerpt ---\n{readme_text}")

                    item = ContentItem(
                        id=self._generate_id("github", "repo", str(repo["id"])),
                        source_type=SourceType.GITHUB,
                        title=f"GitHub Trending: {repo['full_name']} (⭐️ {stars})",
                        url=repo["html_url"],
                        content="\n\n".join(content_parts),
                        author=owner_login,
                        published_at=published_at,
                        profile=source.profile,
                        metadata={
                            "repo": repo["full_name"],
                            "stars": stars,
                            "language": lang,
                            "category": source.category,
                        },
                    )
                    items.append(item)
            else:
                logger.warning("GitHub search API returned status %d", response.status_code)
        except httpx.HTTPError as e:
            logger.warning("Error searching GitHub trending: %s", e)

        # 2. Fetch curated curriculum repos if configured
        curriculum_repos = [
            repo_name
            for batch in source.curriculum_batches
            for repo_name in batch
            if repo_name and "/" in repo_name
        ]
        selected_curriculum: List[str] = []
        if curriculum_repos and source.curriculum_items_per_day:
            start = int(since.strftime("%j")) % len(curriculum_repos)
            selected_curriculum = [
                curriculum_repos[(start + offset) % len(curriculum_repos)]
                for offset in range(
                    min(source.curriculum_items_per_day, len(curriculum_repos))
                )
            ]

        for repo_name in selected_curriculum:
            repo_url = f"{self.base_url}/repos/{repo_name}"
            try:
                res = await self.client.get(
                    repo_url,
                    headers=self._get_headers(),
                    follow_redirects=True,
                )
                if res.status_code == 200:
                    repo = res.json()
                    stars = repo.get("stargazers_count", 0)
                    description = (
                        repo.get("description")
                        or "Classic GitHub Curriculum Repository"
                    )
                    lang = repo.get("language") or "General"
                    item = ContentItem(
                        id=self._generate_id(
                            "github", "curriculum", str(repo["id"])
                        ),
                        source_type=SourceType.GITHUB,
                        title=(
                            f"GitHub 经典名库: {repo['full_name']} "
                            f"(⭐️ {stars})"
                        ),
                        url=repo["html_url"],
                        content=(
                            f"{description}\n\nLanguage: {lang} | Stars: {stars}"
                        ),
                        author=repo["owner"]["login"],
                        published_at=since,
                        profile=source.profile,
                        metadata={
                            "repo": repo["full_name"],
                            "stars": stars,
                            "category": source.category,
                        },
                    )
                    items.append(item)
            except httpx.HTTPError as e:
                logger.warning("Error fetching curriculum repo %s: %s", repo_name, e)

        return items
