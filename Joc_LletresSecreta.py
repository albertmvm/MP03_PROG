import random

def gen_combinacio_secreta():
    lletres = 'qwertyuiopasdfghjklñzxcvbnm'
    combinacio_secreta = ''.join(random.choice(lletres) for _ in range(5))
    return combinacio_secreta

def pistas(combinacio_secreta, intent):
    pista = ''
    for i in range(5):
        if intent[i] == combinacio_secreta[i]:
            pista += 'O'
        elif intent[i] in combinacio_secreta:
            pista += 'X'
        else:
            pista += '.'
    return pista

def joc():
    combinacio_secreta = gen_combinacio_secreta()
    print("Benvingut al joc d'endevinar la combinació de 5 lletres!")

    intent = ''
    while intent != combinacio_secreta:
        intent = input("Escriu 5 lletres minúscules: ")
        if len(intent) != 5 or not intent.islower():
            print("Si us plau, escriu exactament 5 lletres minúscules.")
            continue
        pista = pistas(combinacio_secreta, intent)
        print("La resposta es",([pista]),"Continua intentant-ho!")

    print("La resposta es [OOOOO] , CORRECTE!")
    
joc()
