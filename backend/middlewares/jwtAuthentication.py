from functools import wraps
import utils
from http import HTTPStatus


class JWTAuthentication:

    @staticmethod
    def require_jwt(func):
        @wraps(func)
        def wrapper(handler, *args, **kwargs):

            try:
                auth_header = handler.headers.get('Authorization')

                if not auth_header or auth_header.startswith("Bearer "):
                    response = {
                        "error": "Authorization header missing or invalid"
                    }
                    utils.send_json_response(
                        handler, response, HTTPStatus.UNAUTHORIZED)
                    return

                token = auth_header.split(" ")[1]
                decoded_token = utils.decode_jwt_token(token)
                handler.userID = decoded_token['userID']
                return func(handler, *args, **kwargs)

            except Exception as e:
                utils.send_json_response(
                    handler, {"error": str(e)}, HTTPStatus.UNAUTHORIZED)

        return wrapper
