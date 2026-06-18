from fastapi import APIRouter

from logger import get_logger


logger = get_logger(__name__)
router = APIRouter()


@router.get('/summary')
def get_general_report():
    pass


@router.get('/missions-by-status')
def get_missions_by_status():
    pass


@router.get('/top-agent')
def get_top_agent():
    pass