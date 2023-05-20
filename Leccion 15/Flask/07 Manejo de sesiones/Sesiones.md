# **Manejo de sesiones**

El manejo de sesiones es fundamental para la creación de aplicaciones. Las sesiones son útiles para mantener la autenticación del usuario y para almacenar información temporal que se necesita durante varias solicitudes. Por ejemplo, un sitio web puede utilizar sesiones para almacenar el contenido de un carrito de compras, para que el usuario pueda agregar y eliminar productos mientras navega por el sitio web.

# **Implementación con Flask**

```python
from flask import Flask, request, render_template, url_for, jsonify, session, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = 'Mi_llave_secreta'


# Ruta raíz
@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho login {session["username"]}'
    return 'No ha hecho login'


# Ruta para hacer login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        # Agregar el usuario a la sesión
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')


# Ruta para hacer logout
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


@app.route('/saludar/<nombre>')
def saludar(nombre):
    # Comprobamos que el usuario haya iniciado sesión para mostrar esta ruta
    if session['username']:
        return f'Saludos {nombre}'
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
```

**Aclaraciones**:
La configuración app.secret_key es una cadena secreta utilizada por Flask para proporcionar seguridad a las sesiones y otros aspectos de la aplicación web. La clave secreta se utiliza para firmar los datos almacenados en las cookies del usuario, lo que impide que un usuario malintencionado manipule o falsifique los datos de sesión.




