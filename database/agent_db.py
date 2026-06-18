from database.executes_queries import QueryExecute
from logger import get_logger


logger = get_logger(__name__)
executer = QueryExecute()


class AgentDB:
    @staticmethod
    def create_agent(data: dict) -> int:
        logger.debug("Starting the process of adding an agent with data: %s", data)
        return executer.create_query(
            "INSERT INTO agents (name, specialty, agent_rank) VALUES (%s, %s, %s)",
            tuple(data.values())
        )

    @staticmethod
    def get_all_agents() -> list[dict]:
        return executer.get_query("SELECT * FROM agents")


    @staticmethod
    def get_agent_by_id(agent_id) -> dict:
        return executer.get_query(
            "SELECT * FROM agents WHERE id = %s",
            ( agent_id,),
            one=True
        )

        
    @staticmethod
    def update_agent(agent_id: int, data: dict) -> bool:
        is_updated = 0
        for k, v in data.items():
            is_updated += executer.update_query(
                f"UPDATE agents SET {k} = %s WHERE id = %s",
                (v, agent_id)
            )    
        return is_updated > 0


    @staticmethod
    def deactivate_agent(agent_id: int) -> bool:
        return executer.update_query(
            "UPDATE agents SET is_active = FALSE  WHERE id = %s",
            (agent_id,)
        )
    

    @staticmethod
    def increment_completed(agent_id: int) -> bool:
        return executer.update_query(
            "UPDATE agents SET completed_missions = completed_missions + 1  WHERE id = %s",
            (agent_id,)
        )


    @staticmethod
    def increment_failed(agent_id: int) -> bool:
        return executer.update_query(
            "UPDATE agents SET failed_missions = failed_missions + 1  WHERE id = %s",
            (agent_id,)
        )
    

    @staticmethod
    def get_agent_performance(agent_id: int) -> dict | None:
        agent_ditails = executer.get_query(
            "SELECT completed_missions, failed_missions FROM agents WHERE id = %s",
            (agent_id,),
            one=True
        )
        if agent_ditails is None:
            return None
        
        completed = agent_ditails.get('completed_missions')
        failed = agent_ditails.get('failed_missions')
        total_missions = completed + failed

        return {
            'completed': completed,
            'failed': failed,
            'total': total_missions,
            'success_rate': round((completed / total_missions) * 100, 2),
        }
    

    @staticmethod
    def count_active_agents() -> int:
        return executer.get_query(
            "SELECT COUNT(*) AS total_active FROM agents WHERE is_active = TRUE",
            one=True
        ).get('total_active')


    @staticmethod
    def get_top_agent() -> dict:
        return executer.get_query(
            "SELECT * FROM agents ORDER BY completed_missions DESC LIMIT 1",
            one=True
        )

