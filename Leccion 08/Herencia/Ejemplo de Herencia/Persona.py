class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: Nombre:{self.nombre}, Edad: {self.edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        """
        Lo que hacemos mediante esta inicialización es inicializar tantos los atributos de la clase Empleado tanto como los de la clase Persona
        """
        super().__init__(nombre, edad) # Este método nos permite acceder al método inicializador de la clase Persona. Ahora podremos acceder a los atributos de la clase Persona gracias a nuestro método inicializador y la palabra reservada de super(). 
        self.sueldo = sueldo # Creamos un nuevo atributo para esta clase Empleado que en este caso es sueldo

    def __str__(self):
        return f'Empleado: {super().__str__()}, Sueldo: {self.sueldo}'

empleado1 = Empleado('Juan',28,5000)

# print(empleado1.nombre)
# print(empleado1.edad)
# print(empleado1.sueldo)