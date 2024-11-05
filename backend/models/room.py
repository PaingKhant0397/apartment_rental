from __future__ import annotations
from typing import List, TYPE_CHECKING
from .available_room_type import Available_Room_Type
from .room_status import Room_Status
from .room_type import Room_Type

if TYPE_CHECKING:
    from database import Database


class Room:
    def __init__(self, available_room_type: Available_Room_Type, status: Room_Status, room_no: int, room_size: str, room_floor_no: int, room_id=None):
        self.__room_id = room_id
        self.__available_room_type = available_room_type
        self.__status = status
        self.__room_no = room_no
        self.__room_size = room_size
        self.__room_floor_no = room_floor_no

    def get_room_id(self) -> int:
        return self.__room_id

    def get_available_room_type(self) -> Available_Room_Type:
        return self.__available_room_type

    def get_status(self) -> Room_Status:
        return self.__status

    def get_room_no(self) -> int:
        return self.__room_no

    def get_room_size(self) -> str:
        return self.__room_size

    def get_room_floor_no(self) -> int:
        return self.__room_floor_no

    def to_dict(self) -> dict:
        return {
            'room_id': self.__room_id,
            'available_room_type': self.__available_room_type.to_dict(),
            'status': self.__status.to_dict(),
            'room_no': self.__room_no,
            'room_size': self.__room_size,
            'room_floor_no': self.__room_floor_no
        }

    def insert(self, db: Database) -> Room:
        try:
            query = """
                INSERT INTO
                    room(
                        available_room_type_id,
                        room_status_id,
                        room_no,
                        room_size,
                        room_floor_no
                    )
                VALUES(
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                RETURNING
                    room_id, available_room_type_id, room_status_id, room_no, room_size, room_floor_no;
            """
            values = (
                self.__available_room_type.get_available_room_type_id(),
                self.__status.get_status_id(),
                self.__room_no,
                self.__room_size,
                self.__room_floor_no,
            )
            result = db.insert(query, values)
            if result:
                return Room(
                    room_id=result['room_id'],
                    available_room_type=self.__available_room_type,
                    status=self.__status,
                    room_no=result['room_no'],
                    room_size=result['room_size'],
                    room_floor_no=result['room_floor_no']
                )
            else:
                raise Exception("No result returned after insert")

        except Exception as e:
            raise Exception(f"Error inserting room: {e}")

    def update(self, db: Database) -> Room:
        try:
            query = """
                UPDATE
                    room
                SET
                    available_room_type_id = %s,
                    room_status_id = %s,
                    room_no = %s,
                    room_size = %s,
                    room_floor_no = %s
                WHERE
                    room_id = %s
                RETURNING
                    room_id, available_room_type_id, room_status_id, room_no, room_size, room_floor_no;
            """
            values = (
                self.__available_room_type.get_available_room_type_id(),
                # Ensure correct method for getting room_status_id
                self.__status.get_status_id(),
                self.__room_no,
                self.__room_size,
                self.__room_floor_no,
                self.__room_id
            )

            result = db.update(query, values)

            if result:
                # Create and return updated Room instance with returned result
                return Room(
                    room_id=result['room_id'],
                    available_room_type=self.__available_room_type,
                    status=self.__status,
                    room_no=result['room_no'],
                    room_size=result['room_size'],
                    room_floor_no=result['room_floor_no']
                )
            else:
                raise Exception("No result returned after update")

        except Exception as e:
            raise Exception(f"Error updating room: {e}")

    @staticmethod
    def get_by_id(db: Database, room_id: int) -> 'Room':
        try:
            query = """
                SELECT
                    r.room_id,
                    r.room_no,
                    r.room_size,
                    r.room_floor_no,
                    art.available_room_type_id,
                    art.apartment_id,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    art.room_type_id,
                    rs.room_status_id,
                    rs.room_status_name,
                    rt.room_type_name
                FROM
                    room r
                JOIN available_room_type art ON r.available_room_type_id = art.available_room_type_id
                JOIN room_status rs ON r.room_status_id = rs.room_status_id
                JOIN room_type rt ON art.room_type_id = rt.room_type_id
                WHERE
                    r.room_id = %s;
            """
            values = (room_id,)
            result = db.fetch_one(query, values)

            if result:
                # Create Room_Type instance using fetched room_type_name
                room_type = Room_Type(
                    room_type_name=result['room_type_name'],
                    room_type_id=result['room_type_id']
                )

                available_room_type = Available_Room_Type(
                    apartment_id=result['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount'],
                    available_room_type_id=result['available_room_type_id']
                )
                status = Room_Status(
                    room_status_id=result['room_status_id'],
                    room_status_name=result['room_status_name']
                )

                return Room(
                    room_id=result['room_id'],
                    available_room_type=available_room_type,
                    status=status,
                    room_no=result['room_no'],
                    room_size=result['room_size'],
                    room_floor_no=result['room_floor_no']
                )
            else:
                raise Exception(f"Room with ID {room_id} not found")

        except Exception as e:
            raise Exception(f"Error fetching room by ID: {e}")

    @staticmethod
    def delete(db: Database, room_id: int) -> None:
        try:
            query = """
                DELETE FROM
                    room
                WHERE
                    room_id = %s;
            """
            values = (room_id,)
            db.execute_query(query, values)

        except Exception as e:
            raise Exception(f"Error deleting room: {e}")

    @staticmethod
    def get_all_by_apartment_paginated(db: Database, apartment_id: int, limit: int = 10, offset: int = 0) -> tuple[List['Room'], int]:
        try:
            count_query = """
                SELECT COUNT(*)
                FROM room r
                JOIN available_room_type art ON r.available_room_type_id = art.available_room_type_id
                WHERE art.apartment_id = %s;
            """
            count_result = db.fetch_one(count_query, (apartment_id,))
            total_count = count_result['count']

            query = """
                SELECT
                    r.room_id,
                    r.room_no,
                    r.room_size,
                    r.room_floor_no,
                    art.available_room_type_id,
                    art.apartment_id,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    art.room_type_id,
                    rs.room_status_id,
                    rs.room_status_name,
                    rt.room_type_name
                FROM
                    room r
                JOIN available_room_type art ON r.available_room_type_id = art.available_room_type_id
                JOIN room_status rs ON r.room_status_id = rs.room_status_id
                JOIN room_type rt ON art.room_type_id = rt.room_type_id
                WHERE
                    art.apartment_id = %s
                LIMIT %s OFFSET %s;
            """
            results = db.fetch_all(query, (apartment_id, limit, offset))

            rooms = []
            for result in results:
                # Create Room_Type instance
                room_type = Room_Type(
                    room_type_name=result['room_type_name'],
                    room_type_id=result['room_type_id']
                )

                available_room_type = Available_Room_Type(
                    apartment_id=result['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount'],
                    available_room_type_id=result['available_room_type_id']
                )
                status = Room_Status(
                    room_status_id=result['room_status_id'],
                    room_status_name=result['room_status_name']
                )

                rooms.append(Room(
                    room_id=result['room_id'],
                    available_room_type=available_room_type,
                    status=status,
                    room_no=result['room_no'],
                    room_size=result['room_size'],
                    room_floor_no=result['room_floor_no']
                ))

            return rooms, total_count

        except Exception as e:
            raise Exception(f"Error fetching rooms: {e}")
    from typing import Optional

    @staticmethod
    def get_by_apartment_and_room_type_paginated(
            db: Database, apartment_id: int, room_type_id: int,
            limit: int = 10, offset: int = 0) -> tuple[List['Room'], int]:
        try:
            count_query = """
                SELECT COUNT(*)
                FROM room r
                JOIN available_room_type art ON r.available_room_type_id = art.available_room_type_id
                WHERE art.apartment_id = %s AND art.available_room_type_id = %s AND r.room_status_id = 1;
            """
            count_result = db.fetch_one(
                count_query, (apartment_id, room_type_id))
            total_count = count_result['count']

            query = """
                SELECT
                    r.room_id,
                    r.room_no,
                    r.room_size,
                    r.room_floor_no,
                    art.available_room_type_id,
                    art.apartment_id,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    art.room_type_id,
                    rs.room_status_id,
                    rs.room_status_name,
                    rt.room_type_name
                FROM
                    room r
                JOIN available_room_type art ON r.available_room_type_id = art.available_room_type_id
                JOIN room_status rs ON r.room_status_id = rs.room_status_id
                JOIN room_type rt ON art.room_type_id = rt.room_type_id
                WHERE
                    art.apartment_id = %s AND art.available_room_type_id = %s AND r.room_status_id = 1;
            """
            results = db.fetch_all(
                query, (apartment_id, room_type_id))

            rooms = []
            for result in results:
                room_type = Room_Type(
                    room_type_name=result['room_type_name'],
                    room_type_id=result['room_type_id']
                )

                available_room_type = Available_Room_Type(
                    apartment_id=result['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount'],
                    available_room_type_id=result['available_room_type_id']
                )
                status = Room_Status(
                    room_status_id=result['room_status_id'],
                    room_status_name=result['room_status_name']
                )

                rooms.append(Room(
                    room_id=result['room_id'],
                    available_room_type=available_room_type,
                    status=status,
                    room_no=result['room_no'],
                    room_size=result['room_size'],
                    room_floor_no=result['room_floor_no']
                ))

            return rooms, total_count

        except Exception as e:
            raise Exception(
                f"Error fetching rooms by apartment and room type: {e}")
