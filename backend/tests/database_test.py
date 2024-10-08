# import psycopg2
# from psycopg2 import OperationalError

# class Database:
#     def __init__(self):
#         try:
#             self.connection = psycopg2.connect(
#                 dbname='apartmentRentalDb',
#                 user='postgres',
#                 password='postgres',
#                 host='localhost',
#                 port='5432'
#             )
#             self.cursor = self.connection.cursor()
#             print("Database connected successfully.")
#         except OperationalError as e:
#             print(f"Error connecting to database: {e}")
#             self.connection = None
#             self.cursor = None

#     def is_connected(self):
#         """Check if the database connection is active."""
#         try:
#             if self.connection:
#                 # Execute a simple query to test the connection
#                 self.cursor.execute("SELECT 1;")
#                 return True
#             return False
#         except Exception as e:
#             print(f"Database connection check failed: {e}")
#             return False

#     def create_tables(self):
#         self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS apartments (
#             apartmentId SERIAL PRIMARY KEY,
#             apartmentName VARCHAR(100) NOT NULL,
#             address VARCHAR(255) NOT NULL
#         );
#         """)
#         self.connection.commit()

#     def close(self):
#         if self.cursor:
#             self.cursor.close()
#         if self.connection:
#             self.connection.close()

#     def execute_query(self, query, params=None):
#         self.cursor.execute(query, params)
#         self.connection.commit()

#     def fetch_all(self, query, params=None):
#         self.cursor.execute(query, params)
#         return self.cursor.fetchall()

#     def fetch_one(self, query, params=None):
#         self.cursor.execute(query, params)
#         return self.cursor.fetchone()
