from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Room_Type:

    def __init__(self, roomTypeName: str, roomTypeID: int = None):

        self.__roomTypeID = roomTypeID
        self.__roomTypeName = roomTypeName

    @staticmethod
    def get(db: Database, roomTypeID: int) -> 'Room_Type':
        pass

    @staticmethod
    def all(db: Database) -> List['Room_Type']:
        pass
