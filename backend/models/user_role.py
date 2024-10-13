from __future__ import annotations
from typing import List, TYPE_CHECKING
from utils import setup_logger, object_to_dict

if TYPE_CHECKING:
    from database import Database

# Set up logger
logger = setup_logger(__name__)


class User_Role:

    def __init__(self, userRoleID: int = None, userRoleName: str = None):
        self.__userRoleID = userRoleID
        self.__userRoleName = userRoleName

    def to_dict(self) -> dict:
        try:
            return {
                "userRoleID": self.__userRoleID,
                "userRoleName": self.__userRoleName,
            }
        except Exception as e:
            logger.error(f"Error in to_dict in User: {e}")
            raise

    def get_userRoleID(self) -> int:
        return self.__userRoleID

    def get_userRoleName(self) -> str:
        return self.__userRoleName

    @staticmethod
    def get(db: Database, userRoleID: int) -> 'User_Role':
        """
            Get User Role by userRoleID
        """

        try:
            query = "SELECT userRoleID, userRoleName FROM user_role WHERE userRoleID = %s;"
            values = (userRoleID,)
            result = db.fetch_one(query, values)

            if result:
                return User_Role(
                    userRoleID=result['userroleid'],
                    userRoleName=result['userrolename']
                )
            else:
                logger.warning(
                    f"No user role found with userRoleID: {userRoleID}")
                return None
        except Exception as e:
            logger.error(f"Error getting user role in User_Role: {e}")
            raise

    @staticmethod
    def all(db: Database) -> List['User_Role']:
        """
            Get all User roles
        """
        try:
            query = "SELECT userRoleID, userRoleName FROM user_role;"
            results = db.fetch_all(query)

            return [User_Role(userRoleID=result['userroleid'], userRoleName=result['userrolename']) for result in results]
        except Exception as e:
            logger.error(f"Error retrieving all user roles: {e}")
            raise
