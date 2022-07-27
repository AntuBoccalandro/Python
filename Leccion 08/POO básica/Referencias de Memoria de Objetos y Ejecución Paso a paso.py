"""
1- Atributos de instancia o de objetos. Estos objetos tienen cada uno un valor pero son únicos de cada objeto y no se comparten con los demás objetos. 
"""

class Persona:
    
    def __init__(self, nombre, apellido, edad): # Los argumentos que le pasamos al los atributos
        self.nombre = nombre # Este es un parámetro
        self.apellido = apellido
        self.edad = edad
    
personal=Persona('Juan','Perez',28)
print(f'Objeto Persona1: {personal.nombre} {personal.apellido} {personal.edad}')
                         
persona2=Persona('Karla','Gomez',30)
print(f'Objeto Persona2: {persona2.nombre} {persona2.apellido} {persona2.edad}')