# Closures

Un closure o clausura permite acceder al ámbito de una función exterior desde una función interior. Es decir, si tenemos una función externa que envuelve a una interna y esta recibe por lo menos un parámetro, el hecho de poder acceder a dicho parámetro desde la función interna se conoce como closure. Básicamente la función interna utiliza las variables declaradas en la función externa (la que la contiene).


**Ejemplo**:
```python
def external_function(message):
    upper_message = message.upper()
    def internal_function():
        print(message, upper_message)
    return internal_function

instance = external_function('Hello!')
instance()

# Hello, HELLO
```
En este ejemplo la función externa recibe un mensage que luego es accedido desde la función interna. Además la función externa declara una variable llamada upper_message que también es accedida desde la función interna. 

Es importante saber que si bien la función interna puede acceder a los valores de las variables definidas en la función externa no los puede modificar. Ahora veremos un ejemplo del tipo de error que podríamos obtener al realizar este tipo de acciones.

**Ejemplo**:
```python
def external_function(message):
    def internal_function():
        message = message.upper()
        print(message)
    return internal_function

instance = external_function('Hello!')
instance()

# UnboundLocalError: local variable 'message' referenced before assignment
```
Como vemos obtenemos un error que nos indica que la variable message está referenciada antes de la asignación. Y es que para modificar esta variable message deberíamos especificar que el valor de la variable que queremos modificar no es local. Como veremos a continuación.

```python
def external_function(message):
    def internal_function():
        nonlocal message
        message = message.upper()
        print(message)
    return internal_function

instance = external_function('Hello!')
instance()

# HELLO!
```
Como vemos no obtenemos un error y la variable mensage es modificada por la función interna. Pero este tema va más relacionado a los scopes de la variables y no tanto a los closures, aunque es necesaria su combinación a veces.

# Uso de closures con funciónes lambda

Se puede definir una función lambda que sea retornada por otra función que la envuelva. Esto sigue el mismo concepto de closure pero de una manera ligeramente diferente.

```python
def mostrar(titulo):
    return lambda nombre_persona: print(titulo + ' - ' + nombre_persona)

mostrar_ing = mostrar('Ingeniero')
mostrar_ing('Carlos Lara')

# Ingeniero - Carlos Lara
```
Lo que estpa sucediendo aquí es que primero creamos una instancia de la función externa `mostrar` a la que le pasamos un parámetro. Luego la función lambda interna es llamada cuando instanciamos `mostrar_ing` y le pasamos como parámetro del nombre de la persona. El concepto de closure se aplica porque estamos accediendo a los valores globales de la función externa desde la función interna.

