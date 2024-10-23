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