import database.connection_db as conn
from database.agent_db import AgentDB
from database.mission_db import MissionDB

print(MissionDB.get_mission_by_id(3))

print(MissionDB.assign_mission(3,3))