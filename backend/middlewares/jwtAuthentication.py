from functools import wraps
from http import HTTPStatus
import utils


class JWTAuthentication:

    @staticmethod
    def require_jwt(required_role=None):
        """Auth and access control"""
        def decorator(func):
            @wraps(func)
            def wrapper(handler, *args, **kwargs):
                try:
                    auth_header = handler.headers.get('Authorization')

                    if not auth_header or not auth_header.startswith("Bearer "):
                        # Return here after sending the response
                        return utils.send_json_response(
                            handler, status='error',
                            message="Authorization header missing or invalid",
                            httpStatus=HTTPStatus.UNAUTHORIZED  # fix 'HTTPStatus' typo
                        )

                    token = auth_header.split(" ")[1]
                    decoded_token = utils.decode_jwt_token(token)

                    handler.userID = decoded_token.get('userID')
                    user_role = decoded_token.get('role')

                    if required_role and user_role != required_role:
                        # Return here after sending the response
                        return utils.send_json_response(
                            handler, status='error',
                            message='You do not have permission to access this resource.',
                            httpStatus=HTTPStatus.FORBIDDEN
                        )

                    # If everything is fine, proceed with the main function
                    return func(handler, *args, **kwargs)
                except Exception as e:
                    return utils.send_json_response(
                        handler, status='error',
                        message=f"Error while authenticating: {str(e)}",
                        httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                    )
            return wrapper
        return decorator
