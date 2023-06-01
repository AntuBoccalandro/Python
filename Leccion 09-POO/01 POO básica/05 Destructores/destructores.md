# Destructores

Los objetos en Python existen solo cuando están siendo referenciados, cuando no existe ninguna referencia al objeto Python automáticamente tiene un recolector de basura que se encarga de llamar al método `__del__` que se encarga de eliminar el objeto, esto con el objetivo de no sobrecargar la memoria. El programador también puede definir el método en una clase.

```python
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
    
    def __del__(self):
        print('Object Destroyed')
```

Ahora tenemos disponible la keyword reservada `del` que podemos utilizar para destruir un objeto.

```python
person = Person('John', 'Williams', 1234, 29)
del person

# Object Destroyed
```

NOTA: si sus instancias están involucradas en referencias circulares, vivirán en la memoria mientras se ejecute la aplicación ya que Python no sabe el orden en el cual destruir los objetos.
