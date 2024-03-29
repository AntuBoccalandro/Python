# **Encapsulamiento**

La encapsulación es uno de los pilares de la programación ortientada a objetos. Nos permite regular el acceso a los métodos y atributos de una clase. En cierta manera, enmascara la complejidad de una clase. 

# **Modificadores de acceso**

Los modificadores de acceso son justamente modificadores que me permiten regular el acceso de ciertos atributos y métodos de la clase. Se pueden dividir en tres tipos:

* **Públicos**: son accesibles desde cualquier punto del programa. Dentro y fuera de la clase y sus subcalses. Se define con la siguiente sintaxis `attribute = value`. 
* **Protejidos**: son accesibles porla misma clases, sus subclases y dentro del mismo paquete. Se define con la siguiente sintaxis `_attribute = value`.
* **Privados**: son accesibles únicamente dentro de la misma clase. Este tipo de clases no permite que podamos crear subclases ya que sus atributos y métodos son únicamente accesibles desde la misma clase y no desde otras. Se define con la siguiente sintaxis `__attribute = value`. 


## **Atributos públicos**

```python
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def mostrar_detalles(self):
        print(f'Person: {self.name} {self.lastname} {self.edad}')

person = Person('John', 'Williams', 1234, 29)
person.see_datails()

# Jhon Williams 1234 29
```

## **Atributos protejidos**

```python
class Person:
    def __init__(self, name, lastname, age):
        self._name = name
        self.lastname = lastname
        self.age = age

    def mostrar_detalles(self):
        print(f'Person: {self._name} {self.lastname} {self.edad}')

person = Person('John', 'Williams', 1234, 29)
person.see_datails()

# Error
```

## **Atributos privados**

```python
class Person:
    def __init__(self, name, lastname, age):
        self.__name = name
        self.lastname = lastname
        self.age = age

    def mostrar_detalles(self):
        print(f'Person: {self.__name} {self.lastname} {self.edad}')


class Student(Person):
    def __init__(self, name, lastname, age):
        self.__name = name
        self.lastname = lastname
        self.age = age

    def mostrar_detalles(self):
        print(f'Person: {self.__name} {self.lastname} {self.edad}')


person = Student('John', 'Williams', 1234, 29)
person.mostrar_detalles()

# Error
```

## **Formas de acceder a los atributos aunque estos sean protegidos o privados**

Aunque no es muy intuituva hay maneras de acceder a los atributos privados y protejidos de una clase aunque en teoría no se puedan acceder, pero al no existir la encapsulación es por ello que se puede realizar este tipo de acciones.


**Ejemplo:**
```python
class Padre:
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2
        self.__variable_privada = 3


if __name__ == '__main__':
    # Imprimir todos los atributos de la clase
    padre = Padre()
    print(dir(padre))
    # Accedemos a los atributos de la clase
    print(f'Variable publica: {padre.variable_publica}')
    print(f'Variable protegida: {padre._variable_protegida}')
    # print(f'Variable privada manda error: {padre.__variable_privada}')
    print(f'Variable privada usando name mangling: {padre._Padre__variable_privada}')
```
**La nomenclatura utilizada es la siguiente:**
* Acceder a a un atributo público: `<object>.<atribute_name>`
* Acceder a a un atributo protegido: `<object>.<atribute_name>` 
  * También podemos crear un método que retorne el valor del atributo privado. 
    ```python
    def get_protected_atribute(self):
        return self._variable_protegida
    ```
* Acceder a a un atributo privado:  `<object>._<class_name>__.<atribute_name>` 
  * También podemos crear un método que retorne el valor del atributo privado. 
    ```python
    def get_private_atribute(self):
        return self.__variable_privada
    ```

A la manera de acceder por medio de estas nomenclaturas se lo conoce como Name-Mangling


# **Métodos getter, setters y deleters**

Los métodos getter, setter y deletter nos permiten manipular los accesos a los atributos protegidos o privados de una clase.

## **Método property**

Este decorador `property` corresponde al getter, es decir, accede al atributo para mostralo. Por ejemplo: 
```python
class Persona(object):
    def __init__(self, nombre):
        self.__nombre = nombre 


    @property
    def nombre(self):
        return self.__nombre

cliente = Persona('Juan')
print(cliente.nombre)

# Juan
```
Como vemos podemos acceder al atributo nombre aunque este se encuentre encapsulado (protegido) mediante el decorador @property. Este decorador nos permite acceder al método y que este nos retorne el atributo nombre, pero no accedemos a este directamente.


NOTA: este decorador es útil si queremos "trasformar" un método en un atributo.

## **Método setter**

El decorador `property.setter` nos permite setear un nuevo valor para un atributo, pero al ser un método el que modifica el valor tambien podríamos realizar otras operaciones además de reasignar el nuevo valor, por ejemplo, verificar este nuevo valor antes de asignarlo.
```python
class Persona(object):
    def __init__(self, nombre):
        self.__nombre = nombre 


    @property
    def nombre(self):
        return self.__nombre

    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != '':
            self.__nombre = nuevo_nombre
        else:
            print('El nombre debe ser diferente a ""')

cliente = Persona('Juan')
print(cliente.nombre)
cliente.nombre = 'Juan Cervera'
print(cliente.nombre)

# Juan
# Juan Cervera
```

## **Método deletter**

El método deletter nos permite como el nombre indica eliminar un atributo del objeto. Esto mediante el decorador @property.deleter
```python
class Persona(object):
    def __init__(self, nombre):
        self.__nombre = nombre 


    @property
    def nombre(self):
        return self.__nombre

    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != '':
            self.__nombre = nuevo_nombre
        else:
            print('El nombre debe ser diferente a ""')

    @nombre.delter
    def nombre(self):
        del self.__nombre

cliente = Persona('Juan')
print(cliente.nombre)
cliente.nombre = 'Juan Cervera'
print(cliente.nombre)
del cliente.nombre
print(cliente.nombre)

# Juan
# Juan Cervera
# Error. No existe una proiedad llamada nombre.
```
Como vemos el método deleter nos permite eliminar la propiedad de un objeto aunque esta se encuentre protegida.

