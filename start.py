import random
from character import *
from mobs import *

enemy_name="Slime"
enemy = enemydef(enemy_name)
print(enemy)

#character_name = input("Введи свое имя")
#set_name(character_name)
#print("Вы открываете дверь в подземелье и спускаетесь по ступенькам в темноту")
#print(decor)
#print("Первый этаж")

if enemy_name == Slime:
    print(mobs_text["Slime"])