from Llibreclass import Llibre
from Sociclass import Soci

class Prestec:
    def __init__(self, llibre: Llibre, soci: Soci):
        self.llibre = llibre
        self.soci = soci

    def registrar_prestec(self, data: str):
        self.soci.demanar_prestec(data)
        print(f"Préstec registrat: Llibre {self.llibre.titol}, Soci {self.soci.nom}, Data: {data}")
        self.llibre.prestar()

    def retornar_prestec(self):
        self.soci.retornar_prestec()
        print(f"Devolució de préstec: Llibre {self.llibre.titol}, Soci {self.soci.nom}")
        self.llibre.devolver()

    def mostrar_info(self):
        print(f"Préstec del llibre {self.llibre.titol} al soci {self.soci.nom} {self.soci.cognom}")