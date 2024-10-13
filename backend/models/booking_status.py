
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Booking_Status:

    def __init__(self, bookingStatusID: int, bookingStatusName: str):
        self.__bookingStatusID = bookingStatusID
        self.__bookingStatusName = bookingStatusName

    @staticmethod
    def get(db: Database, bookingStatusID: int) -> 'Booking_Status':
        pass

    @staticmethod
    def all(db: Database) -> List['Booking_Status']:
        pass
