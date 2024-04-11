import gestion_empleados

# Afegir un nou empleat:
gestion_empleados.afegir_empleat("Ana", "Rodriguez", 30)

# Buscar empleats pel nom:
empleats = gestion_empleados.buscar_empleat("Juan")
print("Empleats amb nom 'Juan':", empleats)

# Llistar tots els empleats:
empleats = gestion_empleados.llistar_empleats()
print("Tots els empleats:")
for empleat in empleats:
    print(empleat)