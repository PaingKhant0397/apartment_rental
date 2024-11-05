
from http import HTTPStatus
import utils
from database import Database
from models import Booking, Room_Type, User_Role, User, Booking_Status, Available_Room_Type
from config import CONNECTION_PARAMS
import urllib.parse
import re
from middlewares import RequestValidation, JWTAuthentication


class BookingController:
    required_fields = {
        ('/api/bookings', 'POST'): ['available_room_type', 'user', 'status', 'booking_date'],
        ('/api/bookings', 'PUT'): ['booking_id', 'room_type', 'user', 'status', 'booking_date'],
    }

    @RequestValidation.validate_required_fields(required_fields)
    def do_POST(self):
        """Create a new booking."""
        try:
            db = Database(CONNECTION_PARAMS)
            request_data = self.validated_data

            # Initialize Room_Type object
            room_type = Room_Type(
                room_type_name=request_data['available_room_type']['room_type']['room_type_name'],
                room_type_id=request_data['available_room_type']['room_type']['room_type_id']
            )

            # Initialize Available_Room_Type object using the Room_Type object
            available_room_type = Available_Room_Type(
                available_room_type_id=request_data['available_room_type']['available_room_type_id'],
                room_type=room_type,  # Use the Room_Type object here
                available_room_type_price=request_data['available_room_type']['available_room_type_price'],
                available_room_type_deposit_amount=request_data[
                    'available_room_type']['available_room_type_deposit_amount'],
                apartment_id=request_data['available_room_type']['apartment_id']
            )

            # Initialize User_Role object
            user_role = User_Role(
                user_role_id=request_data['user']['role']['user_role_id'],
                user_role_name=request_data['user']['role']['user_role_name']
            )

            # Initialize User object using the User_Role object
            user = User(
                role=user_role,  # Pass the User_Role object here
                user_id=request_data['user']['user_id'],
                user_name=request_data['user']['user_name'],
                user_email=request_data['user']['user_email'],
                # Assuming password is optional
                user_password=request_data.get('user_password')
            )

            status = Booking_Status(
                booking_status_id=request_data['status']['booking_status_id'],
                booking_status_name=request_data['status']['booking_status_name']
            )

            booking = Booking(
                user=user,
                room_type=available_room_type,  # Use Available_Room_Type object here
                status=status,
                booking_date=request_data['booking_date'],
                booking_comment=request_data.get('booking_comment')
            )

            result = booking.insert(db)
            utils.send_json_response(
                self, data=result.to_dict(), status=HTTPStatus.CREATED
            )
        except Exception as e:
            utils.send_json_response(
                self, {"error": str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

    def do_GET(self):
        """Retrieve all bookings or a single booking by ID."""
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_params = urllib.parse.parse_qs(parsed_url.query)

        match_single = re.match(r'/api/bookings/(\d+)$', path)

        if path == '/api/bookings':
            try:
                limit = int(query_params.get('limit', [10])[0])
                offset = int(query_params.get('offset', [0])[0])

                db = Database(CONNECTION_PARAMS)

                # Fetch all bookings with pagination
                bookings, total_count = Booking.get_all_paginated(
                    db, limit=limit, offset=offset)

                utils.send_json_response(
                    self,
                    data=bookings,
                    httpStatus=HTTPStatus.OK,
                    total_count=total_count
                )
            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error fetching bookings: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        elif match_single:
            booking_id = int(match_single.group(1))
            try:
                db = Database(CONNECTION_PARAMS)
                result = Booking.get_by_id(db, booking_id=booking_id)
                utils.send_json_response(
                    self, data=result.to_dict(), status=HTTPStatus.OK)
            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error fetching booking: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @RequestValidation.validate_required_fields(required_fields)
    def do_PUT(self):
        """Update an existing booking."""
        try:
            db = Database(CONNECTION_PARAMS)
            request_data = self.validated_data

            booking_id = request_data['booking_id']

            # Initialize Room_Type object
            room_type = Room_Type(
                room_type_name=request_data['room_type']['room_type']['room_type_name'],
                room_type_id=request_data['room_type']['room_type']['room_type_id']
            )

            # Initialize Available_Room_Type object using the Room_Type object
            available_room_type = Available_Room_Type(
                available_room_type_id=request_data['room_type']['available_room_type_id'],
                room_type=room_type,  # Use the Room_Type object here
                available_room_type_price=request_data['room_type']['available_room_type_price'],
                available_room_type_deposit_amount=request_data[
                    'room_type']['available_room_type_deposit_amount'],
                apartment_id=request_data['room_type']['apartment_id']
            )

            # Initialize User_Role object
            user_role = User_Role(
                user_role_id=request_data['user']['role']['user_role_id'],
                user_role_name=request_data['user']['role']['user_role_name']
            )

            # Initialize User object using the User_Role object
            user = User(
                role=user_role,  # Pass the User_Role object here
                user_id=request_data['user']['user_id'],
                user_name=request_data['user']['user_name'],
                user_email=request_data['user']['user_email'],
                # Assuming password is optional
                user_password=request_data.get('user_password')
            )

            status = Booking_Status(
                booking_status_id=request_data['status']['booking_status_id'],
                booking_status_name=request_data['status']['booking_status_name']
            )

            booking = Booking(
                booking_id=booking_id,
                user=user,
                room_type=available_room_type,  # Use Available_Room_Type object here
                status=status,
                booking_date=request_data['booking_date'],
                booking_comment=request_data.get('booking_comment')
            )

            result = booking.update(db)
            utils.send_json_response(
                self, data=result, status=HTTPStatus.OK
            )
        except Exception as e:
            utils.send_json_response(
                self, {"error": str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

    @JWTAuthentication.require_jwt("admin")
    def do_DELETE(self):
        booking_id_match = re.match(r'/api/bookings/(\d+)$', self.path)
        if booking_id_match:
            try:
                db = Database(CONNECTION_PARAMS)
                booking_id = int(booking_id_match.group(1))
                Booking.delete(db, booking_id=booking_id)
                utils.send_json_response(
                    self, {"message": "Booking deleted successfully."}, status=HTTPStatus.OK
                )
            except Exception as e:
                utils.send_json_response(
                    self,
                    {"error": f"Error deleting booking: {str(e)}"},
                    status=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)
