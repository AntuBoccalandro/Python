***Índice de contenidos:***
* Imprimir valores por terminal
  * La función print()
  * Imprimir texto de una sola línea
  * Uso de comillas
  * Imprimir texto de varias líneas
  * Imprimir variables
  * Realizar operaciones dentro de la función print()
  * Objectos imprimibles por la función print()
  * Imprimir texto junto a variables
    * Por medio de comas
    * Por medio de concadenación
    * Por medio de f-strings
    * Por medio de formateo
  * Parámetros opcionales de la función print()
    * end
    * sep

# 🖨️ **Imprimir valores por terminal**

Cuando hablamos de imprimir valores por terminal nos referimos a mostar valores, ya sea numéricos o texto a través de la terminal del sistema operativo. Para esta tarea todos los lenguajes tienen una función, en Python se utiliza la función `print()` para esta tarea.

## 🔢 La función print()

La función `print()` imprime valores por la terminal del sistema. Para llamarla simplemente escribimos su sintáxis, como parámetros esta función puede recibir varios pero se puede ejecutar sin ningún parámetro. Si no recibe ningún parámetro se imprimirá un caracter de salto de línea o más conocido como ENTER.

```python
print()
```

## 👊 Imprimir texto de una sola línea

La mayoría de las veces utilizaremos esta función para imprimir texto. Para imprimir texto se debe encerrar al mismo entre comillas simples o dobles. 

```python
print('Hola')
# Hola

print("Hola")
# Hola
```

## 😉 Uso de comillas

El uso de las comillas dependerá de la situación: si se quiere remarcar un texto entre comillas simples dentro del texto se utilizarán comillas dobles que encierren a todo el texto, y visceversa.

```python
print("Esta es una "frase" con estilo")
# Error

print('Esta es una "frase" con estilo')
# Esta es una "frase" con estilo

print("Esta es una 'frase' con estilo")
# Esta es una 'frase' con estilo
```

## 🗑️ Imprimir texto de varias líneas

Si se quiere imprimir texto de varias líneas si bien hay caracteres que nos permiten realizar saltos de línea se puede optar por utilizar tripe comillas simples o dobles que encierren a todo el texto, las reglas de como utilizar las comillas simples o dobles son las mismas. 

```python
print('''
    Primera línea
    Segunda línea
    Tercera línea
''')

#    Primera línea
#    Segunda línea
#    Tercera línea

print("""
    Primera línea
    Segunda línea
    Tercera línea
""")
#       Primera línea
#       Segunda línea
#       Tercera línea

```

El inconveniente es que al imprimir varias líneas como se mostró es que se agrega una tabulación a la izquierda y en ocaciones queremos eliminar esa tabulación, para ello existe una librería que se puede utilizar en esta situación, llamada `textwrap`, se puede instalar con el comando `pip install textwrap`.

```python
import textwrap

var = '''
    Python
    Javascript
    Java
    PHP
    Django
    '''

print(textwrap.dedent(var))
# Python
# Javascript
# Java
# PHP
# Django
```

## 👍 Imprimir valores de variables

Además de texto se puede mostrar valores en la terminal que provengan de variables, el tipo de dato de esta no afecta para nada. Se pueden mostrar números, strings, listas, etc. Si se quiere imprimir el valor de una varaible solo basta con colocar el nombre de la varaible dentro de la función print(). Si se quiere imprimi varias variables no hace falta utilizar la función print() varias veces si no que se pueden separar por comas los nombres de las variables. 

    ```python
    var = 'Hola'
    print(var)
    # Hola

    num = 10
    print(num)
    # 10

    print(var, num)
    # Hola 10
    ```
## 🔠 Realizar operaciones dentro de la función print()

Dentro de la función print() se puede realizar todo tipo de operaciones, como sumas, restas, comparaciónes, etc...es decir que se mostrará el resultado de dicha operación en la terminal. 

```python
a = 10
b = 9

print(a+b)
# 19

print(a>b)
# True
```

## 🧑‍💻 Objetos imprimibles por la función print()

La función print() soporta todo tipo de objeto:

* Datos de tipo secuencia: list, tuple
* Datos de tipo numéricos: int, float, complex
* Datos booleanos: True/False
* Datos de tipo diccionario
* Datos de tipo set
* Objetos
* Funciones
* Operaciones aritméticas/relación/lógicas
* Métodos

## 👌 Imprimir texto junto a variables

Hemos visto como imprimir texto y varaibles, pero en ocaciones se quieren imprimir estos dos elementos de manera conjunta para, por ejemplo, mostrar el valor de una variable a la vez que se indica en texto a que variable pertenece ese valor. Para esto hay muchos métodos y son los siguientes. 

**Por medio de comas**: se separa el texto y las variables por comas.
```python
lenguaje = 'Python'
año = 1991

print(lenguaje, 'se creó en ', año)
# Python se creó en 1991
```

**Por medio de concadenación**: se utiliza el operador `+` para sumar el texto y los datos de tipo string de las variables.
```python
lenguaje = 'Python'
año = '1991'

print(lenguaje+'se creó en'+año)
# Python se creó en 1991
```

Como vemos se imprimimen los valores de las variables entre medio del texto pero hay un inconveniente. Al sumar los datos todos tienen que ser de tipo string y el año es un número por lo que requiere de una conversión de número entero a string, se puede encerrar al número entero entre comillas y transformarlo en un string o utilizar la función incporporada `str()` para realizar esa conversión.

