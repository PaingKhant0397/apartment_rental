from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Rental_Status:

    def __init__(self, rentalStatusName: str, rentalStatusID: int = None):

        self.__rentalStatusID = rentalStatusID
        self.__rentalStatusName = rentalStatusName

    @staticmethod
    def get(db: Database, rentalStatusID: int) -> 'Rental_Status':
        pass

    @staticmethod
    def all(db: Database) -> List['Rental_Status']:
        pass
