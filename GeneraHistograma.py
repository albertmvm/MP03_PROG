import random
def daus():
    # Tirar dos daus i retornar la suma dels resultats
    return random.randint(1, 6) + random.randint(1, 6)

def histograma():
    # Inicialitzar l'array per explicar les repeticions x cada tirada
    repeticions = [0] * 11

    # Realitzar les tirades i comptar les repeticions
    for _ in range(1000):
        sum_tirada = daus()
        repeticions[sum_tirada - 2] += 1

    max_repeticions = max(repeticions)
    valor_max = repeticions.index(max_repeticions) + 2

    # Mostrar el histograma y el máximo
    print("Histograma tirades:")
    for i in range(2, 13):
        print(f"{i}: {'*' * repeticions[i-2]}")
    print(f"El valor més alt és -{valor_max}- amb -{max_repeticions}- repeticions.")

histograma()
