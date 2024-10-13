from utils import setup_logger
from functools import wraps
import json

logger = setup_logger(__name__)


class ErrorHandler:

    @staticmethod
    def handle_error(func):
        @wraps(func)
        def wrapper(handler, *args, **kwargs):
            try:
                return func(handler, *args, **kwargs)
            except Exception as e:
                logger.error(
                    f"Unhandled exception in {func.__name__}: {str(e)}")
                if isinstance(e, ValueError):
                    handler.send_response(400)
                    handler.send_header('Content-Type', 'application/json')
                    handler.end_headers()
                    response = {
                        'status': 'error',
                        'message': str(e)
                    }
                    handler.wfile.write(json.damps(response).encode())
                else:
                    handler.send_response(500)
                    handler.send_header('Content-type', 'application/json')
                    handler.end_headers()
                    response = {
                        'status': 'error',
                        'message': 'Internal server error ' + str(e)
                    }
                    handler.wfile.write(json.dumps(response).encode())
        return wrapper
