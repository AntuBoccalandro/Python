# **Consumir APIs**

Para consumir APIs con Python, necesitamos utilizar una biblioteca que nos permita hacer solicitudes HTTP. Una de las bibliotecas más populares para hacer solicitudes HTTP en Python es la biblioteca requests. Puedes instalarla utilizando pip con el siguiente comando:

```
pip install requests
```

Una vez instalada, podemos empezar a utilizar la biblioteca para hacer solicitudes HTTP a una API. Aquí te muestro un ejemplo de cómo hacer una solicitud GET a una API utilizando la biblioteca requests:

```python
import requests

response = requests.get('https://api.example.com')
print(response.status_code)
print(response.json())
```

En este ejemplo, hacemos una solicitud GET a la URL https://api.example.com utilizando la función get() de la biblioteca requests. La respuesta de la API se almacena en la variable response. Podemos obtener el código de estado de la respuesta utilizando la propiedad status_code, y podemos obtener los datos devueltos por la API utilizando la función json().

## **Trabajando con parámetros de consulta**

Las API a menudo utilizan parámetros de consulta para permitir que los usuarios especifiquen filtros o opciones para las solicitudes. Por ejemplo, una API meteorológica puede permitir que los usuarios especifiquen una ubicación para obtener el pronóstico del tiempo.

Para enviar parámetros de consulta en una solicitud HTTP utilizando la biblioteca requests, podemos pasar un diccionario de parámetros en el argumento params de la función get(). Aquí te muestro un ejemplo:

```python
import requests

params = {
    'q': 'London,UK',
    'appid': 'your_api_key'
}

response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
print(response.json())
```

En este ejemplo, estamos haciendo una solicitud GET a la API del tiempo utilizando la biblioteca requests. Estamos pasando dos parámetros de consulta: q, que especifica la ubicación de la que queremos obtener el pronóstico del tiempo

## **Trabajando con autenticación**

Algunas APIs requieren autenticación para acceder a ellas. Esto puede ser mediante una clave de API o mediante un token de acceso. Para enviar la autenticación en una solicitud HTTP utilizando la biblioteca requests, podemos pasar un diccionario de cabeceras en el argumento headers de la función get(). Aquí te muestro un ejemplo:

```python
import requests

headers = {
    'Authorization': 'Bearer your_access_token'
}

response = requests.get('https://api.example.com', headers=headers)
print(response.json())
```

En este ejemplo, estamos haciendo una solicitud GET a la API utilizando la biblioteca requests. Estamos pasando una cabecera de autenticación Authorization, que contiene nuestro token de acceso.

## **Trabajando con respuestas de paginación**

Algunas APIs utilizan la paginación para limitar la cantidad de datos devueltos en una sola solicitud. Para obtener todos los datos, debemos hacer varias solicitudes y combinar los resultados. Para hacer esto, necesitamos trabajar con la información de paginación devuelta por la API.

Para hacer solicitudes de paginación en una API utilizando la biblioteca requests, podemos utilizar un bucle while para hacer solicitudes adicionales hasta que hayamos recibido todos los datos. Aquí te muestro un ejemplo:

```python
import requests

url = 'https://api.example.com'
params = {
    'page': 1
}
headers = {
    'Authorization': 'Bearer your_access_token'
}

while True:
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    process_data(data)

    if not data.get('next'):
        break

    url = data['next']
```

En este ejemplo, estamos haciendo una solicitud GET a la API utilizando la biblioteca requests. Estamos pasando un parámetro de paginación page, que especifica la página de datos que queremos obtener, y una cabecera de autenticación Authorization, que contiene nuestro token de acceso.

Dentro del bucle while, procesamos los datos devueltos por la API utilizando la función process_data(). Luego, comprobamos si hay más páginas de datos devueltas por la API mediante la clave next en el objeto JSON devuelto por la API. Si hay más páginas, actualizamos la URL de la solicitud para obtener la siguiente página de datos.

## **Conclusión**

En este tutorial, hemos aprendido cómo consumir APIs con Python utilizando la biblioteca requests. Hemos aprendido a trabajar con solicitudes HTTP, parámetros de consulta, autenticación y respuestas de paginación. Con estos conocimientos, deberías ser capaz de consumir la mayoría de las APIs que necesites para tu proyecto en Python.
