import os
import hero_engine


def show(player):
    name = player[0]
    money = player[5]
    potions = player[6]

    while True:

        # очищаем экран и показываем текст лавки
        os.system("cls")
        print(f"{name} приехал в лавку алхимика")

        # показываем персонажа
        print("имя:", name)
        print("деньги:", money)
        print("зелья:", potions)

        # показываем варианты в лавке
        print("1 - купить зелье за 10 монет")
        print("2 - уехать обратно к камню")
        answer = input("\nВведите номер варианта и нажмите ENTER: ")
        if answer == "1":
            os.system("cls")
            if money >= 10:
                money -= 10
                potions += 1
                print("Купили зелье")
            else:
                print("Недостаточно монет!")
            input("\nНажмите ENTER чтобы продолжить")
        elif answer == "2":
            return (player[0], player[1], player[2], player[3], player[4], player[5], player[6])