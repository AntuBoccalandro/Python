# **Jinja**

Jinja es un motor de plantillas rápido, expresivo y extensible. Los marcadores de posición especiales en la plantilla permiten escribir código similar a la sintaxis de Python. Se le pasan datos a la plantilla para renderizar el documento final.

Jinja nos permite incrustar variables, loops y condicionales en los templates. Por medio de jinja podemos desarrollar una cierta lógica dentro de los documentos html.

DOCUMENTACIÓN OFICIAL: https://jinja.palletsprojects.com/en/3.1.x/ 

### **Variables**

```python
{{project}}
```

### **Condicionales**

```python
# If
{% if project == 'Project 1' %}
{% endif %}

# If-else
{% if project == 'Project 1' %}
{% else %}
{% endif %}
```

### **Loops**

```python
{% for project in projects %}
{% endfor %}
```

Esta es la sintaxis de las variables, loops y condicionales. Pero es necesario pasarle al template las variables. Esto se puede realizar mediante la siguiente sintaxis.

```python
def home(request, name):
    return render(request, 'home.html', {
        'name': name
    })
```

### **Comentarios**

```python
{# This is a comment #}
```

