from random import randint, choice

first_names = ("Жран", "Дрын", "Брысь", "Жлыг")
last_names = ("Ужасный", "Зловонный", "Борзый", "Кровавый")


def make_hero(
        name = None,
        hp_now=None,
        hp_max=1,
        lvl=1,
        xp_now=0,
        xp_next=100,
        attack=1,
        defence=0,
        luck=1,
        money=None,
        inventory=None,
) -> list:
    """
    Персонаж это список
    [0] name - имя
    [1] hp_now - здоровье текущее
    [2] hp_max - здоровье максимальное
    [3] lvl - уровень
    [4] xp_now - текущий опыт
    [5] xp_next - опыт до след уровня
    [6] attack - сила атаки
    [7] defence - защита
    [8] luck - удача
    [9] money - деньги
    [10] inventory - список предметов
    """


    if not name:
        name = choice(first_names) + " " + choice(last_names)

    if not hp_now:
        hp_now = randint(1, 100)
        hp_max = hp_now

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


def show_hero(hero):
    print("имя: ", hero[0])
    print("здоровье: ", hero[1], "/", hero[2])
    print("уровень: ", hero[3])
    print("опыт: ", hero[4], "/", hero[5])
    print("сила атаки: ", hero[6])
    print("защита: ", hero[7])
    print("удача: ", hero[8])
    print("деньги: ", hero[9])
    print("список предметов: ", hero[10])
    print("+++++++++++++++++++++++++++++++++++++++")


def levelup(hero: list) -> None:
    """
    [3] lvl - уровень
    [4] xp_now - текущий опыт
    [5] xp_next - опыт до след уровня
    TODO: не прекращать повышать уровень, пока не закончится опыт
    """
    if hero[4] >= hero[5]:
        hero[3] += 1
        hero[5] = hero[3] * 100
        print(f"{hero[0]} получил {hero[3]} уровень\n")


def buy_item(hero: list, price: int):
    """
    [9] money - деньги
    [10] inventory - список предметов
    """
    if hero[9] >= price:
        hero[9] -= price
        hero[10].append("зелье")
        print(f"{hero[0]} купил зелье за {price} монет")
    else:
        print(f"у {hero[0]} недостаточно монет")


def consume_item(hero: list, item: str) -> None:


    """
    Найти предмет в инвентаре героя
    Этот предмет удаляется из инвентаря
    Герой получает эффект от этого предмета
    """






p1 = make_hero(money=100)

p1[4] += 100
levelup(p1)

show_hero(p1)


buy_item(p1, 10)
show_hero(p1)
