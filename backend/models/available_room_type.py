from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database
    from .apartment import Apartment
    from .room_type import Room_Type
    from decimal import Decimal


class Available_Room_Type:

    def __init__(self, apartment: Apartment, room_type: Room_Type, roomPrice: Decimal, depositAmount: Decimal, apartmentRoomTypeID: int = None):

        self.__apartmentRoomTypeID = apartmentRoomTypeID
        self.__apartment = apartment
        self.__room_type = room_type
        self.__roomPrice = roomPrice
        self.__depositAmount = depositAmount

    def save(self, db: Database) -> Available_Room_Type:
        pass

    @staticmethod
    def get(db: Database, apartmentRoomTypeID: int) -> 'Available_Room_Type':
        pass

    @staticmethod
    def delete(db: Database) -> None:
        pass

    @staticmethod
    def get_avaliable_room_types(db: Database, ApartmentID: int) -> List['Available_Room_Type']:
        pass

    @staticmethod
    def all(db: Database) -> List['Available_Room_Type']:
        pass
