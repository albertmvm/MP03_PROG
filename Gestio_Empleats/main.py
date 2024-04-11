import gestion_empleados

# Afegir un nou empleat:
gestion_empleados.afegir_empleat("Miquel", "Corral", 27)

# Buscar empleats pel nom:
empleats = gestion_empleados.buscar_empleat("Paula")
print("Empleats amb nom 'Paula':", empleats)

# Llistar tots els empleats:
empleats = gestion_empleados.llistar_empleats()
print("Tots els empleats:")
for empleat in empleats:
    print(empleat)
