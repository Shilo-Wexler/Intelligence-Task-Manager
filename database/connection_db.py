import mysql.connector

from logger import get_logger
from database.tables import CREATE_AGENTS_TABLE, CREATE_MISSIONS_TABLE


logger = get_logger(__name__)


class ConnCreateError(Exception):
    pass


class ConnectionDB:
    @staticmethod
    def get_connection() -> mysql.connector.connect:
        try:
            return mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='1234',
                database='Intelligence_db',
            )
        except Exception as e:
            logger.critical("Failed to establish connection: %s", e)
            raise ConnCreateError()
    

    @staticmethod
    def create_database() -> None:
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='1234',
                database='Intelligence_db',
            )
        except Exception as e:
            logger.critical("Failed to establish connection: %s", e)
            raise ConnCreateError()
        cursor = connection.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS Intelligence_db")
            logger.info("The Intelligence_db database was successfully created.")
            connection.commit()
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")

    


    @staticmethod
    def create_tables() -> None:
        connection = ConnectionDB.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(CREATE_AGENTS_TABLE)
            connection.commit()
            logger.debug("Passed the agent table creation stage.")
            cursor.execute(CREATE_MISSIONS_TABLE)
            connection.commit()
            logger.debug("Passed the missions table creation stage.")
            logger.info("The tables were created successfully.")
        except Exception as e:
            logger.critical("Failed to establish connection: %s", e)
            raise ConnCreateError()
        finally:
            cursor.close()
            connection.close()
            logger.debug("The connections are closed.")






