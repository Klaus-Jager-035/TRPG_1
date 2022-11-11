def make_hero(
        name="Безымянный",
        hp=1,
        xp=0,
        attack=1,
        defence=0,
        money=0,
        potions=0,
) -> tuple:
    return(name, hp, xp, attack, defence, money, potions)


player = make_hero()
print(player)

