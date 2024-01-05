print("===================================================")
num = int(input("Introduce un número entero: "))
num1 = int(input("Introduce el segundo número entero: "))
num2 = int(input("Introduce un tercer número entero: "))
print("===================================================")

if num < num1 and num1 > num2:
    print("El número mas grande es el: " , num1)
elif num > num2:
    print("El número mas grande es el: " , num)
else:
    print("El número mes gran es el: " , num2)


