# **Entornos Virtuales**

# **¿Qué es un entorno virtual?**

Los entornos virtuales son una manera de aislar un proyecto de Python, esto logra:
* **Evitar la contaminación del sistema**: cuando instalamos muchos paquetes diferentes para aplicaciones diferentes en el sistema se van acumulando estos paquetes. 
*  **Compatibilidad**: la gran cantidad de paquetes puede generar problemas de importación, que no se encuentren paquetes o que entren en conflictos con los demás.
*  **Versiones**: según el proyecto puede que se necesite el mismo paquete pero en diferentes versiones, esto puede hacer que funcione una de las aplicaciones porque tiene la versión correcta, pero la otra no lo haga. Crear entornos virtuales permite separar cada proyecto con sus propias dependencias una de otra. 
* **Practicidad**: en un entorno virtual se tiene instalado solo los paquetes que necesita el proyecto, por lo que se puede tener un listado específico de los paquetes instalados y utilizados en el proyecto. No se listan los paquetes que utilizan otros proyectos y hace más fácil el trabajo.
  
Un entorno virtual de Python es una estructura de carpetas que le brinda todo lo que necesita para ejecutar un entorno de Python liviano pero aislado.

# **¿Cómo funciona un entorno virtual?**

Cuando crea un entorno virtual usando `venv`, el módulo vuelve a crear la estructura de archivos y carpetas de una instalación estándar de Python.

## **Estructura de carpetas**
Cuando se crea un entorno virtual se genera una serie de carpetas iguales a la de una instalación de Python estándar:
```bash
# Ejemplo de Windows. En Linux/MacOS la carpeta Scripts es llamada bin
venv\
│
├── Include\
│
├── Lib\
│   │
│   └── site-packages\
│
├── Scripts\
│   ├── Activate.ps1
│   ├── activate
│   ├── activate.bat
│   ├── deactivate.bat
│   ├── pip.exe
│   ├── pip3.10.exe
│   ├── pip3.exe
│   ├── python.exe
│   └── pythonw.exe
│
└── pyvenv.cfg
```

## **Archivo de configuración**

En lugar de buscar el módulo `os` para determinar la ubicación de la biblioteca estándar, el intérprete de Python primero busca un pyvenv.cfgarchivo. Si el intérprete encuentra este archivo y contiene una clave `home`, entonces el intérprete usará esa clave para establecer el valor de dos variables:

* `sys.base_prefix`: contendrá la ruta al ejecutable de Python utilizado para crear este entorno virtual, que puede encontrar en la ruta definida bajo la homeclave en `pyvenv.cfg`.
* `sys.prefix`: apuntará al directorio que contiene `pyvenv.cfg`. 

Este cambio permite efectivamente que el intérprete de Python en su entorno virtual use los módulos de biblioteca estándar de su instalación base de Python mientras apunta a su directorio interno de paquetes del sitio para instalar y acceder a paquetes externos.

De alguna manera por medio de ciertos archivos de configuración del entorno virtual se crean "enlaces" a la biblioteca estándar de Python que se tiene en la instalación local de Python con la cual se creo el entorno. Esto permite ahorrar bastante memoria y que el entorno virtual no pese tanto.

# **Creación y personalización del entorno virtual**

Cabe aclarar que no hace falta instalar nada, esta funcionalidad ya viene integrada con Python.

## **Crear el entorno virtual**
El nombre del entorno virtual suele llamarse `venv` de `virtual enviroment`.
```bash
python -m venv <nombre_de_entorno>
```
Si se quiere crear la carpeta del entorno virtual con un nombre pero que al ejecutar comandos en la consola queremos verla con otro nombre se puede utilizar el parámetro `--prompt`. 
```python
python -m venv venv --prompt="dev-env"
``` 

## **Activar el entorno virtual**
```bash
# Linux
source venv/bin/activate
# Windows
venv/Scripts/activate
```

## **Limpiar instalaciones del entorno virtual**
Si se quiere eliminar todos los paquetes que se instaló en el entorno virtual en vez de borrarlo y volverlo a crear el parámetro `--clear` permite eliminar todos los paquetes instalados.
```bash
python -m venv venv --clear
```

## **Crear varios entornos virtuales a la vez**
La ejecución de este comando crea dos entornos virtuales separados en dos ubicaciones diferentes. 
```bash
python -m venv venv C:\Users\Name\Documents\virtualenvs\venv-copy
```

## **Actualizar las dependencias principales**
Este parámetro permite crear el entorno virtual instalando la última versión de `pip`.
```bash
python -m venv venv --upgrade-deps
```

## **Crear un entorno virtual sin pip instalado como gestor de dependencias**
La instalación de `pip` ocupa bastante espacio, el parámetro `--without-pip` permite crear el entorno virtual sin instalar `pip`. Se debe tener en cuenta que la instalación de paquetes ya no se podrá realizar mediante pip, sino mediante la instalación manual.
```bash
python -m venv venv --without-pip
```

## **Incluir los site-packages**
Cree un nuevo entorno virtual mientras pasa este argumento. Verá que, además de su directorio de paquetes de sitio local, la ruta al directorio de paquetes de sitio de Python base permanecerá en `sys.path`. Tenga en cuenta que si instala paquetes externos adicionales, Python los colocará en el directorio de site-packages de su entorno virtual. Solo obtiene acceso de lectura al directorio de paquetes del sitio del sistema.
```bash
python -m venv venv --system-site-packages
```

**Otros comandos**
* `--symlinks`: intentará crear enlaces simbólicos en lugar de copias. Esta opción no tendrá ningún efecto en las compilaciones de macOS.
* `--copies`: intentará crear copias de sus archivos binarios de Python en lugar de vincularlos a los ejecutables de la instalación base de Python.

## **Actualizar versión de Python para que coincida con la versión de Python del sistema**

Si ejecuta este comando y ha actualizado su versión de Python desde que creó inicialmente el entorno virtual, mantendrá sus bibliotecas instaladas, pero `venv` actualizará los ejecutables para `pip`.
```bash
python -m venv venv --upgrade
```
 
## **Alternativas a venv**

Existen alternativas como:
* `Virtualenv` es un superconjunto `venv` y proporciona la base para su implementación. Es una herramienta poderosa y extensible para crear entornos de Python aislados.
* `Conda` ofrece administración de paquetes, dependencias y entornos para Python y otros lenguajes.

## **Entornos virtuales en producción**

Los entornos virtuales en producción nunca deben ser subidos. Los servicios de hosting para las aplicaciones como Heroku o Google App Engine ya crean automáticamente este entorno virtual.
