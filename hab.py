import os
from main import *
player = make_hero(name="Вася", hp_now=100, attack=10, inventory=["Меч", "Щит"])

game = True
while game:
    visit_hub(player)
