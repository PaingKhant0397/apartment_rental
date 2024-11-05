import psycopg2
from utils import setup_logger
from .schemaManager import SchemaManager

logger = setup_logger(__name__)


class Database:

    def __init__(self, connection_params):
        self.__connection_params = connection_params

        self.initialize_schema()

    def connect(self):
        """Connect to Database."""
        try:
            conn = psycopg2.connect(**self.__connection_params)
            # logger.info("Database connected successfully.")
            return conn
        except psycopg2.OperationalError as e:
            raise Exception(f"Error connecting to Database: {e}")

        except Exception as e:
            raise Exception(
                f"Unexpected error during database connection: {e}")

    def initialize_schema(self):
        """Create the setup database schema using SchemaManager."""
        try:

            with self.connect() as conn:
                with conn.cursor() as cursor:
                    schema_manager = SchemaManager(cursor)
                    schema_manager.create_tables()
                    conn.commit()
                    # logger.info("Database schema created successfully.")
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
                    # logger.info("Query executed successfully.")
        except psycopg2.DatabaseError as e:
            raise Exception(f"Error executing query: {e}")

    def insert(self, query, params=None):
        """Insert a record and optionally return the last inserted row."""
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    conn.commit()
                    row = cursor.fetchone()
                    if row is None:
                        return None
                    colnames = [desc[0] for desc in cursor.description]
                    return dict(zip(colnames, row))

        except psycopg2.IntegrityError as e:
            raise Exception(f"Integrity error during insert: {e}")

        except psycopg2.DatabaseError as e:
            raise Exception(f"Database error during insert: {e}")

    def update(self, query, params=None):

        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    conn.commit()
                    row = cursor.fetchone()
                    if row is None:
                        return None
                    colnames = [desc[0] for desc in cursor.description]
                    return dict(zip(colnames, row))

        except psycopg2.IntegrityError as e:
            raise Exception(f"Integrity error during insert: {e}")

        except psycopg2.DatabaseError as e:
            raise Exception(f"Database error during insert: {e}")

    def fetch_all(self, query, params=None):
        """Fetch all results from a SELECT query."""
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    rows = cursor.fetchall()
                    if rows is None:
                        return None
                    colnames = [desc[0] for desc in cursor.description]
                    return [dict(zip(colnames, row)) for row in rows]

        except psycopg2.DatabaseError as e:
            raise Exception(f"Error fetching all results: {e}")

    def fetch_one(self, query, params=None):
        """Fetch one result from a SELECT query."""
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    row = cursor.fetchone()
                    if row is None:
                        return None
                    colnames = [desc[0] for desc in cursor.description]
                    return dict(zip(colnames, row))

        except psycopg2.DatabaseError as e:
            raise Exception(f"Error fetching one result: {e}")
