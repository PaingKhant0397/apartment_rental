from http.server import BaseHTTPRequestHandler
from models import User_Role
from utils import setup_logger, handle_unknown_endpoint, send_json_response, get_request_data
logger = setup_logger(__name__)


class User_RoleController(BaseHTTPRequestHandler):

    def do_GET(self):
        user_role = User_Role()
        if self.path == '/api/user_roles':
            try:
                user_roles = user_role.all()
                send_json_response(self, user_roles, 200)
            except Exception as e:
                raise Exception(f"Error fetching user roles: {e}")
        else:
            handle_unknown_endpoint(self)

    def do_POST(self):
        if self.path == '/api/user_roles':
            try:
                request_data = get_request_data(self)
                userRoleName = request_data.get('userRoleName')

                if not userRoleName:
                    raise Exception('userRoleName is required')
                else:
                    user_role = User_Role(userRoleName)
                    inserted_role = user_role.insert()
                    send_json_response(self, inserted_role, 201)
            except Exception as e:
                raise Exception(f"Error saving user_role: {e}")
