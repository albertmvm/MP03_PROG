## Crearem una clase `Biblioteca` en la que gestioni la llista de llibres
# Operacions relacionades: "1- Agregar libro" "2- Prestar libro" "3- Devolver libro" 

class Biblioteca:
    print("\n1. Afegir llibre")
    print("2. Prestar llibre")
    print("3. Tornar llibre")
    print("4. Sortir")

opcio = input("Seleccioneu una opció: ")

# Creem també la classe Llibre amb els atributs: titol, autor, genere, disponibilitat // amb el seus valors *strings i *Booleans

class Llibre:
    titol = str
    autor = str
    genere = str
    disponibilitat = True

biblioteca = []

if opcio == "1":
    titol = input("Introduïu el títol del llibre: ")
    autor = input("Introduïu l'autor del llibre: ")
    genere = input("Introduïu el gènere del llibre: ")
    disponibilitat = True
    llibre = {"titol": titol, "autor": autor, "genere": genere, "disponibilitat": disponibilitat}
    biblioteca.append(llibre)
    print(f'Llibre "{titol}" afegit a la biblioteca.')

elif opcio == "2":
    titol = input("Introduïu el títol del llibre a prestar: ")
    trobat = False
    for llibre in biblioteca:
        if llibre["titol"] == titol and llibre["disponibilitat"]:
            llibre["disponibilitat"] = False
            print(f'Llibre "{titol}" prestat amb èxit.')
            trobat = True
            break
    if not trobat:
        print(f'Llibre "{titol}" no disponible per a préstec.')

elif opcio == "3":
    titol = input("Introduïu el títol del llibre a tornar: ")
    trobat = False
    for llibre in biblioteca:
        if llibre["titol"] == titol and not llibre["disponibilitat"]:
            llibre["disponibilitat"] = True
            print(f'Llibre "{titol}" retornat amb èxit.')
            trobat = True
            break
    if not trobat:
        print(f'No es pot tornar el llibre "{titol}".')

elif opcio == "4":
    print("******* Sortint del programa ********")
else:
    print("Opció no vàlida. Si us plau, seleccioneu una opció correcta.")
