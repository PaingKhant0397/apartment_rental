from __future__ import annotations
from typing import TYPE_CHECKING
from models import User, Admin
from utils import hash_password, generate_jwt_token, check_password

if TYPE_CHECKING:
    from database import Database


class Auth:

    @staticmethod
    def register_user(db: Database, user: User) -> User:
        try:
            hashed_password = hash_password(user.get_user_password())
            user.set_user_password(hashed_password)
            inserted_data = user.insert(db)
            if not inserted_data:
                raise Exception("Inserted data not returned")
            return inserted_data
        except Exception as e:
            raise Exception(f"Error registering user: {e}")

    @staticmethod
    def login_user(db: Database, email: str, password: str) -> dict:
        try:
            user = User.get_by_email(db, email)
            if not user:
                raise ValueError("User not found")

            if not check_password(password, user.get_user_password()):
                raise ValueError("Invalid credentials")

            token = generate_jwt_token(
                id=user.get_user_id(),
                name=user.get_user_name(),
                role=user.get_role().get_user_role_name()
            )

            return {
                "token": token,
                "user": user.to_dict()
            }

        except ValueError as ve:
            raise Exception(f"Authentication failed: {ve}")
        except Exception as e:
            raise Exception(f"Error during login: {e}")

    @staticmethod
    def register_admin(db: Database, admin: Admin) -> 'Admin':
        try:
            hashed_password = hash_password(admin.get_admin_password())
            admin.set_admin_password(hashed_password)
            inserted_data = admin.insert(db)
            if not inserted_data:
                raise Exception("Inserted admin data not returned")
            return inserted_data
        except Exception as e:
            raise Exception(f"Error registering admin: {e}")

    @staticmethod
    def login_admin(db: Database, email: str, password: str) -> dict:
        try:
            admin = Admin.get_by_username(db, email)
            if not admin:
                raise ValueError("Admin not found")

            if not check_password(password, admin.get_admin_password()):
                raise ValueError("Invalid credentials")

            token = generate_jwt_token(
                id=admin.get_admin_id(),
                name=admin.get_admin_username(),
                role=admin.get_admin_role()
            )

            return {
                "token": token,
                "admin": admin.to_dict()
            }

        except ValueError as ve:
            raise Exception(f"Authentication failed: {ve}")
        except Exception as e:
            raise Exception(f"Error during login: {e}")
