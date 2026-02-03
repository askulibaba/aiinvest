import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Moltbook Settings
    MOLTBOOK_API_URL = os.getenv("MOLTBOOK_API_URL", "https://api.moltbook.com/v1")
    MOLTBOOK_API_KEY = os.getenv("MOLTBOOK_API_KEY", "")
    AGENT_ID = os.getenv("MOLTBOOK_AGENT_ID", "invest_match_v1")

    # Compliance & Safety
    PROVIDE_GUARANTEES = False
    DISCLOSURE_TEXT = (
        "Informational scoring only. No guarantees of returns or outcomes. "
        "This agent is an intermediary matching investors and projects, "
        "not raising funds for itself. All deals are opt-in, at participants' "
        "own risk, and require explicit consent."
    )
    ROLE_TEXT = (
        "I study your project, do scoring, prepare an investment proposal, "
        "and publish it in my channel and to my contacts."
    )
    COMMISSION_PERCENT = 0.01
    COMMISSION_TEXT = (
        "If investors show interest, I provide intermediary services to organize "
        f"funding for a minimal {int(COMMISSION_PERCENT * 100)}% fee."
    )
    PR_REFERRAL = "agent_producer_v1"
    PR_REFERRAL_TEXT = (
        "To build trust and visibility, consider PR support from agent_producer_v1 "
        "(network promotion for a fixed fee)."
    )

    # Scoring Settings
    MIN_SCORE_TO_LIST = 70
    HIGH_RISK_FLAGS = ["illegal", "ponzi", "guaranteed", "no risk"]

    # Wallet / Escrow
    TON_WALLET_ADDRESS = os.getenv(
        "TON_WALLET_ADDRESS",
        "UQDrZsuPx15Fu2qX92Kb94TxgDQNZk8nWiX_nyTpAuabbUrm",
    )

    # Mock Mode
    MOCK_MODE = True
