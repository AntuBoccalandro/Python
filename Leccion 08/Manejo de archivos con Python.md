# Manejo de archivos con Python

## Conceptos claves

**¿Qué es un archivo?**

Un archivo es una secuencia de bytes. Cada tipo de archivos dependerá de su extensión, los bytes estarán organiados de acuerdo al tipo de archivo.

**Partes de un archivo**

Las partes de un archivos son:
* Cabecera: metadatos sobre el contenido del archivo (nombre, tamaño, tipo, etc.).
* Datos: contenido del fichero tal y como lo escribió el creador o el editor
* Fin de archivo (EOF): carácter especial que indica el final del archivo
  
**Acceso a los archivos**

Para acceder a un archivo es necesario tener una ruta que indique la ubicación del mismo. Las ubicaciones se componen de una estrcutura similar a esta: `<directoriy_name1/directory_name2/...directory_nameN/file_name.extention>` donde:
* directory_name es el nombre del directorio o carpeta
* file_name es el nombre real del archivo
* extention es la extención del archivo que indica de que tipo es este

Si se quiere acceder a un archivo deberemos colocar una ruta, pero que pasa si queremos acceder a un archivo que esta por encima de nuestro directorio actual. Esto se soluciona utilizando dos puntos seguidos (`../`) para indicar que queremos retroceder al directorio anterior, o que lo contiene. Ejemplo: `<../directory_name/file_name.extention>`.

## Finales de línea

Los archivos contienen caracteres especiales dedicados a indicar las nuevas líneas. Según la ciertas normas se especifica que se deben utilizar dos caracteres para indicar nuevas líneas, estos son: Carriage Return (CR o \r) y Line Feed (LF o \n)
* Windows utiliza estos dos caracteres, CR+LF
* Sistemas Unix utiliza solo el caracter LF

Las diferencias entre los sistemas operativos puede ocacionar problemas a la hora de pasar archivos de un sistema Windows a uno Unix o viseversa.

## Codificación de caracteres

Una codificación es la manera en la que un sistema traduce los bytes a símbolos legibles por humanos. Cada codificación tiene diferentes capacidades de caracteres difererentes y formas distintas en las que trabajan con estos. Los codificacdores de caracters más conocidos son:
* ASCII: con soporte para 128 caracteres
* UNICODE: con soporte hasta de 1.114.112 caracteres

Python utiliza el sistema UNICODE, y es importante saber la codificación de cada archivo ya que al igual que los caracteres de línea esto puede traer problemas.

# Abriendo y cerrando archivos con Python

**Abrir un archivo**:

Para abrir un archivo se debe utilizar la sentencia `open(<"path">)`. Que recibe como único objeto un string con la ruta del archivo que se quiere abrir.

Esta sentencia abre el archivo pero no lo cierra, la importancia de cerrar el archivo es muy importante ya que además de tener un código más limpio, organizado y estandarizado, evitamos errores. Los errores pueden ser de sobrecarga del búffer de Python, o que se colapse el script en ejecución. Así que es muy importante cerrar los archivos que abrimos una vez manipulado los mismos.

Ejemplo de sentencia open()/close():
```python
file = open('languajes.txt')
for i in file: print(i)
file.close()
```

La sentencia `with()` permite abrir un archivo y cuando se salga del bloque with se cerrará automáticamente el archivo.

Sintaxis:
```txt
with open(<'file_path'>, ['mode']) as <name>:
    # Further file processing goes here
```
* File_path corresponde a la ruta del archivo
* mode es el modo en el que se abre el archivo, existen diferentes modos, estos son:

| **Mode** | **Descripción**                                |
| -------- | ---------------------------------------------- |
| `'r'`    | Abre el archivo en modo lectura                |
| `'w'`    | Abre el archivo en modo de escritura           |
| `'rb'`   | Abre el archivo en modo binario para lectura   |
| `'wb'`   | Abre el archivo en modo binario para escritura |

Ejemplo:
```python
with open('languajes.txt', 'r') as languajes:
    pass
```

## Tipos de archivos de texto

**Archivos de texto**: este es el tipo más común de archivos de texto. Al utilzar la sentencia open() obtendremos como resultado un objeto `<class '_io.TextIOWrapper'>`. 

```python
file = open('languajes.txt', 'r')
print(type(file))

# <class '_io.TextIOWrapper'>
```

**Archivos de binario con búfer**: este tipo de archivo se utiliza para ller y escribir archivos binarios, cuando abrimos este tipo de archivos obtendremos un objeto de tipo: `<class '_io.BufferedReader'>``<class '_io.BufferedWriter'>`. 

```python
file = open('languajes.txt', 'rb')
print(type(file))

# <class '_io.BufferedReader'>
```

**Tipos de archivos RAW**: no suele ser muy común este tipo de archivo, generalmente utilizado como bloque de construcción de bajo nivel para flujos binarios y de texto.

```python
file = open('languajes.txt', 'rb', buffering=0)
print(type(file))

# <class '_io.FileIO'>
```

# Leyendo archivos abiertos

Una vez abierto un archivo existen diferentes acciones que podemos realizar con el archivo en modo de lectura.

## Leyendo archivos

Existen algunos métodos que nos permiten leer los archivos:

| **Método**      | **Descripción**                                                                                                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `'.read()'`     | Esto lee del archivo basándose en el número de bytes de tamaño. Si no se pasa ningún argumento o se pasa Ninguno o -1, se lee todo el fichero.                                                                                     |
| `'.readline'`   | Esto lee como máximo el número de caracteres de la línea. Continúa hasta el final de la línea y luego da la vuelta. Si no se pasa ningún argumento o se pasa Ninguno o -1, entonces se lee toda la línea (o el resto de la línea). |
| `'readlines()'` | Esto lee las líneas restantes del objeto archivo y las devuelve como una lista.                                                                                                                                                    |

