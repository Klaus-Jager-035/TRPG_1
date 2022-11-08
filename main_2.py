import os
import game # импортируем файл game.py

def show_menu():
    """
    Печатает на экране главное меню
    Умеет запускать новую игру
    Умеет выходить из программы
    TODO:
    Выборы:
        начать новую игру
        настройки
        загрузка старой игры
        выход
    """

    while True:

        os.system("cls")
        print("1 - начать новую игру")
        print("0 - выйти из игры")

        answer = int(input("Введите номер ответа и нажмите ENTER:  "))

        if answer == 1:
            game.start_new_game()
        elif answer == 0:
            print("Выходим из игры")

            break

show_menu()