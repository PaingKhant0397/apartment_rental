from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Invoice_Status:
    def __init__(self, invoice_status_name: str, invoice_status_id: int = None):
        self.__invoice_status_id = invoice_status_id
        self.__invoice_status_name = invoice_status_name

    def get_invoice_status_id(self) -> int:
        return self.__invoice_status_id

    def get_invoice_status_name(self) -> str:
        return self.__invoice_status_name

    def to_dict(self):
        return {
            "invoice_status_id": self.__invoice_status_id,
            "invoice_status_name": self.__invoice_status_name
        }

    @staticmethod
    def get_by_id(db: Database, invoice_status_id: int) -> Invoice_Status:
        try:
            query = """
                SELECT
                    invoice_status_id,
                    invoice_status_name
                FROM
                    invoice_status
                WHERE
                    invoice_status_id = %s;
            """
            result = db.fetch_one(query, (invoice_status_id,))
            if not result:
                raise ValueError(
                    f"Invoice Status with ID {invoice_status_id} not found.")

            return Invoice_Status(
                invoice_status_name=result['invoice_status_name'],
                invoice_status_id=result['invoice_status_id']
            )
        except Exception as e:
            raise Exception(
                f"Error fetching Invoice Status with ID {invoice_status_id}: {e}")

    @staticmethod
    def get_all(db: Database) -> List[Invoice_Status]:
        try:
            query = """
                SELECT
                    invoice_status_id,
                    invoice_status_name
                FROM
                    invoice_status;
            """
            results = db.fetch_all(query)

            invoice_statuses = []
            for result in results:
                invoice_statuses.append(Invoice_Status(
                    invoice_status_name=result['invoice_status_name'],
                    invoice_status_id=result['invoice_status_id']
                ))

            return invoice_statuses
        except Exception as e:
            raise Exception(f"Error fetching Invoice Statuses: {e}")
