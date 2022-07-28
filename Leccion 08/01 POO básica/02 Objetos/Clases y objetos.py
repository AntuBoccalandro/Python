"""
Creación de un objeto a partir de la clase creada
"""

class Persona:
    
    def __init__(self): # Método de tipo double underscore
        self.nombre = 'Juan' # nombre es un atributo de nuestra clase
        self.apellido = 'Perez'
        self.edad = 28
    
persona1 = Persona() # Creamos un objeto
print(persona1.nombre) # Para acceder a un atributo hacemos lo siguiente
print(persona1.apellido) # Para acceder a un atributo hacemos lo siguiente
print(persona1.edad) # Para acceder a un atributo hacemos lo siguiente