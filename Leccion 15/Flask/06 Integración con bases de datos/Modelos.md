# **Modelos**

En términos generales, los modelos de bases de datos permiten:

* Definir la estructura de los datos: Los modelos permiten definir los tipos de datos que se van a almacenar en la base de datos, así como la relación que existe entre ellos. Esto incluye la definición de tablas, columnas, relaciones entre tablas y restricciones en los datos.

* Acceder y manipular los datos: Los modelos proporcionan una capa de abstracción para acceder a los datos en la base de datos, lo que permite a los desarrolladores interactuar con los datos de una manera más fácil y segura. En lugar de tener que escribir consultas de SQL complejas, los desarrolladores pueden usar una API proporcionada por el framework de la aplicación web para interactuar con los datos.

* Validar y asegurar los datos: Los modelos también pueden incluir validaciones y restricciones de datos, lo que ayuda a garantizar que los datos almacenados en la base de datos sean precisos y seguros. Por ejemplo, los modelos pueden validar que un campo de correo electrónico tenga un formato válido o que un campo de contraseña tenga una longitud mínima.

* Simplificar las migraciones de base de datos: Los modelos también pueden facilitar las migraciones de base de datos. Cuando se cambia la estructura de la base de datos, como agregar o eliminar una tabla o una columna, los modelos pueden automatizar el proceso de actualizar la base de datos a la nueva estructura.

Los ORM normalmente tienen una clase que nos permiten crear los modelos de la base de datos así como la conexión a estas. 

El ORM más conocido para el manejo de bases de datos SQl es MySQLAlchemy, este ORM nos permite crear los modelos de la base de datos.

## **Creación del modelo**

En este ejemplo crearemos diferentes modelos para diferentes entidades, el modelo de Usuario y el modelo de Administrador.

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float


engine = create_engine('sqlite:///productos.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Modelo de usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(120), unique=True, nullable=False)
    contrasena = Column(String(100), nullable=False)
    es_admin = Column(Boolean, default=False)


# Modelo de administrador
class Administrador(Base):
    __tablename__ = 'administradores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(120), unique=True, nullable=False)
    contrasena = Column(String(100), nullable=False)
    nivel_acceso = Column(Integer, nullable=False)


# Modelo de producto
class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
```
Adicional a los modelos podríamos agregar un método constructor, de represetación y alguna acción específica del modelo (como por ejemplo en el modelo de productos tener un método add_product() que agregre un nuevo producto, es algo innesesario de hacer ya que podríamos efecutar directamente la consulta, pero el agregar un método le agrega una capa de abstracción que nos permite interactuar con el modelo de una manera más sencilla e intuitiva).
