from dataclasses import dataclass
from typing import Dict, List
from .config import Config


@dataclass
class ScoreResult:
    score: int
    reasons: List[str]
    flags: List[str]


def score_project(text: str) -> ScoreResult:
    """
    Простая эвристика. В реальной версии сюда добавляется LLM-анализ,
    финансовые метрики, верификация транзакций и т.д.
    """
    text_lower = text.lower()
    score = 50
    reasons: List[str] = []
    flags: List[str] = []

    if "revenue" in text_lower or "ton/mo" in text_lower:
        score += 15
        reasons.append("Есть признаки выручки.")

    if "legal" in text_lower or "compliant" in text_lower:
        score += 10
        reasons.append("Заявлена легальность.")

    if "churn" in text_lower or "retention" in text_lower:
        score += 5
        reasons.append("Упомянута удерживаемость.")

    for flag in Config.HIGH_RISK_FLAGS:
        if flag in text_lower:
            flags.append(flag)
            score -= 25

    score = max(0, min(100, score))
    return ScoreResult(score=score, reasons=reasons, flags=flags)
