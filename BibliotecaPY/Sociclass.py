from Llibreclass import Llibre

class Soci:
    def __init__(self, nom, cognom, id):
        self.nom = nom
        self.cognom = cognom
        self.id = id

    def demanar_prestec(self, data_prestec):
        print(f"El soci {self.nom} {self.cognom} (id: {self.id}) ha demanat un préstec.")

    def retornar_prestec(self):
        print(f"El soci {self.nom} {self.cognom} (id: {self.id}) ha retornat un préstec.")

    def mostrar_info(self):
        print(f"Nom: {self.nom}, Cognom: {self.cognom}, ID de soci: {self.id}")
    
