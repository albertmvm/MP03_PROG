from Llibreclass import Libre
from Sociclass import Soci
from Prestecclass import Prestec


class Biblioteca:
    def __init__(self):
        self.llibres = []
        self.socios = []
        self.prestecs = []

    def afegir_llibre(self, llibre: Libre):
        self.llibres.append(llibre)

    def eliminar_llibre(self, llibre: Libre):
        self.llibres.remove(llibre)

    def afegir_soci(self, soci: Soci):
        self.socios.append(soci)

    def eliminar_soci(self, soci: Soci):
        self.socios.remove(soci)

    def registrar_prestec(self, prestec: Prestec):
        self.prestecs.append(prestec)
        self.eliminar_llibre(prestec.llibre)

    def retornar_prestec(self, prestec: Prestec):
        self.prestecs.remove(prestec)
        self.afegir_llibre(prestec.llibre)

    def mostrar_info(self):
        print("Llibres:")
        for llibre in self.llibres:
            print(f"- {llibre.titol} de {llibre.autor}")

        print("\nSocis:")
        for soci in self.socios:
            print(f"- {soci.nom} {soci.cognom} (ID: {soci.id})")

        print("\nPréstecs:")
        for prestec in self.prestecs:
            print(f"- {prestec.llibre.titol} (Prestat a {prestec.soci.nom} {prestec.soci.cognom})")