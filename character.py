character_characteristic= {
    "Name": None,
    "Health" :15,
    "Damage" :5,
    "Protection":2,
    "Gold":0,
    "Level":0,
    "Shield":1
    }

decor="---------------------------------------------------"

def set_name():
    character_name = input("Введи свое имя")
    character_characteristic["Name"] = character_name

def player_action(enemy):
    action_protection = 0
    for i in range(2):
        while True:
            action=input("Ваш ход:\n1:Удар\n2:Блок\n3:Характеристики противника")
            if action == "1":
                enemy["Health"] -=2
                print(f"\nВы нанесли:{character_characteristic["Damage"]}урона \nЗдоровье врага:{enemy["Health"]}\n")
                break
            elif action == "2":
                action_protection+=1
                print(f"\nВы ставите блок\nВаша защита повышена {action_protection*character_characteristic["Shield"]} ед.")
                character_characteristic["Protection"]+=1
                print(character_characteristic)
                break
            elif action == "3":
                print(f"Здоровье:{enemy["Health"]}\n Защита:{enemy["Protection"]}\n Урон:{enemy["Damage"]}")
            else:
                print("Вы ввели неправильное действие")
                    

character_equipment = {
    "Weapon": None,
    "Armor": None,
    "Accessory": None,
    "Shield": None
}

inventory = []