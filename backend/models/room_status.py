from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Room_Status:

    def __init__(self, room_status_name: str, room_status_id: int = None):
        self.__room_status_id = room_status_id
        self.__room_status_name = room_status_name

    def get_status_id(self) -> int:
        return self.__room_status_id

    def get_status_name(self) -> str:
        return self.__room_status_name

    def to_dict(self) -> dict:
        return {
            'room_status_id': self.__room_status_id,
            'room_status_name': self.__room_status_name
        }

    @staticmethod
    def get_by_id(db: Database, room_status_id: int) -> Room_Status:
        try:
            query = """
                SELECT
                    room_status_id,
                    room_status_name
                FROM
                    room_status
                WHERE
                    room_status_id = %s;
            """
            values = (room_status_id,)
            result = db.fetch_one(query, values)

            if result:
                return Room_Status(
                    room_status_id=result['room_status_id'],
                    room_status_name=result['room_status_name']
                )
            else:
                raise Exception(
                    f"Room Status with ID {room_status_id} not found")

        except Exception as e:
            raise Exception(f"Error fetching Room Status by ID: {e}")

    @staticmethod
    def get_all(db: Database) -> List[Room_Status]:
        try:
            query = """
                SELECT
                    room_status_id,
                    room_status_name
                FROM
                    room_status;
            """
            results = db.fetch_all(query)

            room_statuses = []
            for result in results:
                room_statuses.append(Room_Status(
                    room_status_id=result['room_status_id'],
                    room_status_name=result['room_status_name']
                ))

            return room_statuses

        except Exception as e:
            raise Exception(f"Error fetching Room Statuses: {e}")
