# Estructura del proyecto

La estrucutra del proyecto es muy importante entenderla, ya que cada carpeta y cada archivo tiene un uso en específico así como una dependencia dentro del proyecto.

### __init__.py

Se trata de un archivo que sirve par indicarle a Python que se trata de un módulo.

### Pycache

Se trata de una carpeta que sirve a modo de caché, no es específico de Django, es más del funcionamiento de Python cuando se ejcutan múltiples archivos. 

### Settings.py

Es donde se configura todo el proyecto de Django. 
DEBUG = True, cuando se pasa a producción se debe poner en False
ALLOWED_HOST = []
SECRET_KEY = seguridad de Django
BASE_DIR = donde se encuentran los directorios del proyecto
INSTALLED_APPS = proyectos de Django donde se incluyen las aplicaciones. S ecrean poryectos donde cada parte del proyecto se divide en aplicaciones. 
MIDDLEWARE = procesado de datos de distintos tipos
DATABASES = las bases de datos a las cuales se encuentra conectado Django. Por defecto se encuentra conectado a un módulo de SQLite3. Uno se puede conectar a otras bases de datos.

### urls.py

Es donde se administran las urls del proyecto. Se pueden crear distintas urls para que el usuario pueda consultarlas y obtener información de cada una de ellas. 

### asgi.py

Sirve para la ejecución de Django para cuando el proyecto esté en producción.

### wsgi.py