```python
lenguaje = 'Python'
año = 1991

print(lenguaje+'se creó en'+str(año))
# Python se creó en 1991
```
 
**Por medio de f-strings**: se utilizan los f-strings para poder combinar las variables dentro del texto por medio de llaves. Esta es una de mis maneras preferidas ya que es muy cómoda y facilmente entendible. 
```python
lenguaje = 'Python'
año = 1991

print(f'{lenguaje} se creó en {año}')
# Python se creó en 1991
```

**Por medio de formateo**: se crean juegos de llaves en los cuales luego le pasaremos una lista de elementos que queremos representar en cada llave. Es importante que los elementos estén en orden con respecto a sus llaves.
```python
lenguaje = 'Python'
año = 1991

print('{} se creó en {}'.format(lenguaje, año))
# Python se creó en 1991
```

## 🌐 Parámetros opcionales de la función print()

La función print() puede recibir varios parámetros opcionales que permiten darle un formato diferente a los valores que se imprimirán.

**print(< content >, < end='' >)**: el parámetro `end=''` permite especificar el caracter con el cual se quiere que termine la impresión, por defecto es un caracter de salto de línea `\n`, pero se puede colocar qualquier otro. 
```python
print('Python', end='-')
# Python-

print('Python ', end='lenguaje')
# Python lenguaje
```

NOTA: si se define el parámetro end='' con un string vacío lograremos que la próxima impresión que hagamos se vea al lado de la anterior.

```python
print('Python', end='')
# Python

print('Hello')
# PythonHello
```

**print(< content >, < sep='' >)**: el parámetro `sep=''` permite definir un caracter que separá los elementos que se vallan a imprimir.  
```python
print('Python', 'Javascript', 'PHP', sep='-')
# Python-Javascript-PHP

print('Python', 'Javascript', 'PHP', sep=' ')
# Python Javascipt PHP
```

# **Colorear salida en la consola**

Si se quiere cambiar el color del texto o variables que imprimimos es posible de dos maneras. Por medio de Python o por medio de un módulo llamado colorama.

## Colorear la salida en la consola mediante códigos ANSI

Mediante el siguiente formato de código podemos colorear la salida en la consola.

```python
'\033[cod_formato;cod_color_texto;cod_color_fondom'
```
Donde:
* \033 es el caracter de escape.
* cod_formato es el código de formato especificado en la tabla de estilos.
* cod_color_texto es el código de color de texto especificado en la tabla de estilos.
* cod_color_fondo es el código de color de fondo especificado en la tabla de estilos.
* m es el caracter que cierra el [ de formato.

**Tablas de estilos**:

| **Estilos*** | **Código ANSI** |
| ------------ | --------------- |
| Sin efecto   | 0               |
| Negrita      | 1               |
| Débil        | 2               |
| Cursiva      | 3               |
| Subrayado    | 4               |
| Inverso      | 5               |
| Oculto       | 6               |
| Tachado      | 7               |


**Tabla de colores de texto y fondo**:
| **Colores** | **Texto** | **Fondo** |
| ----------- | --------- | --------- |
| Negro       | 30        | 40        |
| Rojo        | 31        | 41        |
| Verde       | 32        | 42        |
| Amarillo    | 33        | 43        |
| Azul        | 34        | 44        |
| Morado      | 35        | 45        |
| Cian        | 36        | 46        |
| Blanco      | 37        | 47        |


**Ejemplo**:
```python
print("\033[4;35m"+"Texto en negrita y subrayado de color morado")

# Texto en negrita y subrayado de color morado
```

## Colorear la salida en la consola mediante el módulo colorama

**Instalación del módulo**

```bash
pip install colorama
```

**Incluir en el programa**

```python
from colorama import init, Fore, Back, Style
```

# **Tips de formateo de texto a la hora de imprimir valores por consola**

## **Mostrar n decimales**
**Sintaxis**: Donde n es la cantidad de decimales que queremos especificar que se muestren y f hace referencia al tipo de dato float.
```python
<variable>:<0.nf>
```

**Ejemplo**:
```python
from math import pi

print(f'PI es igual a {pi:0.10f}')
# PI es igual a 3.1415926536
```

## **Completado de caracteres**
**Sintaxis**: Donde `character` es el caracter con el que queremos rellenar el espacio (puede ser una letra o un número) seguido de un `caracter clave` que definirá la alineación del texto y luego `n` que corresponde al número de espacios que queremos justificar.
```python
<variable>:<character><keyword><n>
```
**Tabla de alineaciónes**:
* `<` Hacia la izquierda
* `>` Hacia la derecha
* `^` Centrado

**Ejemplo**:
```python
day = int(input('Ingrese el día: '))
month = int(input('Ingrese el mes: '))
year = int(input('Ingrese el año: '))

print(f'{day:0>2}/{month:0>2}/{year}')
# Ingrese el día: 1
# Ingrese el mes: 2
# Ingrese el año: 2023
# 01/02/2023
```

# **Limpiar la terminal**

Si se quiere limpiar la terminal se pueden utilizar dos formas:

## **Limpiar la terminal con el módulo os**
```python
import os

def limpiar_consola():
    if os.name == 'posix':  # Linux y macOS
        os.system('clear')
    else:  # Windows y otros
        os.system('cls')

```

## **Limpiar la terminal con la función print()**
```python
def limpiar_consola_unicode():
    print("\u001b[2J\u001b[H", end='')
```
