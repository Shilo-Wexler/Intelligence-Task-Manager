from fastapi import APIRouter

from logger import get_logger


logger = get_logger(__name__)

router = APIRouter()


@router.post('', status_code=201)
def add_agent(body):
    pass


@router.get('')
def get_all_agents():
    pass


@router.get('/{agent_id}')
def get_agent_by_id(agent_id: int):
    pass


@router.get('/{agent_id}/performance')
def get_agent_performance(agent_id: int):
    pass


@router.put('/{agent_id}')
def update_agent_data(agent_id: int, body):
    pass


@router.put('/{agent_id}/deactivate')
def deactivate_agent(agent_id: int):
    pass