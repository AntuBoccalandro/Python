# **Archivos estáticos**

Los archivos estáticos son archivos que no son generados dinámicamente por la aplicación web en el servidor. Es decir, archivos que están desnvinculados del backend. Estos archivos son: 
* Estilos CSS
* Imágenes, videos y audios
* Javascript
* Documentos PDF, Word, etc.

Flask tiene definida una carpeta llamada `static` en la que podemos almacenar estos archivos estáticos. Esta carpeta la tenemos que crear, pero una vez creada Flask ya sabrá que cuando necesite una imágen o estilo CSS irá a buscarlo a esta carpeta. Dentro de esta carpeta también podríamos crear subcarpetas para organizar el contenido, pero lo importante es el nombre de la carpeta `static`.

# **Función url_for**

La función url_for() en Flask se utiliza para generar URLs para diferentes rutas de una aplicación. En lugar de escribir manualmente la URL en el código HTML o en cualquier otro lugar donde se necesite, url_for() permite que Flask genere la URL de manera dinámica, lo que hace que sea más fácil y menos propenso a errores.

La función url_for() toma como argumento el nombre de la función asociada a una ruta en la aplicación y devuelve la URL correspondiente para esa ruta. Por ejemplo, si se tiene una ruta llamada pagina_de_inicio en la aplicación Flask, se puede utilizar url_for('pagina_de_inicio') para generar la URL correspondiente.

Además, si la ruta requiere argumentos (por ejemplo, si se utiliza una variable en la ruta), se pueden pasar los valores de estos argumentos como argumentos adicionales a la función url_for(). Por ejemplo, si se tiene una ruta que toma un argumento llamado usuario, se puede utilizar url_for('ruta_del_usuario', usuario='juan') para generar la URL correspondiente para el usuario "juan".

Esta función es también utilizada para generar URL que apunten a un contenido estático mediante el parámetro `filename`.

**Ejemplo de código para enlazar un archivo CSS a uno HTML**
Archivo styles.css
```css
body {
    color: white;
    background: black;
}
```

Archivo index.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Título de la página</title>
    <link rel='stylesheet' src='{{ url_for('static', filename='css/estilo.css') }}">
</head>
<body>
    <h1>Encabezado principal</h1>
    <p>Este es un párrafo de ejemplo.</p>
</body>
</html>
```

# **Función send_from_directory**

La función send_from_directory() en Flask se utiliza para enviar archivos estáticos (como imágenes, documentos, etc.) al navegador del cliente. Esta función toma como argumentos el nombre del directorio y el nombre del archivo a enviar.

Cabe resaltar que la función send_from_directory() solo debe utilizarse para enviar archivos que se encuentren en un directorio público y no confidencial, ya que de lo contrario se estaría permitiendo el acceso a dichos archivos a cualquier usuario que conozca la ruta.

**Ejemplo para mostrar imágenes**

```python
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/static/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/img', filename)
```
Cabe recalcar que este ejemplo se puede mejorar utilizando la librería os.

```python
from flask import Flask, send_from_directory
from os import getcwd

app = Flask(__name__)

# Creamos la constante con la ruta, de esta manera podemos tener diferentes rutas para cada tipo de archivo. Al tenerlo todo en constantes podemos ver de un vistazo todas las rutas y modificarlas sin necesidad de buscar en todo el código.
PATH_FILES = getcwd() + '/files/'

@app.route('/static/img/<path:filename>')
def serve_image(filename):
    return send_from_directory(PATH_FILES, filename)
```
