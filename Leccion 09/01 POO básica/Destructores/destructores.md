# Destructores

Los objetos en Python existen solo cuando están siendo referenciados, cuando no existe ninguna referencia al objeto Python automáticamente tiene un recolector de basura que se encarga de llamar al método `__del__` que se encarga de eliminar el objeto, esto con el objetivo de no sobrecargar la memoria. El programador también puede definir el método en una clase.

```python
class Usuario:
    def __init__(Usuario, name, lastname, age):
        Usuario.name = name
        Usuario.lastname = lastname
        Usuario.age = age
    
    def __del__(self):
        print('Objeto destruido')
```

Ahora tenemos disponible la keyword reservada `del` que podemos utilizar para destruir un objeto.

```python
usuario1 = Usuario('Juan', 'Carlos', 29)
del usuario1

# Objeto destruido
```

NOTA: si sus instancias están involucradas en referencias circulares, vivirán en la memoria mientras se ejecute la aplicación ya que Python no sabe el orden en el cual destruir los objetos.
