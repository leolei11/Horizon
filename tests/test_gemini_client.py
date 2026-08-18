import asyncio
from types import SimpleNamespace

from src.ai.client import GeminiClient
from src.models import AIConfig, AIProvider


class FakeModels:
    def __init__(self):
        self.calls = []

    async def generate_content(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(text="{}", usage_metadata=None)


class FakeGoogleClient:
    def __init__(self, *, api_key: str):
        self.api_key = api_key
        self.models = FakeModels()
        self.aio = SimpleNamespace(models=self.models)


def _config(model: str) -> AIConfig:
    return AIConfig(
        provider=AIProvider.GEMINI,
        model=model,
        api_key_env="TEST_GEMINI_KEY",
        temperature=0.3,
        max_tokens=8192,
    )


def test_flash_lite_omits_deprecated_temperature(monkeypatch):
    monkeypatch.setenv("TEST_GEMINI_KEY", "test-key")
    monkeypatch.setattr("src.ai.client.genai.Client", FakeGoogleClient)
    client = GeminiClient(_config("gemini-3.5-flash-lite"))

    asyncio.run(client.complete("system", "user", temperature=0))

    request = client.client.models.calls[0]
    assert request["model"] == "gemini-3.5-flash-lite"
    assert request["config"].temperature is None
    assert request["config"].response_mime_type == "application/json"


def test_existing_flash_keeps_temperature(monkeypatch):
    monkeypatch.setenv("TEST_GEMINI_KEY", "test-key")
    monkeypatch.setattr("src.ai.client.genai.Client", FakeGoogleClient)
    client = GeminiClient(_config("gemini-3.5-flash"))

    asyncio.run(client.complete("system", "user", temperature=0.2))

    request = client.client.models.calls[0]
    assert request["config"].temperature == 0.2
