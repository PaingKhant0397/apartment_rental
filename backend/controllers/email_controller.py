from http.server import BaseHTTPRequestHandler
import json
import utils
from models import EmailUtil  # Adjust the import based on your file structure
from http import HTTPStatus
from middlewares import RequestValidation


class EmailController(BaseHTTPRequestHandler):

    required_fields = {
        ('/api/send-email', 'POST'): ['subject', 'html_body', 'body', 'to_emails'],
    }

    @RequestValidation.validate_required_fields(required_fields)
    def do_POST(self):
        if self.path == '/api/send-email':
            try:
                request_data = self.validated_data

                # Instantiate the EmailUtil
                email_util = EmailUtil()

                # Sending the email

                if request_data['from_email']:
                    email_util.send_email(
                        subject=request_data['subject'],
                        body=request_data['body'],
                        html_body=request_data['html_body'],
                        to_emails=request_data['to_emails'],
                        from_email=request_data['from_email']
                    )
                else:
                    email_util.send_email(
                        subject=request_data['subject'],
                        body=request_data['body'],
                        html_body=request_data['html_body'],
                        to_emails=request_data['to_emails']
                    )

                utils.send_json_response(
                    self,
                    message="Email sent successfully",
                    httpStatus=HTTPStatus.OK
                )

            except Exception as e:
                utils.send_json_response(
                    self,
                    status='error',
                    message=f"Error sending email: {str(e)}",
                    httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)
