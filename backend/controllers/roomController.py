from http.server import BaseHTTPRequestHandler
from models import Room, Available_Room_Type, Room_Status, Room_Type
import utils
from database import Database
from config import CONNECTION_PARAMS
from middlewares import RequestValidation, JWTAuthentication
from http import HTTPStatus
import urllib.parse
import re


class RoomController(BaseHTTPRequestHandler):

    required_fields = {
        ('/api/apartments/\d+/rooms', 'POST'): ['available_room_type', 'status', 'room_no', 'room_size', 'room_floor_no'],
        ('^/api/apartments/\d+/rooms/\d+$', 'PUT'): ['room_id', 'available_room_type', 'status', 'room_no', 'room_size', 'room_floor_no'],
    }

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        apartment_id_match = re.match(r'/api/apartments/(\d+)/rooms$', path)
        room_id_match = re.match(r'/api/apartments/(\d+)/rooms/(\d+)$', path)

        db = Database(CONNECTION_PARAMS)

        if apartment_id_match:
            # Get all rooms for the specified apartment
            apartment_id = int(apartment_id_match.group(1))
            try:
                query_params = urllib.parse.parse_qs(parsed_url.query)
                limit = int(query_params.get('limit', [10])[0])
                offset = int(query_params.get('offset', [0])[0])
                room_type_id = query_params.get('room_type', [None])[0]
                room_type_id = int(room_type_id) if room_type_id else None

                if room_type_id is not None:
                    # Fetch rooms filtered by room type and status 1
                    rooms, total_count = Room.get_by_apartment_and_room_type_paginated(
                        db, apartment_id, room_type_id, limit, offset
                    )
                else:
                    # Fetch all rooms with pagination
                    rooms, total_count = Room.get_all_by_apartment_paginated(
                        db, apartment_id, limit, offset
                    )

                # rooms, total_count = Room.get_all_by_apartment_paginated(
                #     db, apartment_id=apartment_id, limit=limit, offset=offset)

                utils.send_json_response(
                    self, data=rooms, httpStatus=HTTPStatus.OK, total_count=total_count)
            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error fetching rooms: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        elif room_id_match:
            # Get a specific room by ID
            apartment_id = int(room_id_match.group(1))
            room_id = int(room_id_match.group(2))
            try:
                result = Room.get_by_id(db, room_id)
                utils.send_json_response(self, data=result.to_dict())
            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error fetching room: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @JWTAuthentication.require_jwt("admin")
    @RequestValidation.validate_required_fields(required_fields)
    def do_POST(self):
        apartment_id_match = re.match(
            r'/api/apartments/(\d+)/rooms$', self.path)
        if apartment_id_match:
            try:
                # print('work here')
                # return
                db = Database(CONNECTION_PARAMS)
                request_data = self.validated_data

                available_room_type_data = request_data['available_room_type']
                room_type_data = available_room_type_data['room_type']

                # Create RoomType and AvailableRoomType objects
                room_type = Room_Type(
                    room_type_id=room_type_data['room_type_id'],
                    room_type_name=room_type_data['room_type_name']
                )

                available_room_type = Available_Room_Type(
                    available_room_type_id=available_room_type_data['available_room_type_id'],
                    apartment_id=available_room_type_data['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=available_room_type_data['available_room_type_price'],
                    available_room_type_deposit_amount=available_room_type_data[
                        'available_room_type_deposit_amount']
                )

                # Initialize RoomStatus using the status ID from the request data
                room_status = Room_Status.get_by_id(
                    db, request_data['status']['room_status_id'])

                room = Room(
                    available_room_type=available_room_type,
                    status=room_status,
                    room_no=request_data['room_no'],
                    room_size=request_data['room_size'],
                    room_floor_no=request_data['room_floor_no']
                )

                result = room.insert(db)
                utils.send_json_response(
                    self, data=result, message="Room registered successfully", httpStatus=HTTPStatus.CREATED)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error registering room: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @JWTAuthentication.require_jwt("admin")
    @RequestValidation.validate_required_fields(required_fields)
    def do_PUT(self):
        room_id_match = re.match(
            r'/api/apartments/\d+/rooms/(\d+)$', self.path)
        if room_id_match:
            try:
                db = Database(CONNECTION_PARAMS)
                request_data = self.validated_data

                # Create Room_Type directly from the request data
                room_type_data = request_data['available_room_type']['room_type']
                room_type = Room_Type(
                    room_type_id=room_type_data['room_type_id'],
                    room_type_name=room_type_data['room_type_name']
                )

                # Create Available_Room_Type directly from the request data
                available_room_type = Available_Room_Type(
                    available_room_type_id=request_data['available_room_type']['available_room_type_id'],
                    apartment_id=request_data['available_room_type']['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=request_data['available_room_type']['available_room_type_price'],
                    available_room_type_deposit_amount=request_data[
                        'available_room_type']['available_room_type_deposit_amount']
                )

                # Create Room_Status directly from the request data
                room_status_data = request_data['status']
                room_status = Room_Status(
                    room_status_id=room_status_data['room_status_id'],
                    room_status_name=room_status_data['room_status_name']
                )

                # Initialize Room with the constructed objects
                room = Room(
                    # Use room_id extracted from the path
                    room_id=int(room_id_match.group(1)),
                    available_room_type=available_room_type,
                    status=room_status,
                    room_no=request_data['room_no'],
                    room_size=request_data['room_size'],
                    # Ensure room_floor_no is an int
                    room_floor_no=int(request_data['room_floor_no'])
                )

                # Call the update method on the room instance
                result = room.update(db)
                utils.send_json_response(
                    self, data=result.to_dict(), message="Room updated successfully", httpStatus=HTTPStatus.OK
                )

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error updating room: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @JWTAuthentication.require_jwt("admin")
    def do_DELETE(self):
        room_id_match = re.match(
            r'/api/apartments/\d+/rooms/(\d+)$', self.path)
        if room_id_match:
            try:
                db = Database(CONNECTION_PARAMS)
                room_id = int(room_id_match.group(1))
                Room.delete(db, room_id=room_id)
                utils.send_json_response(
                    self, message="Room deleted successfully", httpStatus=HTTPStatus.OK)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error deleting room: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)
