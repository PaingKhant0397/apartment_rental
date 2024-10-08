import json


def handle_unknown_endpoint(handler):
    handler.send_response(404)
    handler.send_header('Content-type', 'application/json')
    handler.end_headers()
    response = {'error': 'unknown endpoint'}
    handler.wfile.write(json.dumps(response).encode())
