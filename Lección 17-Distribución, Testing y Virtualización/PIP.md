# **PIP (Packager Installer for Python)**

El administrador de paquetes estándar para Python es `pip`. Le permite instalar y administrar paquetes que no forman parte de la biblioteca estándar de Python. Cabe aclarar que `pip` se instala automáticamente con la instalación de Python.

En caso de que no esté instalado pip se puede instalar mediante la siguiente guía: [github](https://github.com/pypa/get-pip)

# **Ejecutar pip**

Pip se puede ejecutar como módulo o como un comando del sistema:
* Como módulo: `python -m pip`.
* Como comando del sistema: `pip`.

# **Instalación de paquetes**

**Instalar paquetes en su última versión**
```bash
python -m pip install <package_name>
``` 

**Instalar paquetes especificando su versión**
```bash
python -m pip install <package_name>==<version>
``` 

**Instalar un paquete que no esté disponible**
La url de ejemplo sería reemplazada por la del paquete a instalar. Esto se usa cuando por algún motivo no se puede realizar la instalación específicando el nombre del paquete, esto puede deberse a problemas de acceso denegado a la url de donde se descarga.
```bash
python -m pip install -i https://test.pypi.org/simple/rptree
``` 

**Instalar un paquete desde un repositorio de GitHub**
La url de ejemplo sería reemplazada por la del paquete a instalar.
```bash
python -m pip install git+<github_url>
``` 

# **Actualizar paquetes instalados**

**Actualizar a una versión específica:**
```bash
python -m pip <package_name>==<package_version_to_update> --upgrade
```

**Actualizar un paquete a la última versión:**
```bash
python -m pip <package_name> --upgrade
```

# **Información sobre los paquetes**

**Ver listado de paquetes instalados:**
```bash
python -m pip list
```

**Ver información sobre un paquete específico:**
```bash
python -m pip show <package_name>
```

# **Desintalación de paquetes**
```bash
python -m pip uninstall <package_name>
```
El parámetro -y permite que pip no muestre el cuadro de diálogo donde nos pregunta si estamos seguros que queremos desinstalar el paquete.
```bash
python -m pip uninstall <package_name> -y
```


# **Creación de un archivo con los paquetes necesarios para el proyecto**

Este es un archivo `.txt` que se utiliza para almacenar los paquetes instalados del proyecto (normalmente sobre entornos virtuales). Con este archivo se puede tanto tener un listado de cada paquete y su versión, también permite instalar todos los paquetes desde la terminal, sin necesidad de ir uno por uno instalandolo. 

El nombre del archivo varía pero por conveción se lo suele llamar `requierments.txt`.

**Crear archivo de dependencias:**
```bash
python -m pip freeze > requirements.txt
```

**Si se quiere instalar todos los paquetes de un archivo de requerimientos se utiliza el siguiente comando:**
```bash
python -m pip install -r requirements.txt
```

**Instalar todas las dependecias en su última versión actualizada:**
Si hay una nueva versión disponible para un paquete de la lista, el paquete se actualizará.
```bash
python -m pip install -U -r requirements.txt
```

**Crear archivo de dependencias para producción**
Como nota es importante saber que normalmente se utiliza otro archivo para guardar las dependencias del entorno de producción, ya que muchas veces paquetes como PyTest no son necesarios en un entorno de producción y pueden omitirse. La nomenclatura para este archivo suele ser `requirements_dev.txt` para hacer referencia al los requerimientos durante el desarrollo, y simplemente requierments para el entorno de producción.

```bash
# Archivo requierments_dev.txt
-r requirements.txt
pytest==2.3.1
```
Esto instalará las dependencias tanto escritas en el archivo requierments_dev.txt y además todos los paquetes del archivo requierments (utilizado para el entorno de producción).
```bash
# Comando de instalación
python -m pip install -r requirements_dev.txt
```

**Desinstalar todas las dependencias del archivo requieriments.txt**
Para desintalar las dependencias simplemente se utiliza los comandos ya vistos:
```bash
python -m pip uninstall -r requirements.txt
```
