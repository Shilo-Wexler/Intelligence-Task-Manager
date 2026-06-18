import database.connection_db as conn
from database.agent_db import AgentDB
from database.executes_queries import QueryExecute


a = QueryExecute()
print(AgentDB.create_agent({"name": "shimon", "specialty":"nothing", "agent_rank": "Junior"}))
print(a.get_query("SELECT *  FROM agents WHERE id = 3",one=True))
print("result", AgentDB.get_all_agents())
