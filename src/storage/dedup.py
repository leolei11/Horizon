"""Historical deduplication manager for cross-day item filtering."""

import hashlib
import json
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import List, Dict

from .._file_utils import _atomic_write_text
from ..models import ContentItem

logger = logging.getLogger(__name__)

# Deduplication Retention Windows (in days)
GITHUB_DEDUP_DAYS = 365
DEFAULT_DEDUP_DAYS = 90


class HistoryDeduplicator:
    """Manages persistent historical records to prevent cross-day item duplication."""

    def __init__(self, data_dir: Path):
        self.history_file = data_dir / "pushed_history.json"
        self._records: List[Dict] = []
        self._load()

    def _load(self) -> None:
        if not self.history_file.exists():
            self._records = []
            return
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                self._records = json.load(f)
        except Exception as e:
            logger.warning("Could not load pushed_history.json: %s", e)
            self._records = []

    def save(self) -> None:
        try:
            _atomic_write_text(
                self.history_file,
                json.dumps(self._records, indent=2, ensure_ascii=False)
            )
        except Exception as e:
            logger.warning("Could not save pushed_history.json: %s", e)

    @staticmethod
    def _url_hash(url: str) -> str:
        clean_url = str(url).strip().rstrip("/")
        return hashlib.md5(clean_url.encode("utf-8")).hexdigest()

    @staticmethod
    def _get_repo_name(item: ContentItem) -> str:
        meta = item.metadata or {}
        repo = meta.get("repo")
        if isinstance(repo, str) and repo.strip():
            return repo.strip().lower()
        if "github.com/" in str(item.url):
            parts = str(item.url).split("github.com/")[-1].split("/")
            if len(parts) >= 2:
                return f"{parts[0]}/{parts[1]}".lower()
        return ""

    def is_duplicate(self, item: ContentItem, now: datetime | None = None) -> bool:
        if now is None:
            now = datetime.now(timezone.utc)

        repo_name = self._get_repo_name(item)
        url_h = self._url_hash(str(item.url))

        for rec in self._records:
            rec_time_str = rec.get("pushed_at")
            if not rec_time_str:
                continue
            try:
                rec_time = datetime.fromisoformat(rec_time_str.replace("Z", "+00:00"))
            except ValueError:
                continue

            days_diff = (now - rec_time).days

            # 1. GitHub repo deduplication window: 365 days
            if repo_name and rec.get("repo"):
                if repo_name == rec["repo"].lower() and days_diff < GITHUB_DEDUP_DAYS:
                    return True

            # 2. General URL deduplication window: 90 days
            if rec.get("url_hash") and url_h == rec["url_hash"] and days_diff < DEFAULT_DEDUP_DAYS:
                return True

        return False

    def filter_items(self, items: List[ContentItem]) -> List[ContentItem]:
        now = datetime.now(timezone.utc)
        filtered = []
        dups_count = 0
        for item in items:
            if self.is_duplicate(item, now):
                dups_count += 1
                logger.info("Filtered historical duplicate item: %s (%s)", item.title, item.url)
            else:
                filtered.append(item)
        if dups_count > 0:
            logger.info("Filtered %d historical duplicate items", dups_count)
        return filtered

    def record_pushed_items(self, items: List[ContentItem]) -> None:
        now_str = datetime.now(timezone.utc).isoformat()
        for item in items:
            repo_name = self._get_repo_name(item)
            url_h = self._url_hash(str(item.url))
            rec = {
                "pushed_at": now_str,
                "title": item.title,
                "url": str(item.url),
                "url_hash": url_h,
                "source_type": item.source_type.value,
            }
            if repo_name:
                rec["repo"] = repo_name
            self._records.append(rec)

        # Retain records for max 400 days to keep history lean
        cutoff = datetime.now(timezone.utc) - timedelta(days=400)
        valid_records = []
        for r in self._records:
            t_str = r.get("pushed_at")
            if not t_str:
                continue
            try:
                t = datetime.fromisoformat(t_str.replace("Z", "+00:00"))
                if t >= cutoff:
                    valid_records.append(r)
            except ValueError:
                pass
        self._records = valid_records
        self.save()
