from http.server import BaseHTTPRequestHandler
from models import Invoice_Status
from database import Database
import utils
from config import CONNECTION_PARAMS
from http import HTTPStatus
import re


class InvoiceStatusController(BaseHTTPRequestHandler):
    def do_GET(self):
        # Match request path for getting a specific status or all statuses
        match_all = re.match(r'^/api/invoice_statuses$', self.path)
        match_by_id = re.match(r'^/api/invoice_statuses/(\d+)$', self.path)

        db = Database(CONNECTION_PARAMS)

        if match_by_id:
            try:
                # Extract invoice_status_id from URL
                invoice_status_id = int(match_by_id.group(1))

                # Fetch specific invoice status by ID
                invoice_status = Invoice_Status.get_by_id(
                    db, invoice_status_id)

                if invoice_status:
                    utils.send_json_response(
                        self, message="", data=invoice_status.to_dict()
                    )
                else:
                    utils.send_json_response(
                        self, message="Invoice Status not found", httpStatus=HTTPStatus.NOT_FOUND
                    )

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching Invoice Status: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        elif match_all:
            try:
                # Fetch all invoice statuses
                invoice_statuses = Invoice_Status.get_all(db)
                data = [status.to_dict() for status in invoice_statuses]

                utils.send_json_response(self, message="", data=data)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching Invoice Statuses: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        else:
            utils.handle_unknown_endpoint(self)
