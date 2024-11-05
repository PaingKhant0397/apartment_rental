from __future__ import annotations
from typing import List, TYPE_CHECKING
from utils import setup_logger
if TYPE_CHECKING:
    from database import Database
logger = setup_logger(__name__)


class Admin:

    def __init__(self, admin_id: int = None, admin_username: str = None,  admin_password: str = None, role: str = 'admin'):
        self.__admin_id = admin_id
        self.__admin_username = admin_username
        self.__admin_password = admin_password
        self.__role = role

    def to_dict(self) -> dict:
        return {
            'admin_id': self.__admin_id,
            'role': self.__role,
            'admin_username': self.__admin_username
        }

    def get_admin_role(self) -> str:
        return self.__role

    def get_admin_id(self) -> int:
        return self.__admin_id

    def get_admin_username(self) -> str:
        return self.__admin_username

    def get_admin_password(self) -> str:
        return self.__admin_password

    def set_admin_password(self, admin_password: str) -> None:
        self.__admin_password = admin_password

    @classmethod
    def get_by_username(cls, db: Database, admin_username: str):
        try:
            query = """SELECT 
                            admin_id,
                            admin_username,
                            admin_password 
                        FROM 
                            admin_table 
                        WHERE 
                            admin_username=%s"""
            values = (admin_username,)
            result = db.fetch_one(query, values)
            if result:
                return cls(
                    admin_id=result['admin_id'],
                    admin_username=result['admin_username'],
                    admin_password=result['admin_password'],
                )

        except Exception as e:
            raise Exception(f"Error getting user by username: {e}")

    def insert(self, db: Database) -> 'Admin':
        try:
            query = """
                INSERT INTO admin_table (admin_username, admin_password)
                VALUES (%s, %s)
                RETURNING admin_id, admin_username;
            """
            values = (self.__admin_username, self.__admin_password)
            result = db.insert(query, values)

            if result:
                return Admin(
                    admin_id=result['admin_id'],
                    admin_username=result['admin_username'],
                )
            else:
                logger.warning("Admin insertion failed: No result returned")
                return None
        except Exception as e:
            logger.error(f"Error during admin registration: {e}")
            raise Exception(f"Error during admin registration: {e}")
