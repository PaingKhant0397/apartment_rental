from http.server import BaseHTTPRequestHandler
from models import Available_Room_Type, Room_Type
import utils
from database import Database
from config import CONNECTION_PARAMS
from middlewares import RequestValidation
from http import HTTPStatus
from decimal import Decimal
import re


class AvailableRoomTypeController(BaseHTTPRequestHandler):

    required_fields = {
        ('^/api/apartments/(\d+)/available_room_types$', 'POST'): ['apartment_id', 'room_type', 'available_room_type_price', 'available_room_type_deposit_amount'],
        ('^/api/apartments/(\d+)/available_room_types$', 'PUT'): ['available_room_type_id', 'apartment_id', 'room_type', 'available_room_type_price', 'available_room_type_deposit_amount'],
    }

    def do_GET(self):
        # Check if the request path matches the pattern '/api/apartments/{apartment_id}/available_room_types'
        match_all = re.match(
            r'^/api/apartments/(\d+)/available_room_types$', self.path)
        match_single = re.match(
            r'^/api/apartments/(\d+)/available_room_types/(\d+)$', self.path)

        db = Database(CONNECTION_PARAMS)

        if match_single:
            try:

                available_room_type_id = int(match_single.group(2))

                available_room_type = Available_Room_Type.get_by_id(
                    db, available_room_type_id)

                if available_room_type:
                    utils.send_json_response(
                        self, message="", data=available_room_type)
                else:
                    utils.send_json_response(
                        self, message="Available room type not found", httpStatus=HTTPStatus.NOT_FOUND)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching available room type: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)

        elif match_all:
            try:
                # Extract apartment_id from the URL
                apartment_id = int(match_all.group(1))

                # Fetch available room types by apartment_id
                available_room_types = Available_Room_Type.get_all_by_apartment(
                    db, apartment_id)

                # Check if there are any available room types
                if available_room_types:
                    result = [art.to_dict() for art in available_room_types]
                    utils.send_json_response(self, message="", data=result)
                else:
                    utils.send_json_response(
                        self, message="No available room types found", httpStatus=HTTPStatus.NOT_FOUND)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching available room types: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)

        else:
            utils.handle_unknown_endpoint(self)

    @RequestValidation.validate_required_fields(required_fields)
    def do_POST(self):
        match = re.match(
            r'^/api/apartments/(\d+)/available_room_types$', self.path)
        if match:
            try:
                db = Database(CONNECTION_PARAMS)
                request_data = self.validated_data
                room_type_id = request_data.get(
                    "room_type", {}).get("room_type_id")
                room_type = Room_Type.get_by_id(
                    db, int(room_type_id))

                available_room_type = Available_Room_Type(
                    apartment_id=int(request_data['apartment_id']),
                    room_type=room_type,
                    available_room_type_price=Decimal(
                        request_data['available_room_type_price']),
                    available_room_type_deposit_amount=Decimal(
                        request_data['available_room_type_deposit_amount'])
                )

                result = available_room_type.insert(db)

                utils.send_json_response(
                    self, message="Available room type assigned successfully.", data=result)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error in available room type: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)
        else:
            utils.handle_unknown_endpoint(self)

    def do_DELETE(self):

        match = re.match(
            r'^/api/apartments/(\d+)/available_room_types/(\d+)$', self.path)

        if match:
            try:
                # Use the capture groups from the regex
                apartment_id = int(match.group(1))
                available_room_type_id = int(match.group(2))
                print(
                    f"Apartment ID: {apartment_id}, Available Room Type ID: {available_room_type_id}")

                db = Database(CONNECTION_PARAMS)

                # Proceed with deletion logic
                Available_Room_Type.delete(db, available_room_type_id)

                utils.send_json_response(
                    self, message="Available room type deleted successfully", httpStatus=HTTPStatus.OK)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error deleting available room type id: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)

        else:
            utils.handle_unknown_endpoint(self)

    @RequestValidation.validate_required_fields(required_fields)
    def do_PUT(self):
        # Match the request path to identify the available_room_type_id from the URL
        match = re.match(
            r'^/api/apartments/\d+/available_room_types/(\d+)$', self.path)

        if match:
            try:

                # Get the database connection
                db = Database(CONNECTION_PARAMS)

                request_data = self.validated_data

                # Fetch the existing available room type object
                is_exist = Available_Room_Type.get_by_id(
                    db, request_data['available_room_type_id'])

                if is_exist:

                    room_type_id = request_data.get(
                        "room_type", {}).get("room_type_id")
                    print(f"room_type_id")
                    room_type = Room_Type.get_by_id(
                        db, int(room_type_id))

                    available_room_type = Available_Room_Type(
                        available_room_type_id=int(
                            request_data['available_room_type_id']),
                        apartment_id=int(request_data['apartment_id']),
                        room_type=room_type,
                        available_room_type_price=Decimal(
                            request_data['available_room_type_price']),
                        available_room_type_deposit_amount=Decimal(
                            request_data['available_room_type_deposit_amount'])
                    )

                    updated_available_room_type = available_room_type.update(
                        db)

                    # Send a success response with the updated available room type data
                    utils.send_json_response(self, message="Available room type updated successfully",
                                             data=updated_available_room_type.to_dict(), httpStatus=HTTPStatus.OK)
                else:
                    utils.send_json_response(
                        self, message="Available room type not found", httpStatus=HTTPStatus.NOT_FOUND)

            except Exception as e:
                # Handle any error that occurred during the process
                utils.send_json_response(
                    self, message=f"Error updating available room type: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)

        else:
            # Handle unknown endpoints
            utils.handle_unknown_endpoint(self)
