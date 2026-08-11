import logging

from rich.console import Console

from src import orchestrator as orchestrator_module
from src.logging_config import configure_logging


def test_configure_logging_forces_shared_console(monkeypatch):
    calls = []
    console = Console(stderr=True)
    monkeypatch.setattr(logging, "basicConfig", lambda **kwargs: calls.append(kwargs))

    configure_logging(console)

    assert len(calls) == 1
    assert calls[0]["force"] is True
    assert calls[0]["level"] == logging.WARNING
    assert calls[0]["handlers"][0].console is console


def test_orchestrator_defines_logger_for_optional_video_failures():
    """A video-render error must not become a NameError in its fallback path."""
    assert isinstance(orchestrator_module.logger, logging.Logger)
