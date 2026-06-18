from fastapi import FastAPI
import uvicorn

from logger import get_logger
from routes import agent_routes, mission_routes, report_routes


logger = get_logger(__name__)
app = FastAPI()

app.include_router(
    router=agent_routes.router,
    prefix='/agents',
    tags=['The Agents Section']
)
app.include_router(
    router=mission_routes.router,
    prefix='/missions',
    tags=['The Mission Section']
)
app.include_router(
    router=report_routes.router,
    prefix='/reports',
    tags=['The Reports Section']
)



if __name__ == '__main__':
    try:
        uvicorn.run('main:app', host='localhost', port=8000, reload=True)
    except Exception as e:
        logger.critical(f'Server upload failure: {e}')
