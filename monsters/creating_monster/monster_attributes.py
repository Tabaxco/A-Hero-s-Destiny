import random
from monsters.monster import monstro
from monsters.creating_monster.hp_mana_monster import hp_mana

monstroatt = monstro[1]

def create_monster_attributes(floor, difficulty: str= "easy"):
    attributes = []
    
    for attribute in range(6):
        if difficulty == 'easy':
            attributes.append(random.randint(1, 12) + (floor + 2))
        elif difficulty == 'medium':
            attributes.append(random.randint(10, 14) + (floor + 2))
        elif difficulty == 'boss':
            attributes.append(random.randint(12, 18) + (floor + 2))


    i = 0
    for dict in monstroatt:
        monstroatt[dict] = attributes[i]
        i += 1

    hp_mana(monstro[2], monstro[1]['constituicao'], monstro[1]['inteligencia'] )
