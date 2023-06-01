# **Renderizar HTML**

Anteriormente dijimos que los archivos estáticos son aquellos que no son generados dinámicamente por el servidor de la aplicación. Ahora aprenderemos como generar archivos html para luego envíarselos al usuario para que los visualize.

La función render_template() de Flask es una función que se utiliza para renderizar archivos HTML y otros archivos de plantillas (por ejemplo, archivos Jinja2) en una aplicación Flask. Esta función es muy útil para generar dinámicamente contenido HTML basado en la información proporcionada por la aplicación.

La sintaxis básica de la función `render_template()` es la siguiente:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

En este ejemplo, se define una ruta principal que renderiza un archivo HTML llamado "index.html". El archivo HTML se encuentra en un directorio llamado "templates" dentro del directorio de la aplicación Flask.

Además de renderizar archivos HTML, la función `render_template()` también puede aceptar argumentos que se utilizan en el archivo de plantilla. Por ejemplo, si se quisiera mostrar una lista de nombres en la página "index.html", se podría hacer lo siguiente:

```python
@app.route('/')
def index():
    nombres = ['Juan', 'María', 'Pedro']
    return render_template('index.html', nombres=nombres)
```

En este ejemplo, se define una lista de nombres y se pasa a la función `render_template()` como un argumento con el nombre "nombres". En el archivo de plantilla, se puede utilizar la sintaxis de Jinja2 para iterar sobre la lista y mostrar cada nombre en la página:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de nombres</title>
</head>
<body>
    <h1>Lista de nombres:</h1>
    <ul>
        {% for nombre in nombres %}
            <li>{{ nombre }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

En este ejemplo, se utiliza la sintaxis de Jinja2 para iterar sobre la lista de nombres y mostrar cada uno de ellos en una lista HTML.

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

# **Template inherritance o herencia de plantillas**

Nos permite crear plantillas que podremos heredar en otros templates con la finalidad de poder reutilizar una interfaz para utilizarla en otros templates. 

En el archivo que será el template que heredaremos es conveniente colocarlo en una carpeta llamada layouts y dentro las plantillas html.

En el archivo template que heredaremos colocaremos el html y luego debajo unos bloques de código de Jinja.

**Archivo base.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <nav>
        <!-- Barra de navegación común a todas las páginas -->
    </nav>
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        <!-- Pie de página común a todas las páginas -->
    </footer>
</body>
</html>

```

Template que quiere tomar las propiedades de la plantilla de la que herede.

**Archivo index.html**:
```html
{% extends "base.html" %}

{% block title %}Título de la página{% endblock %}

{% block content %}
    <h1>Contenido de la página</h1>
    <p>Texto adicional de la página</p>
{% endblock %}
```

En este ejemplo, la plantilla "pagina.html" hereda de "base.html" y sobrescribe el título y el contenido de la página. Cuando Flask renderice la plantilla "pagina.html", Jinja2 buscará bloques que hayan sido definidos en la plantilla base ("base.html") y los reemplazará con el contenido de la plantilla hija ("pagina.html").

