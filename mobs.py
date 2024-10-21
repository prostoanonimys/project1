Slime = {
    "Health": 10,
    "Damage": 1,
    "Protection": 1
}

lvl1_mobs = [Slime,]

def enemydef(enemy_name):
    if enemy_name == "Slime":
        enemy = Slime
        return enemy

mobs_text = {
    "Slime": "Вы слышите отдаленное похлюпывание. И чувствуете что ваши ноги прилепают к полу",
}
