from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

# No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.calcular_area())

rectangulo1 = Rectangulo(9, 'Azul')
print(rectangulo1.calcular_area())

print(Cuadrado.mro())