# Excepciones y manejo de errores

# Traceback

Un traceback es un informe que contiene las llamadas a funciones realizadas en su código en un punto específico. Los rastreos se conocen por muchos nombres, incluidos stack trace , stack traceback , backtrace y quizás otros. En Python, el término utilizado es traceback .

Cuando su programa da como resultado una excepción, Python imprimirá el traceback actual para ayudarlo a saber qué salió mal. 

# Lectura de los Traceback

Lo ideal es leerse de abajo hacia arriba:

![](https://translate.google.com/website?sl=en&tl=es&hl=es-419&u=https://files.realpython.com/media/python_traceback_2.b27a4eb060a8.png)

* El recuadro azul contiene la excepción que se ejecuta.
* El recuadro verde contiene el el mensaje de la excepción.
* El recuadro rojo contiene el código que se ejecutó.
* El recuadro amarillo contiene el número de línea y el nombre del módulo, que especifican dónde se puede encontrar el código.

# Lista de los Traceback más frecuentes


## AttributeError

> Se genera cuando falla una referencia de atributo o una asignación.

```python
an_int = 1
an_int.an_attribute

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'an_attribute'
```

## ImportError

> Se genera cuando la declaración de importación tiene problemas para intentar cargar un módulo. También se genera cuando la 'from list' import tiene un nombre que no se puede encontrar.

```python
import asdf

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'asdf'

from collections import asdf
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'asdf'
```

## IndexError

> Se genera cuando un subíndice de secuencia está fuera de rango.

```python
a_list = ['a', 'b']
a_list[3]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

## KeyError

> Se genera cuando no se encuentra una clave de asignación (diccionario) en el conjunto de claves existentes.

```python
a_dict['b']

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'b'
```

## NameError

> Se genera cuando no se encuentra un nombre local o global. 

```python
def greet(persn):
    print(f'Hello, {person}')
greet('World')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in greet
NameError: name 'person' is not defined
```

## SintaxError

> Se genera cuando el analizador encuentra un error de sintaxis.

Cuando se encuentra el error de sintaxis Python indica donde está el error con un signo ^ como ayuda extra para detectar el lugar del problema.

```python
def greet(person)

  File "<stdin>", line 1
    def greet(person)
                    ^
SyntaxError: invalid syntax
```

## TypeError

> Se genera cuando se aplica una operación o función a un objeto de tipo inapropiado. 

```python
a = 1 + '1'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

## ValueError

> Se lanza cuando una operación o función recibe un argumento que tiene el tipo correcto pero un valor inapropiado, y la situación no está descrita por una excepción más precisa como IndexError.

```python
a, b, c = [1, 2]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 3, got 2)
```
