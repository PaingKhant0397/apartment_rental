from .setup_logger import setup_logger
logger = setup_logger(__name__)


def object_to_dict(obj):
    try:
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        else:
            return obj
    except Exception as e:
        logger.error(f"Error converting object to dict: {e}")
        raise Exception(f"Error Seralizing Response")
