#  Seguridad en las bases de datos

Estos conceptos estan sobre todo relacionado a las páginas web.

# Credenciales resguardadas

Las variables de entorno sirven para resguardar las credenciales de la base de datos. Además de algunas configuraciones que pueden ayudarnos a mantener la seguridad de nuestra base de datos.

## Instalación del módulo dotenv

```bash
pip install python-dotenv
```

## Creamos un archivo llamado .env
```text
DB_TOKEN='your password'
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


# Verificación de datos



# Evitar SQL-Injection

## ORMs

Para evitar SQL-Injection podemos utilizar un ORM, ya que este viene con este problema solucionado por el mismo ORM como SQLAlchemy o Peewee. Aunque siempre es bueno utilizar un ORM para evitar este tipo de vulnerabilidades es recomendable leer la documentación para asegurarnos de que este incluya algún sistema anti SQL-Injection.

## String Scape

También podemos realizar un escapado de strings en los formularios donde se ingresen datos. Al realizar un escapado de strings evitamos que el texto ingresado a través de formularios sean código javascript o SQL que puedan ser interpretados por el Back-end y produzcan cambios en este.

```javascript
function escapar(){
	document.getElementById("textoescapado").value = escape(document.getElementById('texto').value);
}
``` 

# Hashear datos sensibles de la base de datos

Si se quiere almacenar datos sensibles en la base de datos

## 

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
