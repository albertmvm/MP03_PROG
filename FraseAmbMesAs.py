def recompte_a(frase):
    # Comptador de lletres 'a' en una frase:
    contador_a = frase.lower().count('a')
    return contador_a


def frase_a(paraules):
    max_a = 0
    frase_max_a = ""
    for frase in paraules:
        contador_a = recompte_a(frase)
        if contador_a > max_a:
            max_a = contador_a
            frase_max_a = frase
    return frase_max_a, max_a


def inici():
    paraules = []
    while True:
        entrada = input("Escriu una frase:> ")
        if entrada.lower() == "FI":
            break
        paraules.append(entrada)
        
        
        # Trobar la frase amb mes lletres 'a':
        frase_max_a, max_a = frase_a(paraules)
        print(f"La frase amb més 'a' és: \"{frase_max_a}\"")
        print(f"Té {max_a} 'a'.")

    print("FI DEL PROGRAMA")
inici()

