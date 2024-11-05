from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Booking_Status:

    def __init__(self, booking_status_name: str, booking_status_id: int = None,):
        self.__booking_status_id = booking_status_id
        self.__booking_status_name = booking_status_name

    def get_booking_status_id(self) -> int:
        return self.__booking_status_id

    def get_booking_status_name(self) -> str:
        return self.__booking_status_name

    def to_dict(self) -> dict:
        """Convert the Booking_Status object to a dictionary."""
        return {
            'booking_status_id': self.__booking_status_id,
            'booking_status_name': self.__booking_status_name
        }

    @staticmethod
    def get_all(db: Database) -> List[Booking_Status]:
        try:
            query = """
                SELECT
                    booking_status_id,
                    booking_status_name
                FROM
                    booking_status;
            """
            results = db.fetch_all(query)

            statuses = []
            for result in results:
                statuses.append(Booking_Status(
                    booking_status_id=result['booking_status_id'],
                    booking_status_name=result['booking_status_name']
                ))

            return statuses

        except Exception as e:
            raise Exception(f"Error fetching booking statuses: {e}")

    @staticmethod
    def get_by_id(db: Database, booking_status_id: int) -> Booking_Status:
        try:
            query = """
                SELECT
                    booking_status_id,
                    booking_status_name
                FROM
                    booking_status
                WHERE
                    booking_status_id = %s;
            """
            result = db.fetch_one(query, (booking_status_id,))

            if result:
                return Booking_Status(
                    booking_status_id=result['booking_status_id'],
                    booking_status_name=result['booking_status_name']
                )
            else:
                raise Exception(
                    f"Booking status with ID {booking_status_id} not found")

        except Exception as e:
            raise Exception(f"Error fetching booking status by ID: {e}")
