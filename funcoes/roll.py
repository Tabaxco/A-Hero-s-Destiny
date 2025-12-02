from random import randint

def rolar(quantidade:int = 1, lados: int = 20):
    resultado = []

    for dados in range(quantidade):
        resultado.append(randint(1, lados))
    
    soma_resultado = sum(resultado)

    print(f"{soma_resultado} ⟵ {resultado} {quantidade}d{lados}")