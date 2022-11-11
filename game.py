import os
import shop
import hero_engine


def start_game():
    os.system("cls")
    print("Игра началась")

    # создаем игрока - КОРТЕЖ
    # [0] имя, [1] здоровье, [2] деньги, [3] зелья
    player = hero_engine.make_hero()



    # начался главный цикл игры
    while True:
        os.system("cls")




        # показываем варианты
        print("1 - Поехать в лавку алхимика")
        print("0 - Выйти в главное меню")

        # выбираем вариант и проверяем его
        answer = input("\nВведите номер варианта и нажмите ENTER: ")
        if answer == "1":
            player = shop.show(player)

start_game()