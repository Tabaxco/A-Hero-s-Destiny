from hero import heroi
from random import randint
from time import sleep
respostas = []

def atributorandom(respostas):
   for atributos in range(6):
      respostas.append(randint(8, 15))

def usuarioroubando(respostas):
    respostas.clear()
    respostas [:] = []
    atributorandom(respostas)

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



def create_hero():
    #Personagem
    specs = heroi[1]

    nome = input('Eu não me lembro direito... Qual é o seu nome? ')
    print(f'Ah... Estou começando a me lembrar, {nome}!')
    print("")
    sleep(2)

    idade = int(input('Quantos anos você têm mesmo? '))
    if idade < 15:
        print('Tão jovem... E já se perdeu nesse mundo...')
    elif idade >= 18:
        print("Você já conheceu os horrores desse mundo, não tem mais nada a perder.")
    elif idade >= 40:
        print("Velho...")
        print("") 
    sleep(2)

    print('De qual raça você era mesmo?')
    print("""
1 - Humano (+1 em todos os atributos)
2 - Vampiro (+2 Destreza, +1 Inteligência)
3 - Elfo (+2 Sabedoria, +1 Carisma)
          """)
    raca = int(input('')) 

    specs['nome'] = nome
    specs['idade'] = idade
    specs['raca'] = raca
    

    # Atributos
    attributes = heroi[0]
    for dict in attributes:
            print(f'Quanto pontos deseja inserir em {dict}?')

            try:
                escolha = int(input('Resposta: '))
                respostas.append(escolha)

            except Exception:
                print("Digite apenas os valores que foram falados!")   

    if sum(respostas) != 72:
        usuarioroubando(respostas)
    if len(respostas) != 6:
        atributorandom(respostas)

    i = 0
    for dict in attributes:
       attributes[dict] = respostas[i]
       i += 1

    print(attributes)
    modifierrace(attributes, raca)
    print(attributes)


create_hero()