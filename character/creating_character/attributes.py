from hero import heroi
from creating_character.usuarioroubou import usuarioroubando, atributorandom
from creating_character.mana_hp import hp_mana
from creating_character.races import modifierrace
from time import sleep

respostas = []
attributes = heroi[1]

def deciding_attributes(raca):

    print("Agora... Quero me lembrar de suas características...")
    sleep(2)
    print("Você possui: 15, 14, 13, 12, 10, 8 para distribuir entre seus atributos.")
    print("Insira os valores corretamente!")
    sleep(2)
    print("")

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
    
    modifierrace(heroi[1], raca)
    
    hp_mana(heroi[2], heroi[1]['constituicao'], heroi[1]['inteligencia'])