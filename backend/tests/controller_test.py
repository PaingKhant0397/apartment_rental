# # controller.py
# from model import ApartmentModel,Apartment



# class ApartmentController:
#     def __init__(self):
#         self.model = ApartmentModel()

#     def add_apartment(self, apartment_name, address):
#         apartment_data = self.model.create_apartment(apartment_name, address)
#         return Apartment(apartment_id=apartment_data[0], apartment_name=apartment_data[1], address=apartment_data[2])

#     def list_apartments(self):
#         return [Apartment(apartment_id=row[0], apartment_name=row[1], address=row[2]) for row in self.model.get_all_apartments()]

#     def get_apartment(self, apartment_id):
#         apartment_data = self.model.get_apartment_by_id(apartment_id)
#         if apartment_data:
#             return Apartment(apartment_id=apartment_data[0], apartment_name=apartment_data[1], address=apartment_data[2])
#         return None

#     def delete_apartment(self, apartment_id):
#         self.model.delete_apartment(apartment_id)
