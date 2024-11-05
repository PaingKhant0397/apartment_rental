

from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING
from .room import Room
from .user import User
from .rental_status import Rental_Status
from .available_room_type import Available_Room_Type
from .room_type import Room_Type
from .user_role import User_Role
from .room_status import Room_Status

if TYPE_CHECKING:
    from database import Database


class Rental:
    def __init__(self, room: Room, user: User, rental_status: Rental_Status, rental_start_date: date, rental_end_date: date, rental_id: int = None):
        self.__rental_id = rental_id
        self.__room = room
        self.__user = user
        self.__rental_status = rental_status
        self.__rental_start_date = rental_start_date
        self.__rental_end_date = rental_end_date

    def get_rental_id(self) -> int:
        return self.__rental_id

    def get_room(self) -> Room:
        return self.__room

    def get_user(self) -> User:
        return self.__user

    def get_rental_status(self) -> Rental_Status:
        return self.__rental_status

    def get_rental_start_date(self) -> str:
        return self.__rental_start_date.isoformat()

    def get_rental_end_date(self) -> str:
        return self.__rental_end_date.isoformat()

    def to_dict(self) -> dict:
        return {
            'rental_id': self.__rental_id,
            'room': self.__room.to_dict(),
            'user': self.__user.to_dict(),
            'rental_status': self.__rental_status.to_dict(),
            'rental_start_date': self.get_rental_start_date(),
            'rental_end_date': self.get_rental_end_date(),
        }

    def insert(self, db: Database) -> Rental:
        try:
            query = """
                INSERT INTO
                    rental(
                        room_id,
                        user_id,
                        rental_status_id,
                        rental_start_date,
                        rental_end_date
                    )
                VALUES(
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                RETURNING
                    rental_id, room_id, user_id, rental_status_id, rental_start_date, rental_end_date;
            """
            values = (
                self.__room.get_room_id(),
                self.__user.get_user_id(),
                self.__rental_status.get_rental_status_id(),
                self.__rental_start_date,
                self.__rental_end_date,
            )
            result = db.insert(query, values)
            print('db result')
            print(result)
            if result:
                return Rental(
                    rental_id=result['rental_id'],
                    room=self.__room,
                    user=self.__user,
                    rental_status=self.__rental_status,
                    rental_start_date=result['rental_start_date'],
                    rental_end_date=result['rental_end_date']
                )
            else:
                raise Exception("No result returned after insert")

        except Exception as e:
            raise Exception(f"Error inserting rental: {e}")

    def update(self, db: Database) -> Rental:
        try:
            query = """
                UPDATE
                    rental
                SET
                    room_id = %s,
                    user_id = %s,
                    rental_status_id = %s,
                    rental_start_date = %s,
                    rental_end_date = %s
                WHERE
                    rental_id = %s
                RETURNING
                    rental_id, room_id, user_id, rental_status_id, rental_start_date, rental_end_date;
            """
            values = (
                self.__room.get_room_id(),
                self.__user.get_user_id(),
                self.__rental_status.get_rental_status_id(),
                self.__rental_start_date,
                self.__rental_end_date,
                self.__rental_id
            )

            result = db.update(query, values)

            if result:
                return Rental(
                    rental_id=result['rental_id'],
                    room=self.__room,
                    user=self.__user,
                    rental_status=self.__rental_status,
                    rental_start_date=result['rental_start_date'],
                    rental_end_date=result['rental_end_date']
                )
            else:
                raise Exception("No result returned after update")

        except Exception as e:
            raise Exception(f"Error updating rental: {e}")

    @staticmethod
    def get_by_id(db: Database, rental_id: int) -> 'Rental':
        try:
            query = """
                SELECT
                    r.rental_id,
                    r.rental_start_date,
                    r.rental_end_date,
                    rm.room_id,
                    rm.room_no,
                    rm.room_size,
                    rm.room_floor_no,
                    rm.room_status_id,
                    art.available_room_type_id,
                    art.apartment_id,
                    a.apartment_name,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    rt.room_type_name,
                    rt.room_type_id,
                    u.user_id,
                    u.user_name,
                    u.user_email,
                    u.user_role_id,
                    rs.rental_status_id,
                    rs.rental_status_name
                FROM
                    rental r
                JOIN room rm ON r.room_id = rm.room_id
                JOIN available_room_type art ON rm.available_room_type_id = art.available_room_type_id
                JOIN user_table u ON r.user_id = u.user_id
                JOIN rental_status rs ON r.rental_status_id = rs.rental_status_id
                JOIN apartment a ON art.apartment_id = a.apartment_id
                JOIN room_type rt ON art.room_type_id = rt.room_type_id
                WHERE
                    r.rental_id = %s;
            """
            result = db.fetch_one(query, (rental_id,))

            if not result:
                raise ValueError(f"Rental with ID {rental_id} not found.")

            room_type = Room_Type(
                room_type_name=result['room_type_name'],
                room_type_id=result['room_type_id']
            )

            available_room_type = Available_Room_Type(
                apartment_id=result['apartment_id'],
                apartment_name=result['apartment_name'],
                room_type=room_type,
                available_room_type_price=result['available_room_type_price'],
                available_room_type_deposit_amount=result['available_room_type_deposit_amount'],
                available_room_type_id=result['available_room_type_id']
            )
            room_status = Room_Status(result['room_status_id'])
            room = Room(
                available_room_type=available_room_type,
                status=room_status,
                room_no=result['room_no'],
                room_size=result['room_size'],
                room_floor_no=result['room_floor_no'],
                room_id=result['room_id']
            )

            user_role = User_Role().get_by_id(db, result['user_role_id'])

            user = User(
                user_id=result['user_id'],
                user_name=result['user_name'],
                user_email=result['user_email'],
                role=user_role
            )

            rental_status = Rental_Status(
                rental_status_id=result['rental_status_id'],
                rental_status_name=result['rental_status_name']
            )

            return Rental(
                rental_id=result['rental_id'],
                room=room,
                user=user,
                rental_status=rental_status,
                rental_start_date=result['rental_start_date'],
                rental_end_date=result['rental_end_date']
            )

        except Exception as e:
            raise Exception(f"Error fetching rental with ID {rental_id}: {e}")

    @staticmethod
    def get_all_paginated(db: Database, limit: int, offset: int) -> tuple[int, list[Rental]]:
        try:
            # Query to count total rentals
            count_query = """
                SELECT COUNT(*) AS total_count
                FROM rental;
            """
            total_count_result = db.fetch_one(count_query)
            total_count = total_count_result['total_count'] if total_count_result else 0

            # Query to fetch paginated rentals
            rentals_query = """
                SELECT
                    r.rental_id,
                    r.rental_start_date,
                    r.rental_end_date,
                    rm.room_id,
                    rm.room_no,
                    rm.room_size,
                    rm.room_floor_no,
                    rm.room_status_id,
                    art.available_room_type_id,
                    art.apartment_id,
                    a.apartment_name,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    rt.room_type_name,
                    rt.room_type_id,
                    u.user_id,
                    u.user_name,
                    u.user_email,
                    u.user_role_id,
                    rs.rental_status_id,
                    rs.rental_status_name
                FROM
                    rental r
                JOIN room rm ON r.room_id = rm.room_id
                JOIN available_room_type art ON rm.available_room_type_id = art.available_room_type_id
                JOIN user_table u ON r.user_id = u.user_id
                JOIN rental_status rs ON r.rental_status_id = rs.rental_status_id
                JOIN apartment a ON art.apartment_id = a.apartment_id
                JOIN room_type rt ON art.room_type_id = rt.room_type_id
                ORDER BY r.rental_id
                LIMIT %s OFFSET %s;
            """

            # Fetching the paginated results with parameters (limit, offset)
            results = db.fetch_all(rentals_query, (limit, offset))

            rentals = []
            for result in results:
                # Create Room_Status instance
                room_status = Room_Status.get_by_id(
                    db, result['room_status_id'])

                # Create Room_Type instance
                room_type = Room_Type(
                    room_type_name=result['room_type_name'],
                    room_type_id=result['room_type_id']
                )

                # Create Available_Room_Type instance
                available_room_type = Available_Room_Type(
                    apartment_id=result['apartment_id'],
                    apartment_name=result['apartment_name'],
                    room_type=room_type,
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount'],
                    available_room_type_id=result['available_room_type_id']
                )

                # Create Room instance
                room = Room(
                    available_room_type=available_room_type,
                    status=room_status,
                    room_no=result.get('room_no'),  # Use get to avoid KeyError
                    room_size=result.get('room_size'),
                    room_floor_no=result.get('room_floor_no'),
                    room_id=result['room_id']
                )

                # Create User instance
                user_role = User_Role().get_by_id(db, result['user_role_id'])

                user = User(
                    user_id=result['user_id'],
                    user_name=result['user_name'],
                    user_email=result['user_email'],
                    role=user_role
                )

                # Create Rental_Status instance
                rental_status = Rental_Status(
                    rental_status_id=result['rental_status_id'],
                    rental_status_name=result['rental_status_name']
                )

                # Append Rental instance to the list
                rentals.append(Rental(
                    rental_id=result['rental_id'],
                    room=room,
                    user=user,
                    rental_status=rental_status,
                    rental_start_date=result['rental_start_date'],
                    rental_end_date=result['rental_end_date']
                ))

            # Return both the total count and the list of rentals
            return total_count, rentals

        except Exception as e:
            raise Exception(f"Error fetching rentals: {e}")

    @staticmethod
    def delete(db: Database, rental_id: int) -> None:
        try:
            query = """
                DELETE FROM
                    rental
                WHERE
                    rental_id = %s;
            """
            values = (rental_id,)
            db.execute_query(query, values)

        except Exception as e:
            raise Exception(f"Error deleting rental: {e}")
