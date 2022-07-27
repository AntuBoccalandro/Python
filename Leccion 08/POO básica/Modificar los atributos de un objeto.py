"""
1- Atributos de instancia o de objetos. Estos objetos tienen cada uno un valor pero son únicos de cada objeto y no se comparten con los demás objetos. 
"""

class Persona:
    
    def __init__(self, nombre, apellido, edad): # Los argumentos que le pasamos al los atributos
        self.nombre = nombre # Este es un parámetro
        self.apellido = apellido
        self.edad = edad
    
persona1=Persona('Juan','Perez',28)
print(f'Objeto Persona1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona1.nombre = 'Juan Carlos' # Esta es la manera que tenemos de cambiar el atributo de un objeto, es decir nos referimos a la clase creada y luego nos referimos al atributo en específico a través del operador '.' y asignamos el nuevo valor al atributo del objeto referido. 
persona1.apellido = 'Elías'
persona1.edad = 40
print(f'Objeto Persona1 con las modificaciones: {persona1.nombre} {persona1.apellido} {persona1.edad}')
                    
persona2=Persona('Karla','Gomez',30)
print(f'Objeto Persona2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

persona2.nombre = 'Elías'
persona2.apellido = 'Carlos'
persona2.edad = 28
print(f'Objeto Persona2 con los valores modificados: {persona2.nombre} {persona2.apellido} {persona2.edad}')