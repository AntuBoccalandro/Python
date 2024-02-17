#  Seguridad en las bases de datos

Estos conceptos estan sobre todo relacionado a las páginas web y como programar estas de la manera más seguras posibles. Para evitar la filtración de datos de nuestra aplicación, que modifiquen los registros, etc. En general, moficaciones en nuestra base de datos por parte de terceros.

# Credenciales resguardadas

Las variables de entorno sirven para resguardar las credenciales de la base de datos. Además de algunas configuraciones que pueden ayudarnos a mantener la seguridad de nuestra base de datos.

## Instalación del módulo dotenv

```bash
pip install python-dotenv
```

## Creamos un archivo llamado .env
```text
DB_TOKEN='your encrypted password'
```

## Archivo de Python
```python
import os
from dotenv import load_dotenv


# Carga todo el contenido de .env en variables de entorno
load_dotenv()  

DB_TOKEN = os.environ.get("DB_TOKEN", "")  
```
Es importante saber que los archivos .env no deben ser subidos al servidor ya que esto resultaría un fallo de seguridad importante. 

# Evitar SQL-Injection
Para evitar un *SQL Injection Attack* y protejer nuestro sitio web (hecho con Flask, Django, etc) de manipulaciones de los datos por parte de terceros veremos las consideraciones de seguridad a tener en cuenta. Pero primero veamos por que medios se puede efectuar este tipo de ataque. 

Los *SQL Injection Attack* se puede efectuar a través de:
* Formularios, ya sean estos de autenticación o un formulario para realizar la carga de datos (como publicaciones, artículos, etc)
* A través de URLs envíadas a la aplicación web en el cual los parámetros de la query se envíen a través de la propia URL por el método GET
* Documentos que se carguen en la aplicación y que sean luego interpretados por el servidor, retornando datos o realizando acciones que no queremos. Tales como devoler la lista de credenciales de usuarios, que nos eliminen los registros de nuestro sitio web, etc.

## Uso de ORMs
Para evitar SQL-Injection podemos utilizar un ORM, ya que este viene con este problema solucionado por el mismo ORM como SQLAlchemy o Peewee. Aunque siempre es bueno utilizar un ORM para evitar este tipo de vulnerabilidades es recomendable leer la documentación para asegurarnos de que este incluya algún sistema anti-SQL-Injection.

# Hashear datos sensibles de la base de datos
Si se quiere almacenar datos sensibles en la base de datos, tales como contraseñas y en general cualquier tipo de credenciales de usuarios o de la propia aplicación es recomendable encriptar estos datos y luego, ya sí, guardarlos en la base de datos.

```python
from werkzeug.security import generate_password_hash, check_password_hash

input_text = input('Enter your password: ')

# Opciones de escriptación para texto 
# generate_password_hash(text, algorithm, length)
texto_encriptado1 = generate_password_hash(texto, 'sha256', 30)

# Checkeamos que la contraseña introducida por el usuario sea igual que su hash
print(f'''
	Contraseña introducida: {input_text}
	Contraseña encriptada: {texto_encriptado1}
	La contraseña ingresada conincide con su hash? {check_password_hash(texo_encriptado, input_text)}
''')  

# Enter your password: Esta no es mi contraseña
# Contraseña introducida: Esta no es mi contraseña
# Contraseña encriptada: 260000$2gQOeu3C5EtvSWWq$7b34afcbe0fa6444433fc2c230ec1d8110c4001db90859dfb6832fe993b666f2
# False
```

**Opciones de encriptación:**
* sha256
* pbkdf2:sha256
* pbkdf2:sha256
* pbkdf2:sha256:30

