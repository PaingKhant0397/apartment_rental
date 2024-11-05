from __future__ import annotations
from typing import TYPE_CHECKING, List
from datetime import date
from decimal import Decimal
from .rental import Rental
from .invoice_status import Invoice_Status
if TYPE_CHECKING:
    from database import Database


class Invoice:
    def __init__(
        self,
        rental: Rental,
        status: Invoice_Status,
        water_bill: Decimal,
        electricity_bill: Decimal,
        total_amount: Decimal,
        issued_date: date,
        due_date: date,
        invoice_id: int = None
    ):
        self.__invoice_id = invoice_id
        self.__rental = rental
        self.__status = status
        self.__water_bill = water_bill
        self.__electricity_bill = electricity_bill
        self.__total_amount = total_amount
        self.__issued_date = issued_date
        self.__due_date = due_date

    def get_invoice_id(self) -> int:
        return self.__invoice_id

    def get_rental(self) -> Rental:
        return self.__rental

    def get_status(self) -> Invoice_Status:
        return self.__status

    def get_water_bill(self) -> Decimal:
        return self.__water_bill

    def get_electricity_bill(self) -> Decimal:
        return self.__electricity_bill

    def get_total_amount(self) -> Decimal:
        return self.__total_amount

    def get_issued_date(self) -> date:
        return self.__issued_date

    def get_due_date(self) -> date:
        return self.__due_date

    def to_dict(self) -> dict:
        return {
            'invoice_id': self.__invoice_id,
            'rental': self.__rental.to_dict(),
            'status': self.__status.to_dict(),
            'water_bill': float(self.__water_bill),
            'electricity_bill': float(self.__electricity_bill),
            'total_amount': float(self.__total_amount),
            'issued_date': self.__issued_date.isoformat(),
            'due_date': self.__due_date.isoformat(),
        }

    def insert(self, db: Database) -> Invoice:
        try:
            query = """
                INSERT INTO
                    invoice(rental_id, invoice_status_id, water_bill,
                            electricity_bill, total_amount, issued_date, due_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING invoice_id, rental_id, invoice_status_id, water_bill, electricity_bill, total_amount, issued_date, due_date;
            """
            values = (
                self.__rental.get_rental_id(),
                self.__status.get_invoice_status_id(),
                self.__water_bill,
                self.__electricity_bill,
                self.__total_amount,
                self.__issued_date,
                self.__due_date
            )
            result = db.insert(query, values)
            if result:
                return Invoice(
                    rental=self.__rental,
                    status=self.__status,
                    water_bill=result['water_bill'],
                    electricity_bill=result['electricity_bill'],
                    total_amount=result['total_amount'],
                    issued_date=result['issued_date'],
                    due_date=result['due_date'],
                    invoice_id=result['invoice_id']
                )
            else:
                raise Exception("No result returned after insert")

        except Exception as e:
            raise Exception(f"Error inserting invoice: {e}")

    def update(self, db: Database) -> Invoice:
        try:
            query = """
                UPDATE
                    invoice
                SET
                    rental_id = %s,
                    invoice_status_id = %s,
                    water_bill = %s,
                    electricity_bill = %s,
                    total_amount = %s,
                    issued_date = %s,
                    due_date = %s
                WHERE
                    invoice_id = %s
                RETURNING invoice_id, rental_id, invoice_status_id, water_bill, electricity_bill, total_amount, issued_date, due_date;
            """
            values = (
                self.__rental.get_rental_id(),
                self.__status.get_invoice_status_id(),
                self.__water_bill,
                self.__electricity_bill,
                self.__total_amount,
                self.__issued_date,
                self.__due_date,
                self.__invoice_id
            )
            result = db.update(query, values)
            if result:
                return Invoice(
                    rental=self.__rental,
                    status=self.__status,
                    water_bill=result['water_bill'],
                    electricity_bill=result['electricity_bill'],
                    total_amount=result['total_amount'],
                    issued_date=result['issued_date'],
                    due_date=result['due_date'],
                    invoice_id=result['invoice_id']
                )
            else:
                raise Exception("No result returned after update")

        except Exception as e:
            raise Exception(f"Error updating invoice: {e}")

    @staticmethod
    def get_by_id(db: Database, invoice_id: int) -> Invoice:
        try:
            query = """
                SELECT invoice_id, rental_id, invoice_status_id, water_bill, electricity_bill, total_amount, issued_date, due_date
                FROM invoice
                WHERE invoice_id = %s;
            """
            values = (invoice_id,)
            result = db.fetch_one(query, values)
            if result:
                rental = Rental.get_by_id(
                    db, result['rental_id'])  # Fetch Rental object
                status = Invoice_Status.get_by_id(
                    db, result['invoice_status_id'])  # Fetch Invoice_Status object
                return Invoice(
                    rental=rental,
                    status=status,
                    water_bill=result['water_bill'],
                    electricity_bill=result['electricity_bill'],
                    total_amount=result['total_amount'],
                    issued_date=result['issued_date'],
                    due_date=result['due_date'],
                    invoice_id=result['invoice_id']
                )
            else:
                raise Exception(f"Invoice with ID {invoice_id} not found")

        except Exception as e:
            raise Exception(f"Error fetching invoice by ID: {e}")

    @staticmethod
    def get_by_rental_id(db: Database, rental_id: int, limit: int = 10, offset: int = 0) -> tuple[List['Invoice'], int]:
        invoices = []
        try:
            count_query = """
                SELECT COUNT(*)
                FROM invoice r
                WHERE rental_id = %s;
            """
            count_result = db.fetch_one(count_query, (rental_id,))
            total_count = count_result['count']
            query = """
                SELECT invoice_id, rental_id, invoice_status_id, water_bill, electricity_bill, total_amount, issued_date, due_date
                FROM invoice
                WHERE rental_id = %s
                LIMIT %s OFFSET %s;;
            """
            values = (rental_id, limit, offset)
            results = db.fetch_all(query, values)

            for result in results:
                rental = Rental.get_by_id(db, result['rental_id'])
                status = Invoice_Status.get_by_id(
                    db, result['invoice_status_id'])

                invoice = Invoice(
                    rental=rental,
                    status=status,
                    water_bill=result['water_bill'],
                    electricity_bill=result['electricity_bill'],
                    total_amount=result['total_amount'],
                    issued_date=result['issued_date'],
                    due_date=result['due_date'],
                    invoice_id=result['invoice_id']
                )
                invoices.append(invoice)

        except Exception as e:
            print(
                f"Error fetching invoices for rental_id {rental_id}: {str(e)}")

        return invoices, total_count

    @staticmethod
    def delete(db: Database, invoice_id: int) -> None:
        try:
            query = """
                DELETE FROM invoice
                WHERE invoice_id = %s;
            """
            values = (invoice_id,)
            db.execute_query(query, values)

        except Exception as e:
            raise Exception(f"Error deleting invoice: {e}")
