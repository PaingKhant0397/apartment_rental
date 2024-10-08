import json

from http.server import BaseHTTPRequestHandler, HTTPServer
# from controller import ApartmentController
# from view import ApartmentView

class RequestHandler(BaseHTTPRequestHandler):
    # apartment_controller = ApartmentController()

    def do_GET(self):
        if self.path == '/':
            response = [{'status': 'success'}]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        # if self.path == '/apartments':
        #     apartments = self.apartment_controller.list_apartments()
        #     self.send_response(200)
        #     self.send_header('Content-type', 'application/json')
        #     self.end_headers()
        #     self.wfile.write(ApartmentView.format_apartments(apartments).encode())
        # elif self.path.startswith('/apartment/'):
        #     apartment_id = int(self.path.split('/')[-1])
        #     apartment = self.apartment_controller.get_apartment(apartment_id)
        #     self.send_response(200 if apartment else 404)
        #     self.send_header('Content-type', 'application/json')
        #     self.end_headers()
        #     self.wfile.write(ApartmentView.format_apartment(apartment).encode())
        # else:
        #     self.send_response(404)
        #     self.end_headers()

    # def do_POST(self):
    #     if self.path == '/apartment':
    #         content_length = int(self.headers['Content-Length'])
    #         body = self.rfile.read(content_length)
    #         data = json.loads(body)
    #         apartment_name = data.get('apartment_name')
    #         address = data.get('address')
    #         apartment = self.apartment_controller.add_apartment(apartment_name, address)
    #         self.send_response(201)
    #         self.send_header('Content-type', 'application/json')
    #         self.end_headers()
    #         self.wfile.write(ApartmentView.format_apartment(apartment).encode())
    #     else:
    #         self.send_response(404)
    #         self.end_headers()

    # def do_PUT(self):
    #     if self.path.startswith('/apartment/'):
    #         apartment_id = int(self.path.split('/')[-1])
    #         content_length = int(self.headers['Content-Length'])
    #         body = self.rfile.read(content_length)
    #         data = json.loads(body)
    #         apartment_name = data.get('apartment_name')
    #         address = data.get('address')
    #         updated_apartment = self.apartment_controller.update_apartment(apartment_id, apartment_name, address)
    #         if updated_apartment:
    #             self.send_response(200)
    #             self.send_header('Content-type', 'application/json')
    #             self.end_headers()
    #             self.wfile.write(ApartmentView.format_apartment(updated_apartment).encode())
    #         else:
    #             self.send_response(404)
    #             self.end_headers()
    #     else:
    #         self.send_response(404)
    #         self.end_headers()

    # def do_DELETE(self):
    #     if self.path.startswith('/apartment/'):
    #         apartment_id = int(self.path.split('/')[-1])
    #         success = self.apartment_controller.delete_apartment(apartment_id)
    #         if success:
    #             self.send_response(204)  # No content
    #             self.end_headers()
    #         else:
    #             self.send_response(404)
    #             self.end_headers()
    #     else:
    #         self.send_response(404)
    #         self.end_headers()