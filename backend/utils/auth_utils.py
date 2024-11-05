import hashlib


def hash_password(password: str):

    return hashlib.sha256(password.encode()).hexdigest()


def check_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password
