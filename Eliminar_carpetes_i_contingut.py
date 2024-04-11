# Demanar al usuari que introdueixi la ruta de la carpeta
ruta_carpeta = input("Introdueix la ruta de la carpeta: ")

def eliminar_elements(ruta_carpeta):
    # Obtenir una llista de tots els elements de la carpeta
    elements = []
    file = open(ruta_carpeta + "\\carpeta.txt", "w")
    file.close()
    with open(ruta_carpeta + "\\carpeta.txt", "r") as f:
        for line in f:
            elements.append(line.strip())
    with open(ruta_carpeta + "\\carpeta.txt", "w") as f:
        pass
    
    # Iterar sobre tots els elements de la carpeta
    for element in elements:
        ruta_element = ruta_carpeta + "\\" + element
    else:
        print("La ruta especificada no és vàlida.")
        
### NO ESTA TERMINAT AQUEST PROGRAMA ###
