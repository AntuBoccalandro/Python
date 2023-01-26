# Loggigin

El login consiste en guardar aquella información útil de acciones o errores, esto con el fin de tener un registro de la aplicación. Al tener un archivo log con todas las acciones o errores de la aplicación podemos resolver problemas más sencillamente o proveer una herramienta de registro de la aplicación. Los datos que podemos guardar en este archivo pueden ser horas, fechas, acciones, errores, etc.

# Importación del módulo logging

Este módulo ya viene incluido en la biblioteca estándar de Python por lo que la importación se realiza desde la sentencia `import`.

```python
import logging
```

# El módulo logging

Este módulo se organiza por niveles de  (ordenados de mayor a menor gravedad desde abajo hacia arriba), estos son:

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

Cada uno de estos niveles proporciona un método de registro:

```python
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```
OUTPUT:
```shell
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

# Configuración del módulo 

Antes de empezar a logear nuestra aplicación es necesario configurar como vamos a realizar el loggin, en que archivo vamos a guardar los registros, etc.

```python
logging.basicConfig(
    level=logging.DEBUG, 
    filename='app.log', 
    filemode='w', 
    format='%(name)s - %(levelname)s - %(message)s'
    )
logging.warning('This will get logged to a file')
```
Acá estamos configurando que el archivo donde se guardarán los registros se llama app.log, el modo de escritura en el que se abrirá el archivo es en modo de escritura y el nivel de gravedad establecido en DEBUG, esto según lo que indica cada parámetro:

* Nivel: El registrador raíz se establecerá en el nivel de gravedad especificado.
* Filename: Especifica el archivo.
* Modoarchivo: Si se indica filename, el fichero se abrirá en este modo. Por defecto es a, que significa append.
* Formato: Es el formato del mensaje de registro.

# Formato

## Formato básico

```python
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
```

OUTPUT:
```shell
18472-WARNING-This is a Warning
```
Aquí se imprime el proceso, luego el nivel del registro y por último el mensaje de registro.

## Agregar tiempo del registro

```python
logging.basicConfig(
    format='%(asctime)s - %(message)s', 
    level=logging.INFO
    )
logging.info('Admin logged in')
```

OUTPUT:
```shell
2018-07-11 20:12:06,288 - Admin logged in
```

## Formateo de fechas

```python
logging.basicConfig(
    format='%(asctime)s - %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S'
    )
logging.warning('Admin logged out')
```

OUTPUT:
```shell
12-Jul-18 20:53:19 - Admin logged out
```

## Variables

También se pueden agregar variables en los mensajes para no mostrar mensajes estáticos y mostrar mensajes dinámicos, como nombres de usuarios.

```python
user = 'John'

logging.error(f'{user} raised an error')
```

# Capturando Stack Traces

Capturar excepciones mediante el parámetro exc_info:

```python
a, b = 5, 0

try:
    division = a / b
except Exception as error:
    logging.error("Se ha producido una excepción", exc_info=True)
```

OUTPUT:
```shell
ERROR:root:Se ha producido una excepción
Traceback (última llamada más reciente):
  File "excepciones.py", line 6, in <módulo>
    c = a / b
ZeroDivisionError: división por cero
[Terminado en 0.2s]
```

Capturar excepciones mediante el método exception:
```python
a, b = 5, 0

try:
    division = a / b
except Exception as error:
    logging.exception("Se ha producido una excepción")
```

# Clases y funciones

Como vemos cuando mostramos un regstro se encuentra el prefijo root:, lo recomendable es crear un nuevo logger que tenga sentido con el módulo de la aplicación que se está registrando.

Las clases más utilizadas definidas en el módulo de registro son las siguientes:

* Logger: Es la clase cuyos objetos se utilizarán en el código de la aplicación directamente para llamar a las funciones.

* LogRecord: Los loggers crean automáticamente objetos LogRecord que tienen toda la información relacionada con el evento que se está registrando, como el nombre del logger, la función, el número de línea, el mensaje, etc.

* Handler: Los manejadores envían el LogRecord al destino de salida requerido, como la consola o un archivo. Handler es una base para subclases como StreamHandler, FileHandler, SMTPHandler, HTTPHandler, y más. Estas subclases envían las salidas de registro a los destinos correspondientes, como sys.stdout o un archivo de disco.

* Formater: Aquí es donde se especifica el formato de la salida especificando un formato de cadena que enumera los atributos que debe contener la salida.

## Registrando un nuevo logger

```python
logger = logging.getLogger('example_logger')
logger.warning('This is a warning')
```

OUTPUT:
```shell
WARNING:example_logger:This is a Warning
```

## Tip

"Se recomienda que utilicemos loggers a nivel de módulo pasando `__name__` como parámetro de nombre a getLogger() para crear un objeto logger ya que el propio nombre del logger nos indicaría desde dónde se están registrando los eventos. `__name__` es una variable especial incorporada en Python que se evalúa como el nombre del módulo actual." 

# Handlers



