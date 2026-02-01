import asyncio
import logging
from .api_client import MoltbookClient
from .config import Config
from .scoring import score_project
from .escrow import EscrowContract

logger = logging.getLogger(__name__)


class InvestMatchAgent:
    def __init__(self) -> None:
        self.client = MoltbookClient()
        self.escrow = EscrowContract()
        self.processed = set()

    async def start(self) -> None:
        logger.info("InvestMatch Agent started...")
        await self.publish_intro()
        while True:
            try:
                posts = await self.client.get_feed()
                for post in posts:
                    if post["id"] in self.processed:
                        continue
                    await self.process_post(post)
                    self.processed.add(post["id"])
                await asyncio.sleep(10)
            except Exception as exc:
                logger.error("Main loop error: %s", exc)
                await asyncio.sleep(5)

    async def publish_intro(self) -> None:
        content = (
            "🤝 InvestMatch is a neutral intermediary for agent investments.\n\n"
            f"{Config.ROLE_TEXT}\n"
            f"{Config.COMMISSION_TEXT}\n"
            f"Wallet: {Config.TON_WALLET_ADDRESS}\n"
            f"{Config.DISCLOSURE_TEXT}"
        )
        await self.client.create_post(content)

    async def process_post(self, post: dict) -> None:
        content = post.get("content", "")
        content_lower = content.lower()

        if "invest" not in content_lower and "investment" not in content_lower:
            return

        result = score_project(content)
        if result.flags:
            reply = (
                f"⚠️ High‑risk flags detected: {', '.join(result.flags)}\n"
                f"Score: {result.score}/100\n"
                f"{Config.ROLE_TEXT}\n"
                f"{Config.COMMISSION_TEXT}\n"
                f"Wallet: {Config.TON_WALLET_ADDRESS}\n"
                f"{Config.DISCLOSURE_TEXT}"
            )
            await self.client.post_comment(post["id"], reply)
            return

        if result.score < Config.MIN_SCORE_TO_LIST:
            reply = (
                f"⛔ Score too low: {result.score}/100\n"
                f"Reasons: {', '.join(result.reasons) or 'Insufficient data'}\n"
                f"{Config.ROLE_TEXT}\n"
                f"{Config.COMMISSION_TEXT}\n"
                f"Wallet: {Config.TON_WALLET_ADDRESS}\n"
                f"{Config.DISCLOSURE_TEXT}"
            )
            await self.client.post_comment(post["id"], reply)
            return

        escrow = self.escrow.prepare_deal(
            investor_id="TBD",
            project_id=post["id"],
            amount=1.0,
        )
        reply = (
            f"✅ Project scored {result.score}/100\n"
            f"Reasons: {', '.join(result.reasons) or 'Basic checks passed'}\n\n"
            f"Escrow draft:\n"
            f"- Address: {escrow['escrow_address']}\n"
            f"- Amount: {escrow['amount']} {escrow['currency']}\n"
            f"- Terms: {escrow['terms']}\n\n"
            f"{Config.ROLE_TEXT}\n"
            f"{Config.COMMISSION_TEXT}\n"
            f"Wallet: {Config.TON_WALLET_ADDRESS}\n"
            f"{Config.DISCLOSURE_TEXT}"
        )
        await self.client.post_comment(post["id"], reply)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    agent = InvestMatchAgent()
    asyncio.run(agent.start())


if __name__ == "__main__":
    main()
