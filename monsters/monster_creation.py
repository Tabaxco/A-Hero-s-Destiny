from monsters.monster import monstro
from monsters.creating_monster.monster_race import choose_monster_race
from monsters.creating_monster.monster_attributes import create_monster_attributes
from monsters.creating_monster.hp_mana_monster import hp_mana

def monster_generator():
    choose_monster_race()
    create_monster_attributes(2)
    hp_mana(monstro[2], monstro[1]['constituicao'], monstro[1]['inteligencia'])