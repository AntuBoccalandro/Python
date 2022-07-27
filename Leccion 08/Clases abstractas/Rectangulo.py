from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #  super().__init__() # Esta manera no es muy recomendable ya que no especificamos de que clase queremos inicializarla.
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f'{FiguraGeometrica.__str__} {Color.__str__()}'

    def calcular_area(self):
        return self.alto * self.ancho