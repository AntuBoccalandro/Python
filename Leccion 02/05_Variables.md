***Índice de contenidos:***
* Variables
  * Definiendo una variable
  * Formas de asignar variables
  * Reasignación de variables
  * Tipos de variables
  * Nombres de variables
    * Camelcase
    * Snake case
    * Significado del nombre de variables
  * Espacios de memoria
  * Intercambio de variables

# 🎯 **Variables**

Las variables son espacios de memoria reservados para almacenar un dato o valor, a dicha variable también se le asigna un nombre con el cual identificarla. Su nombre (variable) viene justamente a que su valor al principio del programa vale, por ejemplo, 2 y al final del programa su valor se modifica o varía y puede valer 10. Para entenderlo de otra manera es como si tuviéramos una caja en la cual podamos meter objetos, a esta caja se le asigna un nombre para poder identificarla de la otras cajas, la caja estaría representando el espacio en memoria, los objetos es dato de la variable y por último el nombre es el identificador que tenemos para diferenciarla de las demás, al ser una caja sus objetos de dentro pueden variar ya que podemos meter otro tipo de objetos, colocar más o retirar algunos.

## 📍 Definiendo una variable

`nombre_de_la_ variable = valor`

Para definir una variable en Python se utiliza el operación de asignación `=`. Este operador asigna un valor a la variable que, mediante el nombre podremos identificarla para poder tratar con el/los datos que almacene.

```python
var = 'Hola'
print(var)
# Hola

num = 10
print(num)
# 10
```
## 📎 Formas de asignar variables
* **Asignación simple**: se asigna un único valor a la variable
    ```python
    mi_var = 'Python'
    ```
* **Asignación múltiple**: se asignar diferentes valores a diferentes varaibles separando los nombres de las variables y sus valores por comas.
    ```python
    a, b, c = 10, 20, 'Python'
    ```
* **Asignación en cadena**: se definen varias variables pero un solo valor para todas.
    ```python
    a = b = c = 10
    ```

## 🚩 Reasignación de variables

En Python, y en cualquier lenguaje de programación los valores de las variables pueden cambiar (es la escencia de las variables, que puedan cambiar su valor). Para reasignar el valor a una variable se debe utilizar el nombre que la identifica, utilizar el operador de asignación y asignarle el nuevo valor. El proceso de reasignación de variables se realiza sintácticamente de la misma manera que la asignación.

```python
num = 10
print(num)
# 10

num = 20
print(num)
" 20
```

## 🎁 Tipos de variables

Cuando nos referimos a tipos de variables nos referimos al tipo de dato que esta almacena, al ser Python un lenguaje de tipado dinámico no es necesario especificar el tipo de dato que alamcenará la variable, además se puede cambiar el tipo de dato que esta contiene, algo que no se puede realizar en lenguajes como C, C++ o C#. No veremos los tipos de datos (en otra sección) pero los mencionaremos:
* Listas
* Tuplas
* Sets
* Diccionarios
* Números enteros/reales/complejos
* Strings
* bytes

## 🎄 Nombres de las variables
Los nombres de las variables no pueden empezar por ningún:
* Números
* Espacios o tabulaciones
* Palabras claves de python

Los nombres de las variables no pueden contener:
* Espacios o tabulaciones
* Guiones  

**Camelcase**: separar palabras mediante las mayúsculas. Se coloca en mayúscula la primera letra de la palabra siguiente a la primera. Ejemplo:
Not Camelcase → `numerouno`                     Camelcase → `numeroUno`

**Snakecase**: separar palabras mediantes underscores o guiones bajos. Python utiliza esta manera y es el estándar entre los desarrolladores y la gupia de estilo PEP8 así que es importante que utilices esta forma de nombrar variables. 
No snakecase → `numerouno`                     Snakecase → `numero_uno`

**Significado del nombre de la variable**
A la hora de crear una variable debemos nombrarla con un nombre que represente el valor que se irá a guardar, ya que si colocamos un nombre que no sea significativo para su uso nos resultará difícil utilizarlas en un programa ya que no sabremos para qué fue creada en un principio. 

Nombre no significativo → variable1 = "Hola"     Nombre significativo → saludo = "Hola"

## 🎒 Espacios de memoria

Las variables se almacenan en partes de la memoria RAM de la computadora. La memoria RAM tiene las denominadas direcciones de memoria, estas direcciónes son accesibles y modificacbles. Si se quiere saber la dirección de memoria en la cual se encuentra almacenada una varaible en python se utiliza la función integrada `id(< object >)`. Esta función también sirve para cualquier otro tipo de objetos. 

```python
variable = 'Hola'
print(id(variable))
# 2292900168208
```

## ✨ Intercambio de variables

Si se quiere intercambiar una variable por otra y viscervsa se puede realizar de varias maneras:

**Forma 1**:
```python
x = 10
y = 20
print(x, y)
# 10 20

temp = x
x = y
y = temp
print(x, y)
# 20 10
```
Creamos una variable temporal que almacenará el valor de la variable x para que luego la asignemos a la variable y, es decir, estamos asignando el valor de x a y. Para la asignar x a y solo hace falta realizar la asignación, ya que no perdemos el valor como pasa con x.

**Forma 2**:
```python
x = 10
y = 20
print(x, y)
# 10 20

y, x = x, y
print(x, y)
# 20 10
```
Como vemos gracias a poder utilizar las comas para asignar varias variables podemos asignar el valor de y a x y de x a y.

**Forma 3**:
```python
x = 10
y = 20
print(x, y)
# 10 20

x = x + y
y = x - y
x = x - y
print(x, y)
# 20 10
```
Como vemos le sumamos a x la variable y. Y a la variable y le restamos x. Por último para recuperar el valor de x solo basta con restarle y.

