class Llibre:
    def __init__(self, titol, autor, quantitat):
        self.titol = titol
        self.autor = autor
        self.quantitat = quantitat

    def prestar(self):
        if self.quantitat > 0:
            self.quantitat -= 1
            print(f"Prestant el llibre: {self.titol} de l'autor: {self.autor}")
        else:
            print(f"No queden exemplars del llibre: {self.titol}")

    def retornar(self):
        self.quantitat += 1
        print(f"Retornant el llibre: {self.titol} de l'autor: {self.autor}")

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Quantitat disponible: {self.quantitat}")
