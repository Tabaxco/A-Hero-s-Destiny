from character.creating_character.specs import deciding_specs
from character.creating_character.attributes import deciding_attributes
from character.hero import heroi
from time import sleep

def starting():

    print('Você finalmente acordou... Eu esperei tanto tempo por isso...')
    sleep(3)
    print('Mas você não se lembra... né? De como veio parar aqui...')
    sleep(3)
    print('Bom... Nem eu mesmo lembro direito. Que tal recomeçarmos?')
    sleep(3)
    print()
    
    race = deciding_specs()
    deciding_attributes(race)
    for dict in heroi:
        print(dict)