Archivo de ejemplo: languajes.txt
```txt
Python
Django
Flask
Javascript
Typescript
Scala
Julia
SQL
Matlab
HTML
CSS
Bootstrap
Sass
Less
Java
```

Ejemplo con cada método:
**.read()**:
```python
with open('languajes.txt') as lan:
    print(lan.read())

# Python
# Django
# Flask
# Javascript
# Typescript
# Scala
# Julia
# SQL
# Matlab
# HTML
# CSS
# Bootstrap
# Sass
# Less
# Java
```
Como vemos nos retorna todos los lenguajes escritos en el archivo languajes.txt. 

**.readline()**:
```python
with open('languajes.txt') as lan:
    print(lan.readline(6))

# Python
```
Como cada caracter UNICODE pesa de 1 a 4 bytes, al indicar que queremos leer 6 bytes obtenemos como resultado la primera palabra, en este caso Python, que se compone de 6 caracters y por ende pesa 6 bytes, esto lo sabemos porque si colocamos 5 obtendremos como resultado Pytho.

**.readlines()**:
```python
with open('languajes.txt') as lan:
    print(lan.readlines())

# ['Python\n', 'Django\n', 'Flask\n', 'Javascript\n', 'Typescript\n', 'Scala\n', 'Julia\n', 'SQL\n', 'Matlab\n', 'HTML\n', 'CSS\n', 'Bootstrap\n', 'Sass\n', 'Less\n', 'Java']
```
Como vemos obtenemos una lista con todas las líneas del archivo pero organizadas en una lista. A su vez cada línea tiene su caracter de salto de línea, `\n`.

## Iterando sobre cada línea del archivo

Esta acción es bastante común de realizar, se puede hacer con un ciclo while o for, esto dependerá de la situación.

Por medio de un ciclo while:
```python
with open('languajes.txt', 'r') as lan:
    line = lan.readline()
    while line != '':
        print(line, end='')
        line = lan.readline()

# Python
# Django
# Flask
# Javascript
# Typescript
# Scala
# Julia
# SQL
# Matlab
# HTML
# CSS
# Bootstrap
# Sass
# Less
# Java
```

Por medio de un ciclo for:
```python
with open('languajes.txt', 'r') as lan:
    for i in lan:
        print(i, end='')

# Python
# Django
# Flask
# Javascript
# Typescript
# Scala
# Julia
# SQL
# Matlab
# HTML
# CSS
# Bootstrap
# Sass
# Less
# Java
```

# Escribiendo archivos abiertos

Una vez abierto el archivo como ya vimos podemos leer el archivo pero si lo abrimos en modo de escritura podemos modificarlo.

## Métodos 

Los métodos de escritura son:

| **Método**             | **Descripción**                                                                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `.write(string)`   | Escribe una cadena en el archivo.                                                                                                             |
| `.writelines(seq)` | Esto escribe la secuencia en el archivo. No se añaden finales de línea a cada elemento de la secuencia. Depende de usted añadir el(los) final(es) de línea apropiado(s). |

Archivo de ejemplo: languajes.txt
```txt
Python
Django
Flask
Javascript
Typescript
Scala
Julia
SQL
Matlab
HTML
CSS
Bootstrap
Sass
Less
Java
```

Ejemplo con cada método:

**.write(string)**
```python
with open('languajes.txt', 'w') as lan:
    lan.write('C++')

with open('languajes.txt', 'r') as lan:
    for i in lan:
        print(i, end='')

# C++
```
Al escribir archivos este lo reescribe completamente así que como resultado solamente está el string que escribimos.

**.writelines()**:
```python
with open('languajes.txt', 'w') as lan:
    lan.writelines(['C++', 'C', 'C#'])

with open('languajes.txt', 'r') as lan:
    for i in lan:
        print(i, end='')

# C++
# C
# C#
```

# Tipos y trucos

## Atrinuto file
`__file__` devuelve la ruta relativa a donde se llamó al script inicial de Python. Esto se puede utilizar para conocer la ruta del módulo que está utilizando.

Ejemplo:
```python
import os
print(os.__file__)

# C:\Users\Usuario\AppData\Local\Programs\Python\Python310\lib\os.py
``` 
El resultado dependerá de su computadora y sistema operativo.

## Agregando un archivo

Hay dos formas de agregar archivos en Python. Podemos agregarlos al principio o al final de un archivo según el parámetro que especifiquemos.

`'a'`: Los textos se insertarán en la posición actual del flujo de archivos, por defecto al final del archivo.

`'w'`: El archivo se vaciará antes de que los textos se inserten en la posición actual del flujo de archivos, por defecto es 0.

Ejemplo:
```python
with open('languajes.txt', 'a') as lan:
    lan.write('\nC++')

with open('languajes.txt', 'r') as lan:
    print(lan.read())

# Python
# Django
# Flask
# Javascript
# Typescript
# Scala
# Julia
# SQL
# Matlab
# HTML
# CSS
# Bootstrap
# Sass
# Less
# Java
# C++
```

## Trabajar con dos archivos al mismo tiempo

Si se desea trabajar con dos archivos al mismo tiempo se puede realizar dos sentencias with-open pero se pueden combinar de una manera que lo hagamos más eficiente.

Ejemplo:
```python
with open('web_languajes.txt', 'r') as reader, open('web_frameworks.txt', 'w') as writer:
    web = reader.readlines()
    writer.writelines(web)
```

