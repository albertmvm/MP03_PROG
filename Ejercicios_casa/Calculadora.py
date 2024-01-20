print("===================================================")
print("                 Menú Calculadora ")
print("===================================================")
print(" 1 - SUMA ")
print(" 2 - RESTA ")
print(" 3 - MULTIPLICACIÓ ")
print(" 4 - DIVISIÓ ")
print(" 5 - DIVISIÓ ENTERA ")
print(" 6 - POTÉNCIA ")
print(" 7 - MODUL / RESIDU \n")

num = int(input("Introdueix l'opció que vols calcular: "))
print("")
if num == 1:
    print("Genial, vols fer una SUMA \n")
    num = int(input("Introdueix el primer valor: "))
    num += int(input("Introdueix el segon valor: "))
    print("\nEl resultat de la suma es:",num)

elif num == 2:
    print("Genial, vols fer una RESTA \n")
    num = int(input("Introdueix el primer valor: "))
    num -= int(input("Introdueix el segon valor: "))
    print("\nEl resultat de la suma es:",num)

elif num == 3:
    print("Genial, vols fer una MULTIPLICACIÓ \n")
    num = int(input("Introdueix el primer valor: "))
    num *= int(input("Introdueix el segon valor: "))
    print("\nEl resultat de la suma es:",num)

elif num == 4:
    print("Genial, vols fer una DIVISIÓ \n")
    num = int(input("Introdueix el primer valor: "))
    num /= int(input("Introdueix el segon valor: "))
    print("\nEl resultat de la suma es:",num)

elif num == 5:
    print("Genial, vols fer una DIVISIÓ ENTERA \n")
    num = int(input("Introdueix el primer valor: "))
    num //= int(input("Introdueix el segon valor: "))
    print("\nEl resultat de la suma es:",num)

elif num == 6:
    print("Genial, vols fer una POTÉNCIA \n")
    num = int(input("Introdueix el primer valor: "))
    num **= int(input("Introdueix el segon valor: "))
    print("\nEl resultat de la suma es:",num)

elif num == 7:
    print("Genial, vols fer MODUL / RESIDU \n")
    num = int(input("Introdueix el primer valor: "))
    num %= int(input("Introdueix el segon valor: "))
    print("\nEl resultat de la suma es:",num)

else:
    print("ERROR. NO ES CAP DE LES 7 OPCIÓNS!!")



