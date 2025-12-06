from character.creating_character.specs import deciding_specs
from character.creating_character.attributes import deciding_attributes
from character.hero import heroi

def starting():
    race = deciding_specs()
    deciding_attributes(race)

starting()

for dict in heroi:
    print(dict)