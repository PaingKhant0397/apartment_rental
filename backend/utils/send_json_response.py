import json
from .setup_logger import setup_logger
from .object_to_dict import object_to_dict

logger = setup_logger(__name__)


def send_json_response(handler, data=None, status='success', message='', httpStatus=200):
    try:
        if data is None:
            data = ''
        elif isinstance(data, list):
            data = [object_to_dict(obj) for obj in data]
        else:
            data = object_to_dict(data)

        response = {
            'status': status,
            'message': message,
            'data': data
        }

        json_response = json.dumps(response)

        handler.send_response(httpStatus)
        handler.send_header('Content-Type', 'application/json')
        handler.send_header('Content-Length', str(len(json_response)))
        handler.end_headers()
        handler.wfile.write(json_response.encode('utf-8'))
    except Exception as e:
        logger.error(f"Error in sending json response: {e}")
        raise Exception(f"Error when sending response.")
