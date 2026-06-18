from fastapi import APIRouter, HTTPException

from logger import get_logger
from schemas.mission_schema import UpdateAgent, NewMission
from services import mission_service
from services.mission_service import (
    MissionCanNotBeExcError, MissionNotFoundError, AgentNotFoundError
    )


logger = get_logger(__name__)
router = APIRouter()


@router.post('', status_code=201)
def add_mission(body: NewMission) -> dict:
    mission = body.model_dump()
    return mission_service.add_mission(mission)
    

@router.get('')
def get_all_missions():
    return mission_service.get_all_missions()


@router.get('/{mission_id}')
def get_mission_by_id(mission_id: int):
    try:
        return mission_service.get_mission_by_id(mission_id)
    except MissionNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"{e}")


@router.put('/{mission_id}/assign/{agent_id}')
def assign_mission(mission_id: int, agent_id: int):
    try:
        mission_service.assign_mission(mission_id, agent_id)
    except MissionNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"{e}")
    except AgentNotFoundError as e: 
        raise HTTPException(status_code=404, detail=f"{e}")
    except MissionCanNotBeExcError as e:
        raise HTTPException(status_code=404, detail=f"{e}")

@router.put('/{mission_id}/start')
def start_mission(mission_id: int):
    try:
        mission_service.start_mission(mission_id)
    except MissionNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"{e}")
    

@router.put('/{mission_id}/complete')
def set_mission_to_complete(mission_id: int):
    try:
        mission_service.set_mission_to_complete(mission_id)
    except MissionNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"{e}")


@router.put('/{mission_id}/fail')
def set_mission_to_fail(mission_id: int):
    try:
        mission_service.set_mission_to_fail(mission_id)
    except MissionNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"{e}")



@router.put('/{mission_id}/cancel')
def cancel_mission(mission_id: int):
    try:
        mission_service.cancel_mission(mission_id)
    except MissionNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"{e}")
    except MissionCanNotBeExcError as e:
        raise HTTPException(status_code=400, detail=f"{e}")

