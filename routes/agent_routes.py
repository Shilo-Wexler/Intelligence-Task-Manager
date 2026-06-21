from fastapi import APIRouter, HTTPException

from logger import get_logger
from services import agent_service
from services.agent_service import AgentNotFoundError
from schemas.agents_schema import NewAgent, UpdateAgent


logger = get_logger(__name__)

router = APIRouter()


@router.post('', status_code=201)
def add_agent(body: NewAgent):
    try:
        agent = body.model_dump()
        logger.info("add agent with ditailes %s", body)
        return agent_service.add_agent(agent)
    except AgentNotFoundError as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail=f"{e}")


@router.get('')
def get_all_agents():
    logger.info("sending all agents")
    return agent_service.get_all_agents()


@router.get('/{agent_id}')
def get_agent_by_id(agent_id: int):
    try:
        logger.info("searching for agent id: %s", agent_id)
        agent = agent_service.get_agent_by_id(agent_id)
        logger.info("returning agent %s", agent)
        return agent
    except AgentNotFoundError as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail=f"{e}")


@router.get('/{agent_id}/performance')
def get_agent_performance(agent_id: int):
    try:
        logger.info("searching for agent id: %s", agent_id)
        agent = agent_service.get_agent_performance(agent_id)
        logger.info("returning performance %s", agent)
        return agent
    except AgentNotFoundError as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail=f"{e}")


@router.put('/{agent_id}')
def update_agent_data(agent_id: int, body: UpdateAgent):
    try:
        detail = body.model_dump(exclude_unset=True)
        logger.info("searching for agent id: %s for updating %s", agent_id, body)
        agent_service.update_agent_data(agent_id, detail)
        logger.info("agent updated successfully")
    except AgentNotFoundError as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail=f"{e}")


@router.put('/{agent_id}/deactivate')
def deactivate_agent(agent_id: int):
    try:
        logger.info("searching for agent id: %s", agent_id)
        agent_service.deactivate_agent(agent_id)
        logger.info("agent deactivate successfully")
    except AgentNotFoundError as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail=f"{e}")
