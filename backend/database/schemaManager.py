from psycopg2 import DatabaseError
from utils import setup_logger

logger = setup_logger(__name__)


class SchemaManager:

    def __init__(self, cursor):
        self.cursor = cursor

    def create_tables(self):
        """Create all tables required for the database schema."""

        queries = [
            # User Role Table
            """
            CREATE TABLE IF NOT EXISTS user_role(
                userRoleID SERIAL PRIMARY KEY,
                userRoleName VARCHAR(20) NOT NULL
            );
            """,
            # Reservation Status Table
            """
            CREATE TABLE IF NOT EXISTS reservation_status(
                reservationStatusID SERIAL PRIMARY KEY,
                reservationStatusName VARCHAR(20) NOT NULL
            );
            """,
            # Room Type Table
            """
            CREATE TABLE IF NOT EXISTS room_type(
                roomTypeID SERIAL PRIMARY KEY,
                roomTypeName VARCHAR(20) NOT NULL,
                roomTypePrice DOUBLE PRECISION  -- Removed the trailing comma
            );
            """,
            # Room Status Table
            """
            CREATE TABLE IF NOT EXISTS room_status(
                roomStatusID SERIAL PRIMARY KEY,
                roomStatusName VARCHAR(20) NOT NULL
            );
            """,
            # Apartment Table
            """
            CREATE TABLE IF NOT EXISTS apartment(
                apartmentID SERIAL PRIMARY KEY,
                apartmentName VARCHAR(20) NOT NULL,
                apartmentDesc TEXT,
                apartmentDateBuilt DATE,
                apartmentAddress VARCHAR(40) NOT NULL,
                apartmentPostalCode VARCHAR(6) NOT NULL,
                apartmentCapacity INTEGER
            );
            """,
            # Room Table
            """
            CREATE TABLE IF NOT EXISTS room(
                roomID SERIAL PRIMARY KEY,
                apartmentID INTEGER NOT NULL,
                roomTypeID INTEGER NOT NULL,
                roomStatusID INTEGER NOT NULL,
                roomNo VARCHAR(10) NOT NULL,
                roomFloorNo VARCHAR(10) NOT NULL,
                roomSize VARCHAR(10),
                FOREIGN KEY (apartmentID) REFERENCES apartment(apartmentID)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (roomTypeID) REFERENCES room_type(roomTypeID)
                    ON DELETE RESTRICT ON UPDATE CASCADE,
                FOREIGN KEY (roomStatusID) REFERENCES room_status(roomStatusID)
                    ON DELETE RESTRICT ON UPDATE CASCADE
            );
            """,
            # User Table
            """
            CREATE TABLE IF NOT EXISTS user_table(
                userID SERIAL PRIMARY KEY,
                userRoleID INTEGER NOT NULL,
                userName VARCHAR(20) NOT NULL,
                userEmail VARCHAR(128) NOT NULL,
                userPassword VARCHAR(128) NOT NULL,
                FOREIGN KEY (userRoleID) REFERENCES user_role(userRoleID)
                    ON DELETE RESTRICT ON UPDATE CASCADE
            );
            """,
            # Reservation Table
            """
            CREATE TABLE IF NOT EXISTS reservation(
                reservationID SERIAL PRIMARY KEY,
                userID INTEGER NOT NULL,
                roomID INTEGER NOT NULL,
                reservationStatusID INTEGER NOT NULL,
                reservationDate DATE NOT NULL,
                reservationComment TEXT,
                FOREIGN KEY (userID) REFERENCES user_table(userID)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (roomID) REFERENCES room(roomID)
                    ON DELETE SET NULL ON UPDATE CASCADE,
                FOREIGN KEY (reservationStatusID) REFERENCES reservation_status(reservationStatusID)
                    ON DELETE SET NULL ON UPDATE CASCADE
            );
            """
        ]

        try:
            for query in queries:
                self.cursor.execute(query)
            # logger.info("Tables Created Successfully.")
        except DatabaseError as e:
            logger.error(f"Error creating tables: {e}")
            raise Exception(f"Error creating tables: {e}")
