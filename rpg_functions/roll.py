from random import randint

def rolar(quantidade:int = 1, lados: int = 20, *bonus):
    resultado = []

    for dados in range(quantidade):
        resultado.append(randint(1, lados))
    
    soma_resultado = sum(resultado)
    for modificador in bonus:
        soma_resultado += modificador
    
    print(f"{soma_resultado} ⟵ {resultado} {quantidade}d{lados}")

    if sum(resultado) == 1:
        mensagem = 'Falha Crítica!'
    elif sum(resultado) == 20:
        mensagem == 'Sucesso Crítico!'
    
    return soma_resultado, resultado, mensagem
