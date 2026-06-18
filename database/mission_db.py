from mysql.connector import IntegrityError

from database.executes_queries import QueryExecute
from database.agent_db import AgentNotFoundError
from logger import get_logger


logger = get_logger(__name__)
executer = QueryExecute()


class MissionNotFoundError(Exception):
    pass


class MissionDB:
    @staticmethod
    def create_mission(data: dict) -> int:
        return executer.create_query(
            """ INSERT INTO missions
                (title, description, location, difficulty, importance, risk_level)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, tuple(data.values())
        )


    @staticmethod
    def get_all_missions() -> list[dict]:
        return executer.get_query(
            "SELECT * FROM missions"
        )
    

    @staticmethod
    def get_mission_by_id(mission_id) -> dict:
        return executer.get_query(
            "SELECT * FROM missions WHERE id = %s",
            ( mission_id,),
            one=True
        )



    @staticmethod
    def assign_mission(m_id, a_id) -> bool:
        return executer.update_query(
            "UPDATE missions SET assigned_agent_id = %s  WHERE id = %s",
            (a_id, m_id)
        )
    


    @staticmethod
    def update_mission_status(mission_id: int, status: str) -> bool:
        return executer.update_query(
            "UPDATE missions SET status = %s  WHERE id = %s",
            (status, mission_id)
        )
    

    
    @staticmethod
    def get_open_missions_by_agent(agent_id: int) -> list[dict]:
        executer.get_query(
            """SELECT * FROM missions
            WHERE assigned_agent_id = %s AND status = %s OR status = %s""",
             (agent_id, 'ASSIGNED', 'IN_PROGRESS')
        )

    

    @staticmethod
    def count_all_missions() -> int:
        return executer.get_query(
            "SELECT COUNT(*) AS total_missions FROM missions",
            one=True
        ).get('total_missions')

    
    @staticmethod
    def count_by_status(status: str) -> int:
        return executer.get_query(
            "SELECT COUNT(*) AS total_missions FROM missions WHERE status = %s",
            (status,),
            one=True
        ).get('total_missions')


    @staticmethod
    def count_open_missions() -> int:
        return executer.get_query( """
            COUNT(*) AS total_missions FROM missions
            WHERE status = %s OR status = %s
            """,
            ('ASSIGNED', 'IN_PROGRESS'),
            one=True
        ).get('total_missions')
    

    @staticmethod
    def count_critical_missions() -> int:
        return executer.get_query("""
            COUNT(*) AS total_missions FROM missions
            WHERE risk_level = CRITICAL 
            """, ('ASSIGNED', 'IN_PROGRESS'),
            one=True
        ).get('total_missions')
        