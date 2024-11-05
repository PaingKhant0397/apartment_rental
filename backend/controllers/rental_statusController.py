from http.server import BaseHTTPRequestHandler
from models import Rental_Status
from database import Database
import utils
from config import CONNECTION_PARAMS
from http import HTTPStatus
import re


class RentalStatusController(BaseHTTPRequestHandler):
    def do_GET(self):
        # Match request path for getting a specific status or all statuses
        match_all = re.match(r'^/api/rental_statuses$', self.path)
        match_by_id = re.match(r'^/api/rental_statuses/(\d+)$', self.path)

        db = Database(CONNECTION_PARAMS)

        if match_by_id:
            try:
                # Extract rental_status_id from URL
                rental_status_id = int(match_by_id.group(1))

                # Fetch specific rental status by ID
                rental_status = Rental_Status.get_by_id(db, rental_status_id)

                if rental_status:
                    utils.send_json_response(
                        self, message="", data=rental_status.to_dict()
                    )
                else:
                    utils.send_json_response(
                        self, message="Rental Status not found", httpStatus=HTTPStatus.NOT_FOUND
                    )

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching Rental Status: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        elif match_all:
            try:
                # Fetch all rental statuses
                rental_statuses = Rental_Status.get_all(db)
                data = [status.to_dict() for status in rental_statuses]

                utils.send_json_response(self, message="", data=data)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching Rental Statuses: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        else:
            utils.handle_unknown_endpoint(self)
