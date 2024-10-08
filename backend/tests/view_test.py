# # view.py
# import json


# class ApartmentView:
#     @staticmethod
#     def format_apartment(apartment):
#         if apartment:
#             return json.dumps({
#                 "apartment_id": apartment.apartment_id,
#                 "apartment_name": apartment.apartment_name,
#                 "address": apartment.address
#             })
#         return json.dumps({"error": "Apartment not found."})

#     @staticmethod
#     def format_apartments(apartments):
#         return json.dumps([{"apartment_id": apartment.apartment_id, "apartment_name": apartment.apartment_name, "address": apartment.address} for apartment in apartments])
