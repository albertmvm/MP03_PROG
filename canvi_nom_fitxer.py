ruta_fitxer = input("Introdueix la ruta del fitxer: ")

# Obtenir el nom del fitxer sense la seva extensió:
nom_fitxer = ruta_fitxer.split(".")[-2]

# Eliminar l'extensió del nom del fitxer:
nom_fitxer_sense_extensio = nom_fitxer.split(".")[0]

# Mostrar el nom del fitxer sense l'extensió:
print("El nom del fitxer sense extensió és:", nom_fitxer_sense_extensio)

