def afegir_empleat(nom, cognom, edat):
    with open("empleats.txt", "a") as f:
        f.write(f"{nom},{cognom},{edat}\n")

def buscar_empleat(nom):
    with open("empleats.txt", "r") as f:
        empleats = f.readlines()
    empleats = [empleat.strip() for empleat in empleats]
    empleats = [empleat for empleat in empleats if empleat.startswith(nom)]
    return empleats

def llistar_empleats():
    with open("empleats.txt", "r") as f:
        empleats = f.readlines()
    empleats = [empleat.strip() for empleat in empleats]
    return empleats

