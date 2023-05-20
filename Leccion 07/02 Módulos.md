# Módulos

Hay muchas formas de crear un programa pero sin duda la modularización es la más utilizada. Consiste en partir el programa o problema en varios trozos para luego tener un programa main que una todos los módulos. Los módulos se los define como archivos externos al programa, ya sean creados por nosotros o instalados desde el manejador de paquetes de Python.


## Importación de librerías

En Python si se quiere importar un módulo se debe utilizar la keyword `import` seguido del nombre del módulo.

**Sintaxis**:
```python
import <module_name>
```
**Ejemplo**:
```python
import math
```
Importamos el módulo math al archivo de Python. Ahora el contenido de este módulo `math` puede ser accedido desde nuestro programa. Pudiendo utilizar las diferentes clases y funciones que este otorga.

Si queremos acceder a las funciones que otroga el módulo deberemos escribir el nombre del módulo seguido de un punto y la función o variable que queramos utilizar.

```python
import math
print(math.pi)

# 3.1415916.....
```

## Renombrar módulo cuando se importa

Si se quiere utilizar alguna función, clase u objeto del módulo se deberá referirse a el mismo y luego utilizar la función que se requiera. Pero si el nombre del módulo es muy largo, o simplemente se lo quiere llamar de otra manera para utilizar sus funciones podemos utilizar la keyword `as` seguido del nuevo nombre.

**Ejemplo**:
```python
import math as m
```

Ahora cada vez que queramos utilizar el módulo podremos referirnos a el con la letra m.
```python
import math as m
print(m.pi)

# 3.1415916.....
```

## Importar un objeto específico del módulo

Importar todo un módulo a un programa supone un gasto de memoria inecesario si solo se presisa una función específica del programa, pero si se desea importar una función, variable o clase del módulo basta con utilizar la keyword `from`.

**Ejemplo**:
```python
from math import pi
print(pi)

# 3.1415916.....
```
Como se vé al solo necesitamos el número pi, y en vez de importar todo el módulo math con todas sus funciones desde el módulo math importamos lo que presisamos, en este caso el número pi.

## Tipos de importaciones

Las importaciones pueden ser absolutas o relativas en donde:
* **Absoluta**: una importación absoluta se da cuando se improta un módulo especificando su ruta. Es decir que es del tipo `from local_package import funtion`. En caso de tener módulos dentro de otros módulos a la hora de importar esos módulos deberemos referirnos al módulo especificando su ubicación dentro de la estrucutura de directorios.
* **Relativa**: una importación relativa especifica el recurso que se va a importar en relación con la ubicación actual. En este tipo de importaciones siempre se utilizará un punto al inicio del nombre del módulo refiriendonos a que el módulo que se quiere importar se encuentra en el mismo directorio que el archivo main. La cantidad de puntos tambien puede variar, siendo `..` acender en una carpeta, inclusive se pueden colocar tres puntos, esto dependerá de donde se encuentra el módulo. Las importaciones se ven algo como esto: `from .package import function`. 

### Python path

Python busca módulos y paquetes en su ruta de importación. Esta es una lista de ubicaciones en las que se buscan módulos para importar. Para ver esta lista de ubicaciones se puede ejecutar el siguiente código: `sys.path`.

```python
import sys
print(sys.path)

# ['', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
```
NOTA: cabe aclarar que las rutas pueden variar de computadora en computadora.

### Estilo de importación

PEP8 define las maneras de estilizar las importanciones, dichas importanciones deben estructurarse de la siguiente manera:

* Primero las importaciones de módulos de la librería estándar.
* Segundo las importaciones de módulos de terceros.
* Tercero las importaciones de módulos locales.

**Ejemplo:**
```python
# Standard Library
import math

# Third parties
import pandas

# Local modules
import result
```

### Creando e instalando un módulo local

Si se tiene un módulo creado localmente si este lo movemos de ruta tendremos que cambiar el código a la hora de importar dicho módulo, instalar un módulo localmente permite tener accesible por toda la computadora dicho módulo pero sin tener que publicarlo en Pypi y realizar todo un módulo si lo que simplemente es no tener que cambiar el código a la hora de mover de ubicación el módulo.

Para crear un módulo disponible para todos los archivos de nuestro entorno podemos crear una serie de archivos básicos que nos permitirán instalarlo localmente.

**Archivo setup.cfg**:
```python
[metadata]
name = local_structure
version = 0.1.0

[options]
packages = structure
```


**Archivo setup.py**:
```python
import setuptools

setuptools.setup()
```

**Comando de instalación local editable**:
```bash
 python -m pip install -e .
```

## Ejemplos de importaciones

Supongamos que tenemos la siguiente estructura de archivos en nuestro proyecto.

```bash

```

