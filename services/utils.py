from logger import get_logger


logger = get_logger(__name__)


def _calculate_risk_level(data: dict) -> str:
    try:
        level_risk_num = data.get('difficulty') * 2 + data.get('importance')
    except TypeError as e:
        logger.error(e)
        raise
    if level_risk_num < 10:
        return "LOW"
    if level_risk_num < 18:
        return "MEDIUM"
    if level_risk_num < 25:
        return "HIGH"
    return "CRITICAL"


def _rating_verification(rating: int) -> bool:
    return 0 < rating < 11



