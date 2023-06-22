# Django Admin Panel

Se trata de un panel de administración que permite administrar el proyecto creado. Mediante la ruta `/admin` ya predefinida al crear el proyecto podemos ingresar al panel de administración.

Se necesita un usuario y contraseña. Este usuario y contraseña ya vienen por defecto como user:admin y password:admin pero si se desea crear un usuario administrador se debe ejecutar el siguiente comando.

```
python manage.py createsuperuser
```

Desde el panel de administración se pueden administrar todas las aplicaciones. Por defecto no aparecerá ningun modelo que podamos adiministrar. Para ello es necesario agregar los modelos a la aplicación.

```python
# Archivo myapp > admin.py
from django.contrib import admin
from .models import Project, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
```
El uso del panel de administración es muy intuitivo y para el control sencillo de la aplicación funciona perfectamente.
