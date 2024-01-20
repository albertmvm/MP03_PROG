#### Métode title() / istitle(): 
nom = input("Nom: ")
cognom = input("Congmom: ") 
nom_complet = f"{nom} {cognom}"
print()
print(f"¿El métode istitle() s'ha aplicat? {nom_complet.istitle()}")

print(f"Aplicant el métode title(): {nom_complet.title()}")

print(f"Tornem a imprimir el nom: {nom_complet}")

print()
nom_complet = nom_complet.title()
print(f"¿El métode istitle() s'ha aplicat? {nom_complet.istitle()}")
print(f"S'ha aplicat el métode title() de forma permanent: {nom_complet}")
