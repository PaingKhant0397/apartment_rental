from __future__ import annotations
from typing import List, TYPE_CHECKING, Optional
import psycopg2

if TYPE_CHECKING:
    from database import Database


class Rental_Status:
    def __init__(self, rental_status_name: str, rental_status_id: Optional[int] = None):
        self.__rental_status_id = rental_status_id
        self.__rental_status_name = rental_status_name

    def get_rental_status_id(self) -> Optional[int]:
        return self.__rental_status_id

    def get_rental_status_name(self) -> str:
        return self.__rental_status_name

    def to_dict(self) -> dict:
        return {
            'rental_status_id': self.__rental_status_id,
            'rental_status_name': self.__rental_status_name
        }

    @classmethod
    def get_by_id(cls, db: Database, rental_status_id: int) -> Rental_Status:
        query = """
        SELECT rental_status_id, rental_status_name
        FROM rental_status
        WHERE rental_status_id = %s;
        """
        try:
            result = db.fetch_one(query, (rental_status_id,))
            if result:
                return cls(rental_status_name=result['rental_status_name'], rental_status_id=result['rental_status_id'])
            else:
                raise ValueError(
                    f"Rental status with ID {rental_status_id} not found.")
        except psycopg2.Error as e:
            raise Exception(
                f"Database error occurred while fetching rental status by ID: {str(e)}")

    @classmethod
    def get_all(cls, db: Database) -> List[Rental_Status]:
        query = """
        SELECT rental_status_id, rental_status_name
        FROM rental_status;
        """
        try:
            results = db.fetch_all(query)
            return [cls(rental_status_name=result['rental_status_name'], rental_status_id=result['rental_status_id']) for result in results]
        except psycopg2.Error as e:
            raise Exception(
                f"Database error occurred while fetching all rental statuses: {str(e)}")
