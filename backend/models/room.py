from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database
    from .available_room_type import Available_Room_Type
    from .room_status import Room_Status


class Room:

    def __init__(self, apartmentRoomType: Available_Room_Type, status: Room_Status, roomNo: int, roomSize: str, roomFloorNo: int, roomID=None):

        self.__roomID = roomID
        self.__apartmentRoomType = apartmentRoomType
        self.__status = status
        self.__roomNo = roomNo
        self.__roomSize = roomSize
        self.__roomFloorNo = roomFloorNo

    def save(self, db: Database) -> 'Room':
        pass

    @staticmethod
    def get(db: Database, roomID: int) -> 'Room':
        pass

    @staticmethod
    def delete(db: Database, roomID: int) -> None:
        pass

    @staticmethod
    def all(db: Database) -> List['Room']:
        pass
