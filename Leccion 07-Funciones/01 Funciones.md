# Funciones

Las funciones son bloques de código que permite ser llamada en cualquier parte del programa. Esto permite la reutilización de un bloque de código varias veces sin la necesidad de repetir las misma sentencias. Las funciones permiten ahorrar muchas líneas de código ya que permiten no repetir código que se utiliza varias veces en un programa.

## Definición de funciones

Las funciones en Python se definen de la siguiente manera:

```python
def <function_name>(<parameter1, parameter2......parameterN>):
  <code>
```

* El nombre de la función corresponde al identificador con el cual podremos llamar a la función, igual que pasa con las variables.
* Los parámetros son una lista de uno o más argumentos que vienen siendo los datos de entrada que recibe la función para operar con ellos.
* El código de la función es básicamente el cuerpo de la función, las operaciones que se realizar dentro del bloque de código al igual que pasa con las sentencias condicionales y loops.

**Ejemplo**:
```python
def suma(a, b):
  print(a + b)
```

## Llamada de funciones

La llamada de funciones corresponden a ejecutar la función. Es decir, si creamos una función y nunca la llamamos esta no se utilizará nunca, al llamar una función lo que estamos haciendo es ejecutar todas las istrucciones que se encuentren dentro de esa función.

**Sintaxis**
```python
<function_name>(<argument1, argument2......argumentN>)
```

**Ejemplo:**
```python
def suma(a, b)
  print(a + b)

suma(10, 20)

# 30
```
NOTA: en el ejemplo se ve como se crea una función llamada suma que tiene como argumento a y b. Adicional a ello el código de la función lo que hace es imprimir la suma de a y b. Luego llamamos a la función y le pasamos como argumentos 10 y 20, estos números se asignarán a los parámetros a y b de la función. El valor de salida de la función es 30. 

## Argumentos 

### **Argumentos fijos**: 
es cuando en una función se definen una cierta cantidad de parámetros, cuando llamemos a la función deberemos pasar esta cantidad de parámetros ya que si no obtendremos un error del tipo: `missing 1 requiered argument`.

* **Sintaxis**:
  ```python
  <<functions_name>>(<argument1, argument2......argumentN>)
  ```

* **Ejemplo**:
  ```python
  def suma(a, b)
    print(a + b)

  suma(10, 20)

  # 30
  ```
NOTA: se definen en la función los parámetros a y b, cuando llamamos a la función debemos pasarle estos dos argumentos, sin estos la función no se ejecutará y obtendremos un error. 

En el caso de pasar variables como argumentos de la función no será necesario que el nombre de estas coincida con el nombre de ,os parámetros de la función, lo importante es que la función reciba la cantidad de argumentos justa.

### **Argumentos de < clave >=< valor >**: 
este tipo de argumentos consiste en colocar como argumento el nombre del parámetro que recibe la función y luego si valor, por ello < clave >=< valor >.

* **Sintaxis**: se detalla la sintaxis a la hora de la llamada de la función y paso de argumentos.
  ```python
  <function_name>(<key1>=<value1>, <key2>=<value2>......<keyN>=<valueN)
  ```

* **Ejemplo**:
  ```python
  def suma(a, b)
    print(a + b)

  suma(a=10, b=20)

  # 30
  ```
NOTA: en este caso es necesario colocar el nombre de la clave con el mismo nombre del argumento de a función, si no obtendremos un error de tipo: `suma() have an argument of key-value inesperated ""`.

Si se tiene una combinación de argumentos fijos y de < clave >=< valor >, los argumentos fijos deberán ir primero que los argumentos de < clave >=< valor >.

```python
# Bad form
def suma(a, b)
  print(a + b)

suma(a=10, 20)

# Good form
def suma(a, b)
  print(a + b)

suma(20, b=10)
```

## **Parámetros por defecto**: 
si en los parámetros de la función se colocan parámetros de tipo < clave >=< valor > este corresponderá a un valor por defecto que tendrá la función.

```python
def suma(a=10, b=20):
  print(a + b)

suma()

# 30
```
NOTA: como vemos auque no le pasemos los parámetros a y b la función se ejecuta sin problemas, eso es porque en verdad ya tienen definidos valores por defecto para a y b por lo que no necesita argumentos si ya los tiene. Si se deseara cambiar los valores de a o b bastaría con pasar como argumento un objeto con el nuevo valor que se quiere para el parámetro por defecto.

