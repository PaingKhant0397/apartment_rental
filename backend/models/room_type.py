from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Room_Type:

    def __init__(self, room_type_name: str, room_type_id: int = None):

        self.__room_type_id = room_type_id
        self.__room_type_name = room_type_name

    def get_room_type_id(self) -> int:
        return self.__room_type_id

    def get_room_type_name(self) -> str:
        return self.__room_type_name

    def to_dict(self) -> dict:
        return {
            "room_type_id": self.__room_type_id,
            "room_type_name": self.__room_type_name
        }

    @classmethod
    def get_by_id(cls, db: Database, room_type_id: int) -> 'Room_Type':
        try:
            query = """
                SELECT
                    room_type_id,
                    room_type_name
                FROM
                    room_type
                WHERE
                    room_type_id = %s;
            """
            values = (room_type_id,)
            result = db.fetch_one(query, values)
            if result:
                return cls(
                    room_type_id=result['room_type_id'],
                    room_type_name=result['room_type_name']
                )
            else:
                return None

        except Exception as e:
            raise Exception(f"Error getting room type by id: {e}")

    @staticmethod
    def get_all(db: Database) -> List['Room_Type']:

        try:
            query = """
                SELECT
                    room_type_id,
                    room_type_name
                FROM
                    room_type;
            """
            results = db.fetch_all(query)
            if results:
                room_types = []
                for result in results:
                    room_types.append(Room_Type(
                        room_type_id=result['room_type_id'],
                        room_type_name=result['room_type_name']
                    ))

                return room_types
            else:
                raise Exception("Error fetching room types")
        except Exception as e:
            raise Exception(f"Error getting room types: {e}")
