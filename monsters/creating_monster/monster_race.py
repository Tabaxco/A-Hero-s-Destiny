from random import randint
from monsters.monster import monstro



racas = ['Goblin', 'Ogro', 'Javali']

def escolher_raca_monstro():
    raca_escolhida = racas[randint(0, len(racas))]
    monstro[0]['raca'] = raca_escolhida
    print(monstro)