from http.server import BaseHTTPRequestHandler
from models import Room_Status
from database import Database
import utils
from config import CONNECTION_PARAMS
from http import HTTPStatus
import re


class RoomStatusController(BaseHTTPRequestHandler):
    def do_GET(self):
        # Match request path for getting a specific status or all statuses
        match_all = re.match(r'^/api/room_statuses$', self.path)
        match_by_id = re.match(r'^/api/room_statuses/(\d+)$', self.path)

        db = Database(CONNECTION_PARAMS)

        if match_by_id:
            try:
                # Extract room_status_id from URL
                room_status_id = int(match_by_id.group(1))

                # Fetch specific room status by ID
                room_status = Room_Status.get_by_id(db, room_status_id)

                if room_status:
                    utils.send_json_response(
                        self, message="", data=room_status.to_dict()
                    )
                else:
                    utils.send_json_response(
                        self, message="Room Status not found", httpStatus=HTTPStatus.NOT_FOUND
                    )

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching Room Status: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        elif match_all:
            try:
                # Fetch all room statuses
                room_statuses = Room_Status.get_all(db)
                data = [status.to_dict() for status in room_statuses]

                utils.send_json_response(self, message="", data=data)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching Room Statuses: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        else:
            utils.handle_unknown_endpoint(self)
