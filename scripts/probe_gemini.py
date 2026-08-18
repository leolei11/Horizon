"""Send one minimal structured-output request through Horizon's Gemini client."""

import asyncio
import json

from dotenv import load_dotenv

from src.ai.client import create_ai_client
from src.storage.manager import StorageManager


async def main() -> None:
    load_dotenv()
    config = StorageManager(data_dir="data").load_config()
    client = create_ai_client(config.ai)
    response = await client.complete(
        system="Return only valid JSON.",
        user='Return exactly this object: {"ok": true}',
        temperature=0,
        max_tokens=256,
    )
    if json.loads(response) != {"ok": True}:
        raise RuntimeError("Gemini probe returned an unexpected JSON object")
    print(f"Gemini probe passed: {config.ai.model}")


if __name__ == "__main__":
    asyncio.run(main())
