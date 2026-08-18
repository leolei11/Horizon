"""Prepare an automated same-day digest replacement inside GitHub Actions."""

import json
import os
import re
from datetime import UTC, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

MODEL_PATTERN = re.compile(r"^gemini-[a-z0-9.-]+$")
SHANGHAI = ZoneInfo("Asia/Shanghai")


def _write_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(f"{path.suffix}.tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def prepare_recovery_run(
    *,
    config_path: Path,
    history_path: Path,
    model_override: str,
    replace_current_day: bool,
    now: datetime | None = None,
) -> tuple[str | None, int]:
    selected_model: str | None = None
    if model_override:
        if not MODEL_PATTERN.fullmatch(model_override):
            raise ValueError("model override must be a Gemini model ID")
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["ai"]["model"] = model_override
        _write_json(config_path, config)
        selected_model = model_override

    removed = 0
    if replace_current_day:
        current = now or datetime.now(UTC)
        current_day = current.astimezone(SHANGHAI).date()
        history = json.loads(history_path.read_text(encoding="utf-8"))
        retained = []
        for record in history:
            pushed_at = datetime.fromisoformat(record["pushed_at"])
            if pushed_at.astimezone(SHANGHAI).date() == current_day:
                removed += 1
            else:
                retained.append(record)
        _write_json(history_path, retained)

    return selected_model, removed


def main() -> None:
    selected_model, removed = prepare_recovery_run(
        config_path=Path("data/config.json"),
        history_path=Path("data/pushed_history.json"),
        model_override=os.getenv("HORIZON_MODEL_OVERRIDE", "").strip(),
        replace_current_day=(
            os.getenv("HORIZON_REPLACE_CURRENT_DAY", "false").casefold() == "true"
        ),
    )
    print(
        "Recovery preparation complete: "
        f"model={selected_model or 'configured default'}, "
        f"removed_today_history={removed}"
    )


if __name__ == "__main__":
    main()
