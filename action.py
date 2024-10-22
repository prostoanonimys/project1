from mobs import *
from character import *


def enemyaction():
    emaction = random.randint(1,2)
    if emaction == 1:
        print(decor)
        print("Враг атакует!")
        character_characteristic["Health"]-=enemy["Damage"]
        print(f"Вы получили: {enemy["Damage"]} урона")
        print(f"Ваше здоровье: {character_characteristic["Health"]}")
        print(decor)
    if emaction ==2:
        print(decor)
        print("Враг защищается!")
        enemy["Protection"]+=["Shield"]
        print(f"{enemy["Protection"]}")
        print(decor)

procentage = 5

def defense_damage(damage,defense):
    defense_procent = defense*procentage
    clear_damage = int(damage*(1-defense_procent/100))
    return clear_damage

def player_action(enemy):
    action_protection = 0
    for i in range(2):
        while True:
            action=input("Ваш ход:\n1:Удар\n2:Блок\n3:Характеристики противника")
            if action == "1":
                print(decor)
                enemy["Health"] -= character_characteristic["Damage"]
                print(f"\nВы нанесли:{character_characteristic["Damage"]}урона \nЗдоровье врага:{enemy["Health"]}")
                print(decor)
                break
            elif action == "2":
                action_protection+=1
                print(decor)
                print(f"\nВы ставите блок\nВаша защита повышена {action_protection*character_characteristic["Shield"]} ед.")
                character_characteristic["Protection"]+=1
                print(character_characteristic)
                print(decor)
                break
            elif action == "3":
                print(decor)
                print(f"Здоровье:{enemy["Health"]}\n Защита:{enemy["Protection"]}\n Урон:{enemy["Damage"]}")
                print(decor)
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

