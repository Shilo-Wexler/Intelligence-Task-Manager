from database.agent_db import AgentDB
from database.mission_db import MissionDB


def get_top_agent():
    return AgentDB.get_top_agent()


def get_general_report():
    return {
        "active_agents_count": AgentDB.count_active_agents(),
        "total_missions": MissionDB.count_all_missions(),
        "open_missions": MissionDB.count_open_missions(),
        "completed_missions": MissionDB.count_by_status("NEW"),
        "failed_missions": MissionDB.count_by_status("FAIL"),
        "critical_missions": MissionDB.count_critical_missions()
    }

def get_by_status(st: str):
    return  MissionDB.count_by_status(st)

