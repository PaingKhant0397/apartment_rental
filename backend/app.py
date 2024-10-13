import json

from http.server import BaseHTTPRequestHandler
from controllers import User_RoleController, UserController, Auth_Controller
from middlewares import ErrorHandler, RequestLogger


from utils import handle_unknown_endpoint


class RequestHandler(BaseHTTPRequestHandler):

    @ErrorHandler.handle_error
    @RequestLogger.log_request
    def do_GET(self):

        if self.path.startswith('/api/user_roles'):
            User_RoleController.do_GET(self)
        elif self.path.startswith('/api/users'):
            UserController.do_GET(self)
        else:
            handle_unknown_endpoint(self)

    @ErrorHandler.handle_error
    @RequestLogger.log_request
    def do_POST(self):

        if self.path.startswith('/api/user_roles'):
            User_RoleController.do_POST(self)
        elif self.path.startswith('/api/users'):
            UserController.do_POST(self)
        elif self.path.startswith('/api/auth'):
            Auth_Controller.do_POST(self)
        else:
            handle_unknown_endpoint(self)