## **Argumentos de longitud variable**: 
son útiles cuando no se sabe la cantidad de argumentos que va a recibir la función. Hasta ahora la cantidad de arguntos debía coincidir con la cantidad de argumetnos de la llamada de la función, pero los argumentos de longitud variable permiten solucionar este problema.

* **Sintaxis**:
  ```python
  def <function_name>(*<argument_name>):
    <code>
  ```
* **Ejemplo**:
  ```python
  def fun(*args):
    print(args)

  fun('Matemática', 'Física', 'UTN')

  # ('Matemática', 'Física', 'UTN')
  ```
  NOTA: al agregar el asterísco delante del nombre del parámetro logramos que la cantidad de parámetros de la función varíe con respecto a la cantidad de argumentos que le pasemos. En el ejemplo se ve que pasamos 3 argumentos pero nos lo tenemos definida esa cantidad de parámetros, podríamos pasarle 500 argumentos si queremos.

Es importante saber que al pasar los argumentos a la función estos se convierten en una tupla, por lo que si queremos operar con ellos debemos tener en cuenta el tipo de dato con el cual estamos trabajando.

Una aplicación de este tipo de argumentos es calcular el promedio de la suma de n datos:

```python
def average(*n):
  average = sum(n) / len(n)
  print(average)

average(1,2,3,4,5,6,7,8,9,10)

# 5.5
```
Es interesante conocer que cuando uno pasa argumento variables lo que hace Python internamente es desempaquetar la secuencia de argumentos pasada para obtener un resultado como el que haríamos manualmente:

```python
# Lo que hacemos
def fun(*n):
  pass

# Lo que pasa internamente con el compilador de Python
def fun(X1, X2, X3, X4......Xn:
  pass
```

## **Argumentos variable de clave-valor**: 
es similar a los argumentos variables anteriormente vistos pero esta sintazis diferente se reserva para recibir una cantidad indeterminada de argumentos de clave-valor, estos se almacenan en forma de diccionario por lo que será necesario concer las propiedades de estos para realizar operaciones.

* **Sintaxis**:
  ```python
  def <function_name>(**<argument_name>)
    <code>
  ```
  Los dos asteriscos `**` indican que los parámetros de la función son de tipo < clave-valor > y variables.

* **Ejemplo**:
  ```python
  def names(**names):
    for i in zip(names.keys(), names.values()):
      print(f'Key=>{i[0]} Value=>{i[1]}')

  names(name1='Juan', name2='Carlos', name3='Jhon')

  # Key=>name1 Value=>Juan
  # Key=>name2 Value=>Carlos
  # Key=>name3 Value=>Jhon
  ```
  NOTA: en el ejemplo se puede ver como a partir de una cantidad de nombres estos se almacenan en un diccionario al que luego se accede a cada calve y valor para mostrarlo en pantalla.

## Orden de los argumentos de la función

El orden de los argumentos de una fnción es importante ya que podríamos tener errores a la hora de ejecutar nuestras funciones. Se pueden combinar los diferentes tipos de argumentos pero no se puede utilizar todos de cualquier manera, deben seguir un orden:
  *  Argumentos fijos o estándar
  *  *args
  *  **kwargs

Ejemplo:
```python
# Good form
def fun(a, b, *c, **d):
  pass

# Bad form
def fun(**a, b, *c, d):
  pass

```

## Especificar el tipo de dato de los parámetros

Si se desea especificar el tipo de dato de los parámetros Python tiene una forma muy sencilla.

**Sintaxis**:
```python
def <function_name>(<argument_name>:<datatype>)
  <code>
```
NOTA: si se ingresa otro tipo de dato del especificado la función se ejecutará sin errores pero si se especifica el tipo de dato es porque si se ingresa otro la función podría fallar o no retornar valores correctos.

**Ejemplo**:
```python
def suma(a:int, b:int)
  suma = a + b 
  return suma

print(suma(10, 20))

# 30
```
Especificar el tipo de dato de los parámetros resulta en una mejor función, además que a la hora de realizar la llamada a la misma podremos ver el tipo de dato de cada argumento que necesita la función.

## Retorno de una función

El retorno de una función consiste en un valor o varios que retorna la función. Para ello se utiliza la palabra reservada `return` que corta la ejecución del código dentro de la función y retorna el valor o variable que se haya definido.

**Sintaxis**:
```python
def <function_name>(<argument_name>)
  <code> 
  return <value>
```
NOTA: el valor que se retorna puede ser simplemente un número o una variable.

