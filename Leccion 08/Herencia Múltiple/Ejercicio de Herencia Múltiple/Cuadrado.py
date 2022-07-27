from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #  super().__init__() # Esta manera no es muy recomendable ya que no especificamos de que clase queremos inicializarla.
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho