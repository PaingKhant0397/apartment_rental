from http.server import BaseHTTPRequestHandler
from models import Booking_Status
from database import Database
import utils
from config import CONNECTION_PARAMS
from http import HTTPStatus
import re


class BookingStatusController(BaseHTTPRequestHandler):
    def do_GET(self):
        # Match request path for getting a specific status or all statuses
        match_all = re.match(r'^/api/booking_statuses$', self.path)
        match_by_id = re.match(r'^/api/booking_statuses/(\d+)$', self.path)

        db = Database(CONNECTION_PARAMS)

        if match_by_id:
            try:
                # Extract booking_status_id from URL
                booking_status_id = int(match_by_id.group(1))

                # Fetch specific booking status by ID
                booking_status = Booking_Status.get_by_id(
                    db, booking_status_id)

                if booking_status:
                    utils.send_json_response(
                        self, message="", data=booking_status.to_dict()
                    )
                else:
                    utils.send_json_response(
                        self, message="Booking Status not found", httpStatus=HTTPStatus.NOT_FOUND
                    )

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching Booking Status: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        elif match_all:
            try:
                # Fetch all booking statuses
                booking_statuses = Booking_Status.get_all(db)
                data = [status.to_dict() for status in booking_statuses]

                utils.send_json_response(self, message="", data=data)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching Booking Statuses: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        else:
            utils.handle_unknown_endpoint(self)
