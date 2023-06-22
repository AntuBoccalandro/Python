# Template inherritance

Nos permite crear plantillas que podremos heredar en otros templates con la finalidad de poder reutilizar una interfaz para utilizarla en otros templates. 

En el archivo que será el template que heredaremos es conveniente colocarlo en una carpeta llamada layouts y dentro las plantillas html.

En el archivo template que heredaremos colocaremos el html y luego debajo unos bloques de código de Jinja.
```html
<h1> Título heredado </h1>

{% block content%}
{% endblock%}
```

Template que quiere tomar las propiedades de la plantilla.
```html
{% extends '<ruta del archivo html>' %}

{% block content%}

<h1> Título heredado </h1>
<!-- Content -->

{% endblock%}
```
