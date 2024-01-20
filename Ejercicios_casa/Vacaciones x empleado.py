print("+++++++++++++++++++++++++++++++++++++++++++")
print("\n    DIAS DE VACACIONES POR CADA AÑO")
print("\n+++++++++++++++++++++++++++++++++++++++++")
print("")

nombre = (input("Introduce el Nombre: "))
clave = int(input("Introduce la Clave (1 - 2 - 3): "))
años = float(input("Introduce los Años en la empresa: "))

if clave == 1:
    print("La clave que a introducido es 1: ")
    if años == 1 and años < 2:
        print("Tiene derecho a 6 dias de vacaciones. ")
        print("FIN DEL PROGRAMA.")

    elif años  >= 2 and años <= 6:
        print("Tiene derecho a 14 dias de vacaciones.")
        print("FIN DEL PROGRAMA.")

    elif años >= 7:
        print("Tiene derecho a 20 dias de vacaciones.")
        print("FIN DEL PROGRAMA.")
    else:
        print("SIN DERECHO A VACACIONES... ")
        print("FIN DEL PROGRAMA.")
elif clave == 2:
    print("La clave que a introducido es 2: ")
    if años == 1 and años < 2:
        print("Tiene derecho a 7 dias de vacaciones. ")
        print("FIN DEL PROGRAMA.")

    elif años  >= 2 and años <= 6:
        print("Tiene derecho a 15 dias de vacaciones.")
        print("FIN DEL PROGRAMA.")

    elif años >= 7:
        print("Tiene derecho a 22 dias de vacaciones.")
        print("FIN DEL PROGRAMA.")
    else:
        print("SIN DERECHO A VACACIONES... ")
        print("FIN DEL PROGRAMA.")

elif clave == 3:
    print("La clave que a introducido es 3: ")
    if años == 1 and años < 2:
        print("Tiene derecho a 10 dias de vacaciones. ")
        print("FIN DEL PROGRAMA.")

    elif años  >= 2 and años <= 6:
        print("Tiene derecho a 20 dias de vacaciones.")
        print("FIN DEL PROGRAMA.")

    elif años >= 7:
        print("Tiene derecho a 30 dias de vacaciones.")
        print("FIN DEL PROGRAMA.")
    else:
        print("SIN DERECHO A VACACIONES... ")
        print("FIN DEL PROGRAMA.")
else:
    clave != 1 or clave != 2 or clave != 3  
    print("LA CLAVE QUE A INTRODUCIDO NO EXISTE... ")
    print("FIN DEL PROGRAMA.")
