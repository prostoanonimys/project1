import random
from character import *
Slime = {
    "Health": 20,
    "Damage": 2,
    "Protection": 1,
    "Shield":1
}

lvl1_mobs = ["Slime","Bat"]

Bat = {
    "Health": 15,
    "Damage": 3,
    "Protection": 0,
    "Shield":0
}

def random_mobe():
    global choise
    return random.randint(0, len(lvl1_mobs)-1)

choise = random_mobe()

enemy_name= lvl1_mobs[choise]
def enemydef():
    if lvl1_mobs[choise] == "Slime":
        return Slime
    elif lvl1_mobs[choise] == "Bat":
        return Bat



enemy = enemydef()

def enemytext(enemy_name):
    print(mobs_text[enemy_name])

mobs_text = {
    "Slime": "Вы слышите отдаленное похлюпывание. И чувствуете что ваши ноги прилепают к полу",
    "Bat": "Вы слышите хлопанье крыльев и писк"
}
