from fastapi import APIRouter

from logger import get_logger
from services import report_service


logger = get_logger(__name__)
router = APIRouter()


@router.get('/summary')
def get_general_report():
    return report_service.get_general_report()


@router.get('/missions-by-status')
def get_missions_by_status(stetus: str):
    return report_service.get_by_status(stetus)
    


@router.get('/top-agent')
def get_top_agent():
    return report_service.get_top_agent()