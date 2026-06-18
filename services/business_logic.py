from logger import get_logger
from database.mission_db import MissionDB


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


def is_active_agent(agent: dict) -> bool:
    return agent.get('is_active')


def agent_has_more_than_3_missions(agent: dict) -> bool:
    return MissionDB.count_open_missions_per_agent(agent.get('id')) >= 3


def is_risk_level_match_role(agent: dict, mission: dict) -> bool:
    return (mission.get('risk_level') != 'CRITICAL' or
            agent.get('agent_rank') == 'Commander')


def is_mission_status_allow_start(mission: dict) -> bool:
    return mission.get('status') in {'ASSIGNED', 'IN_PROGRESS'}


def is_mission_status_allow_finish(mission: dict) -> bool:
    return mission.get('status') == 'IN_PROGRESS'


def is_mission_can_be_canceled(mission: dict) -> bool:
    return mission.get('status') in {'ASSIGNED', 'NEW'}
    

