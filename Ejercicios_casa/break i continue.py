## BREAK
print("While amb la sentencia break: \n")
contador = 0

while contador < 100:
    contador += 1
   
    if contador == 5:
        break
    print("Valor actual de la variable: " , contador)
print("\n FI DEL PROGRAMA, la sentencia break s'ha executat. \n")


## CONTINUE
print("While amb la sentencia continue: \n")
contador = 0

while contador < 10:
    contador += 1
   
    if contador == 5:
        continue
    print("Valor actual de la variable: " , contador)
print("\n FI DEL PROGRAMA, la sentencia continue s'ha executat. \n")
