# urls

Las urls son rutas del proyecto que permite acceder a distintas vistas del proyecto.

En el archivo urls.py del proyecto es donde se crearán las urls del proyecto. 
```python
from django.contrib import admin
from django.urls import path

urlpatters = [
    path('', home),
    path('about/', about),
    path('projects/', projects),
    path('tasks/', tasks)
]
```

Si se tienen varias aplicaciones con cada una de ellas rutas se hace muy poco práctico concetrar las urls de todas las aplicaciones del proyecto en el archivo urls.py. Para ello se creará un archivo urls.py en cada aplicación donde incluiremos la misma sintaxis anterior pero el archivo de urls.py del proyecto se importarán las urls de cada aplicación.
```python
# Archivo myapp > urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', about),
    path('projects/', projects),
    path('tasks/', tasks)
]
```

Incluimos mediante la función include() las urls de la aplicación al archivo de urls.py del proyecto.
```python
# Archivo proyect > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
```
### Params

Los parámetros nos permiten obtener parámetros de una url. Cuando creamos un parámetro para un url está solo se ejecutará si recibe el parámetro especificado, si no Django mostrará un mensaje de error.

Tipos de datos de los parámetros:
* bool
* int
* str
* No secuencias como listas, tuplas o diccionarios

Definir un parámetro
```python
path('hello/<str:name>', home)
```

Si se define un parámetro es neceasrio pasarle el parámetro a la vista para luego operar con el. Si no se quiere operar con este parámetro no será necesario pasarlo como argumento de la vista.

```python
def home(request, name):
    return HttpResponse('Welcome ', name)
``` 
