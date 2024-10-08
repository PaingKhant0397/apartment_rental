import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from utils import setup_logger
from .schemaManager import SchemaManager

logger = setup_logger(__name__)


class Database:

    def __init__(self):
        self.connection_params = {
            'dbname': DB_NAME,
            'user': DB_USER,
            'password': DB_PASSWORD,
            'host': DB_HOST,
            'port': DB_PORT
        }

        self.create_schema()

    def connect(self):
        """Connect to Database."""
        try:
            conn = psycopg2.connect(**self.connection_params)
            logger.info("Database connected successfully.")
            return conn
        except psycopg2.OperationalError as e:
            raise Exception(f"Error connecting to Database: {e}")

        except Exception as e:
            raise Exception(
                f"Unexpected error during database connection: {e}")

    def create_schema(self):
        """Create the database schema using SchemaManager."""
        try:

            with self.connect() as conn:
                with conn.cursor() as cursor:
                    schema_manager = SchemaManager(cursor)
                    schema_manager.create_tables()
                    conn.commit()
                    logger.info("Database schema created successfully.")
        except psycopg2.DatabaseError as e:
            raise Exception(f"Error creating schema: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error creating schema: {e}")

    def execute_query(self, query, params=None):
        """Execute a query (INSERT, UPDATE, DELETE)."""
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    conn.commit()
                    logger.info("Query executed successfully.")
        except psycopg2.DatabaseError as e:
            conn.rollback()
            raise Exception(f"Error executing query: {e}")

    def insert(self, query, params=None):
        """Insert a record and optionally return the last inserted row."""
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    conn.commit()
                    inserted_row = cursor.fetchone()
                    colnames = [desc[0] for desc in cursor.description]
                    data = [dict(zip(colnames, inserted_row))]
                    return data
        except psycopg2.IntegrityError as e:
            conn.rollback()
            raise Exception(f"Integrity error during insert: {e}")

        except psycopg2.DatabaseError as e:
            conn.rollback()
            raise Exception(f"Database error during insert: {e}")

    def fetch_all(self, query, params=None):
        """Fetch all results from a SELECT query."""
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    rows = cursor.fetchall()
                    colnames = [desc[0] for desc in cursor.description]
                    data = [dict(zip(colnames, row)) for row in rows]
                    return data
        except psycopg2.DatabaseError as e:
            raise Exception(f"Error fetching all results: {e}")

    def fetch_one(self, query, params=None):
        """Fetch one result from a SELECT query."""
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    row = cursor.fetchone()
                    colnames = [desc[0] for desc in cursor.description]
                    data = [dict(zip(colnames, row))]
                    return data
        except psycopg2.DatabaseError as e:
            raise Exception(f"Error fetching one result: {e}")
