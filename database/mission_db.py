from mysql.connector import IntegrityError

from database.connection_db import ConnectionDB
from database.agent_db import AgentNotFoundError
from logger import get_logger


logger = get_logger(__name__)


class MissionNotFoundError(Exception):
    pass


class MissionDB:
    @staticmethod
    def create_mission(data: dict) -> dict:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        logger.debug("Starting the process of adding a mission with data: %s", data)
        try:
            level_risk = data.get('difficulty') * 2 + data.get('importance')
            cursor.execute("""
                INSERT INTO missions 
                (title, description, location, difficulty, importance, risk_level)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                tuple(data.values()) + (level_risk,)
            )
            connection.commit()
            agent_id = cursor.lastrowid
            return MissionDB.get_mission_by_id(agent_id)
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")


    @staticmethod
    def get_all_missions() -> list[dict]:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("SELECT * FROM missions")
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.") 
    

    def get_mission_by_id(mission_id) -> dict:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM missions WHERE id = %s",( mission_id,))
            mission = cursor.fetchone()
            if not mission:
                raise MissionNotFoundError(f"No mission exists with ID: {mission_id}")
            return mission
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")


    def assign_mission(m_id, a_id) -> None:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("UPDATE missions SET assigned_agent_id = %s  WHERE id = %s", (a_id, m_id))
            connection.commit()
            if  cursor.rowcount < 0:
                raise MissionNotFoundError(f"No agent exists with ID: {m_id}")
        except IntegrityError as e:
            logger.error("No agent exists with ID: %s, Error: %s",a_id, e)
            if e.errno == 1452:
                raise AgentNotFoundError(f"No mission exists with ID: {a_id}")
            raise
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")  


    @staticmethod
    def update_mission_status(mission_id: int, status: str) -> None:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("UPDATE missions SET status = %s  WHERE id = %s", (status, mission_id))
            connection.commit()
            if  cursor.rowcount < 0:
                raise MissionNotFoundError(f"No mission exists with ID: {mission_id}")
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.") 

    
    @staticmethod
    def get_open_missions_by_agent(agent_id: int) -> list[dict]:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT * FROM missions
                WHERE assigned_agent_id = %s
                AND status = %s OR status = %s
                """, (agent_id, 'ASSIGNED', 'IN_PROGRESS')
            )
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")
    

    @staticmethod
    def count_all_missions() -> int:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT COUNT(*) AS total_missions FROM missions")
            return cursor.fetchone().get('total_missions')
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")

    
    @staticmethod
    def count_by_status(status: str) -> int:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT COUNT(*) AS total_missions FROM missions WHERE status = %s", (status,))
            return cursor.fetchone().get('total_missions')
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")


    @staticmethod
    def count_open_missions() -> int:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("""
                COUNT(*) AS total_missions FROM missions
                WHERE status = %s OR status = %s
                """, ('ASSIGNED', 'IN_PROGRESS')
            )
            return cursor.fetchone().get('total_missions')
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")

    




