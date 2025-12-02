from hero import heroi
from random import randint

respostas = []

def atributorandom(respostas):
   for atributos in range(6):
      respostas.append(randint(1, 15))

def usuarioroubando(respostas):
    respostas.clear()
    respostas [:] = []
    atributorandom(respostas)


for dict in heroi:
    for k, v in dict.items():
        print(f'Quanto pontos deseja inserir em {k}?')

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
    for k, v in dict.items():
       dict[k] = respostas[i]
       i += 1
