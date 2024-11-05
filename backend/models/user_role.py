from __future__ import annotations
from typing import List, TYPE_CHECKING
from utils import setup_logger, object_to_dict

if TYPE_CHECKING:
    from database import Database

# Set up logger
logger = setup_logger(__name__)


class User_Role:

    def __init__(self, user_role_id: int = None, user_role_name: str = None):
        self.__user_role_id = user_role_id
        self.__user_role_name = user_role_name

    def to_dict(self) -> dict:
        try:
            return {
                "user_role_id": self.__user_role_id,
                "user_role_name": self.__user_role_name,
            }
        except Exception as e:
            logger.error(f"Error in to_dict in User_Role: {e}")
            raise

    def get_user_role_id(self) -> int:
        return self.__user_role_id

    def get_user_role_name(self) -> str:
        return self.__user_role_name

    @staticmethod
    def get_by_id(db: Database, user_role_id: int) -> 'User_Role':
        """
            Get User Role by user_role_id
        """
        try:
            query = "SELECT user_role_id, user_role_name FROM user_role WHERE user_role_id = %s;"
            values = (user_role_id,)
            result = db.fetch_one(query, values)

            if result:
                return User_Role(
                    user_role_id=int(result['user_role_id']),
                    user_role_name=result['user_role_name']
                )
            else:
                logger.warning(
                    f"No user role found with user_role_id: {user_role_id}")
                return None
        except Exception as e:
            logger.error(f"Error getting user role in User_Role: {e}")
            raise

    @staticmethod
    def all(db: Database) -> List['User_Role']:
        """
            Get all User Roles
        """
        try:
            query = "SELECT user_role_id, user_role_name FROM user_role;"
            results = db.fetch_all(query)

            return [User_Role(user_role_id=result['user_role_id'], user_role_name=result['user_role_name']) for result in results]
        except Exception as e:
            logger.error(f"Error retrieving all user roles: {e}")
            raise
