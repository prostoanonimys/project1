from mobs import *
from character import *

procentage = 5
enemy_protection = 0
player_protection = 0


def defense_damage(damage,defense):
    defense_procent = defense*procentage
    clear_damage = int(damage*(1-defense_procent/100))
    return clear_damage


# enemyaction

def enemy_protection_cleanse():
    enemy["Protection"] = enemy["Protection"]-enemy_protection*(1+enemy["Shield"])

def attack_enemy():
    result = defense_damage(enemy["Damage"],character_characteristic["Protection"])
    return result

def enemyaction():
    global enemy_protection
    emaction = random.randint(1,2)
    if emaction == 1:
        print(decor)
        print("Враг атакует!")
        character_characteristic["Health"]-=attack_enemy()
        print(f"Вы получили: {attack_enemy()} урона")
        print(f"Ваше здоровье: {character_characteristic["Health"]}")
        print(decor)
    if emaction ==2:
        print(decor)
        print("Враг защищается!")
        enemy["Protection"]+=enemy["Shield"]
        print(f"{enemy["Protection"]}")
        print(decor)
        enemy_protection+=1

# /enemyaction




# playeraction

def player_protection_cleanse():
    character_characteristic["Protection"] = character_characteristic["Protection"]-player_protection*(1+character_characteristic["Shield"])

def attack_player():
    result = defense_damage(character_characteristic["Damage"],enemy["Protection"])
    return result

def player_action(enemy):
    global player_protection
    for i in range(2):
        while True:
            action=input("Ваш ход:\n1:Удар\n2:Блок\n3:Характеристики противника\n4:Ваши характеристики")
            if action == "1":
                print(decor)
                enemy["Health"] -= attack_player()
                print(f"\nВы нанесли:{attack_player()}урона \nЗдоровье врага:{enemy["Health"]}")
                print(decor)
                break
            elif action == "2":
                player_protection+=1
                print(decor)
                print(f"\nВы ставите блок\nВаша защита повышена {player_protection*character_characteristic["Shield"]} ед.")
                character_characteristic["Protection"]+=1+enemy["Shield"]
                print(character_characteristic)
                print(decor)
                break
            elif action == "3":
                print(decor)
                print(f"Здоровье:{enemy["Health"]}\n Защита:{enemy["Protection"]}\n Урон:{enemy["Damage"]}")
                print(decor)
            elif action == "4":
                print(decor)
                print(f"Здоровье:{character_characteristic["Health"]}\n Защита:{character_characteristic["Protection"]}\n Урон:{character_characteristic["Damage"]}")
                print(decor)
            else:
                print("Вы ввели неправильное действие")

#/playeraction


def fight(enemy):
    while enemy["Health"] > 0 and character_characteristic["Health"] > 0:
        player_action(enemy)
        enemy_protection_cleanse()
        if enemy["Health"] <= 0:
            print("Вы победили врага!")
            character_characteristic["Experience"]+=enemy["Experience"]
            print(character_characteristic["Experience"])
            break
        enemyaction()
        player_protection_cleanse()
        print(enemy["Protection"])
        if character_characteristic["Health"] <= 0:
            print("Вы проиграли.")
            break

