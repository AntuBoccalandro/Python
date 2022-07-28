class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
    
    # Este método se lo llama destructor. Lo que hace es destruir a un objeto creado y muestra una serie de código que hallamos colocado
    def __del__(self):
        print(f'Pesona: {self._nombre} {self._apellido}')


persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Lara'
persona1.edad = 30
persona1.mostrar_detalle()