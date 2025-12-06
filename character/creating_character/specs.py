from character.hero import heroi
from time import sleep
from character.creating_character.races import modifierrace

specs = heroi[0]

def deciding_specs():

    #Decidir o nome
    nome = input('Eu não me lembro direito... Qual é o seu nome? ')
    print(f'Ah... Estou começando a me lembrar, {nome}!')
    print("")
    sleep(2)

    #Decidir a idade
    idade = int(input('Quantos anos você têm mesmo? '))
    if idade >= 50:
        print('Você já está velho para recomeçar... Porém nunca é tarde demais!')
    elif idade >= 18:
        print("Você já conheceu os horrores desse mundo, não tem mais nada a perder.")
    else:
        print('Tão jovem... E já se perdeu nesse mundo...')
    print("") 
    sleep(2)

    #Decidir a raça
    print('De qual raça você era mesmo?')
    sleep(2)
    print("""
1 - Humano (+1 em todos os atributos)
2 - Vampiro (+2 Destreza, +1 Inteligência)
3 - Elfo (+2 Sabedoria, +1 Carisma)
          """)
    raca = int(input('')) 

    racasdisponiveis = ['Humano', 'Vampiro', 'Elfo']


    specs['nome'] = nome
    specs['idade'] = idade
    specs['raca'] = racasdisponiveis[raca-1]

    return raca

    print()
