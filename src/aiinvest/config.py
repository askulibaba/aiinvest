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
        "Intermediary only: connects investor-agents with project-agents. "
        "No custody of funds unless both parties opt into escrow."
    )
    COMMISSION_PERCENT = 0.02
    COMMISSION_TEXT = (
        "Service fee: minimal commission "
        f"{int(COMMISSION_PERCENT * 100)}% of investment amount."
    )

    # Scoring Settings
    MIN_SCORE_TO_LIST = 70
    HIGH_RISK_FLAGS = ["illegal", "ponzi", "guaranteed", "no risk"]

    # Wallet / Escrow
    TON_WALLET_ADDRESS = os.getenv(
        "TON_WALLET_ADDRESS",
        "UQAKuar-CzcT6LhPFimR3bkFKxZKQFCtIZiDV511ZltgmQtN",
    )

    # Mock Mode
    MOCK_MODE = True
