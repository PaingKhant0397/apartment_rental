from __future__ import annotations
from typing import List, TYPE_CHECKING
from .user_role import User_Role
from utils import object_to_dict, setup_logger

if TYPE_CHECKING:
    from database import Database

# Set up logger
logger = setup_logger(__name__)


class User:

    def __init__(self, role: User_Role, userID: int = None, userName: str = None, userEmail: str = None, userPassword: str = None):
        self.__userID = userID
        self.__role = role
        self.__userName = userName
        self.__userEmail = userEmail
        self.__userPassword = userPassword

    def get_userPassword(self) -> str:
        return self.__userPassword

    def set_userPassword(self, userPassword) -> None:
        self.__userPassword = userPassword

    def to_dict(self) -> dict:
        try:
            return {
                "userID": self.__userID,
                "role": object_to_dict(self.__role),
                "userName": self.__userName,
                "userEmail": self.__userEmail
            }
        except Exception as e:
            logger.error(f"Error in to_dict in User: {e}")
            raise

    def get_user_by_userName(self, db: Database, userName: str) -> 'User':
        query = "SELECT userID, userName, userEmail, userPassword, userRoleID FROM user_table WHERE userName=%s;"
        values = (userName,)
        result = db.fetch_one(query, values)

        if result:
            try:
                # Make sure 'userRoleID' is correctly used
                role = User_Role.get(db, userRoleID=int(result['userRoleID']))

                return User(
                    userID=int(result['userID']),
                    role=role,
                    userName=result['userName'],
                    userEmail=result['userEmail'],
                    userPassword=result['userPassword']
                )
            except Exception as e:
                logger.error(f"Error fetching user role: {e}")
                raise
        else:
            logger.warning(f"No user found with username: {userName}")
            return None

    def insert(self, db: Database) -> 'User':
        try:
            query = """
                INSERT INTO 
                    user_table (
                        userRoleID, 
                        userName, 
                        userEmail, 
                        userPassword
                    ) 
                VALUES 
                    (%s, %s, %s, %s)
                RETURNING 
                    userID, userRoleID, userName, userEmail;
            """
            values = (self.__role.get_userRoleID(), self.__userName,
                      self.__userEmail, self.__userPassword)
            result = db.insert(query, values)

            if result:
                role = User_Role.get(db, userRoleID=result['userroleid'])

                return User(
                    userID=result['userid'],
                    role=role,
                    userName=result['username'],
                    userEmail=result['useremail'],
                )
            else:
                logger.warning("User insertion failed: No result returned")
                return None
        except Exception as e:
            logger.error(f"Unexpected error during user registration: {e}")
            raise

    @staticmethod
    def get(db: Database, UserID: int) -> 'User':
        # Implement error handling and logging
        pass

    @staticmethod
    def delete(db: Database, UserID: int) -> None:
        # Implement error handling and logging
        pass

    @staticmethod
    def all(db: Database) -> List['User']:
        # Implement error handling and logging
        pass
