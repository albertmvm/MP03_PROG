temperatures = []
dia = 1
mes = 1

def inici():
    while True:
        mostrar_menu()
        opcio = input("Opcio: ").upper()

        if opcio == "RT":
            registrar_temperatures()
        elif opcio == "MJ":
            mostrar_mitjana()
        elif opcio == "DF":
            mostrar_diferencia()
        elif opcio == "FI":
            break
        else:
            print("Opcio incorrecta!")

def mostrar_menu():
    print("Benvingut al registre de temperatures")
    print("-------------------------------------")
    print("[RT] Registrar temperatures setmanals.")
    print("[MJ] Consultar temperatures setmanals.")
    print("[DF] Consultar temperatura mitjana.")
    print("[FI] Sortir.")

def registrar_temperatures():
    if len(temperatures) >= (52 * 7):
        print("Ja tenim totes les temperatures apuntades.")
    else:
        llegir_temperatures_teclat()
        incrementar_data()
        
def mostrar_mitjana():
    if len(temperatures) > 0:
        mitjana = sum(temperatures) / len(temperatures)
        print(f"Fins avui {dia} de {nom_mes()} la mitjana ha estat de {mitjana} graus.")
    else:
        print("No hi ha temperatures registrades.")

def mostrar_diferencia():
    if len(temperatures) > 0:
        diferencia = max(temperatures) - min(temperatures)
        print(f"Fins avui {dia} de {nom_mes()} la diferencia maxima ha estat de {diferencia} graus.")
    else:
        print("No hi ha temperatures registrades.")

def llegir_temperatures_teclat():
    lector = input("Escriu les temperatures d'aquesta setmana: ")
    temperatures.extend([float(temp.replace(',', '.')) for temp in lector.split()])

def incrementar_data():
    global mes, dia
    dies_mes = dies_mes_actual()

    dia += 7

    if dia > dies_mes:
        dia -= dies_mes
        mes += 1

        if mes > 12:
            mes = 1

def dies_mes_actual():
    if mes == 2:
        return 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def nom_mes():
    noms_mesos = ["Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre"]
    return noms_mesos[mes - 1]

inici()
