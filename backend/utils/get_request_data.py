import json


def get_request_data(handler):
    try:
        # if 'Content-Length' not in handler.headers:
        #     raise ValueError("Content-Length header is missing.")

        content_length = int(handler.headers['Content-Length'])
        body = handler.rfile.read(content_length)
        request_data = json.loads(body)

        # missing_fields = [
        #     field for field in required_fields if field not in request_data]

        # if missing_fields:
        #     raise ValueError(
        #         f"Error: Missing fields {', '.join(missing_fields)}")

        return request_data
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON in request body.")
    except ValueError as ve:
        raise ValueError(f"Error getting request data: {ve}")
