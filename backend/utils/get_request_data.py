import json
from urllib.parse import parse_qs
from .parse_multipart_form_data import parse_multipart_form_data


def get_request_data(handler):
    try:
        content_type = handler.headers.get('Content-Type', '')
        content_length = int(handler.headers['Content-Length'])
        body = handler.rfile.read(content_length)

        if 'application/json' in content_type:
            request_data = json.loads(body)
        elif 'application/x-www-form-urlencoded' in content_type:
            # Handle URL encoded form data
            request_data = parse_qs(body.decode('utf-8'))
            request_data = {key: value[0]
                            for key, value in request_data.items()}
        elif 'multipart/form-data' in content_type:
            request_data = parse_multipart_form_data(handler, body)

            if not request_data:
                raise Exception("Error parsing form data")
        else:
            raise ValueError("Unsupported Content-Type")

        return request_data
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON in request body.")
    except ValueError as ve:
        raise ValueError(f"Error getting request data: {ve}")
    except Exception as e:
        raise Exception(f"Error getting request data: {e}")
