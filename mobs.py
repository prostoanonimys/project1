import random
from character import *
Slime = {
    "Health": 15,
    "Damage": 1,
    "Protection": 1,
    "Shiel":1
}

lvl1_mobs = [Slime,]


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
