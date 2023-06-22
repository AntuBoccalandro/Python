# Formularios

Los formularios son esenciales para cualquier aplicación para que el usuario pueda enviar datos para que luego el Back-end los procesee para devolver datos denuevo al usuario.

Django permite recibir los datos de formularios creados manualmente pero también incluye maneras de crear formularios mediante herramientas del mismo lenguaje.

### Creación de formularios con Django

Primero es necesario que en la aplicación se cree un nuevo archivo llamado forms.py. En este archivo importaremos desde `django`, `forms`.

```python
touch forms.py
```

```python
# myapp > forms.py
from django import forms
```
