from random import randint

nomes = []
nome_escolhido = None

nomeogros = ['Invictus', 'Adamant', 'Sorark', 'Bork']
nomesgoblins = ['Jonas', 'Geraldo', 'Shinanigans']

def gerar_nome(raca):
    if raca not in ('Ogro', 'Goblin'):
        return raca
    
    if raca == 'Ogro':
        nomes = nomeogros
        return nomes[randint(0, len(nomes))]
    
    if raca == 'Goblin':
        nomes = nomesgoblins
        return nomes[randint(0, len(nomes))]

print(gerar_nome('Ogro'))