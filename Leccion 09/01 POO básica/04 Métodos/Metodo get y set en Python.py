"""
El encapsulamiento existe para que no se peuda acceder directamente a un elemento desde fuera de la clase. Pero de alguna manera hay que hacerlo, es por eso que se suelen crear los métodos get y set.

Método get: 
Este método se utilizará para acceder al atributo

Método set:
Este método se utilizará para moficicar al atributo

"""

class User:
    def __init__(self, name, lastname, password, edad):
        self.name = name
        self.lastname = lastname
        self._password = password 
        self.edad = edad

    # Este decorador hace es que podamos acceder al atributo como atributo y no utilizando el método get. Pero lo que enrealidad hace es llamar indirectamente al método get pero puediendolo utilizar como si fuera un atributo y no un método.
    @property
    def password(self): 
        # Este es nuestro método get. Lo que hace es recuperar o retornar el valor del atributo _password. Pero este método lo que hace es mostrar el valor del atributo _password, pero podemos seguir modificandolo desde fuera de la clase con la línea de cósigo especial ya vista. Es por eso que se utiliza el método o el decorador set, que nos permitirá bloquear de cualquier edición al valor del atributo _password.
        return self._password
    
    # Este decorador acompañado de esta función que la llamamos 'set' nos permite acceder al atributo como si fuera un atributo y no un método. 
    @password.setter
    def password(self, password):
        # Nuestro método set nos permite modificar el valor del atributo como si fuera como cualquier otro. Es decir que gracias a este método por más de que tengamos 'bloqueado' el atributo password podemos modificarlo de la siguiete manera: usuario1.password = 3492834. Como vemos puedo hacerlo como si fuera un atributo normal y corriente y no de la siguiete manera: usuario1._password = 123912879 --> Acá utilizamos el guión bajo, una práctica de lo nada buena. Este método set lo que hace es llamar indirectamente al método get (anteriormente definido) y luego nos permite recuperar el valor del atributo a través del método get.
        self._password = password

    def mostrar_detalles(self):
        print(f'Usuario1: {self.name} {self.lastname} {self._password} {self.edad}')

usuario1 = User('Juan', 'Carlos', 1234, 24)

print(usuario1.password) # Como vemos gracias a nuestro método set estamos pudiendo acceder al atributo y no modificarlo gracias al dicho método set. Pudiendo hací evitar tener que llamar al método password() y utilizarlo como si fuera un atributo normal y corriente.

usuario1.password = 'Nueva contraseña' # Como vemos gracias a nuestro método set podemos modificar el valor del atributo de manera normal y corriente sin utilizar los underscores y gracias a nuestro método get podemos obtener el valor del atributo modificado.
print(usuario1.password)