
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database
    from datetime import date
    from available_room_type import Available_Room_Type


class Apartment:

    def __init__(self,  apartmentName: str, apartmentAddress: str, apartmentDesc: str, apartmentDateBuilt: date, apartmentPostalCode: int, apartmentCapacity: int, apartmentID: int = None, availableRoomTypes: List[Available_Room_Type] = []):
        self.__apartmentID = apartmentID
        self.__apartmentName = apartmentName,
        self.__apartmentAddress = apartmentAddress
        self.__apartmentDesc = apartmentDesc
        self.__apartmentDateBuilt = apartmentDateBuilt
        self.__apartmentPostalCode = apartmentPostalCode
        self.__apartmentCapacity = apartmentCapacity
        self.__availableRoomTypes = availableRoomTypes

    def save(self, db: Database) -> 'Apartment':
        pass

    @staticmethod
    def get(db: Database, apartmentID: int) -> 'Apartment':
        pass

    @staticmethod
    def delete(db: Database) -> None:
        pass

    @staticmethod
    def all(db: Database) -> List['Apartment']:
        pass
