# # import json
# # import os
# # from character import *
# # from action import *
# # from mobs import *

# character_data = "character_data.json"

# script_dir = os.path.dirname(os.path.abspath(__file__))
# character_data = os.path.join(script_dir, "character_data.json")

# def load_character(default_characteristic):
#     if os.path.exists(character_data):
#         with open(character_data, "r") as file:
#             character_characteristic = json.load(file)
#             print("Данные загружены.")
#             return character_characteristic
#     else:
#         print("Файл сохранения не найден. Используются базовые характеристики.")
#         return character_characteristic

# def save_character(character):
#     with open(character_data, "w") as file:
#         json.dump(character, file)
#         print("Данные сохранены.")