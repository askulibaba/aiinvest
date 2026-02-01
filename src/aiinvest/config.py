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
        "This is informational scoring only. No guarantees of returns. "
        "All deals are opt-in and at participants' own risk."
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
