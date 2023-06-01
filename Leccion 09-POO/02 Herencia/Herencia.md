# **Herencia**

La herencia es uno de los pilares fundamentales de la programación orientada a objetos que consiste en heredar los atributos y métodos de una clase padre a una clase hija.

Para definir una clase que herede de otra es necesario colocar unos paréntesis en la clase hija el nombre de la clase que queremos que esta herede.

NOTA: Si no redefinimos el método init en las subclases el método constructor que utilizará la subclase será herederada de la clase padre.

```python
class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def presentation(self):
        print(f'Hi, I am {self.name} and i {self.age} years old.')


class Employee(Person):
    def __init__(self, name, age, id, salary, position, company):
        super().__init__(name, age, id)
        self.salary = salary
        self.position = position
        self.company = company

    def anual_salary(self):
        return self.salary * 12


class Student(Person):
    def __init__(self, name, age, id, college, course, subjects):
        super().__init__(name, age, id)
        self.college = college
        self.course = course
        self.subjects = subjects

    
    def see_subjects(self):
        return self.subjects


john = Person('John', 29, 1234)
print(john.id)
# Hi, I am John and i 29 years old.

worker = Employee('Johny', 39, 123, 10000, 'Software Engineer', 'Google')
print(worker.anual_salary())
# 120000

student = Student('William', 29, 123, 'uasd', 9, ['item1', 'teim1', 'item3'])
print(student.see_subjects())
# ['item1', 'teim1', 'item3']
```

## Método super

En pocas palabras, la función `super()` nos permite acceder a los métodos de la clase padre desde una de sus hijas


## Verificar clases y subclases

Las subclases son aquellas clases que heredan de otras clases, estas denominadas clases padre.

Si queremos saber si una clase hereda de otra clase podemos utilizar los metodos `__bases__` y `__subclasess__`. 

```python
print(Person.__bases__)
# (<class '__main__.Person'>,)
```

```python
print(Empoyee.__subclasses__())
# [<class '__main__.Person'>]
```
Como vemos nos muestra 

## Tipos de herencia

* Herencia simple
* Herencia múltiple
* Herencia multinivel

# Herencia Simple

Consiste en una o varias subclases que heredan de la misma clase padre. Por ejemplo:

```python
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    
class Student(Person):
    def __init__(self, name, lastname, age, university):
        Person.__init__(self, name, lastname, age)
        self.university = university


class Employee(Person):
    def __init__(self, name, lastname, age, stand):
        Person.__init__(self, name, lastname, age)
        self.stand = stand



print(f'''
    Person is a subclass? {issubclass(Person, Person)}
    Studdent is a subclass? {issubclass(Student, Person)}
    Employee is a subclass? {issubclass(Employee, Person)}
''')

# Person is a subclass? True
# Studdent is a subclass? True
# Employee is a subclass? True
```
Como vemos todas son subclases, Student hereda de Person y Employee hereda también de Person. Pero si Person dice que es una subclase pero no estamos heredando de nada  ¿Por qué sucede esto? Esto se debe a que todas las clases en Python heredan indirectamente de la clase Object, es por eso que aunque no indiquemos que cualquier clase herede de Object estas lo hacen de igual forma.

# Herencia Múltiple

La herencia múltiple es aquella en la que una subclase hereda de dos o más clases padres, obteniendo todas las propiedades de estas.

```python
class Base1:
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name

class Base2:
    def __init__(self, lastname):
        self.lastname = lastname
        
    def getLastname(self):
        return self.lastname

class MultiDerived(Base1, Base2):
    def __init__(self, name, lastname, age):
        Base1.__init__(self, name)
        Base2.__init__(self, lastname)
        self.age = age
        
    def getAge(self):
        return self.age


base1 = Base1('John')
base2 = Base1('Williams')
MultiDerived1 = MultiDerived('John', 'Williams', 23)

print(base1.getName())
print(base2.getLastname())
print(MultiDerived1.getName())

# John
# Williams
# John 
``` 
Como vemos la subclase MultiDerived hereda de Base1 y Base2, como consecuencia de esto los métodos y atributos de estas clases son heredados MultiDerived. Al crear la instancia de esta clase como vemos nos pide los parámetros name, lastname y age. De los cuales name y lastname fueron heredados de Base1 y Base2, en el caso del atributo age este es creado en esta subclase y no pertenece a las clases padre.

# Herencia Multinivel

La herencia multinivel consiste en una clase padre de la que derivar diferentes subclases que se van heredando sus propiedades una con otra.

```python
class Base:
    def __init__(self, atr1):
        self.atr1 = atr1


class Derived1(Base):
    def __init__(self, atr1, atr2):
        super().__init__(atr1)
        self.atr2 = atr2


class Derived2(Derived1):
    def __init__(self, atr1, atr2, atr3):
        super().__init__(atr1, atr2)
        self.atr3 = atr3


base = Base(1)
derived1 = Derived1(1, 2)
derived2 = Derived2(1, 2, 3)


print(Derived2.__mro__)

# (<class '__main__.Derived2'>, 
# <class '__main__.Derived1'>, 
# <class '__main__.Base'>, 
# <class 'object'>)
```
Como vemos podemos ver la jerarquía de clases gracias al método `mro`. Este método nos permite ver que clases derivan de otras.

