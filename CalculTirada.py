def calcular_prob(valor):
    if valor < 2 or valor > 12:
        print("El valor no esta entre 2 i 12.")
        return

    # Inicialitzar una llista per emmagatzemar la quantitat de vegades que s'obté cada suma
    repeticions = [0] * 11

    # Definir el nombre total de tirades possibles (dos daus de sis cares)
    total_tirades = 36

    # Iterar sobre totes les combinacions possibles de llançaments de daus:
    for i in range(1, 7):
        for j in range(1, 7):
            suma = i + j
            # Incrementar el comptador de la suma corresponent si és igual o menor que el valor ingressat:
            if suma <= valor:
                repeticions[suma - 2] += 1

    # Calcular la probabilitat multiplicant la suma de les repeticions x 100 , dividint entre el total de tirades possibles
    probabilitat = sum(repeticions) * 100 / total_tirades

    print("La probabilitat és", round(probabilitat,1),"%.")


def inici():
    # Inici del programa x pantalla:
    print("Escriu el valor a calcular [2 - 12]: ")
    valor = int(input())

    # Calcular la probabilitat per al valor ingressat:
    calcular_prob(valor)

inici()
