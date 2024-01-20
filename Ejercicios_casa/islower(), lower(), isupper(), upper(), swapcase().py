#### Métode islower() / lower(): 'lletres minúscules'
nom = "Albert"
cognom = "Martinez"
nom_complet = f"{nom} {cognom}"

print()
print("Totes les lletres estan en minúscules?",nom_complet.islower())
print("Imprimeix per pantalla el nom_complet amb minúscules:",nom_complet.lower())

#### Métode isupper() / upper(): 'lletres majúscules'
nom = "Albert"
cognom = "Martinez"
nom_complet = f"{nom} {cognom}"

print()
print("Totes les lletres estan en majúscules?",nom_complet.isupper())
print("Imprimeix per pantalla el nom_complet amb majúscules:",nom_complet.upper())

#### Métode swapcase():
## 'lletres minúscules a - MAJÚSCULES'
nom_complet = "albert martinez"
print()
print("Nom complet amb minúscules:",nom_complet.swapcase())

## lletres MAJÚSCULES a - minúscules
nom_complet1 = "ALBERT MARTINEZ"
print()
print("Nom complet amb majúscules:",nom_complet1.swapcase())

#### Métode capitalize() // fa que la primera lletra del 'str' sigui MAJÚSCULA
print("\nAbans del metode 'capitalize()':",nom_complet)
print("Aplicant el métode 'capitalize()':",nom_complet.capitalize())

## En cas de que tot estigui en majúscules, deixa la primera lletra en majúscula i la resta les canvia en minúscules:
print("\nAbans del metode 'capitalize()':",nom_complet1)
print("Aplicant el métode 'capitalize()':",nom_complet1.capitalize())




