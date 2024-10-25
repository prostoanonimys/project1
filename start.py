import random
from character import *
from mobs import *
from action import *
from save import *

# # set_name()
# print("Вы открываете дверь в подземелье и спускаетесь по ступенькам в темноту")
# print(decor)
print(character_characteristic)
print("Первый этаж")
enemytext(enemy_name)
print(f"Ваш враг:{enemy_name}")
print(character_characteristic)
fight(enemy)
print(character_characteristic)
save_character(character_characteristic)