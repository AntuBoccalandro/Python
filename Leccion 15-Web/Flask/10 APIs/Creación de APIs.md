# **Creación de APIs con Flask**

Primero empecemos definiendo los conceptos básicos.


## **¿Qué es una API?**

Una API (Application Programming Interface) es un conjunto de reglas, protocolos y herramientas que permiten a los desarrolladores interactuar con una aplicación o sistema para obtener o enviar datos y realizar acciones. Existen diferentes tipos de APIs pero la más simple de entender y para emepezar es la API RESTful.

## **¿Qué es una API RESTful?**

Esta API utiliza el protocolo HTTP y sigue una arquitectura basada en recursos. Es ampliamente utilizada en aplicaciones web y móviles. La sigla RESTful se refiere a un estilo de arquitectura de software que se utiliza en las API para construir servicios web. REST (Representational State Transfer) es un conjunto de principios y restricciones que establece cómo los recursos web deben ser definidos y direccionados a través de URIs (Identificadores Uniformes de Recursos) y cómo se deben manipular a través de los métodos HTTP (GET, POST, PUT, DELETE, entre otros).

**Aclaración**: URI es la sigla en inglés de Identificador Uniforme de Recursos (Uniform Resource Identifier). Es un identificador global y único que se utiliza para identificar recursos en la web, como páginas web, imágenes, archivos, servicios web, entre otros.

Un URI consta de tres partes principales:
* Esquema: Especifica el protocolo utilizado para acceder al recurso, como HTTP, HTTPS, FTP, entre otros.
* Autoridad: Especifica la ubicación del recurso, como el nombre de dominio o la dirección IP del servidor.
* Ruta: Especifica la ubicación exacta del recurso dentro del servidor, como el nombre de archivo o la ruta de acceso.

Por ejemplo, la siguiente es una URI que identifica la página principal de la página web de Google: `https://www.google.com/`. En este caso, `https` es el esquema, `www.google.com` es la autoridad y `/` es la ruta que indica la página principal del sitio web.

# **Creación de APIs con Flask**

Esta es una tarea bastante sencilla por si sola, aunque puede complicarse si esta API tiene que hacer consultas a bases de datos o recibir muchas peticiones al momento.

En este ejemplo implementaremos diferentes APIs, una que funcione con los métodos básicos (GET, POST, PUT y DELETE) que se conecte a una base de datos SQL y otra que funcione con una base de datos NoSQL, para este ejemplo utilizaremos MySQL y MongoDB para la no relacional.

## **Flask marshmallow**

Flask Marshmallow es una extensión de Flask que se utiliza para validar y deserializar datos de entrada en Flask. Está basada en Marshmallow, una biblioteca de Python para la serialización y deserialización de datos.

Flask Marshmallow se utiliza para validar y deserializar datos en Flask para asegurarse de que los datos de entrada sean válidos y estén en el formato correcto antes de enviarlos a una base de datos o a una API. También se puede utilizar para serializar datos de salida en el formato adecuado.

Para instalar Flask Marshmallow, puedes usar pip. Ejecuta el siguiente comando en tu terminal:

```bash
pip install flask-marshmallow
```

Para utilizar Flask Marshmallow en tu aplicación Flask, primero debes importarlo y crear una instancia de la clase Marshmallow. A continuación, debes registrar la instancia en tu aplicación Flask. Puedes hacerlo de la siguiente manera:

```python
from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)
```

Una vez que hayas registrado la instancia de Marshmallow en tu aplicación Flask, puedes crear esquemas de Marshmallow para validar y deserializar los datos de entrada. Los esquemas de Marshmallow se definen como clases Python que heredan de la clase marshmallow.Schema. Aquí tienes un ejemplo:

```python
from marshmallow import fields

class UserSchema(ma.Schema):
    id = fields.Integer()
    username = fields.String(required=True)
    email = fields.Email(required=True)
```

