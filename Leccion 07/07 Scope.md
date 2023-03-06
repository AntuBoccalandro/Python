# Scope

Cuando hablamos del scope nos referimos al alcance que tienen las variables. Es decir, si tienen un alcance local o global.

# Local scope

Las variables de alcance local son aquellas definidas dentro de una función. Estas no pueden ser accedidas desde fuera de la función y se limitan a solo poder ser accedidas y modificadas desde esa función.


```python
var = 10

def function():
    var = 20
    print(f'{var} -> {id(var)}')

function()
print(f'{var} -> {id(var)}')

# 20 -> 1631910363984
# 10 -> 1631910363664
```
Como vemos a pesar de que definimos una variable llamada `var` fuera y dentro de la función, el valor de la variable `var` no es modificada por la función, ya que la variable `var` de dentro de la función no es la misma que la de fuera. La variable dentro de la función es de local scope y la de fuera de la función representa una variable global, es decir, tiene un global scope. Para terminar, como podemos ver loss identificadores de cada variable son diferentes, esto nos dice que se trata de variables diferentes.

Esto se puede observar mejor por medio de los identificadores de la variable.
```python
var = 10

def function():
    global var
    var = 20
    print(var)

function()
print(var)

# 20 -> 1899907908432
# 20 -> 1899907908432
```
A diferencia del caso anterior podemos observar que al declarar como global la variable `var` dentro de la función esta se comportará como una variable que no está fuera de la función, por lo que desde fuera de la función podemos acceder a su valor. Adicionalmente vemos que ahora al declarar `var` dentro de la función como global y al la variable tener el mismo nombre que la anteriormente variable declarada `var` fuera de la función, sobreescribimos su valor. Para terminar vemos que los identificadores de las dos variables son el mismo, esto nos dice que además de tratarse de la misma variable estan en el mismo ámbito, ya que si no no serían la misma, como pasa en el ejemplo anterior.

# Global scope

Las variables de alcance global son aquellas que son definidas para todo el programa. Es decir, son accesibles por todo el programa.

## Modificador global

Si se quiere definir una variable global dentro de una función puedes utilizar la keyword `global` que permite definir una variable dentro de una función, que originalmente sería de alcance local pero es "convertida" en una de alcance global. La sintaxis de este modificador consiste en utilizar la keyword global, especificar la variable que queremos cambiar su scope a global y luego, en otra línea, podremos definir el valor de la variable. Algo que sin duda podrían mejorar en Python, es una manera de declarar variables globales o no-locales en una sola línea sin la necesidad de utilizar dos para este proceso.

**Comparativa entre una función con una variable de local-scope y una convertida a global-scope**:
```python
def function():
    var = 20
    print(var)


function()
print(var)

# NameError
```
Se produce un error porque la variable `var` no está definida fuera de la función.

```python
def function():
    global var
    var = 20


function()
print(var)

# 20
```
Vemos el valor 20 ya que la variable `var` es tiene un alcance global y puede ser accedida desde fuera de la función.


# Funciones anidadas

Si definimos una variable local dentro de la función A podremos acceder a ella desde la función anidada B, pero solo para leerla. Si queremos modificar su valor tendremos que utilizar el modificador nonlocal. Sucede exactamente lo mismo cuando queremos modificar una variable global desde dentro de una función. Dicho con otras palabras una variable local actúa como variable global para las funciones anidadas dentro de su mismo contexto.

```python
def main_function():
	var = 10

	def internal_function():
		var = 20
		print(f'Valor en función anidada es {var}')

	print(f'var en función padre antes es {var}')
	internal_function()
	print(f'var en función padre después es {var}')

main_function()

# var en main_function antes es 10
# var en internal_function es 20
# var en main_function después es 10
```
Analicemos los resultados. Como vemos el valor de var antes es 10, el valor que hemos definido en un principio, mostramos entonces dicho valor por pantalla. Luego se llama a la función internal_function, esta muestra el valor de la variable var, que es definida con el valor de 20, mostramos dicho valor por pantalla. Por útltimo mostramos el valor de var por otra vez, pero obtenemos el valor de 10 por pantalla y no 20, porque? Esto se debe a que las funciones hijas dentro de las funciones padre solo pueden leer los valores de las variables definidas por la función padre, pero no modificarlos, es por esto que cuando mostramos el valor de var definida en internal_function obtenemos el valor de 20 y luego cuando volvemos a mostrar el valor de la variable el valor de 10, porque no se esta sobreescribiendo la variable, en verdad var definida en main_function e internal_function se tratan de variables diferentes, con un distinto alcance.

## Modificador nonlocal

El modificador nonlocal al igual que global primero se modifica su scope y luego se define su valor. Este modificador hace que la variable que estamos especificando no sea local y sea global. En el caso de funciones anidadas el definir una variable como nolocal significa que es global, pero solo en el alcance de la función padre que la contiene.

```python
def main_function():
	var = 10

	def internal_function():
		nonlocal var
        var = 20
		print(f'Valor en función anidada es {var}')

	print(f'var en función padre antes es {var}')
	internal_function()
	print(f'var en función padre después es {var}')

main_function()

# var en main_function antes es 10
# var en internal_function es 20
# var en main_function después es 20
```
Como vemos esta vez si se modifica el valor de la variable var ya que le estamos diciendo que esta no sea local (nonlocal) por lo que al tener el mismo nombre que la var definida en main_function esta se ve sobreescrita, viendo por pantallas nosotros dos veces el valor de 20.

# Función globals y locals

En Python la función globals() devuelve el diccionario que contiene todas las variables del ámbito global actual. Se puede usar este diccionario para acceder al valor de dichas variables y modificarlo.

La función locals() en Python devuelve un diccionario que contiene todas las variables del ámbito local actual. Se puede utilizar para acceder al valor de las variables locales pero no para modificarlas, pues es un diccionario de solo lectura.

```python
var = 10

def function():
	var = 20
	print(f'La variable local var es {locals()["var"]}')
	print(f'La variable global var es {globals()["var"]}')

function()
globals()['var'] = 30
print(f'La variable global var es ahora {var}')

# La variable local valor es 20
# La variable global valor es 10
# La variable global valor es ahora 30
```
Como vemos mediante el uso de la función globals y locals y los diccionarios que estas retornan, podemos modificar los valores de las variables globales y locales. En el ejemplo podemos observar primero mostramos el valor de la variable var en su ámbito local, luego mostramos la variable var de ámbito global y por último mostramos el valor de la variable var pero esta siendo antes modificada por medio de la función globals y modificando el valor de la variable var almacenada en el diccionario de variables globales.

