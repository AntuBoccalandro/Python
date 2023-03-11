# Objetos

Un objeto  es una instancia de una clase. Una clase es como un modelo, mientras que una instancia es una copia de la clase con valores reales. Para crear un objeto es necesario tener una clase anteriormente definida para poder crear un objeto con las características bases que esta incluye. 

Un objeto se crea a partir de la creación de una variable que será el nombre con el cual nos referiremos al objeto, seguida de la referencia a la clase y la serie de atributos. Veámoslo en código.

Clase modelo Person:
```python
class Person:
    name = 'John'
    lastname = 'Williams'
    age = 29
```

Creación de un objeto:
```python
person = Person()
```

Mostrar los atributos del objeto `person`:
```python
print(person.name, person.lastname, person.age)

# John Williams 29
```
Como vemos hemos creado la clase `Person` que tiene una serie de atributos definidos: name, lastname y age. Estas son variables al fin al cabo, que inicializamos con un valor. Pero dijimos que la funcionalidad de las clases es la de crear objetos que tengan atributos personalizados y diferentes para cada uno de ellos. Esto es posible pero para ello tenemos que conocer a los métodos constructores que permiten crear un objeto que para ser creado debamos pasarle como parámetros los atributos que queremos que esta instancia tenga.