**Ejemplo**:
```python
def suma(a, b)
  suma = a + b 
  return suma

print(suma(10, 20))

# 30
```

NOTA: como vemos se define la función con el nombre de suma y luego se suman sus dos parámetros y se retorna el valor de la variable suma. Si no se utiliza la función print() nunca veremos el valor que retorna la función. Los valores que retorna la función no se imprimen en pantalla.

## Especificar retorno

Si bien no es necesario especificar el tipo de dato que retorna la función, si es una buena práctica utilizarlo ya que permite saber el dato que se espera de la función. Además cuando llamemos a la función además de los parámetros de la función veremos el tipo de dato que retorna.
**Sintaxis**:
```python
def <function_name>(<argument_name>) -> <datatype>
  <code> 
```
NOTA: el nombre del tipo de dato debe estar escrito de la forma abreviada, tales como: `int`, `str`, `list`, etc.

**Ejemplo**:
```python
def suma(a, b)-> int
  suma = a + b 
  return suma

print(suma(10, 20))

# 30
```
## Importación de funciones

Las funciones así como las librerías o clases se pueden importar, es decir, utilizar las funciones de un archivo en otro diferente.

```python
from <filename> import <function_name>
```

El código anterior muestra la importación de una función desde un archivo. La palabra `from` indica el archivo desde donde vamos a importar la función e `import <function_name>` permite importar la/s funciones que se quieran importar.

A contuación se detalla las diferentes opciones de importar una o varias funciones de un archivo.

* **Importar una función de un archivo**
  ```python
  from my_functions import function
  ```
* **Importar varias funciones de un archivo**
  ```python
  from my_functions import function1, function2, function3
  ```
* **Importar todas las funciones de un archivo**
  ```python
  from my_functions import *
  ```
* **Importar el archivo completo**
  ```python
  import my_functions
  ```

## Recibir funciones como parámetros

Al igual que podemos utilizar variables como argumentos de la función, también podemos recibir funciones como parámetros. Esto si te das cuenta tiene lógica. Las funciones al igual que las variables tienen un identificador (el nombre de la función o el nombre de la variable) con el cual podemos referirnos. 

**Ejemplo**:
```python
def fun(x, double):
  return double(x)

def double(x):
  return x * 2

fun(10, double)

# 20 
```

Como vemos tenemos dos funciones. La primera, fun() recibe como argumentos una variable x y lo que parecería ser una variable pero es la función double, anteriormente declarada. La función fun retorna el resultado que retorna la función double(x). Tambien declaramos otra funcion llamada double() que recibe como argumento a x y retorna su doble. Por último, cuando llamamos a la función fun() le pasamos el valor de x y el nombre de la función. Como resultado obtenemos 20. 

En este ejemplo no tiene sentido separar en dos funciones estas acciones tan sencillas, pero es muy útil para funciones grandes. Aunque no es una práctica muy recomendable porque estamos creando una función que depende de una o más funciones. Por lo que si hubiese algún error en cualquiera de las funciones de la que dependa la principal se produciría un error. Además de que no es modularizable fácilmente.

## Funciones anónimas

Las funciones anónimas son solamente funciones que no tienen un identificador con el cual nosotros podamos llamar a esa función. En Python este concepto se lo une con las lambda fuctions. El nombre de la keyword `lambda` viene dado por las matemáticas. 

**Sintaxis**:
```python
lambda <arguments>: <expresion>
```

**Ejemplo**:
```python
x = 10
lambda x: x * 2

# 20
```
Como vemos la expresión retorna 20, esto porque la función recibe como parámetros a x, luego la expresión dentro de la función expresa la multiplicación de x por dos. Por lo que el resultado final es 20. Pero esta función al ser una función anónima no es posible llamarla, al no tener un nombre con el cual identificarla como si fuese una variable o una función.

Las funciones lambda se limitan a operaciones de una línea. Es decir, no podemos utilizar varias líneas de código como en las funciones definidas. 

Este tipos de funciones son bastante utilizadas en programación funcional, map, filters y reduce.

**Las funciones lambda no son recomendables de utilizar para los siguientes casos**:
* En el manejo de listas cuando la misma operación se puede simplificar o quedar más legible es recomendable utilizar list-comprenhencion.
* En el uso de creación de métodos para clases como en este ejemplo:
  ```python
  class User:
    mostrar = lambda self: print('Funcion mostrar...')
    saludar = lambda self: print('Funcion saludar...')
  ```
  El código no queda muy entendible y puede ser confuso. Para este caso sería mejor utilizar la sintaxis tradicional para definir métodos.

