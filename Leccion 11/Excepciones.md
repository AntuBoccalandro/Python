# Excepciones

Python termina de ejecutar un programa tan pronto encuentra un error.

## Excepciones VS Errores de sintaxis

Los errores de sintaxis se dan cuando el intérprete de Python detecta una declaración incorrecta. Por ejemplo: un paréntesis de más o de menos.

Las excepciones en cambio son declaraciones sintáticamente correctas pero que generar un error, este ocurrido por la mala lógica del programa o intentar realizar acciones incorrectas. Ejemplos de excepciones podrían ser: divición por cero, sumar un string con un integer, etc. Además las excepciones pueden ser definidas por el usuario a diferenia de los errores de sintaxis. Python al encontrar un error lanza una excepción correspondiente de la lista de excepciones. 

# Generación de una excepción personalizada

Si se quiere lanzar una excepción ante una condición se puede utiliza la palabra reservada `Exception` a continuación se debe describir la excepción para mostrar el error y así solucionarlo.

```python
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
```

# Realizar una afirmación

Para evitar lanzar un error al mitad de la ejecución del programa se puede realizar una afirmación que en caso de ser False se detenga la ejecución del programa y lanze una exepción de tipo: `AssertionError`.

```python
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
```

# Manejo de excepciones

## Cláusula try-except

Sintáxis:
![](https://translate.google.com/website?sl=en&tl=es&hl=es-419&u=https://files.realpython.com/media/try_except.c94eabed2c59.png)

La sentenca try indica que en caso de ser verdadera se ejecute el bloque de código. En caso de haber algún error se ejecutará el bloque except. Cabe aclarar que si el bloque except incluya una condición de error para ejecutarse y no sea la excepción que lanzé el bloque try se lanzará directamente la expeción y no se ejecutará el bloque except.

Ejemplo práctico:
```python
import sys

def only_run_linux():
    assert ('linux' in sys.platform), 'This code runs on Linux only.'

try:
    only_run_linux()
except:
    print('Error')
```

Un ejemplo utilizando excepciones:
```python
import sys

def only_run_linux():
    assert ('linux' in sys.platform), 'This code runs on Linux only.'

try:
    only_run_linux()
except AsessertionError as error:
    print(error)
```

Otra ejemplo pero esta vez utilizado varias cláusulas `except`:
```python
try:
    only_run_linux()
    with open('file.txt') as file:
        print(file.read())
except FileNotFoundError as fnf:
    print(fnf)
except AssertionError as error:
    print(error)
```
En este código hay dos sentencias except por lo que en caso de no encontrarse el archivo se ejecuta la primer línea y en caso de que el archivo esté pero se esté ejecutando el programa en un sistema que no sea Linux se ejecutará el segundo bloque except.

## Cláusula else

Sintaxis:
![](https://translate.google.com/website?sl=en&tl=es&hl=es-419&u=https://files.realpython.com/media/try_except_else.703aaeeb63d3.png)

La cláusula else se ejecutará solo cuando no haya ninguna excepción, por lo que se incluye luego de una cláusula except.

Ejemplo práctico:
```python
try:
    only_run_linux()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
```

## Cláusula finnaly

Sintaxis:
![](https://translate.google.com/website?sl=en&tl=es&hl=es-419&u=https://files.realpython.com/media/try_except_else_finally.a7fac6c36c55.png)

La cláusula finnaly sirve para ejecutar un bloque de código. Este bloque de código se ejecutará sin importar el código anterior.

Ejemplo práctico:
```python
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
```

# Resumen

* El trybloque le permite probar un bloque de código en busca de errores.
* El exceptbloque le permite manejar el error.
* El elsebloque te permite ejecutar código cuando no hay ningún error.
* El finallybloque le permite ejecutar código, independientemente del resultado de los bloques de prueba y excepción.