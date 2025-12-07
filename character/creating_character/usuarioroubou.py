from random import randint


def atributorandom(respostas):
   for atributos in range(6):
      respostas.append(randint(8, 15))

def usuarioroubando(respostas):
    respostas.clear()
    atributorandom(respostas)