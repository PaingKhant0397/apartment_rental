from __future__ import annotations
from typing import List, TYPE_CHECKING
from .room_type import Room_Type
if TYPE_CHECKING:
    from database import Database
    from decimal import Decimal


class Available_Room_Type:

    def __init__(self, apartment_id: int, room_type: Room_Type, available_room_type_price: Decimal, available_room_type_deposit_amount: Decimal, available_room_type_id: int = None, apartment_name: str = None,):

        self.__available_room_type_id = available_room_type_id
        self.__apartment_id = apartment_id
        self.__apartment_name = apartment_name
        self.__room_type = room_type
        self.__available_room_type_price = available_room_type_price
        self.__available_room_type_deposit_amount = available_room_type_deposit_amount

    def get_available_room_type_id(self) -> int:
        return self.__available_room_type_id

    def get_apartment_id(self) -> int:
        return self.__apartment_id

    def get_room_type(self) -> Room_Type:
        return self.__room_type

    def get_available_room_type_price(self) -> Decimal:
        return self.__available_room_type_price

    def get_available_room_type_deposit_amount(self) -> Decimal:
        return self.__available_room_type_deposit_amount

    def to_dict(self) -> dict:
        return {
            'available_room_type_id': self.__available_room_type_id,
            'apartment_id': self.__apartment_id,
            'apartment_name': self.__apartment_name,
            'room_type': self.__room_type.to_dict(),
            'available_room_type_price': float(self.__available_room_type_price),
            'available_room_type_deposit_amount': float(self.__available_room_type_deposit_amount)
        }

    def insert(self, db: Database) -> Available_Room_Type:
        try:
            query = """
                INSERT INTO
                    available_room_type(
                        apartment_id,
                        room_type_id,
                        available_room_type_price,
                        available_room_type_deposit_amount
                    )
                VALUES(
                    %s,
                    %s,
                    %s,
                    %s
                )
                RETURNING
                    available_room_type_id,apartment_id, room_type_id, available_room_type_price, available_room_type_deposit_amount;
            """
            values = (
                self.__apartment_id,
                self.__room_type.get_room_type_id(),
                self.__available_room_type_price,
                self.__available_room_type_deposit_amount,
            )
            result = db.insert(query, values)
            if result:
                room_type = Room_Type.get_by_id(db, result['room_type_id'])
                return Available_Room_Type(
                    available_room_type_id=result['available_room_type_id'],
                    apartment_id=result['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount']
                )
            else:
                raise Exception(f"No result returned after insert")

        except Exception as e:
            raise Exception(f"Error inserting available room type: {e}")

    def update(self, db: Database) -> Available_Room_Type:
        try:
            query = """
                UPDATE
                    available_room_type
                SET
                    apartment_id = %s,
                    room_type_id = %s,
                    available_room_type_price = %s,
                    available_room_type_deposit_amount = %s
                WHERE
                    available_room_type_id = %s
                RETURNING
                    available_room_type_id, apartment_id, room_type_id, available_room_type_price, available_room_type_deposit_amount;
            """
            values = (
                self.__apartment_id,
                self.__room_type.get_room_type_id(),
                self.__available_room_type_price,
                self.__available_room_type_deposit_amount,
                self.__available_room_type_id  # For WHERE condition
            )

            # Assuming db.update executes the query and returns the result
            result = db.update(query, values)
            if result:
                room_type = Room_Type.get_by_id(db, result['room_type_id'])
                return Available_Room_Type(
                    available_room_type_id=result['available_room_type_id'],
                    apartment_id=result['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount']
                )
            else:
                raise Exception(f"No result returned after update")

        except Exception as e:
            raise Exception(f"Error updating available room type: {e}")

    @staticmethod
    def get_by_id(db: Database, available_room_type_id: int) -> 'Available_Room_Type':
        try:
            query = """
                SELECT
                    art.available_room_type_id,
                    art.apartment_id,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    rt.room_type_id,
                    rt.room_type_name
                FROM
                    available_room_type art
                INNER JOIN
                    room_type rt ON art.room_type_id = rt.room_type_id
                WHERE
                    art.available_room_type_id = %s;
            """
            values = (available_room_type_id,)
            result = db.fetch_one(query, values)

            if result:
                room_type = Room_Type(
                    room_type_id=result['room_type_id'],
                    room_type_name=result['room_type_name']
                )

                return Available_Room_Type(
                    available_room_type_id=result['available_room_type_id'],
                    apartment_id=result['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount']
                )
            else:
                raise Exception(
                    f"Available room type with ID {available_room_type_id} not found")

        except Exception as e:
            raise Exception(f"Error fetching available room type by ID: {e}")

    @staticmethod
    def delete(db: Database, available_room_type_id: int) -> None:
        try:
            query = """
                DELETE FROM
                    available_room_type
                WHERE
                    available_room_type_id = %s;
            """
            values = (available_room_type_id,)
            db.execute_query(query, values)

        except Exception as e:
            raise Exception(f"Error deleting available room type: {e}")

    @staticmethod
    def get_all_by_apartment(db: Database, apartment_id: int) -> List['Available_Room_Type']:
        try:
            query = """
                SELECT 
                    art.available_room_type_id,
                    art.apartment_id,
                    art.available_room_type_price,
                    art.available_room_type_deposit_amount,
                    rt.room_type_id,
                    rt.room_type_name
                FROM 
                    available_room_type art
                INNER JOIN 
                    room_type rt ON art.room_type_id = rt.room_type_id
                WHERE 
                    art.apartment_id = %s;
            """
            values = (apartment_id,)
            results = db.fetch_all(query, values)

            # Ensure results is not None and is a list
            if results is None:
                return []

            available_room_types = []

            for result in results:
                room_type = Room_Type(
                    room_type_id=result['room_type_id'],
                    room_type_name=result['room_type_name']
                )

                available_room_type = Available_Room_Type(
                    available_room_type_id=result['available_room_type_id'],
                    apartment_id=result['apartment_id'],
                    room_type=room_type,
                    available_room_type_price=result['available_room_type_price'],
                    available_room_type_deposit_amount=result['available_room_type_deposit_amount']
                )

                available_room_types.append(available_room_type)

            return available_room_types

        except Exception as e:
            raise Exception(
                f"Error fetching available room types for apartment {apartment_id}: {e}")
