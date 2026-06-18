from fastapi import APIRouter

from logger import get_logger


logger = get_logger(__name__)
router = APIRouter()


@router.post('')
def add_mission(body):
    pass


@router.get('')
def get_all_missions():
    pass


@router.get('/{mission_id}')
def get_mission_by_id(mission_id: int):
    pass


@router.put('/{mission_id}/assign/{agent_id}')
def assign_mission(mission_id: int, agent_id: int):
    pass


@router.put('/{mission_id}/start ')
def start_mission(mission_id: int):
    pass


@router.put('/{mission_id}/complete')
def set_mission_to_complete(mission_id: int):
    pass


@router.put('/{mission_id}/fail')
def set_mission_to_fail(mission_id: int):
    pass



@router.put('/{mission_id}/cancel')
def cancel_mission(mission_id: int):
    pass

