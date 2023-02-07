# Decoradores

Los decordadores en Python son funciones que modifican el comportamiento de otras funciones. 


# Definir un decorador

Para definir un decorador se debe crear una función como cualquier otra que recibe como parámetro la función a decorar. Dentro del decordaro se debe crear una función más que será la que encapsulará a la función pasada como parámetro.

# Entendimiento de las funciones

Todo el Python es un objeto. Sabiendo esto podemos definir a una función como un objeto que hereda de la clase Object, de hecho una función tiene atributos!

```python
def my_function(a, b):
    return a + b

print(my_function.__name__)

# my_function
```
Como vemos hasta una función tiene atributos. En este caso mostramos el nombre de la función.

## Referencias Vs llamadas

Cuando hablamos de funciones no es lo mismo llamar a la función que referenciarnos. 
* Cuando llamamos a una función estamos ejecutando el bloque de código, obteniendo los resultados que esta retorne. Para llamar a una función es necesario utilizar el identificador de la misma seguida de sus parámetros, si es que tiene, encerrados entre paréntesis.
* Cuando referenciamos a una función estamos refiriendonos a la posición de memoria del objeto. Para referenciar a una función solo hace falta utilizar su identificador, que si a este le agregamos los paréntesis se convierte en una llamada a la función. 

**Comparativa**:
```python
def suma(a, b):
    return a + b

call = suma(2, 10)
instance = suma
call_again = instance(5, 10)

print(call, '\n', instance, '\n', call_again)

# 12 
# <function suma at 0x000002130C473E20> 
# 15
```
Como vemos cuando llamamos a la función por medio de su identificador y los paréntesis el valor de la suma se almacena en la variable `call`. Por otro lado vemos que cuando no utilizamos los paréntesis nos estamos referenciarnos a la función, dicho valor es almacenado en la variable `instance`. Por último volvemos a realizar una llamada a la función suma, pero no utilizando el identificador de la función directamente, si no utilizando la instancia previamente almacenada en la variable `instance`.

# Definiendo un decorador sin parámetros

Antes de definir un decorador es necesario conocer su estructura

## Estructura    

```python
def <external_function>(<function>):
    def <internal_function>():
        <code>
    return <function_instance>

@<external_function>
def <own_function>():
    pass

own_function()
```
Revisemos cada parte de un decorador:
* Función externa: es la función que contiene al decorador. La función externa recibe como parámetro a la función que se está decorando.
  * Retorno de la instancia: retorna la instancia de la función decorada, para que luego se pueda llamar a la función decorada con las modificaciones.
* Función interna: es la función que realiza la acción en sí, es decir, la modificación de la función decorada.
  * Código: es el contenido de la función como tal. 

Lo que llamo a las funciones internas también se las llama envolventes, porque envuelven a la función que se está modificando.

## Ejemplo sin parámetros en la función decorada

```python
def external_function(function):
    def internal_funcion():
        print('Inicio del decorador')
        function()
        print('Fin del decorador')
    return internal_funcion


@external_function
def function():
    print('Función decorada')


function()

# Inicio del decorador
# Función decorada
# Fin del decorador
```
Como vemos cuando decoramos la función se muestran las modificaciones, como los dos mensajes de Inicio del decorador y Fin del decorador. Entre medio de los dos mensajes se encuentra la función decorada, que al ejecutarse se imprime el mensaje Función decorada. 

## Diagrama de funcionamiento de un decorador

![](https://i.ibb.co/hHRYj55/image.png)


## Ejemplo con parámetros en la función decorada

```python
def only_pairs(function):
    def pairs(a, b):
        if a % 2 == 0 and b % 2 == 0:
            return function(a, b)
        return -1
    return pairs


@only_pairs
def suma(a, b):
    return a + b


print(suma(2, 9))
print(suma(2, 4))

# -1 
# 6
```
En este ejempo en decorador only_pairs modifica la función para que solo si los parámetros a y b son pares ejecute la función. La función puede realizar cualquier acción con los parámetros, pero al utilizar el decorador only_pairs esto hace que se modifique la función decorada.


# Definiendo un decorador con parámetros

Un decorador con parámetros es aquel que puede recibir parámetros, esto con el fin de que el decorador implemente alguna característica que no tenga que ver con los parámetros de la función decorada.

## Estructura

```python
def <decorator_name>(<parameter>):
    def <real_decorator>(<function>):
        def <wrapper>(<function_params>):
            return <result>
        return <wrapper>
    return <real_decorator>
```

## Ejemplo

```python
from functools import reduce


def only_pairs(maxsize):
    def decorator(function):
        def wrapper(lista):
            pairs = list(filter(lambda item: item % 2 == 0, lista))
            result = function(pairs)
            return maxsize if result >= maxsize else result
        return wrapper
    return decorator



@only_pairs(maxsize=100)
def multiplicar(lista):
    return reduce(lambda acum, item: acum * item, lista)


print(multiplicar([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 100
```
Como vemos retorna 100 en vez de 384 porque en el parámetro del decorador indicamos que el tamaño máximo sea de 100 por lo que si el resultado exede dicho resultado se mostrará el valor máximo y no el real de la multiplicación.

