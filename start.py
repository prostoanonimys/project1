import random
from character import *
from mobs import *
from action import *
from save import *

# # set_name()
# print("Вы открываете дверь в подземелье и спускаетесь по ступенькам в темноту")
# print(decor)

character_characteristic = load_character()
print(character_characteristic)
print("Первый этаж")
enemytext(enemy_name)
print(f"Ваш враг:{enemy_name}")
fight(enemy)

save_character(character_characteristic)