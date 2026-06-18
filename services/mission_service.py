from database.mission_db import MissionDB
from database.agent_db import AgentDB
import services.business_logic as rules



class MissionNotFoundError(Exception):
    pass


class AgentNotFoundError(Exception):
    pass


class MissionCanNotBeExcError(Exception):
    pass


def add_mission(body: dict) -> dict:
    risk_level = rules._calculate_risk_level(body)
    body['risk_level'] = risk_level
    mission_id = MissionDB.create_mission(body)
    return MissionDB.get_mission_by_id(mission_id)


def get_all_missions() -> list[dict]:
    return MissionDB.get_all_missions()


def get_mission_by_id(mission_id: int) -> dict:
    mission = MissionDB.get_mission_by_id(mission_id)
    if not mission:
        raise MissionNotFoundError()
    return mission


def assign_mission(mission_id: int, agent_id: int) -> None:
    mission = MissionDB.get_mission_by_id(mission_id)
    agent = AgentDB.get_agent_by_id(agent_id)
    if not mission:
        raise MissionNotFoundError()
    if not agent:
        raise AgentNotFoundError()

    if not rules.is_active_agent(agent):
        raise MissionCanNotBeExcError()
    
    if not rules.is_mission_status_allow_start(mission):
        raise MissionCanNotBeExcError()
    
    if rules.agent_has_more_than_3_missions():
        raise MissionCanNotBeExcError()
    
    if not rules.is_risk_level_match_role(agent, mission):
        raise MissionCanNotBeExcError()
    
    MissionDB.assign_mission(mission_id, agent_id)


def start_mission(mission_id: int) -> None:
    is_update = MissionDB.update_mission_status(mission_id, "IN_PROGRESS")
    if not is_update:
        raise MissionNotFoundError
    

def set_mission_to_complete(mission_id: int):
    mission = MissionDB.get_mission_by_id(mission_id)
    if not mission:
        raise MissionNotFoundError()
    agent_id = mission.get('assigned_agent_id')
    MissionDB.update_mission_status(mission_id, 'COMPLETE')
    AgentDB.increment_completed(agent_id)


def set_mission_to_fail(mission_id: int):
    mission = MissionDB.get_mission_by_id(mission_id)
    if not mission:
        raise MissionNotFoundError()
    agent_id = mission.get('assigned_agent_id')
    MissionDB.update_mission_status(mission_id, 'FAIL')
    AgentDB.increment_failed(agent_id)


def cancel_mission(mission_id: int):
    mission = MissionDB.get_mission_by_id(mission_id)
    if not mission:
        raise MissionNotFoundError()
    if not rules.is_mission_can_be_canceled(mission):
        raise MissionCanNotBeExcError

    MissionDB.update_mission_status(mission_id, 'CANCEL')














 
 
    

