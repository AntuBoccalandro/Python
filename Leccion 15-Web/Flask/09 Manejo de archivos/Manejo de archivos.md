# **Manejo de archivos**

En esta sección veremos el manejo de archivos con Flask. Aprenderemos como guardar archivos enviados por el usuario y luego guardarlos en una carpeta de la aplicación, aunque también podríamos guardarlo en un servicio de cloud u otro servidor, también aprendermos como mostrar contenido como imágenes o pdfs en la página web, y por último aprederemos como eliminar archivos.

# **Obteniendo archivos enviados por el usuario**

En secciones anteriores vimos que en los formularios el usuario puede ingresar datos y luego nosostros recuperar esos datos, bueno lo mismo pasa con los archivos, solo que cambiaremos algunos parámetros.

## **Guardar archivo de un formulario**
```python
from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect
from os import getcwd


app = Flask(__name__)

# Ruta donde almacenaremos los archivos.
PATH = getcwd()+'\\files\\'


# Ruta para subir los arhivos
@app.route('/', methods=['GET'])
def upload():
    return render_template('index.html')


# Ruta para guardar los archivos. Lo recibimos del formulario y luego lo guardamos en una carpeta de la aplicación.
@app.route('/save', methods=['POST'])
def save_file():
    files = request.files['nameofFile']
    files.save(PATH+files.filename)
    return redirect(url_for('upload'))


if __name__ == '__main__':
    app.run(debug=True)
```

## **Guardar varios archivos al mismo tiempo**

Para guardar varios archivos al mismo tiempo debemos cambiar un parámetro del selector de archivos en el formulario html, ya que por defecto no nos deja seleccionar más de un archivo.

**Archivo formulario.html**
```html
<form action="/save" method="POST" enctype="multipart/form-data">
    <!-- El atributo multipart nos permite seleccionar más de un archivo -->
    <input type="file" name="files" mutipart>
</form>
```

**Archivo app.py**
```python
# Ruta para guardar los archivos. Lo recibimos del formulario y luego lo guardamos en una carpeta de la aplicación.
@app.route('/save', methods=['POST'])
def save_file():
    # El método getlist nos permite obtener una lista de los archivos envíados a través del formulario
    files = request.files.getlist('files')

    # Iternamos sobre los diferentes archivos subidos
    for file in files:
        file.save(os.path.join('C:\\Users\\Usuario\\Desktop\\Test Flask Forms\\Flask Test 1\\files\\', file.filename))
    
    return redirect(url_for('upload'))
```

## **Validación de archivos**

Si queremos mostrar unicamente cierto/s tipo de archivo que se pueda subir al formulario podemos agregar un atributo al input del formulario.

```html
<form action="/save" method="POST" enctype="multipart/form-data">
    <!-- Separamos por comas las extenciones de archivo -->
    <input type="file" accept=".jpg, .jpeg, .png" >
</form>
```

## **Guardar carpetas**

Hasta ahora si queríamos subir varios archivos teníamos que seleccionarlos, pero si estoy creado una aplicación donde el usuario debe subir carpetas, como podemos hacer para subir todo el contenido de esta al servidor.

**Formulario html**:
```html
<form action="/save" method="POST" enctype="multipart/form-data">
    <input type="file" name="file" multipart>
</form>
```

**Backend en Python**:
```python

```
