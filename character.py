import json
import os

character_data = "character_data.json"

script_dir = os.path.dirname(os.path.abspath(__file__))
character_data = os.path.join(script_dir, "character_data.json")

def load_character(default_characteristic):
    if os.path.exists(character_data):
        with open(character_data, "r") as file:
            character_characteristic = json.load(file)
            print("Данные загружены.")
            return character_characteristic
    else:
        print("Файл сохранения не найден. Используются базовые характеристики.")
        return character_characteristic

def save_character(character):
    with open(character_data, "w") as file:
        json.dump(character, file)
        print("Данные сохранены.")


load_character()
character_characteristic= {
    "Name": None,
    "Health" :15,
    "Damage" :5,
    "Protection":2,
    "Gold":0,
    "Level":0,
    "Shield":1,
    "Experience":0
    }

decor=str("\n---------------------------------------------------\n")

def set_name():
    character_name = input("Введи свое имя")
    character_characteristic["Name"] = character_name

character_equipment = {
    "Weapon": None,
    "Armor": None,
    "Accessory": None,
    "Shield": None
}

inventory = []