from database.connection_db import ConnectionDB
from logger import get_logger


logger = get_logger(__name__)


class AgentNotFoundError(Exception):
    pass

class AgentDB:
    @staticmethod
    def get_all_agents() -> list[dict]:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("SELECT * FROM agents")
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.") 

    @staticmethod
    def get_agent_by_id(agent_id) -> dict:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("SELECT * FROM agents WHERE id = %s",( agent_id,))
            agent = cursor.fetchone()
            if not agent:
                raise AgentNotFoundError(f"No agent exists with ID: {agent_id}")
            return agent
            
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")


    @staticmethod
    def create_agent(data: dict) -> dict:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        logger.debug("Starting the process of adding an agent with data: %s", data)
        try:
            cursor.execute("INSERT INTO agents (name, specialty, agent_rank) VALUES (%s, %s, %s)", tuple(data.values()))
            connection.commit()
            agent_id = cursor.lastrowid
            return AgentDB.get_agent_by_id(agent_id)
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.") 


        
    @staticmethod
    def update_agent(agent_id: int, data: dict) -> bool:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            for k, v in data.items():
                quary = f"UPDATE agents SET {k} = %s WHERE id = %s"
                cursor.execute(quary, (v, agent_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")
    
    @staticmethod
    def deactivate_agent(agent_id: int) -> bool:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("UPDATE agents SET is_active = FALSE  WHERE id = %s", (agent_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")
    

    @staticmethod
    def increment_completed(agent_id: int) -> bool:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("UPDATE agents SET completed_missions = completed_missions + 1  WHERE id = %s", (agent_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")
    

    def increment_failed(agent_id: int) -> bool:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("UPDATE agents SET failed_missions = failed_missions + 1  WHERE id = %s", (agent_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")
    

    @staticmethod
    def get_agent_performance(agent_id: int) -> dict:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("SELECT completed_missions, failed_missions FROM agents WHERE id = %s", (agent_id,))
            result = cursor.fetchone()
            completed = result.get('completed_missions')
            failed = result.get('failed_missions')
            total_missions = completed + failed
            return {
                'completed': result.get('completed_missions'),
                'failed' : result.get('failed_missions'),
                'success_rate': round((completed / total_missions) * 100, 2)
            }
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")
    

    def count_active_agents() -> int:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("SELECT COUNT(*) AS total_active FROM agents WHERE is_active = TRUE;")
            return cursor.fetchone().get('total_active')
        
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")
    