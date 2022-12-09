from random import randint, choice
import os

first_names = ("Жран", "Дрын", "Брысь", "Жлыг")
last_names = ("Ужасный", "Зловонный", "Борзый", "Кровавый")


def make_hero(
        name=None,
        hp_now=None,
        hp_max=None,
        lvl=1,
        xp_now=0,
        attack=1,
        defence=1,
        luck=1,
        money=None,
        inventory=None,
) -> list:
    """
    Персонаж - это список
    [0] name - имя
    [1] hp_now - здоровье текущее
    [2] hp_max - здоровье максимальное
    [3] lvl - уровень
    [4] xp_now - опыт текущий
    [5] xp_next - опыт до следующего уровня
    [6] attack - сила атаки, применяется в бою
    [7] defence - защита, применяется в бою
    [8] luck - удача
    [9] money - деньги
    [10] inventory - список предметов
    """
    if not name:
        name = choice(first_names) + " " + choice(last_names)
        if not hp_now:
            hp_now = randint(1, 100)

    if not hp_max:
        hp_max = hp_now

    xp_next = lvl * 100

    if money is None:
        money = randint(0, 100)

    if not inventory:
        inventory = []


    return [
        name,
        hp_now,
        hp_max,
        lvl,
        xp_now,
        xp_next,
        attack,
        defence,
        luck,
        money,
        inventory
    ]


def show_hero(hero:list) -> None:
    print("имя:", hero[0])
    print("здоровье:", hero[1], "/", hero[2])
    print("уровень:", hero[3])
    print("опыт:", hero[4], "/", hero[5])
    print("атака:", hero[6])
    print("защита:", hero[7])
    print("удача:", hero[8])
    print("деньги:", hero[9])
    print("инвентарь:", hero[10])
    print("")


def levelup(hero: list) -> None:
    while hero[4] >= hero[5]:
        hero[3] += 1
        hero[5] = hero[3] * 100
        print(f"\n{hero[0]} получил {hero[3]} уровень\n")


def buy_item(hero: list, item: str, price: int) -> None:
    if hero[9] >= price:
        hero[9] -= price
        hero[10].append(item)
        print(f"{hero[0]} купил {item} за {price} монет")
    else:
        print(f"У {hero[0]} не хватило {price - hero[9]} монет")


def consume_item(hero: list, idx: int) -> None:    # что растет с уровнем
    """
     Разные эфекты от зелий
    """
    if idx <= len(hero[10]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[10][idx]}")
        if hero[10][idx] == "зелье":
            hero[1] += 10
            if hero[1] > hero[2]:
                hero[1] = hero[2]
        elif hero[10][idx] == "яблоко":
            pass
        else:
            print("Герой умер")
            hero[1] = 0
        hero[10].pop(idx)


def play_dice(hero: list, bet: int) -> None:
    if bet > 0:
        if bet <= hero[9]:
            hero_score = randint(2, 12)
            casino_score = randint(2, 12)
            print(f"{hero[0]} выбросил {hero_score}")
            print(f"Трактирщик выбросил {casino_score}")
            if hero_score > casino_score:
                hero[9] += bet
                print(f"{hero[0]} выиграл {bet} монет")
            elif hero_score < casino_score:
                hero[9] -= bet
                print(f"{hero[0]} проиграл {bet} монет")
            else:
                print("Ничья")
        else:
            print(f"у {hero[0]} нет столько монет")
    else:
        print("Ставки начинаются с одной монеты")


def combat_turn(attacker, defender):
    """
     использовать защиту
    """
    if attacker[1] > 0:
        damage = attacker[6]
        defender[1] -= damage
        print(f"{attacker[0]} ударил {defender[0]} на {damage} урона")



def start_fight(hero: list) -> None:
    """
    TO DO:
    Нужен противник
    Обмен ударами пока живы
    Итог боя: проигрыш или победа
    Победа: прибавка опыта, забрать предметы врага в инвентарь
    Проигрыш: закончить игру
    """

    enemy = make_hero(hp_now=30, xp_now=1000, money=25, inventory=["меч гладиатора", "шапка Мономаха"])
    while hero[1] > 0 and enemy [1] > 0:
        os.system("cls")
        combat_turn(hero, enemy)
        combat_turn(enemy, hero)
        print("")
        show_hero(hero)
        show_hero(enemy)
        input("\nНажмите ENTER, чтобы продолжить")
    get_award(hero, enemy)


def get_award(hero, enemy) -> None:
    if hero[1] > 0 and enemy[1] <= 0:
        os.system("cls")
        print(f"{hero[0]} победил")
        hero[4] += enemy[4]
        print(f"{hero[0]} получил {enemy[4]} опыта и теперь у {hero[0]} {hero[4]} опыта")

        hero[9] += enemy[9]
        print(f"{hero[0]} получил {enemy[9]} монет и теперь у {hero[0]} {hero[9]} монет")

        hero[10] += enemy[10]
        print(f"{hero[0]} получил {enemy[10]} врага и теперь у него: {hero[10]}")

        levelup(hero)

    elif hero[1] < 0 and enemy[1] >= 0:
        print(f"{enemy[0]} победил")


def choose_options(hero: list, text: str, options: list) -> int:
    """
    Описание ситуации, где происходит выбор
    Принимает список возможных вариантов
    Спросить пользователя
    Проверяет, есть ли вариант пользователя в возможных вариантах, если есть, тогда возвращает вариант пользователя
    """
    os.system("cls")
    show_hero(hero)
    print(text)
    for num, option in enumerate (options):
        print(f"{num}. {option}")
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try: # что пробуем сделать?
        option = int(option)
    except: # сработает, если try вызвал ошибку
        print("Ошибка, введите целое неотрицательное число")
    else: # если трай без ошибки
        if option < len(options) and option > -1:
            return option
        else:
            print("Такой выбор невозможен")


def visit_hub(hero: list) -> None:
    text = "Герой приехал к камню, отсюда идут несколько дорог: "

    options = [
        "Купить зелье",
        "Употребить первый предмет в инвентаре",
        "Драться с разбойником",
        "Сыграть в кости",
        "Сходить на арену"
    ]

    option = choose_options(hero, text, options)
    os.system("cls")
    if option == 0:
        buy_item(hero, item="зелье", price=10)
    elif option == 1:
        consume_item(hero, 0)
    elif option == 2:
        start_fight(hero)
    elif option == 3:
        play_dice(hero, 10)
    elif option == 4:
        visit_arena(hero)
    else:
        print("Такой выбор пока не сделан")
    input("Нажмите ENTER, чтобы продолжить")



def visit_shop(hero):
    """
    TODO:
    Текст
    Товары с ценами
    Покупка и эффекты в функции консьюм
    """

    pass


def visit_arena(hero: list) -> None:
    text = ""
    options = [
        "Сражаться",
        "Выйти в Хаб",
        "Получить ввод пользователя"
    ]
    if "зелье " in hero[10]:
        options.append("Выпить зелье")
    option = choose_options(hero, text, options)
    if option == 0:
        start_fight(hero)
    elif option == 1:
        return visit_hub(hero)
    elif option == 2:
        idx = choose_options(hero, "Введите номер предмета и нажмите ENTER", hero[10])
        if idx is not None:
            consume_item(hero, idx)
        visit_arena(hero)
        
