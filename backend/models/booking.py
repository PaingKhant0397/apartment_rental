from __future__ import annotations
from typing import List, Tuple
from typing import List, TYPE_CHECKING
from datetime import date

from .user import User
from .user_role import User_Role
from .available_room_type import Available_Room_Type
from .booking_status import Booking_Status
from .room_type import Room_Type

if TYPE_CHECKING:
    from database import Database


class Booking:

    def __init__(self, user: User, room_type: Available_Room_Type, status: Booking_Status, booking_date: date, booking_comment: str = None, booking_id: int = None,):
        self.__booking_id = booking_id
        self.__user = user
        self.__room_type = room_type
        self.__status = status
        self.__booking_date = booking_date
        self.__booking_comment = booking_comment

    def get_booking_id(self) -> int:
        return self.__booking_id

    def get_user(self) -> User:
        return self.__user

    def get_room_type(self) -> Available_Room_Type:
        return self.__room_type

    def get_status(self) -> Booking_Status:
        return self.__status

    def get_booking_date(self) -> date:
        return self.__booking_date

    def get_booking_comment(self) -> str:
        return self.__booking_comment

    def to_dict(self) -> dict:
        """Convert the Booking object to a dictionary."""
        return {
            'booking_id': self.__booking_id,
            'user': self.__user.to_dict(),
            'room_type': self.__room_type.to_dict(),
            'status': self.__status.to_dict(),
            'booking_date': str(self.__booking_date),  # Convert date to string
            'booking_comment': self.__booking_comment
        }

    def insert(self, db: Database) -> Booking:
        try:
            query = """
                INSERT INTO
                    booking(available_room_type_id, user_id,
                            booking_status_id, booking_date, booking_comment)
                VALUES(%s, %s, %s, %s, %s)
                RETURNING booking_id, available_room_type_id, user_id, booking_status_id, booking_date, booking_comment;
            """
            values = (
                self.__room_type.get_available_room_type_id(),
                self.__user.get_user_id(),
                self.__status.get_booking_status_id(),
                self.__booking_date,
                self.__booking_comment
            )
            result = db.insert(query, values)
            if result:
                return Booking(
                    booking_id=result['booking_id'],
                    user=self.__user,
                    room_type=self.__room_type,
                    status=self.__status,
                    booking_date=result['booking_date'],
                    booking_comment=result['booking_comment']
                )
            else:
                raise Exception("No result returned after insert")

        except Exception as e:
            raise Exception(f"Error inserting booking: {e}")

    def update(self, db: Database) -> Booking:
        try:
            query = """
                UPDATE
                    booking
                SET
                    available_room_type_id = %s,
                    user_id = %s,
                    booking_status_id = %s,
                    booking_date = %s,
                    booking_comment = %s
                WHERE
                    booking_id = %s
                RETURNING booking_id, available_room_type_id, user_id, booking_status_id, booking_date, booking_comment;
            """
            values = (
                self.__room_type.get_available_room_type_id(),
                self.__user.get_user_id(),
                self.__status.get_booking_status_id(),
                self.__booking_date,
                self.__booking_comment,
                self.__booking_id
            )

            result = db.update(query, values)
            if result:
                return Booking(
                    booking_id=result['booking_id'],
                    user=self.__user,
                    room_type=self.__room_type,
                    status=self.__status,
                    booking_date=result['booking_date'],
                    booking_comment=result['booking_comment']
                )
            else:
                raise Exception("No result returned after update")

        except Exception as e:
            raise Exception(f"Error updating booking: {e}")

    @staticmethod
    def delete(db: Database, booking_id: int) -> None:
        try:
            query = """
                DELETE FROM
                    booking
                WHERE
                    booking_id = %s;
            """
            values = (booking_id,)
            db.execute_query(query, values)

        except Exception as e:
            raise Exception(f"Error deleting booking: {e}")

    @staticmethod
    def get_by_id(db: Database, booking_id: int) -> Booking:

        try:
            query = """
                SELECT
                    b.booking_id,
                    b.booking_date,
                    b.booking_comment,
                    art.available_room_type_id,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    rt.room_type_name,
                    rt.room_type_id,
                    a.apartment_id,
                    a.apartment_name,
                    u.user_id,
                    u.user_name,
                    u.user_email,
                    bs.booking_status_id,
                    bs.booking_status_name
                FROM
                    booking b
                JOIN available_room_type art ON b.available_room_type_id = art.available_room_type_id
                JOIN room_type rt ON art.room_type_id = rt.room_type_id
                JOIN apartment a ON art.apartment_id = a.apartment_id
                JOIN user_table u ON b.user_id = u.user_id
                JOIN booking_status bs ON b.booking_status_id = bs.booking_status_id
                WHERE b.booking_id = %s;
            """
            result = db.fetch_one(query, (booking_id,))

            if not result:
                raise Exception(f"Booking with ID {booking_id} not found.")

            # Adjust user role as needed
            role = User_Role(user_role_id=1, user_role_name='normal')
            user = User(
                user_id=result['user_id'],
                user_name=result['user_name'],
                user_email=result['user_email'],
                role=role
            )
            room_type = Available_Room_Type(
                available_room_type_id=result['available_room_type_id'],
                apartment_id=result['apartment_id'],
                room_type=Room_Type(
                    result['room_type_name'], result['room_type_id']),
                available_room_type_price=result['available_room_type_price'],
                available_room_type_deposit_amount=result['available_room_type_deposit_amount']
            )
            status = Booking_Status(
                result['booking_status_id'], result['booking_status_name']
            )

            return Booking(
                booking_id=result['booking_id'],
                user=user,
                room_type=room_type,
                status=status,
                booking_date=result['booking_date'],
                booking_comment=result['booking_comment']
            )

        except Exception as e:
            raise Exception(f"Error fetching booking by ID: {e}")

    @staticmethod
    def get_all_paginated(db: Database, limit: int, offset: int) -> Tuple[List[Booking], int]:

        try:
            query = """
                SELECT
                    b.booking_id,
                    b.booking_date,
                    b.booking_comment,
                    art.available_room_type_id,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    rt.room_type_name,
                    rt.room_type_id,
                    a.apartment_id,
                    a.apartment_name,
                    u.user_id,
                    u.user_name,
                    u.user_email,
                    bs.booking_status_id,
                    bs.booking_status_name
                FROM
                    booking b
                JOIN available_room_type art ON b.available_room_type_id = art.available_room_type_id
                JOIN room_type rt ON art.room_type_id = rt.room_type_id
                JOIN apartment a ON art.apartment_id = a.apartment_id
                JOIN user_table u ON b.user_id = u.user_id
                JOIN booking_status bs ON b.booking_status_id = bs.booking_status_id
                ORDER BY b.booking_id
                LIMIT %s OFFSET %s;
            """
            bookings_data = db.fetch_all(query, (limit, offset))

            # Fetch total count of bookings
            count_query = "SELECT COUNT(*) FROM booking;"
            total_count = db.fetch_one(count_query)['count']

            bookings = []
            for result in bookings_data:
                role = User_Role(user_role_id=1, user_role_name='normal')
                user = User(user_id=result['user_id'],
                            user_name=result['user_name'],
                            user_email=result['user_email'],
                            role=role
                            )
                room_type = Available_Room_Type(
                    available_room_type_id=result['available_room_type_id'],
                    apartment_id=result['apartment_id'],
                    apartment_name=result['apartment_name'],
                    room_type=Room_Type(result['room_type_name'],
                                        result['room_type_id']),
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount']
                )
                status = Booking_Status(
                    booking_status_id=result['booking_status_id'], booking_status_name=result['booking_status_name'])

                bookings.append(Booking(
                    booking_id=result['booking_id'],
                    user=user,
                    room_type=room_type,
                    status=status,
                    booking_date=result['booking_date'],
                    booking_comment=result['booking_comment']
                ))

            return bookings, total_count

        except Exception as e:
            raise Exception(f"Error fetching bookings with pagination: {e}")
