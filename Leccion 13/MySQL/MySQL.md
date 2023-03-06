# Conexión de Python a MySQL

MySQL es una base de datos de tipo SQL. Python incluye diferentes módulos que permiten conectarnos a MySQL.

# Instalación de mysql-connect-python

Este módulo permite la conexión con una base de datos de tipo MySQL. Incluye funcionalidades para conectarse, obtener registros y ejecutar consultas. Es importante saber que no es un ORM, para ello existen módulos como SQLAlchemy.

Se instala mediante el comando:
```shell 
pip install mysql-connector-python
```

## Importar el módulo

```python
import mysql.connector
```

# Conexión

```python
conn = mysql.connector.connect(
    user='Your user of database',
    password='Your database pasword',
    database='Your database name',
    host='Your host',
    port=xxxx
)
```

# Ejecutar consultas

Para ejecutar una consulta a la base de datos luego de conectarnos es necesario antes: crear un cursor, ejecutar la consulta, comprometer los cambios y luego cerrar el cursor y la conexión.

```python
conn = mysql.connector.connect(
    user='Your user of database',
    password='Your database pasword',
    database='Your database name',
    host='Your host',
    port=xxxx
)

# Create a cursor
cursor = conn.cursor()

# Execute the query
cursor.excecute('SELECT * FROM table')

# Commit the query
cursor.commit()

# Close the cursor
cursor.close()

# Close the connection
conn.close()
```


# Operaciones CRUD

Las operaciones CRUD incluyen:
* Creaciónde registros
* Eliminación de registros
* Actualización de registros
* Lectura de registros

Las operaciones CRUD y el resto de consultas SQL se realizan de la misma manera que el la terminal o adminstrador de PostreSQL ya que el módulo `psycopg2` no es un ORM y se ejecutan las consultas SQL directamente estas se realizan de la misma manera en todos los lenguajes SQL con algunas salvedades de cada uno. 

[GUÍA DE MYSQL ↗](https://github.com/AntuBoccalandro/Databases)

Lo que es importante saber son algunas funciones del módulo que permiten la interacción luego con SQL.

# Funcionalidades del módulo


## Obtener valores de la base de datos

Una vez establecida la conexión y creado el cursor se pueden utilizar estos tres métodos:

* `fetchone`: devolverá la primera fila del resultado.
  
    ```python
    print(cursor.fetchone())
    
    # ('John', 'Highway 21')
    ```

Como se puede ver ejemplificado en código se ve claramente la diferencia entre los tres métodos.

* `cursor.fetchall()` obtiene todas las filas del resultado de una consulta. Devuelve todas las filas como una lista de tuplas. Si no hay ningún registro, se devuelve una lista vacía.
  
    ```python
    print(cursor.fetchall())
    
    # ('John', 'Highway 21')
    # ('Peter', 'Lowstreet 27')
    # ('Amy', 'Apple st 652')
    # ('Hannah', 'Mountain 21')
    # ('Michael', 'Valley 345')
    # ('Sandy', 'Ocean blvd 2')
    # ('Betty', 'Green Grass 1')
    # ('Richard', 'Sky st 331')
    # ('Susan', 'One way 98')
    # ('Vicky', 'Yellow Garden 2')
    # ('Ben', 'Park Lane 38')
    # ('William', 'Central st 954')
    # ('Chuck', 'Main Road 989')
    # ('Viola', 'Sideway 1633')
    # ('Michelle', 'Blue Village') 
    ```

* `cursor.fetchmany([size])` devuelve el número de filas especificado por el argumento size. Cuando se llama repetidamente, este método obtiene el siguiente conjunto de filas de un resultado de consulta y devuelve una lista de tuplas. Si no hay más filas disponibles, devuelve una lista vacía.
  
    ```python
    print(cursor.fetchmany(10))
    
    # ('John', 'Highway 21')
    # ('Peter', 'Lowstreet 27')
    # ('Amy', 'Apple st 652')
    # ('Hannah', 'Mountain 21')
    # ('Michael', 'Valley 345')
    # ('Sandy', 'Ocean blvd 2')
    # ('Betty', 'Green Grass 1')
    # ('Richard', 'Sky st 331')
    # ('Susan', 'One way 98')
    # ('Vicky', 'Yellow Garden 2')
    ```


* `cursor.fetchone()` devuelve un único registro o None si no hay más filas disponibles.
    ```python
    print(cursor.fetchone())
    
    # ('John', 'Highway 21')
    ```

Como se puede ver fácilmente en los ejemplos de código las diferencias entre los tres métodos.

NOTA: como nota adicional se puede observar que cuando llamamos a cuaquiera de estos métodos estos nos retornan listas de tuplas que podemos recorrer para realizar acciones o visualizaciones de los datos.

