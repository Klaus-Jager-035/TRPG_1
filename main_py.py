from random import randint, choice

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
    print("инвентарь:", hero[10])  # TODO: показать предметы и их количество
    print("")


def levelup(hero: list) -> None:
    """
    TODO: что растет с уровнем?
    TODO: не прекращать повышать уровень, пока текущий опыт больше нужного для повышения
    """
    if hero[4] >= hero[5]:
        hero[3] += 1
        hero[5] = hero[3] + 100
        print(f"{hero[0]} получил {hero[3]} уровень\n")


def buy_item(hero: list, price: int) -> None:
    """
    Покупает предмет за price монет и кладет его в инвентарь героя
    """
    if hero[9] >= price:
        hero[9] -= price
        hero[10].append("зелье")
        print(f"{hero[0]} купил зелье за {price} монет!")
    else:
        print(f"У {hero[0]} нет столько монет!")


def consume_item(hero: list, idx: int) -> None:
    if idx <= len(hero[10]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[10][idx]}")
        if hero[10][idx] == "хлеб":
            hero[2] += 10
            if hero[2] > hero[1]:
                hero[2] = hero[1]
        elif hero[10][idx] == "бублик":
            hero[2] += 2
        else:
            print(f"{hero[1]} употребил что-то неизвестное")
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
                print(f"{hero[0]} выиграл и получает {bet} монет")
            elif hero_score < casino_score:
                hero[9] -= bet
                print(f"{hero[0]} проиграл {bet} монет")
            else:
                print("Ничья")
                
            
        else:
            print(f"У {hero[0]} нет столько монет")
    else:
        print("Такая ставка невозможна! Ставки начинаются от 1 монеты")


def fight(hero: list) -> None:
    """
    Нужен противник
    Обмениватсья ударами, пока живы
    Итог боя: проигрыш или победа
    Победа: добавить опыт от врага, забрать вещи врага в инвентарь, пнуть врага
    Проигрыш: закончить игру
    """
    pass















        
        
