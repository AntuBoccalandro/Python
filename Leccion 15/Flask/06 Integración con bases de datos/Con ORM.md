# **Integración de base de datos con ORM**

Los ORMs nos permiten crear una capa de abstracción sobre la base de datos. Las operaciones sobre la base de datos serán las mismas, aunque si queremos realizar consultas muy complejas a la base de datos siempre podremos recurrir a ejecutar consultas SQL o NoSQL directamente, sin utilizar las funciones que agrege el ORM.


# **Utilización de flask_mysqlalchmey

El ORM más conocido `flask_mysqlalchmey`. Este ORM nos sirve para bases de datos SQL, como MySQL, SQLite3 o PostgreSQL.

Este ORM nos permite crear tanto el modelo de la base de datos como ejecutar las consultas a esta. El módulo "original" se llama MySQLAlchemy, pero la existe una variante de este módulo llamado `flask_mysqlalchmey` que tiene integración con Flask.

## **Conexión**

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
```

## **SQLALCHEMY_DATABASE_URI**

**Aquí se muestran las diferentes url para las diferentes bases de datos**:
* **SQLite3**: `sqlite:///project.db`
* **MySQL**: `mysql://<username>:<password>@<host>/<database>` 
* **PostgreSQL**: `postgresql://<username>:<password>@<host>/<database>` 


## **Creación de Modelos**

```python
# Modelo de usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    correo = db.Column(db.String(120))


# Creación de la tabla
with app.app_context():
    db.create_all()
```

En este ejemplo creamos un modelo simple. Pero SQLAlchmey tiene muchos más tipos de datos y parámetros que le podemos pasar, como una columna de la base de datos que sea de tipo fecha.

## **Operaciones CRUD**

```python
@app.route("/users")
def user_list(): 
    # Listado de usuarios
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return users

@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        # Añadimos un registro nuevo a la base de datos
        db.session.add(user)
        # Concretamos los cambios
        db.session.commit()
        return redirect('/users')

    return render_template("user/create.html")

# 
@app.route("/user/<int:id>")
def user_detail(id):
    # Filtrar un registro por su id. La función get_or_404 retorna un registro y en caso de que este no exista lanza un error 404.
    user = db.get_or_404(User, id)
    return render_template("user/detail.html", user=user)

@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    # Obtener registro a eliminar
    user = db.get_or_404(User, id)

    if request.method == "POST":
        # Eliminamos el usuario específico
        db.session.delete(user)
        # Concretamos los cambios
        db.session.commit()
        return redirect('/users')

    return render_template("user/delete.html", user=user)
```
