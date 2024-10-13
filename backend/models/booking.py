from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database
    from .user import User
    from .available_room_type import Available_Room_Type
    from .booking_status import Booking_Status
    from datetime import date


class Booking:

    def __init__(self, user: User, roomType: Available_Room_Type, status: Booking_Status, bookingDate: date, bookingComment: str = None, bookingID: int = None):

        self.__bookingID = bookingID
        self.__user = user
        self.__room = roomType
        self.__status = status
        self.__bookingDate = bookingDate
        self.__bookingComment = bookingComment

    def save(self, db: Database) -> 'Booking':
        pass

    @staticmethod
    def get(db: Database, bookingID: int) -> 'Booking':
        pass

    @staticmethod
    def delete(db: Database, bookingID: int) -> None:
        pass

    @staticmethod
    def all(db: Database) -> List['Booking']:
        pass
