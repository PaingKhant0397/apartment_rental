import json
from .setup_logger import setup_logger
from .object_to_dict import object_to_dict

logger = setup_logger(__name__)


def send_json_response(handler, data=None, status='success', message='', httpStatus=200, total_count=None, ):
    try:
        print(message)
        if data is None:
            data = ''
        elif isinstance(data, list):

            data = [object_to_dict(obj) if hasattr(
                obj, '__dict__') else obj for obj in data]
        elif hasattr(data, '__dict__'):

            data = object_to_dict(data)

        if total_count is not None:
            data = {
                'total_count': total_count,
                'data': data
            }

        json_response = json.dumps(data)

        handler.send_response(httpStatus)
        handler.send_header('Access-Control-Allow-Origin', '*')
        handler.send_header('Access-Control-Allow-Methods',
                            'POST,GET,DELETE,PUT')
        handler.send_header('Access-Control-Allow-Headers',
                            'Content-Type, Authorization')
        handler.send_header('Access-Control-Allow-Credentials', 'true')
        handler.send_header('Content-Type', 'application/json')
        handler.send_header('Content-Length', str(len(json_response)))
        handler.end_headers()

        handler.wfile.write(json_response.encode('utf-8'))

    except Exception as e:
        logger.error(f"Error in sending JSON response: {e}")
        raise Exception(f"Error in sending JSON response: {e}")
