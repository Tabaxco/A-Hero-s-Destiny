from character.character_creation import starting
from utils.cleanshell import cleanse
from character.hero import heroi
from time import sleep
from monsters.monster_creation import monster_generator
from rpg_functions import combat
from monsters.monster import monstro

monster_generator()
print(monstro[2]['hp'])
print(combat.atacar(12, monstro[2]['hp']))
print(combat.atacar(12, monstro[2]['hp']))
print(combat.atacar(12, monstro[2]['hp']))