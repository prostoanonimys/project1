from mobs import *
from character import *
from mobs import *

def enemyaction():
    emaction = random.randint(1,2)
    if emaction == 1:
        print("Враг атакует!")
        character_characteristic["Health"]-=Slime["Damage"]
        print(f"Вы получили: {Slime["Damage"]} урона")
        print(f"Ваше здоровье: {character_characteristic["Health"]}")
    if emaction ==2:
        print("Враг защищается!")
        Slime["Protection"]+=Slime["Shield"]
        print(f"{Slime["Protection"]}")

def player_action(enemy):
    action_protection = 0
    for i in range(2):
        while True:
            action=input("Ваш ход:\n1:Удар\n2:Блок\n3:Характеристики противника")
            if action == "1":
                enemy["Health"] -= character_characteristic["Damage"]
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

def fight(enemy):
    while enemy["Health"] > 0 and character_characteristic["Health"] > 0:
        player_action(enemy)
        if enemy["Health"] <= 0:
            print("Вы победили врага!")
            break
        enemyaction()
        if character_characteristic["Health"] <= 0:
            print("Вы проиграли.")
            break

