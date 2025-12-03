from random import randint

def rolar(quantidade:int = 1, lados: int = 20, *bonus):
    resultado = []

    for dados in range(quantidade):
        resultado.append(randint(1, lados))
    
    soma_resultado = sum(resultado)
    for modificador in bonus:
        soma_resultado += modificador
    
    print(f"{soma_resultado} ⟵ {resultado} {quantidade}d{lados}")
