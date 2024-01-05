print(" ============================================== ")
print("      INTRODUEIX DOS NUMEROS PER COMPARAR: ")
print(" ==============================================")


numero1 = int(input("Introdueix el primer número: ")) 
numero2 = int(input("Introdueix el segon número: "))

print("Els numeros a comparar son: ", numero1, " i " , numero2)

if numero1 == numero2:
    print( numero1 , "són iguals ", numero2)
if numero1 < numero2:
    print(numero1 , "és més petit que ", numero2)
if numero1 > numero2:
    print( numero1 , "és més gran que ", numero2)
if numero1 != numero2:
    print(numero1 , "és diferent que ", numero2)
if numero1 >= numero2:
    print( numero1 , "és més gran o igual que ", numero2)
if numero1 <= numero2:
    print( numero1 , "és més petit o igual que ", numero2)
else:
    ("xxxxxxxxxxxxxxxxx    ERROR    xxxxxxxxxxxxxxx")