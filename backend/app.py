import json
import os
import mimetypes

from http.server import BaseHTTPRequestHandler
from controllers import EmailController, RentalStatusController, BookingStatusController, InvoiceStatusController, RoomStatusController, InvoiceController, RentalController, BookingController, RoomController, RoomTypeController, ApartmentController, User_RoleController, UserController, Auth_Controller, AvailableRoomTypeController
from middlewares import ErrorHandler, RequestLogger

from urllib.parse import urlparse, parse_qs
from utils import handle_unknown_endpoint
import re


class RequestHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, DELETE, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
        self.end_headers()

    @ErrorHandler.handle_error
    @RequestLogger.log_request
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)

        limit = query_params.get('limit', [None])[0]
        offset = query_params.get('offset', [None])[0]

        if path.startswith('/assets/apartments/'):
            self.serve_static_file()
        elif path.startswith('/api/user_roles'):
            User_RoleController.do_GET(self)

        elif path.startswith('/api/users'):
            UserController.do_GET(self)

        elif path.startswith('/api/room_types'):
            RoomTypeController.do_GET(self)

        elif re.match(r'^/api/apartments/\d+/available_room_types$', path):
            AvailableRoomTypeController.do_GET(self)

        elif re.match(r'^/api/apartments/\d+/available_room_types/\d+$', path):
            AvailableRoomTypeController.do_GET(self)

        elif re.match(r'^/api/apartments/\d+/rooms$', path):
            RoomController.do_GET(self)

        elif re.match(r'^/api/apartments/\d+/rooms/\d+$', path):
            RoomController.do_GET(self)

        elif path.startswith('/api/apartments'):
            ApartmentController.do_GET(self)

        elif path.startswith('/api/bookings'):
            BookingController.do_GET(self)

        elif re.match(r'^/api/rentals/\d+/invoices$', path):
            InvoiceController.do_GET(self)

        elif re.match(r'^/api/rentals/\d+/invoices/\d+$', path):
            InvoiceController.do_GET(self)

        elif path.startswith('/api/rentals'):
            RentalController.do_GET(self)

        elif re.match(r'^/api/invoice_statuses/\d+$', path):
            InvoiceStatusController.do_GET(self)

        elif re.match(r'^/api/invoice_statuses$', path):
            InvoiceStatusController.do_GET(self)

        elif re.match(r'^/api/rental_statuses/\d+$', path):
            RentalStatusController.do_GET(self)

        elif re.match(r'^/api/rental_statuses$', path):
            RentalStatusController.do_GET(self)

        elif re.match(r'^/api/room_statuses/\d+$', path):
            RoomStatusController.do_GET(self)

        elif re.match(r'^/api/room_statuses$', path):
            RoomStatusController.do_GET(self)

        elif re.match(r'^/api/booking_statuses/\d+$', path):
            BookingStatusController.do_GET(self)

        elif re.match(r'^/api/booking_statuses$', path):
            BookingStatusController.do_GET(self)

        else:
            handle_unknown_endpoint(self)

    @ErrorHandler.handle_error
    @RequestLogger.log_request
    def do_POST(self):

        if self.path.startswith('/api/user_roles'):
            User_RoleController.do_POST(self)

        elif self.path.startswith('/api/users'):
            UserController.do_POST(self)

        elif self.path.startswith('/api/auth'):
            Auth_Controller.do_POST(self)

        elif re.match(r'^/api/apartments/\d+/available_room_types$', self.path):
            AvailableRoomTypeController.do_POST(self)

        elif re.match(r'^/api/apartments/\d+/rooms$', self.path):
            RoomController.do_POST(self)

        elif self.path.startswith('/api/apartments'):
            ApartmentController.do_POST(self)
        elif self.path.startswith('/api/bookings'):
            BookingController.do_POST(self)
        elif re.match(r'^/api/rentals/\d+/invoices$', self.path):
            InvoiceController.do_POST(self)
        elif self.path.startswith('/api/rentals'):
            RentalController.do_POST(self)
        elif self.path == '/api/send-email':
            EmailController.do_POST(self)
        else:
            handle_unknown_endpoint(self)

    @ErrorHandler.handle_error
    @RequestLogger.log_request
    def do_DELETE(self):

        if re.match(
                r'^/api/apartments/\d+/available_room_types/\d+$', self.path):
            AvailableRoomTypeController.do_DELETE(self)
        elif re.match(r'^/api/apartments/\d+/rooms/\d+$', self.path):
            RoomController.do_DELETE(self)
        elif re.match(r'^/api/apartments/\d+', self.path):
            ApartmentController.do_DELETE(self)
        elif re.match(r'^/api/bookings/\d+$', self.path):
            BookingController.do_DELETE(self)
        elif re.match(r'^/api/rentals/\d+/invoices/\d+$', self.path):
            InvoiceController.do_DELETE(self)
        elif re.match(r'^/api/rentals/\d+$', self.path):
            RentalController.do_DELETE(self)
        else:
            handle_unknown_endpoint(self)

    def do_PUT(self):

        if re.match(
                r'^/api/apartments/\d+/available_room_types/(\d+)$', self.path):
            AvailableRoomTypeController.do_PUT(self)
        elif re.match(r'^/api/apartments/\d+/rooms/\d+$', self.path):
            RoomController.do_PUT(self)
        elif re.match(r'^/api/apartments/\d+', self.path):
            ApartmentController.do_PUT(self)
        elif re.match(r'^/api/bookings/\d+$', self.path):
            BookingController.do_PUT(self)
        elif re.match(r'^/api/rentals/\d+/invoices/\d+$', self.path):
            InvoiceController.do_PUT(self)
        elif re.match(r'^/api/rentals/\d+$', self.path):
            RentalController.do_PUT(self)
        else:
            handle_unknown_endpoint(self)

    def serve_static_file(self):
        file_path = os.path.join(os.getcwd(), self.path[1:])

        # Check if the file exists
        if os.path.isfile(file_path):
            self.send_response(200)
            self.send_header('Content-Type', self.guess_type(file_path))
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

    def guess_type(self, path):
        if path.endswith('.png'):
            return 'image/png'
        elif path.endswith('.jpg') or path.endswith('.jpeg'):
            return 'image/jpeg'
        elif path.endswith('.gif'):
            return 'image/gif'
        else:
            return 'application/octet-stream'
