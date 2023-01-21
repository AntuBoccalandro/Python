# Crea un programa que mediante clases, objetos y métodos calcule el area de un rectagulo. Los valores como base y altura deben ser introducidos por el usuario

class Get_area:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))

datos = Get_area(base, altura)

print(f'El area del rectángulo es de: {datos.area()}')