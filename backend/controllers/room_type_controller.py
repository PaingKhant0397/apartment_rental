from http.server import BaseHTTPRequestHandler
from models import Room_Type
import utils
from database import Database
from config import CONNECTION_PARAMS
# from middlewares import RequestValidation
from http import HTTPStatus
import re


class RoomTypeController(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/api/room_types':
            try:
                db = Database(CONNECTION_PARAMS)

                result = Room_Type.get_all(db)

                utils.send_json_response(
                    self, message="", data=result)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error in room types : {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)

        elif re.match(r'^/api/room_types/\d+$', self.path):
            try:

                room_type_id = int(self.path.split('/')[-1])

                db = Database(CONNECTION_PARAMS)
                room_type = Room_Type.get_by_id(db, room_type_id)

                if room_type:
                    utils.send_json_response(
                        self, message="", data=room_type.to_dict())
                else:
                    utils.send_json_response(
                        self, message="Room type not found", httpStatus=HTTPStatus.NOT_FOUND)

            except ValueError:
                utils.send_json_response(
                    self, message="Invalid room type ID", httpStatus=HTTPStatus.BAD_REQUEST)
            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching room type: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)
        else:
            utils.handle_unknown_endpoint(self)
