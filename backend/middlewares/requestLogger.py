from utils import setup_logger
from functools import wraps

logger = setup_logger(__name__)


class RequestLogger:

    @staticmethod
    def log_request(func):
        @wraps(func)
        def wrapper(handler, *args, **kwargs):
            log_text = f"Method: {handler.command} - Path: {handler.path} "
            logger.info(log_text)
            return func(handler, *args, **kwargs)
        return wrapper
