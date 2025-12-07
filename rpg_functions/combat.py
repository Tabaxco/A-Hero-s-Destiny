from character.hero import heroi

persoatt = heroi[1].copy()
persohpmana= heroi[2].copy()

def levardano(persohpmana, dano, resistencia = 0):
    hpatual = persohpmana['hp'] - (dano - resistencia)
    return hpatual


