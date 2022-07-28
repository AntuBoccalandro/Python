"""
1- 
"""

class Persona:
    
    def __init__(self, nombre, apellido, edad): # Los argumentos que le pasamos al los atributos
        self.nombre = nombre # Este es un parámetro
        self.apellido = apellido
        self.edad = edad
    
persona1 = Persona('Juan', 'Perez', 28) # Creamos un objeto con los argumentos
print(persona1.nombre) 
print(persona1.apellido) 
print(persona1.edad) 