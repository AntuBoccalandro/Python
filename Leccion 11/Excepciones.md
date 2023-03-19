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

Para evitar lanzar un error al mitad de la ejecución del programa se puede realizar una afirmación que en caso de ser False se detenga la ejecución del programa y lanze una exepción de tipo: `AssertionError`. Las aserciones son una expresion booleana, si es verdadera el programa continua normalmente si es falso se lanza una excepcion, con un mensaje de manera opcional.

**Sintaxis**:
```python
assert <condition>, [message]
```

```python
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
```

**Otro ejemplo de asserts**:
```python
def comprobar_lista(lista_calificaciones):
    assert any(lista_calificaciones), 'The list of califications is empty'


lista_calificaciones = []
comprobar_lista(lista_calificaciones)

# AssertinError: The list of califications is empty
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


# Creación de una excepción

Si se quiere crear una excepción propia Python no los deja muy fácil. Simplemenete hay que crear una clase con el nombre de la excepción que queremos crear y luego esta clase heredará de Exception.

```python
class CustomException(Exception):
    pass
```
Dentro de la clase luego podríamos agregar el código que querramos para agregarle "funcionalidad" a la excepción. 

También se pueden crear excepciones personalizadas que hereden de otras excepciones como ValueError o ZeroDivision.

## Mejorando la excepción personalizada

```python
class MyHttpException(Exception):
    def __init__(self, code=500, message='Internal server error'):
        self.code = code
        self.message = message

try:
    raise MyHttpException
except MyHttpException as err:
    print(err)
```
En este caso creamos una excepción personalizada que nos permite capturar errores Http. Entonces creamos dos atributos por defecto llamados code (haciendo referencia al código de respuesta Http) y el atributo message. Al crear estos objetos podemos lanzar la excepción y mostrar tanto la excepción como sus valores independientes, entonces podríamos saber tanto el código re respuesta ante la que se lanza esta excepción como su mensage.

Además al ser una clase podremos modificar sus atributos y de esta manera hacer que la excepción sea aplicable a varias partes del código. 

```python
try:
    raise MyHttpException(code=404, message='Not found')
except MyHttpException as err:
    print(err.code)
    print(err.message)

# 400
# Not found
```

También es importante la genericidad de las excepciones, es decir, que una excepción sea bastante genérica para que luego creemos otras excepciones que hereden de esta.

# Resumen 

* `Try` le permite probar un bloque de código en busca de errores.
* `Except` le permite manejar el error.
* `Else` te permite ejecutar código cuando no hay ningún error.
* `Finally` le permite ejecutar código, independientemente del resultado de los bloques de prueba y excepción.
