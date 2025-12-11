from character.hero import heroi
from monsters.monster import monstro
from rpg_functions.roll import rolar

persoatt = heroi[1].copy()
persohpmana= heroi[2].copy()

monsteratt = monstro[1].copy
monsterhpmana = monstro[2].copy


def levardano(persohpmana, dano, resistencia = 0):
    hpatual = persohpmana['hp'] - (dano - resistencia)
    return hpatual

def atacar(dano, hpmonstro):
    monstrohpatual = monstro[2]['hp']
    monstro[2]['hp'] =  ( monstrohpatual - dano)
    monstrohpatual = monstro[2]['hp']
    return monstrohpatual

def desvio(destreza):
    rolar(bonus=destreza)
    