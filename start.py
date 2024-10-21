import random
from character import *
from mobs import *
enemy=slime
decor="---------------------------------------------------"

character_name = input("Введи свое имя")
set_name(character_name)
print("Вы открываете дверь в подземелье и спускаетесь по ступенькам в темноту")
print(decor)
print("Первый этаж")
if enemy == slime:
    print(mobs_text["Slime"])