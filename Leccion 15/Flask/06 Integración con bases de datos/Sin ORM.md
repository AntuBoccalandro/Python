# **Integración de base de datos con ORM**

Veremos las diferentes bases de datos con las cuales podemos integrar nuestra aplicación.

# **SQLite3**

Esta base de datos es muy simple pero es útil para proyectos simples y pequeños.

## **Conexión**

```python
from flask import Flask
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('your database path.db')
```
Estas serían las configuraciones de la base de dato, pero para concer como tratar con este tipo de base de dato recomendamos leer la sección de [manejo de bases de datos con Python con SQLite3 ↗](../../Leccion%2013/SQLite3/SQLite3.md)

# **MySQL**

Utilizaremos el módulo `flask-mysql` que lo instalaremos mediante el comando `pip install flask-mysql`.

## **Conexión**


```python
from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'my database host'
app.config['MYSQL_DATABASE_USER'] = 'my database user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your password'
app.config['MYSQL_DATABASE_DB'] = 'my database name'
app.config['MYSQL_DATABASE_PORT'] = 'my database host port'

mysql.init_app(app)
```
Estas serían las configuraciones de la base de dato, pero para concer como tratar con este tipo de base de dato recomendamos leer la sección de [manejo de bases de datos con Python con MySQL ↗](../../Leccion%2013/MySQL/MySQL.md)

# **PostgreSQL**



```python
import psycopg2
from flask import Flask


app = Flask(__name__)


# Conexión a la base de datos
conn = psycopg2.connect(
    host='Your host',
    database='Your database name',
    user='Your user of database',
    password='Your database pasword',
    port=xxxx
  )
```
Estas serían las configuraciones de la base de dato, pero para concer como tratar con este tipo de base de dato recomendamos leer la sección de [manejo de bases de datos con Python con PostgreSQL ↗](../../Leccion%2013/PostgreSQL/PostgreSQL.md)

