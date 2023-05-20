# **Rutas**

Primero tenemos que entender que es un endpoint. Un endpoint se refiere a un punto final o una dirección URL que se expone por una aplicación para que los clientes puedan interactuar con ella a través de una API (Interfaz de Programación de Aplicaciones).

Los endpoints son esencialmente funciones que se ejecutan en el servidor y que proporcionan datos o realizan acciones solicitadas por los clientes. Los clientes pueden enviar solicitudes HTTP a estos endpoints con diferentes métodos como GET, POST, PUT, DELETE, entre otros, para obtener o enviar datos al servidor.

Por ejemplo, un endpoint puede ser una dirección URL que permita a un cliente enviar una solicitud GET para obtener información de un usuario en particular. El backend recibirá la solicitud, procesará la información y devolverá la respuesta al cliente.

Los endpoints son una parte importante del desarrollo de la API porque definen la estructura y el comportamiento de la misma. Además, es importante que los desarrolladores documenten correctamente los endpoints para que los clientes puedan entender cómo interactuar con la API.

# **Creación de una ruta/endpoint en Flask**

Para crear una ruta se utiliza el decorador `@app_name.route(<'url'>, [methods=['method1', 'method2', 'methodN']])`. El parámetro esencial es la url o endpoint y luego podemos especificar el método HTTP que este utilizará.

```python
@app.route('/', methods=['GET'])
def main_view():
    return 'Main view'
``` 
Al acceder a esta ruta podremos ver el texto "Main view" en la pestaña del navegador.

# **Recibir parámetros de un endpoint**

Si queremos podemos agregar parámetros al endpoint para que el usuario nos envíe información a través de esta url. Para ello debemos seguir la siguiente sintaxis:

```python
@app_name.route(<'/<data_type:user_name>'>, [methods=['method1', 'method2', 'methodN']])
```
Es importante especificar el tipo de dato para que solo accedamos al endpoint enviando la información correcta.

```python
@app.route('/<str:user_name>', methods=['GET'])
def main_view(user_name):
    return f'Welcome back {user_name}!'
``` 

Ahora cuando accedamos al endpoint y accedamos a la siguiente ruta por ejemplo `/Juan` veremos el texto "Welcome back Juan!" en la pestaña del navegador.

# **Abreviar métodos  HTTP**

Si queremos ser más directos podemos en vez de definir un endpoint y asignarle el método HTTP de este, directamente podemos utilizar un decorador que utilize un método en específico y lo defina de esta manera.

```python
# Antes
@app.route('/', methods=['GET'])
def main_view():
    return 'Main view'

# Después
@app.get('/')
def main_view():
    return 'Main view'
```
De hecho hasta en la documentación de la librería especifica que la segunda manera es un shortcut de `@app.route('endpoint', methods=[])`

# **Protejer rutas**

Veremos como ejecutar rutas antes y despues que otras para tener un manejo más consiso de las rutas. 

En este ejemplo, se utiliza el decorador `@before_request `para definir una función que se ejecutará antes de todas las demás rutas. Dentro de esta función, puedes colocar el código que deseas ejecutar antes de que se procese la solicitud.

La ruta protegida simplemente está decorada con el decorador `@app.route`, sin embargo, puedes colocar el código que deseas ejecutar en la ruta protegida dentro de la función. Si deseas proteger esta ruta, puedes agregar alguna lógica de autenticación en esta función.

Finalmente, se utiliza el decorador `@after_request` para definir una función que se ejecutará después de todas las demás rutas. Dentro de esta función, puedes colocar el código que deseas ejecutar después de que se procese la solicitud. En este ejemplo, simplemente se devuelve la respuesta de la solicitud, pero puedes modificarla o agregar alguna información adicional en esta función.

```python
# Ruta que se ejecutará antes de todas las demás rutas
@app.before_request
def antes_de_la_solicitud():
    # Aquí puedes colocar el código que deseas ejecutar antes de que se procese la solicitud
    pass

# Ruta protegida
@app.route('/protegido')
def protegido():
    # Aquí puedes colocar el código que deseas ejecutar en la ruta protegida
    # Si la ruta no está protegida, simplemente omite esta sección de código
    pass

# Ruta que se ejecutará después de todas las demás rutas
@app.after_request
def despues_de_la_solicitud(response):
    # Aquí puedes colocar el código que deseas ejecutar después de que se procese la solicitud
    return response
```
