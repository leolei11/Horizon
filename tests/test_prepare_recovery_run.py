import json
from datetime import UTC, datetime
from pathlib import Path

import pytest

from scripts.prepare_recovery_run import prepare_recovery_run


def _write(path: Path, value: object) -> None:
    path.write_text(json.dumps(value), encoding="utf-8")


def test_prepares_model_override_and_replaces_only_current_shanghai_day(tmp_path):
    config_path = tmp_path / "config.json"
    history_path = tmp_path / "history.json"
    _write(config_path, {"ai": {"model": "gemini-3.5-flash-lite"}})
    _write(
        history_path,
        [
            {"pushed_at": "2026-08-18T07:17:00+00:00", "id": "today"},
            {"pushed_at": "2026-08-17T07:17:00+00:00", "id": "older"},
        ],
    )

    model, removed = prepare_recovery_run(
        config_path=config_path,
        history_path=history_path,
        model_override="gemini-3.6-flash",
        replace_current_day=True,
        now=datetime(2026, 8, 18, 8, tzinfo=UTC),
    )

    assert model == "gemini-3.6-flash"
    assert removed == 1
    assert json.loads(config_path.read_text())["ai"]["model"] == "gemini-3.6-flash"
    assert json.loads(history_path.read_text()) == [
        {"pushed_at": "2026-08-17T07:17:00+00:00", "id": "older"}
    ]


def test_rejects_non_gemini_model_override(tmp_path):
    config_path = tmp_path / "config.json"
    history_path = tmp_path / "history.json"
    _write(config_path, {"ai": {"model": "gemini-3.5-flash-lite"}})
    _write(history_path, [])

    with pytest.raises(ValueError, match="Gemini model ID"):
        prepare_recovery_run(
            config_path=config_path,
            history_path=history_path,
            model_override="../../other-model",
            replace_current_day=False,
        )
