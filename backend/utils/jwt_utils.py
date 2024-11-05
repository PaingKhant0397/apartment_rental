import jwt
import datetime

from config import JWT_SECRET_KEY


def generate_jwt_token(id, name, role):
    try:
        payload = {
            "id": id,
            "name": name,
            "role": role,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
        }

        return jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

    except Exception as e:
        raise Exception(f"Error Generating Token: {e}")


def decode_jwt_token(token):
    try:
        decoded_pay_load = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=['HS256'])
        return decoded_pay_load
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired.")
    except jwt.InvalidTokenError:
        raise Exception("Invalid Token.")
    except Exception as e:
        raise Exception(f"Error Decoding Token: {e}")
