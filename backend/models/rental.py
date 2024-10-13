from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database
    from .room import Room
    from .user import User
    from .rental_status import Rental_Status
    from datetime import date


class Rental:

    def __init__(self, room: Room, user: User, status: Rental_Status, rentInDate: date, rentOutDate: date, rentalID: int = None):

        self.__rentalID = rentalID
        self.__room = room
        self.__user = user
        self.__status = status
        self.__rentInDate = rentInDate
        self.__rentOutDate = rentOutDate

    def save(self, db: Database) -> 'Rental':
        pass

    @staticmethod
    def get(db: Database, rentalID: int) -> 'Rental':
        pass

    @staticmethod
    def delete(db: Database, rentalID: int) -> None:
        pass

    @staticmethod
    def all(db: Database) -> List['Rental']:
        pass
