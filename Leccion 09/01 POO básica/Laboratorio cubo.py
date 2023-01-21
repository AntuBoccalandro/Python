class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto
    
    def calcular_volumen(self):
        return self.ancho * self.profundo * self.alto

ancho = int(input('Ingrese el ancho del cubo: '))
profundo = int(input('Ingrese la profundidad del cubo: '))
alto = int(input('Ingrese el alto del cubo: '))

datos = Cubo(ancho, profundo, alto)

print(f'El volumenn del cubo con las dimensiones = {datos.ancho} * {datos.profundo} * {datos.alto} y su volumen es: {datos.calcular_volumen()} m3')