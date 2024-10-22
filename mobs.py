import random
from character import *


# enemies_types

Slime = {
    "Health": 20,
    "Damage": 2,
    "Protection": 1,
    "Shield":1
}

Bat = {
    "Health": 15,
    "Damage": 3,
    "Protection": 0,
    "Shield":0
}

# /enemies_types


lvl1_mobs = ["Slime","Bat"]


# enemy_radnomization

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

# /enemy_radnomization



# enemy_text

def enemytext(enemy_name):
    print(mobs_text[enemy_name])

mobs_text = {
    "Slime": "Вы слышите отдаленное похлюпывание. И чувствуете что ваши ноги прилепают к полу",
    "Bat": "Вы слышите хлопанье крыльев и писк"
}

# /enemy_text
