# # model.py
# from database import Database



# class Apartment:
#     def __init__(self, apartment_id, apartment_name, address):
#         self.apartment_id = apartment_id
#         self.apartment_name = apartment_name
#         self.address = address


# class ApartmentModel:
#     def __init__(self):
#         self.db = Database()
#         self.db.create_tables()

#     def create_apartment(self, apartment_name, address):
#         self.db.execute_query("INSERT INTO apartments (apartment_name, address) VALUES (%s, %s);", (apartment_name, address))
#         return self.db.fetch_one("SELECT * FROM apartments ORDER BY apartment_id DESC LIMIT 1;")

#     def get_all_apartments(self):
#         return self.db.fetch_all("SELECT * FROM apartments;")

#     def get_apartment_by_id(self, apartment_id):
#         return self.db.fetch_one("SELECT * FROM apartments WHERE apartment_id = %s;", (apartment_id,))

#     def delete_apartment(self, apartment_id):
#         self.db.execute_query("DELETE FROM apartments WHERE apartment_id = %s;", (apartment_id,))
