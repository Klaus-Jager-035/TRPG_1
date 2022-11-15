from random import randint, choice

first_names = ("Жран", "Дрын", "Брысь", "Жлыг")
last_names = ("Ужасный", "Зловонный", "Борзый", "Кровавый")

def make_hero(
        name = None,
        hp_now=None,
        hp_max=1,
        lvl=1,
        xp_now=1,
        xp_next=1000,
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
    print("name", hero[0])

p1 = make_hero()
p2 = make_hero()
p3 = make_hero(name="Vasya", money=0)

p2[10] = "semki"

show_hero(p1)
