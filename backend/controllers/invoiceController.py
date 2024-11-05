from http.server import BaseHTTPRequestHandler
from models import Invoice, Invoice_Status, Rental
import utils
from database import Database
from config import CONNECTION_PARAMS
from middlewares import RequestValidation
from http import HTTPStatus
from decimal import Decimal
import re
from datetime import datetime
import urllib.parse


class InvoiceController(BaseHTTPRequestHandler):
    required_fields = {
        ('^/api/rentals/(\d+)/invoices$', 'POST'): ['rental', 'status', 'water_bill', 'electricity_bill', 'total_amount', 'issued_date', 'due_date'],
        ('^/api/rentals/(\d+)/invoices/(\d+)$', 'PUT'): ['invoice_id', 'rental', 'status', 'water_bill', 'electricity_bill', 'total_amount', 'issued_date', 'due_date'],
    }

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        # Match the request path to identify the rental_id and optionally the invoice_id
        match_all = re.match(r'^/api/rentals/(\d+)/invoices$', path)
        match_single = re.match(
            r'^/api/rentals/(\d+)/invoices/(\d+)$', path)

        db = Database(CONNECTION_PARAMS)

        if match_single:
            try:
                rental_id = int(match_single.group(1))
                invoice_id = int(match_single.group(2))

                # Fetch the specific invoice by ID
                invoice = Invoice.get_by_id(db, invoice_id)

                if invoice and invoice.get_rental().get_rental_id() == rental_id:
                    utils.send_json_response(
                        self, message="", data=invoice.to_dict())
                else:
                    utils.send_json_response(
                        self, message="Invoice not found for this rental", httpStatus=HTTPStatus.NOT_FOUND)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching invoice: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)

        elif match_all:
            try:
                rental_id = int(match_all.group(1))
                query_params = urllib.parse.parse_qs(parsed_url.query)
                limit = int(query_params.get('limit', [10])[0])
                offset = int(query_params.get('offset', [0])[0])
                # Fetch all invoices for the rental
                invoices, total_count = Invoice.get_by_rental_id(db, rental_id)

                if invoices:
                    utils.send_json_response(
                        self, message="", data=invoices, total_count=total_count)
                else:
                    utils.send_json_response(
                        self, message="No invoices found for this rental", httpStatus=HTTPStatus.NOT_FOUND)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error fetching invoices: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)

        else:
            utils.handle_unknown_endpoint(self)

    @RequestValidation.validate_required_fields(required_fields)
    def do_POST(self):
        match = re.match(r'^/api/rentals/(\d+)/invoices$', self.path)
        if match:
            try:
                db = Database(CONNECTION_PARAMS)
                request_data = self.validated_data

                rental_id = request_data.get("rental", {}).get("rental_id")
                invoice_status_id = request_data.get(
                    "status", {}).get("invoice_status_id")
                water_bill = Decimal(request_data['water_bill'])
                electricity_bill = Decimal(request_data['electricity_bill'])
                total_amount = Decimal(request_data['total_amount'])
                issued_date = request_data['issued_date']
                due_date = request_data['due_date']

                # Fetch the rental object using the rental_id
                rental = Rental.get_by_id(db, rental_id)
                if not rental:
                    utils.send_json_response(
                        self, message="Rental not found", httpStatus=HTTPStatus.NOT_FOUND
                    )
                    return

                # Fetch the invoice status using the invoice_status_id
                invoice_status = Invoice_Status.get_by_id(
                    db, invoice_status_id)
                if not invoice_status:
                    utils.send_json_response(
                        self, message="Invoice status not found", httpStatus=HTTPStatus.NOT_FOUND
                    )
                    return

                # Create the Invoice object
                invoice = Invoice(
                    rental=rental,
                    status=invoice_status,
                    water_bill=water_bill,
                    electricity_bill=electricity_bill,
                    total_amount=total_amount,
                    issued_date=issued_date,
                    due_date=due_date
                )

                # Insert the invoice into the database
                result = invoice.insert(db)

                # Send a success response
                utils.send_json_response(
                    self, message="Invoice registered successfully.", data=result
                )

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error registering invoice: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR
                )
        else:
            utils.handle_unknown_endpoint(self)

    @RequestValidation.validate_required_fields(required_fields)
    def do_PUT(self):
        match = re.match(r'^/api/rentals/(\d+)/invoices/(\d+)$', self.path)

        if match:
            try:
                rental_id = int(match.group(1))
                invoice_id = int(match.group(2))
                db = Database(CONNECTION_PARAMS)

                existing_invoice = Invoice.get_by_id(db, invoice_id)

                if existing_invoice and existing_invoice.get_rental().get_rental_id() == rental_id:
                    request_data = self.validated_data

                    status = Invoice_Status.get_by_id(
                        db, int(request_data['status']['invoice_status_id']))

                    updated_invoice = Invoice(
                        rental=existing_invoice.get_rental(),  # Keep the same rental object
                        status=status,
                        water_bill=Decimal(request_data['water_bill']),
                        electricity_bill=Decimal(
                            request_data['electricity_bill']),
                        total_amount=Decimal(request_data['total_amount']),
                        issued_date=datetime.fromisoformat(
                            request_data['issued_date']),
                        due_date=datetime.fromisoformat(
                            request_data['due_date']),
                        invoice_id=existing_invoice.get_invoice_id()
                    )

                    updated_invoice_result = updated_invoice.update(db)
                    utils.send_json_response(
                        self, message="Invoice updated successfully.", data=updated_invoice_result.to_dict())
                else:
                    utils.send_json_response(
                        self, message="Invoice not found for this rental", httpStatus=HTTPStatus.NOT_FOUND)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error updating invoice: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)
        else:
            utils.handle_unknown_endpoint(self)

    def do_DELETE(self):
        match = re.match(r'^/api/rentals/(\d+)/invoices/(\d+)$', self.path)

        if match:
            try:
                rental_id = int(match.group(1))
                invoice_id = int(match.group(2))
                db = Database(CONNECTION_PARAMS)

                existing_invoice = Invoice.get_by_id(db, invoice_id)

                if existing_invoice and existing_invoice.get_rental().get_rental_id() == rental_id:
                    Invoice.delete(db, invoice_id)
                    utils.send_json_response(
                        self, message="Invoice deleted successfully", httpStatus=HTTPStatus.OK)
                else:
                    utils.send_json_response(
                        self, message="Invoice not found for this rental", httpStatus=HTTPStatus.NOT_FOUND)

            except Exception as e:
                utils.send_json_response(
                    self, message=f"Error deleting invoice: {str(e)}", httpStatus=HTTPStatus.INTERNAL_SERVER_ERROR)

        else:
            utils.handle_unknown_endpoint(self)
