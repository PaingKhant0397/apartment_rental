from http.server import BaseHTTPRequestHandler
from models import Rental, Available_Room_Type, User, Rental_Status, Room_Type, Room, Room_Status
import utils
from database import Database
from config import CONNECTION_PARAMS
from middlewares import RequestValidation, JWTAuthentication
from http import HTTPStatus
import urllib.parse
import re


class RentalController(BaseHTTPRequestHandler):

    required_fields = {
        ('/api/rentals', 'POST'): ['room', 'rental_status', 'user', 'rental_start_date', 'rental_end_date'],
        ('/api/rentals', 'PUT'): ['rental_id', 'room', 'rental_status', 'user', 'rental_start_date', 'rental_end_date']
    }

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        rental_id_match = re.match(r'/api/rentals/(\d+)$', path)
        db = Database(CONNECTION_PARAMS)

        if rental_id_match:
            rental_id = int(rental_id_match.group(1))
            try:
                rental = Rental.get_by_id(db, rental_id)
                utils.send_json_response(self, data=rental.to_dict())
            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error fetching rental: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            try:
                query_params = urllib.parse.parse_qs(parsed_url.query)
                limit = int(query_params.get('limit', [10])[0])
                offset = int(query_params.get('offset', [0])[0])
                total_count, rentals = Rental.get_all_paginated(
                    db, limit=limit, offset=offset)

                utils.send_json_response(
                    self, data=rentals, httpStatus=HTTPStatus.OK, total_count=total_count)
            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error fetching rentals: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

    @JWTAuthentication.require_jwt("admin")
    @RequestValidation.validate_required_fields(required_fields)
    def do_POST(self):
        if re.match(r'/api/rentals$', self.path):
            try:
                db = Database(CONNECTION_PARAMS)
                request_data = self.validated_data
                # print(request_data['room'])
                # return
                room_type_data = request_data['room']['available_room_type']['room_type']

                room_type = Room_Type(
                    room_type_id=room_type_data['room_type_id'],
                    room_type_name=room_type_data['room_type_name']
                )

                available_room_type_data = request_data['room']['available_room_type']
                available_room_type = Available_Room_Type(
                    available_room_type_id=available_room_type_data['available_room_type_id'],
                    apartment_id=available_room_type_data['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=available_room_type_data['available_room_type_price'],
                    available_room_type_deposit_amount=available_room_type_data[
                        'available_room_type_deposit_amount']
                )

                room_data = request_data['room']
                room_status_data = room_data['status']
                room_status = Room_Status(
                    room_status_id=room_status_data['room_status_id'],
                    room_status_name=room_status_data['room_status_name']
                )
                room = Room(
                    available_room_type=available_room_type,
                    status=room_status,
                    room_no=room_data['room_no'],
                    room_size=room_data['room_size'],
                    room_floor_no=room_data['room_floor_no'],
                    room_id=room_data['room_id']
                )

                # Initialize RentalStatus and User
                rental_status = Rental_Status.get_by_id(
                    db, request_data['rental_status']['rental_status_id'])
                user = User.get_user_by_id(db, request_data['user']['user_id'])

                rental = Rental(
                    room=room,
                    user=user,
                    rental_status=rental_status,
                    rental_start_date=request_data['rental_start_date'],
                    rental_end_date=request_data['rental_end_date']
                )

                result = rental.insert(db)
                # print(result)

                # return
                utils.send_json_response(
                    self, data=result, message="Rental registered successfully", httpStatus=HTTPStatus.CREATED)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error registering rental: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @ JWTAuthentication.require_jwt("admin")
    @ RequestValidation.validate_required_fields(required_fields)
    def do_PUT(self):
        rental_id_match = re.match(r'/api/rentals/(\d+)$', self.path)
        if rental_id_match:
            try:
                db = Database(CONNECTION_PARAMS)
                request_data = self.validated_data
                rental_id = int(rental_id_match.group(1))

                room_type_data = request_data['room']['available_room_type']['room_type']
                room_type = Room_Type(
                    room_type_id=room_type_data['room_type_id'],
                    room_type_name=room_type_data['room_type_name']
                )

                available_room_type_data = request_data['room']['available_room_type']
                available_room_type = Available_Room_Type(
                    available_room_type_id=available_room_type_data['available_room_type_id'],
                    apartment_id=available_room_type_data['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=available_room_type_data['available_room_type_price'],
                    available_room_type_deposit_amount=available_room_type_data[
                        'available_room_type_deposit_amount']
                )

                room_data = request_data['room']
                room_status_data = room_data['status']
                room_status = Room_Status(
                    room_status_id=room_status_data['room_status_id'],
                    room_status_name=room_status_data['room_status_name']
                )
                room = Room(
                    available_room_type=available_room_type,
                    status=room_status,
                    room_no=room_data['room_no'],
                    room_size=room_data['room_size'],
                    room_floor_no=room_data['room_floor_no'],
                    room_id=room_data['room_id']
                )

                # Initialize RentalStatus and User
                rental_status = Rental_Status.get_by_id(
                    db, request_data['rental_status']['rental_status_id'])
                user = User.get_user_by_id(db, request_data['user']['user_id'])
                rental = Rental(
                    rental_id=rental_id,
                    room=room,
                    user=user,
                    rental_status=rental_status,
                    rental_start_date=request_data['rental_start_date'],
                    rental_end_date=request_data['rental_end_date']
                )

                result = rental.update(db)
                utils.send_json_response(self, data=result.to_dict(
                ), message="Rental updated successfully", httpStatus=HTTPStatus.OK)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error updating rental: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @ JWTAuthentication.require_jwt("admin")
    def do_DELETE(self):
        rental_id_match = re.match(r'/api/rentals/(\d+)$', self.path)
        if rental_id_match:
            try:
                db = Database(CONNECTION_PARAMS)
                rental_id = int(rental_id_match.group(1))
                Rental.delete(db, rental_id=rental_id)
                utils.send_json_response(
                    self, message="Rental deleted successfully", httpStatus=HTTPStatus.OK)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error deleting rental: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)