## String Scape en Python
Para evitar que por medio de los formularios de nuestro sitio web podemos realizar un escapado de string. En Python esto se puede hacer de la siguiente manera:
```python
from markupsafe import escape

not_escaped_param = "'; DROP TABLE users; --" # "'; DROP TABLE users; --"
escaped_param = escape(not_escaped_param) # &#39;; DROP TABLE users; --
```
Como vemos, al escapar el string la comilla simple (') se a reemplazado por su equivalente escapado. Lo veremos igual en el HTMl pero no se interpretará. Pero esta solución no es definitiva, solo puede hacer de un filtrado más de cara al atacante. Los puntos siguientes conforman los más importantes.

También se pueden utilizar listas negras y blancas para la validación de inputs en un formulario. Además de definir bien los inputs en el HTMl, pero estos son fácilmente modificables.

## String Scape en Javascript
También podemos realizar un escapado de strings en los formularios donde se ingresen datos. Al realizar un escapado de strings evitamos que el texto ingresado a través de formularios sean código javascript o SQL que puedan ser interpretados por el Back-end y produzcan cambios en este.

```javascript
function escapar(){
	document.getElementById("textoescapado").value = escape(document.getElementById('texto').value);
}
``` 

## Realizar consultas a la base de datos de manera segura
Si realizamos las consultas manualmente a través de SQL, escribiendo la misma en dicho lenguaje, es necesario tener algunas consideraciones a la hora de pasar los parámetros a nuestra consulta. Ya que podríamos estar pasando de manera insegura los parámetros a nuestra consulta y esto ocacionar que nos cuelen un *SQL Injection Attack*. A continuación vemos las maneras incorrectas y correctas de realizar queries a nuestra DB.

```python
# BAD EXAMPLES. DON'T DO THIS!
cursor.execute("SELECT admin FROM users WHERE username = '" + username + '")
cursor.execute("SELECT admin FROM users WHERE username = '%s' % username)
cursor.execute("SELECT admin FROM users WHERE username = '{}'".format(username))
cursor.execute(f"SELECT admin FROM users WHERE username = '{username}'")
```

```python
# SAFE EXAMPLES. DO THIS!
cursor.execute("SELECT admin FROM users WHERE username = %s'", (username, ))
cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username})
```

## Uso de listas blancas sobre las listas negras

### Lista Blanca:
Una lista blanca especifica qué elementos son permitidos o válidos. Todos los demás elementos se consideran potencialmente peligrosos y son rechazados.

```python
# Lista blanca de nombres de usuario permitidos
whitelist_usernames = ['alice', 'bob', 'charlie']

# Función para verificar si un nombre de usuario está en la lista blanca
def is_valid_username(username):
    return username in whitelist_usernames
```

En este ejemplo, solo los nombres de usuario `alice`, `bob` y `charlie` serían considerados válidos. Cualquier otro nombre de usuario sería rechazado.

### Lista Negra:
Una lista negra especifica qué elementos deben ser evitados o rechazados. Todo lo que no esté en la lista negra se considera válido.

```python
# Lista negra de caracteres especiales que deben ser evitados
blacklist_special_characters = ['<', '>', '"', "'", ';', '--', '/*', '*/']

# Función para verificar si un string contiene caracteres especiales de la lista negra
def contains_special_characters(input_string):
    for character in blacklist_special_characters:
        if character in input_string:
            return True
    return False
```

En este ejemplo, se considera que cualquier string que contenga alguno de los caracteres especiales listados en `blacklist_special_characters` es potencialmente peligroso y debe ser rechazado.

Es importante tener en cuenta que las listas negras pueden ser menos seguras que las listas blancas, ya que es difícil prever y enumerar todos los posibles valores o caracteres peligrosos. Por lo tanto, **siempre es recomendable utilizar listas blancas siempre que sea posible** para garantizar una protección más sólida contra vulnerabilidades.

## Mantener actualizadas las tecnologías
Mantener actualizadas las librerías, frameworks, bases de datos y en general cualquier tecnología que utilice nuestra aplicación es recomendable para evitar problemas de seguridad. Asegúrate de que tu servidor se encuentre actualizado, los programas en este también, y sobre todo las tecnologías que uses en la aplicación alojada.

## Tener bien definidos los permisos de cada tipo de usuario
Es crucial que cada tipo de usuario en tu aplicación, como podrían ser: administrador, comprador, vendedor, moderador, etc; deben tener los mínimos permisos necesarios para desempeñar su rol. Es decir, el administrador o creador tendrá todos los permisos. Pero si el comprador (entendiéndolo en un contexto de un E-Commerce como aquella cuenta de usuario que solo puede comprar productos) tiene permisos para poder editar registros, crear publicaciones, posts, etc, aunque este no tenga una cuenta de vendedor podría ser una posible entrada para realizar ataques a la aplicación. Así que siempre mantiene bien definidos los permisos y aquellas acciones que puede realizar cada tipo de usuario.

## Realizar consultas parametrizadas y procedimientos almacenados
Utilizar consultas parametrizadas y procedimientos almacenados es una práctica recomendada en el desarrollo de aplicaciones para mejorar la seguridad, la legibilidad del código y el rendimiento de las consultas SQL. Estas técnicas ayudan a mitigar los riesgos de SQL Injection y a mejorar la robustez y la eficiencia de tu aplicación.

# Limitar la visibilidad de los resultados
Adicionalmente a los puntos anteriores, resulta interesante el limitar los resultados que se muestran en la aplicación. Esto prevendrá la filtración de todos los datos de nuestra base de datos por ejemplo. Para ello existe un parámetro en los ORMs o en la consultas SQL llamado `LIMIT`.