En este ejemplo, hemos definido un esquema para validar y deserializar los datos de entrada del usuario. El esquema tiene tres campos: id, username y email. El campo id es un campo entero, mientras que los campos username y email son campos de cadena. Los campos username y email se han definido como obligatorios mediante el uso del argumento required=True.

Una vez que hayas definido un esquema de Marshmallow, puedes utilizarlo para validar y deserializar los datos de entrada en tu aplicación Flask. Puedes hacerlo de la siguiente manera:

```python
from flask import request

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_schema = UserSchema()
    errors = user_schema.validate(user_data)
    if errors:
        return errors, 400
    # Crear el usuario en la base de datos
    return 'Usuario creado correctamente', 201
```

En este ejemplo, hemos definido una vista de Flask que crea un nuevo usuario. La vista utiliza el esquema UserSchema para validar y deserializar los datos de entrada del usuario. Si los datos de entrada no son válidos, la vista devuelve una respuesta con el código de estado HTTP 400 Bad Request y una lista de errores de validación. Si los datos de entrada son válidos, la vista crea un nuevo usuario en la base de datos y devuelve una respuesta con el código de estado HTTP 201 Created.

# **Ejemplo de API de cursos**

Esta API se conectará a una base de datos MySQL y nos permitirá realizar operaciones CRUD sobre esta, agregando, modificando y listando cursos.

## **Archivo de configuración llamado config.py**
```python
class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'S3rv3r'
    MYSQL_DB = 'api_flask'


config = {
    'development': DevelopmentConfig
}
```

## **Archivo de validaciones llamado validaciones.py**
```python
# Valida el código (si es numérico y de longitud 6).
def validar_codigo(codigo: str) -> bool:
    return (codigo.isnumeric() and len(codigo) == 6)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 30 caracteres).
def validar_nombre(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 30)

# Valida que los créditos estén entre 1 y 9.
def validar_creditos(creditos: str) -> bool:
    creditos_texto = str(creditos)
    if creditos_texto.isnumeric():
        return (creditos >= 1 and creditos <= 9)
    else:
        return False
```

## **Archivo de la API como tal llamado app.py**
```python
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config
from validaciones import *


app = Flask(__name__)
conexion = MySQL(app)


@app.route('/cursos', methods=['GET'])
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso ORDER BY nombre ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos = []
        for fila in datos:
            curso = {'codigo': fila[0], 'nombre': fila[1], 'creditos': fila[2]}
            cursos.append(curso)
        return jsonify({'cursos': cursos, 'mensaje': "Cursos listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def leer_curso_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'codigo': datos[0], 'nombre': datos[1], 'creditos': datos[2]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/cursos/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        curso = leer_curso_bd(codigo)
        if curso != None:
            return jsonify({'curso': curso, 'mensaje': "Curso encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


@app.route('/cursos', methods=['POST'])
def registrar_curso():
    if (validar_codigo(request.json['codigo']) and validar_nombre(request.json['nombre']) and validar_creditos(request.json['creditos'])):
        try:
            curso = leer_curso_bd(request.json['codigo'])
            if curso != None:
                return jsonify({'mensaje': "Código ya existe, no se puede duplicar.", 'exito': False})
            else:
                cursor = conexion.connection.cursor()
                sql = """INSERT INTO curso (codigo, nombre, creditos) 
                VALUES ('{0}', '{1}', {2})""".format(request.json['codigo'],
                                                     request.json['nombre'], request.json['creditos'])
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de inserción.
                return jsonify({'mensaje': "Curso registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


@app.route('/cursos/<codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    if (validar_codigo(codigo) and validar_nombre(request.json['nombre']) and validar_creditos(request.json['creditos'])):
        try:
            curso = leer_curso_bd(codigo)
            if curso != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE curso SET nombre = '{0}', creditos = {1} 
                WHERE codigo = '{2}'""".format(request.json['nombre'], request.json['creditos'], codigo)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "Curso actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        curso = leer_curso_bd(codigo)
        if curso != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM curso WHERE codigo = '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Curso eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
```
