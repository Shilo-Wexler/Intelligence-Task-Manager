from database.agent_db import AgentDB
from logger import get_logger


logger = get_logger(__name__)


class AgentNotFoundError(Exception):
    pass


def add_agent(body: dict) -> dict:
    agent_id = AgentDB.create_agent(body)
    return AgentDB.get_agent_by_id(agent_id)


def get_all_agents() -> list[dict]:
    return AgentDB.get_all_agents()


def get_agent_by_id(agent_id: int) -> dict:
    agent = AgentDB.get_agent_by_id(agent_id)
    if not agent:
        raise AgentNotFoundError("There is no agent with ID number %s.", agent_id)
    return agent


def get_agent_performance(agent_id: int) -> dict:
    performance = AgentDB.get_agent_performance(agent_id)
    if not performance:
        raise AgentNotFoundError("There is no agent with ID number %s.", agent_id)
    return performance


def update_agent_data(agent_id: int, body: dict) -> None:
    details = body.model_dump(exclude_unset=True)
    is_update = AgentDB.update_agent(agent_id, details)
    if not is_update:
        raise AgentNotFoundError("There is no agent with ID number %s.", agent_id)


def deactivate_agent(agent_id: int) -> None:
    is_update = AgentDB.deactivate_agent(agent_id)
    if not is_update:
        raise AgentNotFoundError("There is no agent with ID number %s.", agent_id)
