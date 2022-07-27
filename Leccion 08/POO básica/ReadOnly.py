# Read Only o solo leer en Python.

class User:
    def __init__(self, name, lastname, password, edad):
        self.name = name
        self.lastname = lastname
        self._password = password # Como solo podemos ver el valor del atributo y no podemos moficicarlo se dice que es una variable read-Only o de solo lectura, ya que no podemso modificar el valor del atributo. Esto se logra mediante el método get solamente ya que al quitar el método set no podremos modificar el valor de nuestra variable encapsuslada.
        self.edad = edad

    @property
    def password(self): 
        return self._password

    def mostrar_detalles(self):
        print(f'Usuario1: {self.name} {self.lastname} {self._password} {self.edad}')

usuario1 = User('Juan', 'Carlos', 1234, 24)

print(usuario1.password) 

usuario1.password = 'Nueva contraseña'
print(usuario1.password)