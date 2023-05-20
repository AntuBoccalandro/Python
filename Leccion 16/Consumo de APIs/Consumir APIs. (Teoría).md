# **Consumir APIs con Python**

# **Paso 1: Instalación de bibliotecas**
El siguiente comando instala la librería `requests`.

```
pip install requests
```

# **Paso 2: Importación de bibliotecas**
Una vez instalada la biblioteca `requests`, importémosla en nuestro código Python. Abre tu editor de texto o IDE favorito y crea un nuevo archivo Python. En la parte superior del archivo, agrega la siguiente línea:

```python
import requests
```

# **Paso 3: Realizar una solicitud GET**
Ahora que hemos configurado todo, podemos comenzar a consumir una API. Empecemos con una solicitud GET básica. Utilizaremos el servicio web "JSONPlaceholder" (https://jsonplaceholder.typicode.com/) para hacer solicitudes de ejemplo. Este servicio proporciona datos de prueba en formato JSON. Agrega el siguiente código a tu archivo Python:

```python
response = requests.get('https://jsonplaceholder.typicode.com/posts')
```

En este ejemplo, estamos haciendo una solicitud GET a la URL `'https://jsonplaceholder.typicode.com/posts'`. La función `get()` de la biblioteca `requests` realiza la solicitud y devuelve la respuesta.

# **Paso 4: Manejar la respuesta de la API**
Ahora que hemos realizado la solicitud, vamos a manejar la respuesta de la API. Podemos acceder al código de estado de la respuesta, el contenido y otros detalles. Agrega el siguiente código después de la solicitud GET:

```python
if response.status_code == 200:
    # La solicitud fue exitosa
    data = response.json()  # Obtener el contenido de la respuesta como JSON
    print(data)
else:
    # La solicitud falló
    print('Error:', response.status_code)
```

En este ejemplo, verificamos si el código de estado de la respuesta es 200, lo que indica una solicitud exitosa. Luego, utilizamos el método `json()` de la respuesta para obtener el contenido en formato JSON y lo imprimimos. Si la solicitud falla, simplemente imprimimos el código de estado.

# **Paso 5: Enviar parámetros en una solicitud GET**
A veces, es posible que necesites enviar parámetros en una solicitud GET. Puedes hacerlo agregando los parámetros a la URL. Agrega el siguiente código después del paso 4:

```python
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
```

En este ejemplo, estamos enviando un parámetro llamado `'userId'` con un valor de `1`. La URL resultante será `'https://jsonplaceholder.typicode.com/posts?userId=1'`. La biblioteca `requests` se encargará de construir la URL con los parámetros y enviar la solicitud.

# **Paso 6: Enviar datos en una solicitud POST**
Aparte de las solicitudes GET, también puedes enviar datos en una solicitud POST. Agrega el siguiente código después del paso 5:

```python
data = {
    'title': 'Mi título',
    'body': 'Contenido de mi publicación',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)
```

En este ejemplo, estamos creando un diccionario llamado `data` que contiene los datos que queremos enviar en la solicitud POST. Luego, utilizamos la función `post()` de la biblioteca `requests` para enviar la solicitud a la URL especificada junto con los datos.

# **Paso 7: Manejar autenticación básica**
Si la API requiere autenticación básica, puedes incluir las credenciales en la solicitud. Agrega el siguiente código después del paso 6:

```python
username = 'usuario'
password = 'contraseña'
response = requests.get('https://api.example.com/endpoint', auth=(username, password))
```

En este ejemplo, estamos utilizando el parámetro `auth` en la función `get()` para incluir las credenciales de autenticación básica. Simplemente proporciona el nombre de usuario y la contraseña como una tupla.

# **Paso 8: Manejar cabeceras personalizadas**
A veces, es posible que necesites enviar cabeceras personalizadas en tu solicitud. Puedes hacerlo utilizando el parámetro `headers`. Agrega el siguiente código después del paso 7:

```python
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer mi_token'
}
response = requests.get('https://api.example.com/endpoint', headers=headers)
```

En este ejemplo, estamos creando un diccionario llamado `headers` que contiene las cabeceras personalizadas que deseamos enviar en la solicitud. Luego, utilizamos el parámetro `headers` en la función `get()` para incluir las cabeceras en la solicitud.

# **Paso 9: Manejar errores de solicitud**
Es importante manejar adecuadamente los errores de solicitud en caso de que algo salga mal. Puedes utilizar bloques `try-except` para capturar y manejar excepciones. Agrega el siguiente código después del paso 8:

```python
try:
    response = requests.get('https://api.example.com/endpoint')
    response.raise_for_status()  # Lanza una excepción si la solicitud falla
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as error:
    print('Error de solicitud:', error.response.status_code)
except requests.exceptions.RequestException as error:
    print('Error de conexión:', error)
```

En este ejemplo, utilizamos el método `raise_for_status()` de la respuesta para lanzar una excepción si la solicitud falla con un código de estado no exitoso. Luego, utilizamos bloques `except` para capturar y manejar diferentes tipos de excepciones, como `HTTPError` y `RequestException`.

¡Por supuesto! Aquí tienes más información y técnicas avanzadas para utilizar APIs con Python:

# **Paso 10: Autenticación con tokens de acceso (OAuth2)**
Algunas APIs utilizan OAuth2 para la autenticación. En este caso, necesitarás obtener un token de acceso y utilizarlo en tus solicitudes. Puedes utilizar la biblioteca `requests_oauthlib` para simplificar este proceso. Aquí tienes un ejemplo:

```python
from requests_oauthlib import OAuth2Session

# Configurar los datos de autenticación
client_id = 'tu_client_id'
client_secret = 'tu_client_secret'
authorization_base_url = 'https://api.example.com/oauth/authorize'
token_url = 'https://api.example.com/oauth/token'
redirect_uri = 'http://localhost/callback'

# Crear la sesión OAuth2
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
authorization_url, state = oauth.authorization_url(authorization_base_url)

# Imprimir la URL de autorización y obtener el código de autorización del usuario
print('Por favor, visita la siguiente URL para autorizar la aplicación:')
print(authorization_url)
authorization_code = input('Ingresa el código de autorización: ')

# Obtener el token de acceso
token = oauth.fetch_token(token_url, authorization_response=authorization_code, client_secret=client_secret)

# Utilizar el token de acceso en las solicitudes
headers = {'Authorization': f'Bearer {token["access_token"]}'}
response = requests.get('https://api.example.com/endpoint', headers=headers)
```

Este ejemplo muestra cómo utilizar OAuth2 para obtener un token de acceso y utilizarlo en las solicitudes. Debes reemplazar `tu_client_id`, `tu_client_secret`, `authorization_base_url` y `token_url` con los valores correctos proporcionados por la API que estés utilizando.

**Paso 11: Paginación**
Algunas APIs devuelven conjuntos de datos largos divididos en páginas. Puedes utilizar la paginación para obtener todos los datos de manera incremental. Aquí tienes un ejemplo utilizando la biblioteca `requests`:

```python
base_url = 'https://api.example.com/endpoint'
params = {'page': 1, 'per_page': 50}  # Configurar parámetros de paginación
all_data = []

while True:
    response = requests.get(base_url, params=params)
    data = response.json()
    all_data.extend(data)
    
    if len(data) < params['per_page']:
        break  # Se ha alcanzado la última página
    
    params['page'] += 1

# Utilizar los datos obtenidos
print(all_data)
```

En este ejemplo, utilizamos los parámetros `page` y `per_page` para indicar qué página obtener y cuántos elementos por página. Iteramos sobre todas las páginas hasta que la respuesta devuelva menos elementos que `per_page`, lo que significa que hemos alcanzado la última página.

# **Paso 11: Control de velocidad (Rate Limiting)**
Algunas APIs imponen límites de velocidad (rate limits) para controlar la cantidad de solicitudes que puedes hacer en un determinado período de tiempo. Puedes utilizar la biblioteca `ratelimit` para respetar estos límites. Aquí tienes un ejemplo:

```python
from ratelimit import limits, sleep_and_retry

@sleep_and_retry  # Retry decorator para esperar antes de reintentar
@limits(calls=10, period=60)  # 10 solicitudes por minuto
def make_request():
    response = requests.get('https://api.example.com/endpoint')
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Error:', response.status_code)

# Realizar solicitudes respetando el límite de velocidad
for _ in range(20):
    make_request()
```
En este ejemplo, utilizamos el decorador @limits(calls=10, period=60) para especificar que queremos hacer un máximo de 10 solicitudes por minuto. El decorador @sleep_and_retry se encargará de esperar el tiempo necesario antes de reintentar la solicitud en caso de que se supere el límite de velocidad.

**4. Manejo de errores y excepciones**
Es importante tener en cuenta el manejo adecuado de errores y excepciones al trabajar con APIs. Aquí hay algunas prácticas recomendadas:

* Utiliza bloques try-except para capturar y manejar excepciones, como requests.exceptions.RequestException, requests.exceptions.HTTPError, json.JSONDecodeError, etc.
* Verifica el código de estado de la respuesta (response.status_code) para determinar si la solicitud fue exitosa o no.
* Maneja los errores específicos de la API según la documentación proporcionada. Algunas APIs devuelven códigos de error personalizados en el cuerpo de la respuesta que puedes utilizar para obtener más información sobre el error.
* Utiliza la función response.raise_for_status() para lanzar una excepción en caso de un código de estado no exitoso (por ejemplo, 4xx o 5xx), lo que te permitirá capturar y manejar el error adecuadamente.

**5. Uso de bibliotecas específicas**
Dependiendo de la API que estés utilizando, puede haber bibliotecas específicas disponibles que simplifiquen aún más el proceso de consumo y utilización de la API. Estas bibliotecas pueden proporcionar funciones y métodos adicionales para manejar casos específicos o realizar tareas comunes. Antes de comenzar, verifica si la API que estás utilizando tiene una biblioteca oficial o bibliotecas de terceros recomendadas.


