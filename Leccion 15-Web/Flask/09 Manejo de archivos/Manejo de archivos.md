# **Manejo de archivos**

En esta sección veremos el manejo de archivos con Flask. Aprenderemos como guardar archivos enviados por el usuario y luego guardarlos en una carpeta de la aplicación, aunque también podríamos guardarlo en un servicio de cloud u otro servidor, también aprendermos como mostrar contenido como imágenes o pdfs en la página web, y por último aprederemos como eliminar archivos.

# **Obteniendo archivos enviados por el usuario**

En secciones anteriores vimos que en los formularios el usuario puede ingresar datos y luego nosostros recuperar esos datos, bueno lo mismo pasa con los archivos, solo que cambiaremos algunos parámetros.

## **Guardar archivo de un formulario**
```python
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Esta variable se obtiene de la configuración de la aplicación, convenientemente

# Verificación de tipo de archivo, para evitar archivos con intenciones maliciosas o que interprete nuestro backend
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Chequeo para saber si se recibió un archivo como tal
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # Si el usuario no selecciona un archivo, el navegador envía un archivo vacío sin nombre.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # Guardado como tal del archivo recibido
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

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

    # Iternamos sobre los diferentes archivos subidos y los guardamos uno por uno
    for file in files:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
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
