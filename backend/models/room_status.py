from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Room_Status:

    def __init__(self, roomStatusName: str, roomStatusID: int = None):

        self.__roomStatusID = roomStatusID
        self.__roomStatusName = roomStatusName

    @staticmethod
    def get(db: Database, roomStatusID: int) -> 'Room_Status':
        pass

    @staticmethod
    def all(db: Database) -> List['Room_Status']:
        pass
