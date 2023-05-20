# **Conexión de Python a SQLite3**

SQlite3 es una base de datos sin servidor, sin configuración y sin administrador, lo que significa que no requiere una configuración compleja, ni un servidor de base de datos separado para su funcionamiento.

## **Importar el módulo**

Este módulo ya viene preinstalado con Python, por lo que no hace falta instalarla.

```python
import sqlite3
```

# **Conexión**

```python
import sqlite3

conn = sqlite3.connect('example.db')
```

# **Ejecutar consultas**

Para ejecutar una consulta a la base de datos luego de conectarnos es necesario antes: crear un cursor, ejecutar la consulta, comprometer los cambios y luego cerrar el cursor y la conexión.

```python
import sqlite3


conn = sqlite3.connect('example.db')

# Crear una tabla
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT NOT NULL,
             edad INTEGER NOT NULL);''')

# Insertar datos en la tabla
conn.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 28))

# Leer datos de la tabla
cursor = conn.execute("SELECT id, nombre, edad from usuarios")
for row in cursor:
    print("ID = ", row[0])
    print("Nombre = ", row[1])
    print("Edad = ", row[2])

# Actualizar datos en la tabla
conn.execute("UPDATE usuarios set edad = ? where nombre = ?", (30, "Juan"))

# Eliminar datos de la tabla
conn.execute("DELETE from usuarios where id = ?", (1,))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()
```


# **Operaciones CRUD**

Las operaciones CRUD incluyen:
* Creaciónde registros
* Eliminación de registros
* Actualización de registros
* Lectura de registros

[GUÍA DE SQL ↗](https://github.com/AntuBoccalandro/Databases)

Lo que es importante saber son algunas funciones del módulo que permiten la interacción luego con SQL.

# **Funcionalidades del módulo**


## **Obtener valores de la base de datos**

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

