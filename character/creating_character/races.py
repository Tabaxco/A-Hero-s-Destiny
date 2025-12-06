def modifierrace(hero, race):
    if race == 1:
        for k in hero:
            hero[k] += 1
    elif race == 2:
        hero["destreza"] += 2
        hero["inteligencia"] += 1
    elif race == 3:
        hero['sabedoria'] += 2
        hero['carisma'] += 1