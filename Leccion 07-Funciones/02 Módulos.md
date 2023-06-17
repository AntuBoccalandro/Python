# **Módulos**

Hay muchas formas de crear un programa pero sin duda la modularización es la más utilizada. Consiste en partir el programa o problema en varios trozos para luego tener un programa main que una todos los módulos. Los módulos se los define como archivos externos al programa, ya sean creados por nosotros o instalados desde el manejador de paquetes de Python.


## **Importación de librerías**

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

## **Renombrar módulo cuando se importa**

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

## **Importar un objeto específico del módulo**

Importar todo un módulo a un programa supone un gasto de memoria inecesario si solo se presisa una función específica del programa, pero si se desea importar una función, variable o clase del módulo basta con utilizar la keyword `from`.

**Ejemplo**:
```python
from math import pi
print(pi)

# 3.1415916.....
```
Como se vé al solo necesitamos el número pi, y en vez de importar todo el módulo math con todas sus funciones desde el módulo math importamos lo que presisamos, en este caso el número pi.

## **Tipos de importaciones**

Las importaciones pueden ser absolutas o relativas en donde:
* **Absoluta**: una importación absoluta se da cuando se improta un módulo especificando su ruta. Es decir que es del tipo `from local_package import funtion`. En caso de tener módulos dentro de otros módulos a la hora de importar esos módulos deberemos referirnos al módulo especificando su ubicación dentro de la estrucutura de directorios.
* **Relativa**: una importación relativa especifica el recurso que se va a importar en relación con la ubicación actual. En este tipo de importaciones siempre se utilizará un punto al inicio del nombre del módulo refiriendonos a que el módulo que se quiere importar se encuentra en el mismo directorio que el archivo main. La cantidad de puntos tambien puede variar, siendo `..` acender en una carpeta, inclusive se pueden colocar tres puntos, esto dependerá de donde se encuentra el módulo. Las importaciones se ven algo como esto: `from .package import function`. 

### **Python path**

Python busca módulos y paquetes en su ruta de importación. Esta es una lista de ubicaciones en las que se buscan módulos para importar. Para ver esta lista de ubicaciones se puede ejecutar el siguiente código: `sys.path`.

```python
import sys
print(sys.path)

# ['', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
```
NOTA: cabe aclarar que las rutas pueden variar de computadora en computadora.

### **Estilo de importación**

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
import .calc
```

## **Colocación de Alias a las importaciones**
Algunos paquetes que se importan tienen nombres largos, colocarles alias hace más sencilla la sintaxis del lenguaje.
```python
import tkinter as tk
```
Ahora en vez de utilizar la sintaxis `tkinter.<funcion>` deberemos utilizar la sintaxis `tk.<function>`.


# **Creando nuestro propio módulo y subiéndolo a PyPi**

Lo primero es definir la estructura del módulo:
```bash
realpython-reader/
│
├── src/
│   └── reader/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.toml
│       ├── feed.py
│       └── viewer.py
│
├── tests/
│   ├── test_feed.py
│   └── test_viewer.py
│
├── LICENSE
├── MANIFEST.in
├── README.md
└── pyproject.toml
```

## **Asignarle un nombre al paquete de Python**
Este será el nombre que aparecerá en PyPi, lo ideal es que coincida con el nombre con el cual el usuario que instale el paquete lo importe en su aplicación, pero esto no tiene porque ser así, no es necesario la conincidencia del nombre del paquete al instalarlo por medio de pip y el nombre con el cual se importa el paquete en la aplicación.

## **Configuración del paquete**
**Configuración del sistema de compilación**: este archivo si o sí debe llamarse `pyproject.toml`. El sistema de compilación hacer referencia al sistema por el cual Python compila el paquete al instalarlo.
```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"
```
**Configuración del paquete**: las configuraciones del proyecto variaran según el paquete que se esté creando, pero hay constantes que siempre se mantendrán.
```toml
# pyproject.toml

[build-system]
requires      = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "realpython-reader"
version = "1.0.0"
description = "Read the latest Real Python tutorials"
readme = "README.md"
authors = [{ name = "Real Python", email = "info@realpython.com" }]
license = { file = "LICENSE" }
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
keywords = ["feed", "reader", "tutorial"]
# Dependencias del proyecto
dependencies = [
    "feedparser >= 5.2.0",
    "html2text",
    'tomli; python_version < "3.11"',
]
requires-python = ">=3.9"
# Dependencias que no son necesarias para el funcionamiento, si no más para el desarrollo, como pytest
[project.optional-dependencies]
dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]

