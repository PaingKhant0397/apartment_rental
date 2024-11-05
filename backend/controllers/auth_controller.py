from http.server import BaseHTTPRequestHandler
from middlewares import RequestValidation
from models import User, User_Role, Admin
from auth import Auth
from utils import send_json_response, handle_unknown_endpoint, setup_logger
from database import Database
from config import CONNECTION_PARAMS

logger = setup_logger(__name__)


class Auth_Controller(BaseHTTPRequestHandler):

    required_fields_map = {
        ('/api/auth/register_user', 'POST'): ['user_role_id', 'user_name', 'user_email', 'user_password'],
        ('/api/auth/login_user', 'POST'): ['user_email', 'user_password'],
        ('/api/auth/register_admin', 'POST'): ['admin_username', 'admin_password'],
        ('/api/auth/login_admin', 'POST'): ['admin_username', 'admin_password'],
    }

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()

    @RequestValidation.validate_required_fields(required_fields_map=required_fields_map)
    def do_POST(self):
        db = Database(CONNECTION_PARAMS)

        if self.path == '/api/auth/register_user':
            try:
                request_data = self.validated_data
                user_role_id = 1
                user_name = request_data['user_name']
                user_email = request_data['user_email']
                user_password = str(request_data['user_password'])

                role = User_Role.get_by_id(db, user_role_id=user_role_id)
                if not role:
                    logger.warning(
                        f"User role not found for user_role_id: {user_role_id}")
                    raise ValueError("Invalid user role")

                user = User(
                    user_name=user_name,
                    role=role,
                    user_email=user_email,
                    user_password=user_password
                )

                response_data = Auth.register_user(db, user)
                send_json_response(self, data=response_data, status='success',
                                   message="Account Registration Successful")

            except Exception as e:
                logger.error(f"Error during user registration: {e}")
                raise Exception(f"Error during user registration: {e}")

        elif self.path == '/api/auth/login_user':
            try:
                request_data = self.validated_data
                user_email = request_data['user_email']
                user_password = request_data['user_password']

                response_data = Auth.login_user(db, user_email, user_password)
                send_json_response(self, data=response_data,
                                   message="Login Successful")

            except Exception as e:
                logger.error(f"Error during login: {e}")
                raise Exception(f"Error During login.")

        elif self.path == '/api/auth/register_admin':
            try:
                request_data = self.validated_data

                admin_username = request_data['admin_username']

                admin_password = str(request_data['admin_password'])

                admin = Admin(admin_username=admin_username,
                              admin_password=admin_password)

                response_data = Auth.register_admin(db, admin)
                send_json_response(self, data=response_data, status='success',
                                   message="Account Registration Successful")

            except Exception as e:
                logger.error(f"Error during admin registration: {e}")
                raise Exception(f"Error during admin registration: {e}")

        elif self.path == '/api/auth/login_admin':
            try:
                request_data = self.validated_data
                admin_username = request_data['admin_username']
                admin_password = request_data['admin_password']

                response_data = Auth.login_admin(
                    db, admin_username, admin_password)
                send_json_response(self, data=response_data,
                                   message="Login Successful")

            except Exception as e:
                logger.error(f"Error during login: {e}")
                raise Exception(f"Error During login.")
        else:
            handle_unknown_endpoint(self)
