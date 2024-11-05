from http.server import BaseHTTPRequestHandler
from models import Apartment
import utils
from database import Database
from config import CONNECTION_PARAMS
from middlewares import RequestValidation, JWTAuthentication
from http import HTTPStatus
import urllib.parse
import re


class ApartmentController(BaseHTTPRequestHandler):

    required_fields = {
        ('/api/apartments', 'POST'): ['apartment_name', 'apartment_address', 'apartment_desc', 'apartment_date_built', 'apartment_postal_code', 'apartment_capacity'],
        ('^/api/apartments/\d+$', 'PUT'): ['apartment_id', 'apartment_name', 'apartment_address', 'apartment_desc', 'apartment_date_built', 'apartment_postal_code', 'apartment_capacity'],
    }

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_params = urllib.parse.parse_qs(parsed_url.query)

        match_single = re.match(r'/api/apartments/(\d+)$', self.path)
        if path == '/api/apartments':
            try:

                limit = int(query_params.get('limit', [10])[0])
                offset = int(query_params.get('offset', [0])[0])

                db = Database(CONNECTION_PARAMS)

                apartments, total_count = Apartment.get_all_paginated(
                    db, limit=limit, offset=offset)

                utils.send_json_response(
                    self, data=apartments, httpStatus=HTTPStatus.OK, total_count=total_count)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error fetching apartments: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        elif match_single:
            apartment_id = int(match_single.group(1))
            db = Database(CONNECTION_PARAMS)
            result = Apartment.get_by_id(db, apartment_id=apartment_id)
            utils.send_json_response(self, data=result)
        else:
            utils.handle_unknown_endpoint(self)

    @JWTAuthentication.require_jwt("admin")
    @RequestValidation.validate_required_fields(required_fields)
    def do_POST(self):
        if self.path == '/api/apartments':
            try:
                db = Database(CONNECTION_PARAMS)
                request_data = self.validated_data

                apartment_image_filename = None

                if 'apartment_image' in request_data:
                    file = request_data['apartment_image']
                    upload_folder_name = 'apartments'
                    try:
                        apartment_image_filename = utils.ImageUtil.save_image(
                            file, upload_folder_name)
                    except ValueError as e:
                        utils.send_json_response(
                            self, {'error': str(e)}, HTTPStatus.BAD_REQUEST)
                        return

                apartment = Apartment(
                    apartment_name=request_data['apartment_name'],
                    apartment_address=request_data['apartment_address'],
                    apartment_desc=request_data['apartment_desc'],
                    apartment_date_built=request_data['apartment_date_built'],
                    apartment_postal_code=request_data['apartment_postal_code'],
                    apartment_capacity=request_data['apartment_capacity'],
                    apartment_image=apartment_image_filename
                )

                result = apartment.insert(db)
                utils.send_json_response(
                    self, data=result, message="Apartment registered successfully", httpStatus=HTTPStatus.CREATED)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error registering apartment: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @JWTAuthentication.require_jwt("admin")
    @RequestValidation.validate_required_fields(required_fields)
    def do_PUT(self):
        match = re.match(r'/api/apartments/(\d+)$', self.path)
        if match:
            try:
                db = Database(CONNECTION_PARAMS)
                request_data = self.validated_data

                apartment_image_filename = None

                if 'apartment_image' in request_data:
                    file = request_data['apartment_image']
                    upload_folder_name = 'apartments'

                    # Check if the file is a string (URL or existing filename)
                    if isinstance(file, str):
                        # Use the string directly as the apartment image filename
                        apartment_image_filename = file
                    else:
                        # Proceed with the file upload if it's not a string
                        try:
                            apartment_image_filename = utils.ImageUtil.save_image(
                                file, upload_folder_name)
                        except ValueError as e:
                            utils.send_json_response(
                                self, {'error': str(e)}, HTTPStatus.BAD_REQUEST)
                            return

                # Create an Apartment instance with the provided data
                apartment = Apartment(
                    apartment_id=int(request_data['apartment_id']),
                    apartment_name=request_data['apartment_name'],
                    apartment_address=request_data['apartment_address'],
                    apartment_desc=request_data['apartment_desc'],
                    apartment_date_built=request_data['apartment_date_built'],
                    apartment_postal_code=request_data['apartment_postal_code'],
                    apartment_capacity=request_data['apartment_capacity'],
                    apartment_image=apartment_image_filename
                )

                # Update the apartment in the database
                result = apartment.update(db)
                utils.send_json_response(
                    self, data=result, message="Apartment updated successfully", httpStatus=HTTPStatus.CREATED)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error updating apartment: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @JWTAuthentication.require_jwt("admin")
    def do_DELETE(self):
        match = re.match(r'/api/apartments/(\d+)$', self.path)
        if match:
            try:
                db = Database(CONNECTION_PARAMS)
                apartment_id = int(match.group(1))
                deleted_apartment = Apartment.delete(
                    db, apartment_id=apartment_id)
                utils.send_json_response(
                    self, message="Apartment Deleted successfully", httpStatus=HTTPStatus.CREATED)

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error registering apartment: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)
