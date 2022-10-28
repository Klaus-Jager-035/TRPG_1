import os
import med_shop

def show_menu():
    """
    Данная функция показывает главное меню
    В ней начинается игра или завершается программа
    Нужно сделать настройку цвета текста и сохранения с загрузками!
    """
    while True:
        os.system('cls')
        print("1 - начать")
        print("2 - выйти")
        answer = input("Введите номер ответа и нажмите Enter: ")
        if answer == "1":
            start_game()
            break
        elif answer == "2":
            print("Выход из игры")
            break
    print("Выход из меню")


def start_game():
    """
    Эта функция создает персонажа и запускает игру
    p_name -  имя персонажа
    p_money - деньги персонажа
    p_pp - адекватность персонажа
    p_hp - сопротивляемость к уроку игрока
    med_pill - таблетки
    
    """

    p_name = input("Введите имя  игрока и нажмите Enter: ")
    if not p_name: p_name = "Вано"
    p_money = 500
    p_pp = 100
    p_hp = 100

    
    #главный цикл игры
    is_game = True
    while is_game:
        os.system('cls')
        print(f"имя: {p_name}")
        print(f"жизни: {p_hp}")
        print(f"адекватость персонажа: {p_pp}")
        print(f"деньги: {p_money}")
        
        print(f"{p_name} подъехал")
        print("1 - Поехать к аптекарю")
        print("2 - Поехать разбираться с врагами")
        print("3 - Поехать далековато (погулять)")
        
        choise = input(f"Нужно выбрать место, куда поедет {p_name}: ")
        if choise == "1":
            med_shop.med_shop(p_name, p_money, p_pp, p_hp)
        elif choise == "2":
            print("Поехал разбираться с врагами ")
        elif choise == "3":
            print("Поехал далековато (погулять)")
        

show_menu()
