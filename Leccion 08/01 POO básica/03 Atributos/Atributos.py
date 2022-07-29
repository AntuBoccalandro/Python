# Atributos en Python
# Los atributos son las propiedades que se le dan a un objeto, como por ejemplo, velocidad (si hablamos de u auto) o color, etc...

class Auto():
    def __init__(self, color, velocidad, precio):
        self.color = color
        self.velocidad = velocidad
        self.precio = precio
    
automovil = Auto('Rojo', 250, 60000)
print(f'Color: {automovil.color}, Velocidad: {automovil.velocidad}, Precio: ${automovil.precio}')