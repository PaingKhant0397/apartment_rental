
from __future__ import annotations
from typing import List, TYPE_CHECKING
from models import User
from utils import hash_password

if TYPE_CHECKING:
    from database import Database


class Auth:

    @staticmethod
    def register_user(db: Database, user: User) -> 'User':
        try:
            hashed_password = hash_password(user.get_userPassword())
            user.set_userPassword(hashed_password)
            inserted_data = user.insert(db)
            if not inserted_data:
                raise Exception("Inserted data not returned")
            return inserted_data
        except Exception as e:
            raise Exception(f"Error Registering user: {e}")

    @staticmethod
    def login(self, user):
        pass