[project.urls]
Homepage = "https://github.com/realpython/reader"

[project.scripts]
realpython = "reader.__main__:main"
```

La información mínima que debes incluir en tu pyproject.tomles la siguiente:

* `name`: especifica el nombre de su paquete tal como aparecerá en PyPI.
* `version`: establece la versión actual de su paquete.

Como muestra el ejemplo anterior, puede incluir mucha más información. Algunas de las otras claves en pyproject.tomlse interpretan de la siguiente manera:

* `classifiers`: describe su proyecto utilizando una lista de clasificadores . Deberías usarlos ya que hacen que tu proyecto sea más fácil de buscar.
* `dependencies`: enumera las dependencias que tiene su paquete con las bibliotecas de terceros. readerdepende de feedparser, html2texty tomli, por lo que se enumeran aquí.
`project.urls`: agrega enlaces que puede usar para presentar información adicional sobre su paquete a sus usuarios. Puede incluir varios enlaces aquí.
`project.scripts`: crea scripts de línea de comandos que llaman a funciones dentro de su paquete. Aquí, el nuevo realpython comando llama main() dentro del `reader.__main__` módulo.

## **Documentación del paquete**
La documentación del paquete es fundamental, permite a los usuarios que se descargan el paquete saber como utilizarlo. Al publicar el paquete en PyPi es recomendable incluir un archivo README.md que incluya una descripción del proyecto y una guía rápida de como utilizarlo, así como enlaces a github, la documentación, etc.

## **Probar el paquete**
Antes de publicar el paquete, como es algo que utilizará otras personas debe estar testeado para asegurarse la máxima robustez del código.

## **Versiones del paquete**
Con respecto al versionado del paquete debe ser claro y seguir estas reglas:
* La nomenclatura debe ser MAJOR.MINOR.PATCH, ejemplo: 12.4.9
* Incremente la versión MAJOR cuando realice cambios de API incompatibles.
* Incremente la versión MINOR cuando agregue funcionalidad de manera compatible con versiones anteriores.
* Aumente la versión de PATCH cuando realice correcciones de errores compatibles con versiones anteriores. 
* Se debe restablecer a PATCH a 0 cuando se incremente MINOR, y restablecer tanto PATCH como MINOR a 0 cuando se incremente MAJOR. Ejemplo: 12.4.9 -> 13.0.0

## **Agregar archivos de recurso al paquete**
A veces, tendrá archivos dentro de su paquete que no son archivos de código fuente. Los ejemplos incluyen archivos de datos, binarios, documentación y, como en este ejemplo, archivos de configuración.

Para asegurarse de que dichos archivos se incluyan cuando se construya su proyecto, utilice un archivo `MANIFEST.in`. Este archivo debe estar en el mismo directorio que `pyproject.toml`.
```txt
# MANIFEST.in

include src/reader/*.toml
```

## **Licencia del paquete**
Esto dependerá del proyecto, pero normalmente se suele utilizar la licencia MIT.


## **Instalar el paquete localmente**
enga en cuenta el punto ( .) al final del comando. Es una parte necesaria del comando e indica pipque desea instalar el paquete ubicado en el directorio de trabajo actual. En general, esta debería ser la ruta al directorio que contiene su `pyproject.toml `archivo.
```bash
python -m pip install --editable .
```

## **Publicar el paquete en PyPi**
Se debe crear una cuenta en PyPi desde el sitio web oficial, luego deberá ejecutar un comando para instalar las herramientas que permitirán construir y subir el paquete a internet:
```bash
python -m pip install build twine
```

**Construir el paquete**:
```bash
python -m build
```

**Comprobar la existencia del paquete creado**:
```bash
twine check dist/*
```

**Cargar paquete a PyPi**:
Twine le pedirá su nombre de usuario y contraseña.
```bash
twine upload dist/*
```

**Instalar el paquete mediante pip**:
El comando es el de siempre, pero esta vez el nombre del paquete es el que nosostros creamos.
```bash
python -m pip install <your-package-name>
```
