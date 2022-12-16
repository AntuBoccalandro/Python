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

## Orden de los argumentos de la fución

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
