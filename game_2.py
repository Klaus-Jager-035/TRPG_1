import os
import shop



def start_new_game():
    """
    Создает персонажа:
        имя
        здоровье
        деньги
        зелья
    """


    hp = 100
    money = 10
    potions = 0

    # создаем персонажа
    player_name = input("Введите имя игрока и нажмите ENTER:  ")
    if not player_name:
        player_name = "Безымянный"

    player = (player_name, 100, 10, 0)

    # запусскаем главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        print(f"имя: {player[0]}")
        print(f"здоровье: {player[1]}")
        print(f"деньги: {player[2]}")
        print(f"зелья: {player[3]}")


        print("Ситуация:")
        print(f"{player_name} приехал к камню")

        print("1 - Поехать на битву")
        print("2 - поехать в казино")
        print("3 - поехать в лавку алхимика")
        print("0 - выйти в главное меню")

        answer = input("нажмите ENTER для продолжения: ")
        if answer == "1":
            pass
        elif answer == "2":
            pass
        elif answer == "3":
            player = shop.visit_shop(player)
        elif answer == "0":
            is_game = False