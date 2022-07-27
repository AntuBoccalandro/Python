""""
El encapsulamiento.

ATRIBUTOS PÚBLICO: son aquellos atributos que pueden ser accedidos y modificados directamente desde fuera de nuestra clase utilizando el nombre de la variable y seleccionando el atributo. Ejemplo: user.name = 'Juan'

_ATRIBUTO: cuando colocamos un underscode '_' delante del nobre del atributo lo que haremos es hacer que nada más se pueda utilizar, llamar o modificar este atributo dentro de la misma clase haciendo imposible desde afuera de la clase acceder a dicho atributo. Ejemplo: self._contraseña = contraseña 

El encapsulamiento existe para que no se peuda acceder directamente a un elemento desde fuera de la clase.
"""

class User:
    def __init__(self, name, lastname, password, edad):
        self.name = name
        self.lastname = lastname
        self._password = password # Este atributo se podrá modificar y  acceder (solo con una línea de código específica que transpase este bloqueo.), a esto se lo conoce como atributo encapsulado. No son las mejores prácticas pero se suele poner el underscore para indicar que este atributo no debería ser modificado.
        self.edad = edad

    def mostrar_detalles(self):
        print(f'Usuario1: {self.name} {self.lastname} {self._password} {self.edad}')

usuario1 = User('Juan', 'Carlos', 1234, 24)

usuario1._password = 9999 # Al colocar el atributo con un underscore adelante logramos pasarnos esta especie de 'protección' y podemos modificar el elemento a pesar de este no tener que poder ser accedido. Pero con esta línea de código logramos saltarnos esta 'protección' del atributo.

usuario1.mostrar_detalles()


class User:
    def __init__(self, name, lastname, password, edad):
        self.name = name
        self.lastname = lastname
        self.__password = password 
        self.edad = edad

    def mostrar_detalles(self):
        print(f'Usuario1: {self.name} {self.lastname} {self.__password} {self.edad}')

usuario1 = User('Juan', 'Carlos', 1234, 24)

usuario1.__password = 9999 # Al estar completamente encapsulado este atributo la modificacación que le hagamos no se aplicará al mismo. Siendo completamente inaxesible y ineeditable desde fuera de la clase.

usuario1.mostrar_detalles()