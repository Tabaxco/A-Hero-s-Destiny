from random import randint
from monsters.monster import monstro

racas = ['Goblin', 'Ogro', 'Javali', 'Esqueleto']

def choose_monster_race():
    raca_escolhida = racas[randint(0, len(racas))]
    monstro[0]['raca'] = raca_escolhida