class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'Color: {self.color} Ruedas: {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()} Velocidad: {self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f'{super().__str__()} Tipo: {self.tipo}'

vehiculo = Vehiculo('Azul', 4)
print(f'Objeto: Vehiculo --> {vehiculo}')

coche = Coche('Rojo', 4, 190)
print(f'Objeto: Coche --> {coche}')

bicicleta = Bicicleta('Negro', 2, 'Mountain Bike')
print(f'Objeto: Bicicleta --> {bicicleta}')