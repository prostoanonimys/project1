import random
from character import *
from mobs import *

enemy_name="Slime"
enemy = enemydef(enemy_name)
enemyaction()
# set_name()

# print("Вы открываете дверь в подземелье и спускаетесь по ступенькам в темноту")
# print(decor)
# print("Первый этаж")

# enemytext(enemy_name)

player_action(enemy)
print(enemy)