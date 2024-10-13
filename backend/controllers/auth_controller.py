from http.server import BaseHTTPRequestHandler
from middlewares import RequestValidation
from models import User, User_Role
from auth import Auth
from utils import send_json_response, handle_unknown_endpoint, setup_logger
from database import Database
from config import CONNECTION_PARAMS

logger = setup_logger(__name__)


class Auth_Controller(BaseHTTPRequestHandler):

    required_fields_map = {
        ('/api/auth/register_user'): ['userRoleID', 'userName', 'userEmail', 'userPassword'],
    }

    @RequestValidation.validate_required_fields(required_fields_map=required_fields_map)
    def do_POST(self):
        db = Database(CONNECTION_PARAMS)
        if self.path == '/api/auth/register_user':
            try:
                request_data = self.validated_data
                userRoleID = int(request_data['userRoleID'])
                userName = request_data['userName']
                userEmail = request_data['userEmail']
                userPassword = str(request_data['userPassword'])

                role = User_Role.get(db, userRoleID=userRoleID)
                if not role:
                    logger.warning(
                        f"User role not found for userRoleID: {userRoleID}")
                    raise ValueError(f"Invalid user role")

                user = User(
                    userName=userName,
                    role=role,
                    userEmail=userEmail,
                    userPassword=userPassword
                )

                response_data = Auth.register_user(db, user)
                send_json_response(self, response_data)

            except Exception as e:
                logger.error(f"Error during user registration: {e}")
                raise Exception("Internal Server Error")

        else:
            handle_unknown_endpoint()