## Chaching de funciones o memoización

El caching de funciones consiste en alamacenar los resultados de la función en caché para que si se realiza una segunda llamada a la función esta retorne el resultado en caché y no tenga que volver a calcular. Esta práctica en funciones que realizen cálculos que lleven bastante tiempo y consumo de recursos permite ahorrar bastante tiempo.

### Implentación manual

```python
def is_prime(num, _cache={}):
    if num not in _cache:
        _cache[num] = True
        for n in range(2, num):
            if num % n == 0:
                _cache[num] = False
                break
    return _cache[num]
```
Como vemos creamos un diccionario llamado _cache, este diccionario será el responsable de guardar los resultados de la función. Cuando se ejecute por primera vez la función no tendrá ningún valor guardado en la caché por lo que se realizará el cálculo correspondiente y se guardará en la caché, para que la segunda vez que se ejecute la función se realize la comprobación del argumento en la caché, si esto es verdadero se volverá a calcular el resultado, en caso de que el argumento ya haya sido ingresado anteriormente se retornará directamente el resultado almacenado en la caché.

### Implementación utilizando functools

El módulo functools incorpora un decorador que nos permite implementar un sistema de caché en nuestras funciones sin necesidad de modificarlas, simplemente agregando un decorador.
```python
from functools import lru_cache
```

```python
# El maxsize de este decorador es 128.
@lru_cache(maxsize=128)
def is_prime(num):
  for n in range(2, num):
      if num % n == 0:
        return True
  return False
``` 

# Funciones anidadas

Las funciones anidadadas, al igual que los ciclos anidados, o condicionales anidados, consiste en tener funciones dentro de otras 
funciones. Este tema será de utilidad para los decoradores.

**Ejemplo**:
```python
def external_function():
    def internal_function():
        print('I am an internal function')
    internal_function()


external_function()
internal_function()

# I am a internal function
# NameError
```
Como vemos la función externa contiene a una función interna que imprime un mensaje por consola, la función que contiene a la función interna lo que hace, además de contener otras funciones, es llamarla para que la función interna se ejecute. Entonces cuando llamamos a la función externa lo que estamos haciendo es llamar a la función interna. Algo a tener en cuenta es que podemos llamar a la función externa desde nuestro programa principal, pero no podemos llamar a las funciones internas. Las funciones internas se encuentran contenidas o protegidas por la función externa, es por eso que cuando intentamos llamar a la función interna desde fuera de la función contenedora obtenemos un error, en este caso un NameError, ya que para Python esta función no se encuentra definida.

**Ejemplo**:
```python
def one():
  def two():
    def three():
      def four():
        print('I am a four function')
      four()
    three()
  two()


one()

# I am a four function
```
En este ejemplo se dispone de 4 funciones, una conteniendo a la otra. Como vemos las funciones se van llamando una a la otra pero sin llegar a ejecutar la función `one` ya que esta directamente la llamaremos desde el programa principal.

Este tema se verá con más detalle en la creación de decoradores. Los decoradores tienen una estructura de funciones anidadas, reciben como parámetros a otras funciones y logran integrar todo el concimiento sobre funciones.


# Objetos callables

Los objetos callables son aquellos que permiten ser llamados o invocados. Ejemplos de objetos callable son las funciones. 

La función built-in callable nos permite pasarle la referencia del objeto que queremos evaluar si es de tipo callable o no. Esta función retornará un booleano True si el objeto es callable o False en caso de que no lo sea.

Si queremos que una clase defina objetos que se puedan llamar como funciones tenemos que sobreescribir el metodo `__call__`.

```python
class Mostrar:
    def __init__(self, titulo):
        self.titulo = titulo

    def __call__(self, mensaje):
        return self.titulo + ' - ' + mensaje

mostrar_doctor = Mostrar('Doctor')
print(mostrar_doctor('Carlos Ugalde'), ' / ', callable(mostrar_doctor))

# Doctor - Carlos Ugade / True
```
Como vemos el objeto mostrar_doctor es de tipo callable. Esto sucede porque en una instancia de una clase sin el método `__call__` los objetos que creemos a partir de esta clase no será llamable. En cambio en esta clase al definir el método `__call__` hará que los objetos que creemos puedan ser llamados y hasta pasarle parámetros. 


