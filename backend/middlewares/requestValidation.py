from functools import wraps
from http import HTTPStatus

import utils


class RequestValidation:

    def validate_required_fields(required_fields_map):

        def decorator(func):
            @wraps(func)
            def wrapper(handler, *args, **kwargs):
                path = handler.path
                method = handler.command
                required_fields = required_fields_map.get((path, method), [])

                request_data = utils.get_request_data(handler)

                missing_field = [
                    field for field in required_fields if field not in request_data]

                if missing_field:
                    response = {
                        "error": f"Missing required fields: {', '.join(missing_field)}"}
                    utils.send_json_response(
                        handler, response, HTTPStatus.BAD_REQUEST)
                handler.validated_data = request_data

                return func(handler, *args, **kwargs)

            return wrapper

        return decorator
