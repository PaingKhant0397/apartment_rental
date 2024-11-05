
from __future__ import annotations
from database import Database
from .room_type import Room_Type
from .available_room_type import Available_Room_Type
from typing import List, TYPE_CHECKING

from datetime import date, datetime
from decimal import Decimal
from .available_room_type import Available_Room_Type
from .room_type import Room_Type
if TYPE_CHECKING:
    from database import Database


class Apartment:

    def __init__(self,  apartment_name: str, apartment_address: str, apartment_desc: str, apartment_postal_code: int, apartment_capacity: int, apartment_image: str, apartment_date_built: date = None,  apartment_id: int = None, available_room_types: List[Available_Room_Type] = []):
        self.__apartment_id = apartment_id
        self.__apartment_name = apartment_name
        self.__apartment_image = apartment_image
        self.__apartment_address = apartment_address
        self.__apartment_desc = apartment_desc
        self.__apartment_date_built = apartment_date_built
        self.__apartment_postal_code = apartment_postal_code
        self.__apartment_capacity = apartment_capacity
        self.__available_room_types = available_room_types

    def to_dict(self) -> dict:
        return {
            'apartment_id': self.__apartment_id,
            'apartment_name': self.__apartment_name,
            'apartment_image': self.__apartment_image,
            'apartment_address': self.__apartment_address,
            'apartment_desc': self.__apartment_desc,
            'apartment_date_built': self.__apartment_date_built.isoformat() if isinstance(self.__apartment_date_built, date) else str(self.__apartment_date_built),
            'apartment_postal_code': self.__apartment_postal_code,
            'apartment_capacity': self.__apartment_capacity,
            'available_room_types': [available_room_type.to_dict() for available_room_type in self.__available_room_types]
        }

    def get_apartment_id(self):
        return self.__apartment_id

    def get_apartment_name(self):
        return self.__apartment_name

    def get_apartment_address(self):
        return self.__apartment_address

    def get_apartment_desc(self):
        return self.__apartment_desc

    def get_apartment_date_built(self):
        return self.__apartment_date_built

    def get_apartment_postal_code(self):
        return self.__apartment_postal_code

    def get_apartment_capacity(self):
        return self.__apartment_capacity

    def get_available_room_type(self):
        return self.__available_room_type

    def insert(self, db: Database) -> 'Apartment':
        try:
            query = """
                INSERT INTO
                    apartment(
                        apartment_name,
                        apartment_image,
                        apartment_address,
                        apartment_desc,
                        apartment_date_built,
                        apartment_postal_code,
                        apartment_capacity
                    )
                VALUES(
                    %s,%s,%s,%s,%s,%s,%s
                )
                RETURNING 
                    apartment_id,apartment_name,apartment_image,apartment_address,apartment_desc,
                    apartment_date_built,apartment_postal_code,apartment_capacity;
            """

            values = (
                self.__apartment_name,
                self.__apartment_image,
                self.__apartment_address,
                self.__apartment_desc,
                self.__apartment_date_built,
                self.__apartment_postal_code,
                self.__apartment_capacity,
            )

            result = db.insert(query, values)
            if result:
                apartment_date_built = result['apartment_date_built'] if isinstance(
                    result['apartment_date_built'], date) else datetime.strptime(result['apartment_date_built'], '%Y-%m-%d').date()
                return Apartment(
                    apartment_id=result['apartment_id'],
                    apartment_name=result['apartment_name'],
                    apartment_image=result['apartment_image'],
                    apartment_desc=result['apartment_desc'],
                    apartment_address=result['apartment_address'],
                    apartment_capacity=result['apartment_capacity'],
                    apartment_date_built=apartment_date_built,
                    apartment_postal_code=result['apartment_postal_code']
                )
            else:
                raise Exception(
                    "No result returned")
        except Exception as e:
            raise Exception(f"Error registering apartment: {e}")

    def update(self, db: Database) -> 'Apartment':
        try:
            query = """
                    UPDATE 
                        apartment 
                    SET
                        apartment_name=%s,
                        apartment_image=%s,
                        apartment_address=%s,
                        apartment_desc=%s,
                        apartment_date_built=%s,
                        apartment_postal_code=%s,
                        apartment_capacity=%s
                    WHERE 
                        apartment_id=%s
                    RETURNING 
                        apartment_id,apartment_name,apartment_image,apartment_address,apartment_desc,
                        apartment_date_built,apartment_postal_code,apartment_capacity;
                """

            values = (
                self.__apartment_name,
                self.__apartment_image,
                self.__apartment_address,
                self.__apartment_desc,
                self.__apartment_date_built,
                self.__apartment_postal_code,
                self.__apartment_capacity,
                self.__apartment_id
            )

            result = db.update(query, values)
            if result:
                apartment_date_built = result['apartment_date_built']
                if isinstance(apartment_date_built, str):
                    try:
                        print(f"date built is {apartment_date_built}")
                        apartment_date_built = datetime.strptime(
                            apartment_date_built, '%Y-%m-%d').date()
                    except ValueError:

                        apartment_date_built = None
                available_room_types = Available_Room_Type.get_all_by_apartment(
                    db, apartment_id=result['apartment_id'])
                apartment = Apartment(
                    apartment_id=result['apartment_id'],
                    apartment_name=result['apartment_name'],
                    apartment_image=result['apartment_image'],
                    apartment_desc=result['apartment_desc'],
                    apartment_address=result['apartment_address'],
                    apartment_capacity=result['apartment_capacity'],
                    apartment_date_built=apartment_date_built,
                    apartment_postal_code=result['apartment_postal_code'],
                    available_room_types=available_room_types
                )
                return apartment
            else:
                raise Exception(
                    "No result returned")
        except Exception as e:
            raise Exception(f"Error updating apartment: {e}")

    @staticmethod
    def get_by_id(db: Database, apartment_id: int) -> 'Apartment':
        try:
            query = """
                SELECT 
                    apartment_id,
                    apartment_name,
                    apartment_address,
                    apartment_desc,
                    apartment_image,
                    apartment_date_built,
                    apartment_postal_code,
                    apartment_capacity
                FROM 
                    apartment 
                WHERE 
                    apartment_id = %s
            """
            values = (apartment_id,)
            result = db.fetch_one(query, values)

            if result:
                apartment_date_built = result['apartment_date_built']
                if isinstance(apartment_date_built, str):
                    try:
                        print(f"date built is {apartment_date_built}")
                        apartment_date_built = datetime.strptime(
                            apartment_date_built, '%Y-%m-%d').date()
                    except ValueError:

                        apartment_date_built = None
                available_room_types = Available_Room_Type.get_all_by_apartment(
                    db, apartment_id=apartment_id)
                apartment = Apartment(
                    apartment_id=result['apartment_id'],
                    apartment_name=result['apartment_name'],
                    apartment_image=result['apartment_image'],
                    apartment_desc=result['apartment_desc'],
                    apartment_address=result['apartment_address'],
                    apartment_capacity=result['apartment_capacity'],
                    apartment_date_built=apartment_date_built,
                    apartment_postal_code=result['apartment_postal_code'],
                    available_room_types=available_room_types
                )
                return apartment

            else:
                raise Exception(f"No apartment found with id: {apartment_id}")
        except Exception as e:
            raise Exception(f"Error getting apartment by id: {e}")

    @staticmethod
    def delete(db: Database, apartment_id: int) -> None:
        try:
            query = """
                DELETE 
                    FROM 
                        apartment 
                    WHERE apartment_id=%s;
            """
            values = (apartment_id,)
            db.execute_query(query, values)

        except Exception as e:
            raise Exception(f"Error deleting apartment: {e}")

    @staticmethod
    def get_all_paginated(db: Database, limit: int, offset: int) -> tuple[List[Apartment], int]:
        """
        Fetch all apartments with pagination, joining with available room types and room types.
        Args:
            db (Database): The database connection instance.
            limit (int): Maximum number of results to return.
            offset (int): Number of results to skip before starting to return results.
        Returns:
            List[Apartment]: A list of Apartment objects.
        """
        try:

            query = """
                SELECT 
                    apartment_id,
                    apartment_name,
                    apartment_image,
                    apartment_address,
                    apartment_desc,
                    apartment_date_built,
                    apartment_postal_code,
                    apartment_capacity
                FROM 
                    apartment 
                ORDER BY 
                    apartment_id
                LIMIT %s OFFSET %s;
            """

            apartments_data = db.fetch_all(query, (limit, offset))
            count_query = "SELECT COUNT(*) FROM apartment"

            apartments_data = db.fetch_all(query, (limit, offset))
            total_count = db.fetch_one(count_query)['count']

            apartments = []
            for result in apartments_data:
                apartment_date_built = result['apartment_date_built'] if isinstance(
                    result['apartment_date_built'], date) else datetime.strptime(result['apartment_date_built'], '%Y-%m-%d').date()

                apartment_id = result['apartment_id']

                available_room_types = Available_Room_Type.get_all_by_apartment(
                    db, apartment_id=apartment_id)

                apartment = Apartment(
                    apartment_id=apartment_id,
                    apartment_name=result['apartment_name'],
                    apartment_image=result['apartment_image'],
                    apartment_desc=result['apartment_desc'],
                    apartment_address=result['apartment_address'],
                    apartment_capacity=result['apartment_capacity'],
                    apartment_date_built=apartment_date_built,
                    apartment_postal_code=result['apartment_postal_code'],
                    available_room_types=available_room_types
                )
                apartments.append(apartment)

            # Return the list of Apartment objects
            return apartments, total_count

        except Exception as e:

            raise Exception(f"Error fetching apartments with pagination: {e}")
