character_characteristic= {
    "Name": None,
    "Health" :15,
    "Damage" :5,
    "Protection":2,
    "Gold":0,
    "Level":0
    }

decor="---------------------------------------------------"

def set_name(character_name):
    character_characteristic["Name"] = character_name

def player_action():
    action=input("Ваш ход:/n1:Удар/n2:Блок/n3:Характеристики противника")
    

character_equipment = {
    "Weapon": None,
    "Armor": None,
    "Accessory": None,
    "Shield": None
}

inventory = []