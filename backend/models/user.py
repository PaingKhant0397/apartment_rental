from __future__ import annotations
from typing import List, TYPE_CHECKING
from .user_role import User_Role
from utils import object_to_dict, setup_logger

if TYPE_CHECKING:
    from database import Database

# Set up logger
logger = setup_logger(__name__)


class User:

    def __init__(self, role: User_Role, user_id: int = None, user_name: str = None, user_email: str = None, user_password: str = None):
        self.__user_id = user_id
        self.__role = role
        self.__user_name = user_name
        self.__user_email = user_email
        self.__user_password = user_password

    def get_user_id(self) -> int:
        return self.__user_id

    def get_role(self) -> User_Role:
        return self.__role

    def get_user_name(self) -> str:
        return self.__user_name

    def get_user_email(self) -> str:
        return self.__user_email

    def get_user_password(self) -> str:
        return self.__user_password

    def set_user_password(self, user_password: str) -> None:
        self.__user_password = user_password

    def to_dict(self) -> dict:
        try:
            return {
                "user_id": self.__user_id,
                "role": self.__role.to_dict(),
                "user_name": self.__user_name,
                "user_email": self.__user_email
            }
        except Exception as e:
            logger.error(f"Error in to_dict in User: {e}")
            raise Exception(f"Error in converting User to dict: {e}")

    @classmethod
    def get_by_email(cls, db: Database, email: str) -> 'User':
        try:
            query = "SELECT user_id, user_name, user_email, user_password, user_role_id FROM user_table WHERE user_email=%s;"
            values = (email,)
            result = db.fetch_one(query, values)

            if result:
                role = User_Role.get_by_id(
                    db, user_role_id=int(result['user_role_id']))
                return cls(
                    user_id=int(result['user_id']),
                    role=role,
                    user_name=result['user_name'],
                    user_email=result['user_email'],
                    user_password=result['user_password']
                )
            else:
                logger.warning(f"No user found with email: {email}")
                return None
        except Exception as e:
            logger.error(f"Error fetching user by email: {e}")
            raise Exception(f"Error fetching user by email: {e}")

    @classmethod
    def get_user_by_id(cls, db: Database, user_id: int) -> 'User':
        try:
            query = "SELECT user_id, user_name, user_email, user_password, user_role_id FROM user_table WHERE user_id=%s;"
            values = (user_id,)
            result = db.fetch_one(query, values)

            if result:
                role = User_Role.get_by_id(
                    db, user_role_id=int(result['user_role_id']))
                return cls(
                    user_id=int(result['user_id']),
                    role=role,
                    user_name=result['user_name'],
                    user_email=result['user_email'],
                    user_password=result['user_password']
                )
            else:
                logger.warning(f"No user found with user_id: {user_id}")
                return None
        except Exception as e:
            logger.error(f"Error fetching user by ID: {e}")
            raise Exception(f"Error fetching user by ID: {e}")

    def get_user_by_user_name(self, db: Database, user_name: str) -> 'User':
        try:
            query = "SELECT user_id, user_name, user_email, user_password, user_role_id FROM user_table WHERE user_name=%s;"
            values = (user_name,)
            result = db.fetch_one(query, values)

            if result:
                role = User_Role.get_by_id(
                    db, user_role_id=int(result['user_role_id']))
                return User(
                    user_id=int(result['user_id']),
                    role=role,
                    user_name=result['user_name'],
                    user_email=result['user_email'],
                    user_password=result['user_password']
                )
            else:
                logger.warning(f"No user found with user_name: {user_name}")
                return None
        except Exception as e:
            logger.error(f"Error fetching user by user_name: {e}")
            raise Exception(f"Error fetching user by user_name: {e}")

    def insert(self, db: Database) -> 'User':
        try:
            query = """
                INSERT INTO 
                    user_table (
                        user_role_id, 
                        user_name, 
                        user_email, 
                        user_password
                    ) 
                VALUES 
                    (%s, %s, %s, %s)
                RETURNING 
                    user_id, user_role_id, user_name, user_email;
            """
            values = (self.__role.get_user_role_id(), self.__user_name,
                      self.__user_email, self.__user_password)
            result = db.insert(query, values)

            if result:
                role = User_Role.get_by_id(
                    db, user_role_id=result['user_role_id'])
                return User(
                    user_id=result['user_id'],
                    role=role,
                    user_name=result['user_name'],
                    user_email=result['user_email'],
                )
            else:
                logger.warning("User insertion failed: No result returned")
                return None
        except Exception as e:
            logger.error(f"Unexpected error during user registration: {e}")
            raise Exception(f"Error during user registration: {e}")

    @staticmethod
    def delete(db: Database, user_id: int) -> None:
        try:
            query = "DELETE FROM user_table WHERE user_id=%s;"
            values = (user_id,)
            db.execute(query, values)
            logger.info(f"User with user_id: {user_id} deleted successfully.")
        except Exception as e:
            logger.error(f"Error deleting user by ID: {e}")
            raise Exception(f"Error deleting user by ID: {e}")

    @staticmethod
    def all(db: Database) -> List['User']:
        try:
            query = "SELECT user_id, user_name, user_email, user_password, user_role_id FROM user_table;"
            results = db.fetch_all(query)

            users = []
            print(results)
            for result in results:
                role = User_Role.get_by_id(
                    db, user_role_id=int(result['user_role_id']))
                users.append(User(
                    user_id=int(result['user_id']),
                    role=role,
                    user_name=result['user_name'],
                    user_email=result['user_email'],
                    user_password=result['user_password']
                ))

            return users
        except Exception as e:
            logger.error(f"Error fetching all users: {e}")
            raise Exception(f"Error fetching all users: {e}")
