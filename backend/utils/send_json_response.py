import json


def send_json_response(handler, data, status=200):
    json_data = json.dumps(data)
    handler.send_response(status)
    handler.send_header('Content-Type', 'application/json')
    handler.send_header('Content-Length', str(len(json_data)))
    handler.end_headers()
    handler.wfile.write(json_data.encode('utf-8'))
