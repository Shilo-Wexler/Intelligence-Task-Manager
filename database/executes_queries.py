from typing import Any

from database.connection_db import ConnectionDB
from logger import get_logger


logger = get_logger(__name__)


class QueryExecute:
    def __init__(self):
        self.connection = ConnectionDB.get_connection()
    

    def create_query(self, query: str, params: tuple) -> int | None:
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            logger.debug("The cursor is closed.") 
    


    def update_query(self, query: str, params: tuple) -> bool:
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            logger.debug("The cursor is closed.") 



    def get_query(self, query: str, params: tuple = tuple(), one: bool=False) -> Any:
        try:
            cursor = self.connection.cursor(dictionary=True)

            cursor.execute(query, params)

            if one:
                return cursor.fetchone()
            return cursor.fetchall()
        finally:
            cursor.close()
            logger.debug("The cursor is closed.") 



