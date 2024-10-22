import random
from character import *
Slime = {
    "Health": 10,
    "Damage": 1,
    "Protection": 1,
    "Shiel":1
}

lvl1_mobs = [Slime,]

def enemyaction():
    emaction = random.randint(1,2)
    if emaction == 1:
        print("Враг атакует!")
        character_characteristic["Health"]-=Slime["Damage"]
        print(f"Вы получили: {Slime["Damage"]} урона")
        print(f"Ваше здоровье: {character_characteristic["Health"]}")
    if emaction ==2:
        print("Враг защищается!")
        Slime["Protection"]+=Slime["Shiel"]
        print(f"{Slime["Protection"]}")

def enemydef(enemy_name):
    if enemy_name == "Slime":
        enemy = Slime
        return enemy

def enemytext(enemy_name):
    if enemy_name == "Slime":
        print(mobs_text["Slime"])

mobs_text = {
    "Slime": "Вы слышите отдаленное похлюпывание. И чувствуете что ваши ноги прилепают к полу",
}
