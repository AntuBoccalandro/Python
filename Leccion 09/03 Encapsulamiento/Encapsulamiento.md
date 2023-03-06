# **Encapsulamiento**

La encapsulación es uno de los pilares de la programación ortientada a objetos. Nos permite regular el acceso a los métodos y atributos de una clase. En cierta manera, enmascara la complejidad de una clase. 

# Modificadores de acceso

Los modificadores de acceso son justamente modificadores que me permiten regular el acceso de ciertos atributos y métodos de la clase. Se pueden dividir en tres tipos:

* **Públicos**: son accesibles desde cualquier punto del programa. Dentro y fuera de la clase y sus subcalses. Se define con la siguiente sintaxis `attribute = value`. 
* **Protejidos**: son accesibles porla misma clases, sus subclases y dentro del mismo paquete. Se define con la siguiente sintaxis `_attribute = value`.
* **Privados**: son accesibles únicamente dentro de la misma clase. Este tipo de clases no permite que podamos crear subclases ya que sus atributos y métodos son únicamente accesibles desde la misma clase y no desde otras. Se define con la siguiente sintaxis `__attribute = value`. 

# Ejemplos de encapsulamiento

## Atributos públicos

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

## Atributos protejidos

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

## Atributos privados

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
person.see_datails()

# Error
```

# ReadOnly
