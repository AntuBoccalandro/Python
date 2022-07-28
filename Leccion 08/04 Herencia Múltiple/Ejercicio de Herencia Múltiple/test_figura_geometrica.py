from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')


# MRO - Method Resolution Order. Este método nos permite aber la jerarquía de clases dentro de nuestro programa. Permitienonos ver todo el camino que hace Python hasta llegar a la clase padre que siempre será Object. Nos muestra el orden en el que se mandan a llamar los métodos de las clases.
print(Cuadrado.mro())