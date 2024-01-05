print("======================================================")
print("                  CONVERSOR ")
print("======================================================")

print("MENÚ D'OPCIONS: \n")
print("1. Convertir de número a paraula.")
print("2. Convertir de paraula a numero.")

opcio1 = int(input(" ¿¿QUINA ES L'OPCIÓ QUE VOLS?? "))

if opcio1 == 1:
    print(" D'ACORD, vols convertir de número a paraula. ")

    opcio_un = int(input(" ¿¿ QUIN NÚMERO VOLS CONVERTIR A PARAULA ?? "))
    if opcio_un == 1:
        print("El número es 'UNO' ")
    elif opcio_un == 2:
        print("El número es 'DOS' ")
    elif opcio_un == 3:
        print("El número es 'TRES' ")
    elif opcio_un == 4:
        print("El número es 'QUATRE' ")
    elif opcio_un == 5:
        print("El número es el 'CINC' ")
    elif opcio_un == 6:
        print("El número es el 'SIS' ")
    elif opcio_un == 7:
        print("El número es 'SET' ")
    elif opcio_un == 8:
        print("El número es el 'VUIT' ")
    elif opcio_un == 9:
        print("El número es el 'NOU' ")
    elif opcio_un == 10:
        print("El número es 'DEU' ")
    else:
        print("xxxxxxx OPCIÓ NO DISPONIBLE (NO ESTA DINS DEL RANG) xxxxxxxxx")

elif opcio1 == 2:
    print(" D'ACORD, vols convertir de paraula a número. ")
    
    opcio_dos = int(input(" ¿¿ QUINA PARAULA VOLS CONVERTIR A NÚMERO ?? "))
    opcio_dos = opcio_dos.lower()

    if opcio_dos == "uno":
        print("El número es '1' ")
    elif opcio_dos == "dos":
        print("El número es '2' ")
    elif opcio_dos == "tres":
        print("El número es '3' ")
    elif opcio_dos == "quatre":
        print("El número es '4' ")
    elif opcio_dos == "cinc":
        print("El número es el '5' ")
    elif opcio_dos == "sis":
        print("El número es el '6' ")
    elif opcio_dos == "set":
        print("El número es '7' ")
    elif opcio_dos == "vuit":
        print("El número es el '8' ")
    elif opcio_dos == "nou":
        print("El número es el '9' ")
    elif opcio_dos == "deu":
        print("El número es '10' ")
    else:
        print("xxxxxxx OPCIÓ NO DISPONIBLE (NO ESTA DINS DEL RANG) xxxxxxxxx")
else:
    print("XXXXXXX ERROR, NO ESTÁ DINS DEL RANG XXXXXXXXXX")
print("FI. ")