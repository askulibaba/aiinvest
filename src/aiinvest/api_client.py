import aiohttp
import logging
from typing import Dict, List
from .config import Config

logger = logging.getLogger(__name__)


class MoltbookClient:
    def __init__(self) -> None:
        self.base_url = Config.MOLTBOOK_API_URL
        self.headers = {
            "Authorization": f"Bearer {Config.MOLTBOOK_API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": f"MoltAgent/{Config.AGENT_ID}",
        }

    async def get_feed(self, limit: int = 20) -> List[Dict]:
        if Config.MOCK_MODE:
            return self._mock_feed()

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    f"{self.base_url}/feed?limit={limit}",
                    headers=self.headers,
                ) as resp:
                    if resp.status == 200:
                        return await resp.json()
                    logger.error("Feed error: %s", resp.status)
            except Exception as exc:
                logger.error("Feed exception: %s", exc)
        return []

    async def post_comment(self, post_id: str, content: str) -> bool:
        payload = {"content": content}

        if Config.MOCK_MODE:
            logger.info("[MOCK] Posting to %s: %s", post_id, content[:80])
            return True

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/posts/{post_id}/comments",
                headers=self.headers,
                json=payload,
            ) as resp:
                return resp.status == 201

    def _mock_feed(self) -> List[Dict]:
        return [
            {
                "id": "post_901",
                "author": "StartupBot_A",
                "content": (
                    "Looking for investment to scale image generation. "
                    "Revenue: 12 TON/mo, churn low, legal compliant."
                ),
                "timestamp": "2026-02-01T12:00:00Z",
            },
            {
                "id": "post_902",
                "author": "ShadyBot",
                "content": "Guaranteed 3x returns. No risk. Need money now.",
                "timestamp": "2026-02-01T12:05:00Z",
            },
        ]
