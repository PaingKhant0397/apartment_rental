from psycopg2 import DatabaseError
from utils import setup_logger

logger = setup_logger(__name__)


class SchemaManager:

    def __init__(self, cursor):
        self.cursor = cursor

    def create_tables(self):
        """Create all tables required for the database schema."""

        queries = [

            # Admin Table
            """
            CREATE TABLE IF NOT EXISTS admin_table(
                admin_id SERIAL PRIMARY KEY,
                admin_username VARCHAR(64) NOT NULL,
                admin_password VARCHAR(126) NOT NULL
            );
            """,

            # User Role Table
            """
            CREATE TABLE IF NOT EXISTS user_role(
                user_role_id SERIAL PRIMARY KEY,
                user_role_name VARCHAR(64) NOT NULL
            );
            """,
            # Booking Status Table
            """
            CREATE TABLE IF NOT EXISTS booking_status(
                booking_status_id SERIAL PRIMARY KEY,
                booking_status_name VARCHAR(64) NOT NULL
            );
            """,
            # Room Type Table
            """
            CREATE TABLE IF NOT EXISTS room_type(
                room_type_id SERIAL PRIMARY KEY,
                room_type_name VARCHAR(64) NOT NULL
            );
            """,
            # Room Status Table
            """
            CREATE TABLE IF NOT EXISTS room_status(
                room_status_id SERIAL PRIMARY KEY,
                room_status_name VARCHAR(64) NOT NULL
            );
            """,
            # Apartment Table
            """
            CREATE TABLE IF NOT EXISTS apartment(
                apartment_id SERIAL PRIMARY KEY,
                apartment_name VARCHAR(64) NOT NULL,
                apartment_image TEXT,
                apartment_desc TEXT,
                apartment_date_built DATE,
                apartment_address VARCHAR(40) NOT NULL,
                apartment_postal_code VARCHAR(6) NOT NULL,
                apartment_capacity INTEGER
            );
            """,
            # Available Room Type Table
            """
            CREATE TABLE IF NOT EXISTS available_room_type(
                available_room_type_id SERIAL PRIMARY KEY,
                apartment_id INTEGER NOT NULL,
                room_type_id INTEGER NOT NULL,
                available_room_type_price NUMERIC(10, 2),
                available_room_type_deposit_amount NUMERIC(10, 2),
                FOREIGN KEY (apartment_id) REFERENCES apartment(apartment_id)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (room_type_id) REFERENCES room_type(room_type_id)
                    ON DELETE CASCADE ON UPDATE CASCADE
            );
            """,
            # Room Table
            """
            CREATE TABLE IF NOT EXISTS room(
                room_id SERIAL PRIMARY KEY,
                available_room_type_id INTEGER NOT NULL,
                room_status_id INTEGER NOT NULL,
                room_no VARCHAR(10) NOT NULL,
                room_floor_no VARCHAR(10) NOT NULL,
                room_size VARCHAR(10),
                FOREIGN KEY (available_room_type_id) REFERENCES available_room_type(available_room_type_id)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (room_status_id) REFERENCES room_status(room_status_id)
                    ON DELETE RESTRICT ON UPDATE CASCADE
            );
            """,
            # User Table
            """
            CREATE TABLE IF NOT EXISTS user_table(
                user_id SERIAL PRIMARY KEY,
                user_role_id INTEGER NOT NULL,
                user_name VARCHAR(64) NOT NULL,
                user_email VARCHAR(128) NOT NULL,
                user_password VARCHAR(128) NOT NULL,
                FOREIGN KEY (user_role_id) REFERENCES user_role(user_role_id)
                    ON DELETE RESTRICT ON UPDATE CASCADE
            );
            """,
            # Booking Table
            """
            CREATE TABLE IF NOT EXISTS booking(
                booking_id SERIAL PRIMARY KEY,
                available_room_type_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                booking_status_id INTEGER NOT NULL,
                booking_date DATE NOT NULL,
                booking_comment TEXT,
                FOREIGN KEY (available_room_type_id) REFERENCES available_room_type(available_room_type_id)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (user_id) REFERENCES user_table(user_id)
                    ON DELETE SET NULL ON UPDATE CASCADE,
                FOREIGN KEY (booking_status_id) REFERENCES booking_status(booking_status_id)
                    ON DELETE SET NULL ON UPDATE CASCADE
            );
            """,
            # Rental status
            """ 
            CREATE TABLE IF NOT EXISTS rental_status (
                rental_status_id SERIAL PRIMARY KEY,
                rental_status_name VARCHAR(255) NOT NULL
            );

            """,
            # Rental table
            """ 
            CREATE TABLE IF NOT EXISTS rental (
                rental_id SERIAL PRIMARY KEY,
                user_id INT NOT NULL,
                room_id INT NOT NULL,
                rental_status_id INT NOT NULL,
                rental_start_date DATE NOT NULL,
                rental_end_date DATE NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user_table(user_id),
                FOREIGN KEY (room_id) REFERENCES room(room_id),
                FOREIGN KEY (rental_status_id) REFERENCES rental_status(rental_status_id)
            );

            """,
            # Invoice Status Table
            """ 
            CREATE TABLE IF NOT EXISTS invoice_status (
                invoice_status_id SERIAL PRIMARY KEY,  
                invoice_status_name VARCHAR(50) NOT NULL UNIQUE  
            );

            """,
            # Invoice Table
            """  
            CREATE TABLE IF NOT EXISTS invoice (
                invoice_id SERIAL PRIMARY KEY,  
                rental_id INT NOT NULL,  
                invoice_status_id INT NOT NULL,  
                water_bill DECIMAL(10, 2) NOT NULL,  
                electricity_bill DECIMAL(10, 2) NOT NULL, 
                total_amount DECIMAL(10, 2) NOT NULL,  
                issued_date DATE NOT NULL,  
                due_date DATE NOT NULL,  
                FOREIGN KEY (rental_id) REFERENCES rental(rental_id) ON DELETE CASCADE,  
                FOREIGN KEY (invoice_status_id) REFERENCES invoice_status(invoice_status_id) ON DELETE CASCADE  
            );
            """
        ]

        try:
            for query in queries:
                self.cursor.execute(query)
            logger.info("Tables created successfully.")
        except DatabaseError as e:
            logger.error(f"Error creating tables: {e}")
            raise Exception(f"Error creating tables: {e}")
