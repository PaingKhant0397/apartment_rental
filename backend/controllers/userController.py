from http.server import BaseHTTPRequestHandler
from models import User
from utils import handle_unknown_endpoint, send_json_response, get_request_data
from config import CONNECTION_PARAMS
from middlewares import JWTAuthentication, RequestValidation
from database import Database


class UserController(BaseHTTPRequestHandler):

    required_fields_map = {
        ('/api/users', 'POST'): ['userRoleID', 'userName', 'userEmail', 'userPassword'],
        ('/api/users', 'PUT'): ['userID', 'userRoleID', 'userName', 'userEmail', 'userPassword'],
    }

    @JWTAuthentication.require_jwt("admin")
    def do_GET(self):
        db = Database(CONNECTION_PARAMS)
        if self.path == '/api/users':
            try:
                users = User.all(db)
                send_json_response(self, users, 200)
            except Exception as e:
                raise Exception(f"Error fetching users: {e}")
        else:
            handle_unknown_endpoint(self)

    @RequestValidation.validate_required_fields(required_fields_map=required_fields_map)
    def do_POST(self):
        if self.path == '/api/users':
            try:
                request_data = self.validated_data
                userRoleID = request_data.get('userRoleID')
                userName = request_data.get('userName')
                userEmail = request_data.get('userEmail')
                userPassword = request_data.get('userPassword')

                user = User(userRoleID, userName, userEmail, userPassword)
                inserted_user = user.insert()
                send_json_response(self, inserted_user)
            except Exception as e:
                raise Exception(f"Error saving user: {e}")
        else:
            handle_unknown_endpoint(self)
