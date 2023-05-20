# **Envío de emails**

Se pueden enviar emails de diferentes maneras, utilizando un módulo creado para Flask o un módulo a parte, en este caso veremos la primera (en la sección de automatizaciones veremos la segunda forma).

# **Módulo flask_email**

Este módulo es necesario instalarlo, esto mediante pip:
```python
pip install Flask-Mail
```

Ahora importaremos la parte que nos interesa del módulo:
```python
from flask_mail import Mail, Message
```

Ahora realizaremos las configuraciones de la aplicación:
```python
app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tu_cuenta@gmail.com'
app.config['MAIL_PASSWORD'] = 'tu_contraseña_de_aplicación'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
```
NOTA: la contraseña de aplicación debe ser generada desde el panel de administración de la cuenta de google que envíe este correo. Hay que dirigirse a la sección de contraseñas de aplicaciones y luego generar una nueva con la categoría de otro, el nombre que le coloquemos a esta categoría es indiferente, es solo para identificarla.

**Enviar el email**:

No es necesario crear una ruta para enviar un correo para el ejemplo lo mostramos así. La otra opción que hay es crear una carpeta utils en la aplicación y crear un módulo que se encarge de enviar los mails y, por ejemplo, cuando nos dirigimos a la ruta de resetear contraseña ejecutemos la función de este módulo que envíe los mails de restabelecimiento de contraseña (que tenga un cuerpo del email ya definido).

```python
@app.route('/send/<email>')
def enviar_correo(email):
    mensaje = Message('Correo de prueba', sender='tu_cuenta@gmail.com', recipients=[email])
    mensaje.body = 'Este es un correo de prueba enviado desde Flask'
    mail.send(mensaje)
    return 'Correo enviado!'
```

**Enviar HTML en el mail**

Si queremos estilizar el email podemos utilizar html en el cuerpo del mail.
```python
mensaje = Message('Correo de prueba', sender='tu_cuenta@gmail.com', recipients=[email])
    mensaje.html = '<h1>Este es un correo de prueba enviado desde Flask</h1>'
    mail.send(mensaje)
```


**Enviar HTML de un archivo en el mail**

```python
with app.open_resource("ruta_al_archivo.html") as archivo:
    contenido_html = archivo.read().decode('utf-8')
mensaje = Message('Correo de prueba con HTML desde un archivo', 
                  sender='tu_cuenta@gmail.com', 
                  recipients=['destinatario@gmail.com'])
mensaje.html = contenido_html
mail.send(mensaje)
```



