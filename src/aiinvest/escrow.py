import logging
from typing import Dict
from .config import Config

logger = logging.getLogger(__name__)


class EscrowContract:
    """
    Заглушка для управления эскроу‑контрактом.
    Реальная интеграция с TON должна включать:
    - создание контракта,
    - депозиты сторон,
    - условия выплат,
    - арбитраж по спорам.
    """

    def __init__(self) -> None:
        self.wallet = Config.TON_WALLET_ADDRESS

    def prepare_deal(self, investor_id: str, project_id: str, amount: float) -> Dict:
        logger.info(
            "Preparing escrow deal investor=%s project=%s amount=%s",
            investor_id,
            project_id,
            amount,
        )
        return {
            "escrow_address": "EQD_FAKE_ESCROW_ADDRESS",
            "amount": amount,
            "currency": "TON",
            "terms": "Release funds on milestone confirmation. No guarantees.",
        }
