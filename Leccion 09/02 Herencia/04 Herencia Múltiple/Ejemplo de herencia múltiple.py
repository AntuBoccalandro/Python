class FiguraGeometrica():
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

class Color():
    def __init__(self, color):
        self.color = color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        #  super().__init__() # Esta manera no es muy recomendable ya que no especificamos de que clase queremos inicializarla.
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho 

cuadrado1 = Cuadrado(5,'rojo')
print(cuadrado1.ancho)
print(cuadrado1.largo)
print(cuadrado1.color)
print(cuadrado1.calcular_area())