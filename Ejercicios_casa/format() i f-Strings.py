##### Métode .format():
## Ex 1: 
nom = "Albert"
edat = 20
print("\nHola {}, tens {} anys".format(nom, edat))

## Ex 2:
print("Hola {nom}, tens {edat} anys".format(nom = "Albert", edat = 20))

## Ex 3:
nom = "Albert"
edat = 20
print("Hola {0}, tens {1} anys \n".format(nom, edat))

##### f-Strings:
## Ex 1:
print(f"El resultat de la suma 5 + 5 = {5+5}")

## Ex 2:
nom = "Albert"
altura = 1.70
edat = 20

print(f"Hola {nom}, tens {edat} anys i una estatura de {altura}m")

## Ex 3:
nom = input("¿Quin és el teu nom? ")
num1 = int(input("Introdueix un número: "))
num2 = int(input("Introdueix un segon número: "))

print (f"Hola {nom} el resultat de {num1} + {num2} és: {num1 + num2}")