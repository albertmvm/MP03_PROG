# Crear llista per emmagatzemar els noms d'usuari

usuaris = []

while True:
    # Mostrar opcions que veurà l'usuari
    print("\n Opcions Disponibles:")
    print(" 1. Afegir un usuari")
    print(" 2. Eliminar un usuari")
    print(" 3. Llistar tots els usuaris ")
    print(" 4. Sortir")

    # Demanar que triï una opció l'usuari
    opcio = input("Selecciona una opció (1-2-3-4): ")

    if opcio == '1':
        nou_usuari = input("Introdueix el nom d'usuari: ")
        usuaris.append(nou_usuari)
        print("Usuari" , nou_usuari, "AFEGIT CORRECTAMENT!! ")
    elif opcio == '2':
        usuari_eliminar = input("Introdueix el nom d'usuari que vols eliminar: ")
        if usuari_eliminar in usuaris:
            usuaris.remove(usuari_eliminar)
            print("Usuari" , usuari_eliminar, "ELIMINAT CORRECTAMENT. ")
        else:
            print("ERROR. L'usuari" , usuari_eliminar, "NO es troba en la llista. ")
    elif opcio == '3':
        #Llistar tots els usuaris
        print("\n Llista usuaris: ")
        for usuari in usuaris:
            print(usuari)
    elif opcio == '4':
        print("FI DEL PROGRAMA. ")
        break
    else:
        print("ERROR. Selecciona una opció (1-2-3-4).")
