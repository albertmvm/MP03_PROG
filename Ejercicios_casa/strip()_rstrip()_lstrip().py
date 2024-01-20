##### Métode strip()
## Ex 1. "Eliminar els espais al inici i al final."
str = "\tHola Albert\n"
print(str)
str = str.strip()
print(str)

## Ex 2. "Eliminar la lletra 't' al inici i al final."
str = "Hola Albert\n"
print(str)
str = str.strip("t")
print(str)

##### Métode rstrip()
## Ex 1. "Eliminar els espais al final (a la dreta)"
str = "\tHola Albert\n"
print(str)
str = str.rstrip("H t \t\n")
print(str)

##### Métode lstrip()
## Ex 2. "Eliminar els espais del principi (a l'esquerra)"
str = "\tHola Albert\n"
print(str)
str = str.lstrip("H t \t\n")
print(str)

