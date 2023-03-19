# **Context managers**

En Python existe una Keyword llamada `with` que permite ahorrarnos algunas líneas de código y escribir código más Pythonic. 


**Ejemplo de uso de un context manager**:

```python
with open('file.txt') as file_obj:
    print(file_obj.read())
```

**Ejemplo de la misma operación sin context manager**
```python
file_obj = open('file.txt')
try:
    print(file_obj.read())
finally:
    file_obj.close()
```

Como se puede observar al utilizar el context manager `with` nos ahorramos varias líneas de código y además queda más legible.


# **Gestores de contexto con clases**

Los gestores de contexto nos permiten ahorrarnos código. Por ejemplo al abrir un archivo, etc. En Python existen los métodos `__enter__` y `__exit__` que nos permiten trabajar con este tipo de funcionalidad.

Primero veamos la teoría:
* **__init__(self, params)**: la función init
* **__enter__(self)**: se ejecuta automáticamente se entra al bloque with.
* **__exit__(self, exc_type, exc_value, traceback)**: se ejecuta siempre al final del bloque with, aunque ocurra una excepción este método se ejecutará.
  * exc_type: Tipo de excepción que fue lanzada. En nuestro ejemplo sería <class 'Exception'>
  * exc_value: Valor de la excepción en el caso de que fuera proporcionado.
  * traceback: Objecto traceback con más información acerca de la excepción.

**Creando nuestro propia clase que permita al uso del context manager with**:
```python
class MiClaseFichero:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def __enter__(self):
        self.fichero = open(self.nombre_fichero, 'w')
        return self.fichero

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichero:
            self.fichero.close()


with MiClaseFichero('file.txt') as fichero:
    print(fichero.read())
```
Lo que está sucediendo es lo siguiente:
* En el `__init__` guardamos el nombre del fichero que queremos crear, nada nuevo.
* En el `__enter__` creamos un fichero, lo almacenamos en nuestra clase, y devolvemos la referencia que será usada dentro del with.
* Por último en el `__exit__` cerramos el fichero si estaba abierto.

# **Definiendo nuestros propios context managers**

## **Gestores de contexto con decoradores**

Si no queremos utilizar programación orientada a objetos o simplemente implementar esta solución implica crear código innesesario o que se podría reducir, podemos utilizar el decorador `@contextmanager`.

```python
from contextlib import contextmanager

@contextmanager
def gestor_fichero(nombre_fichero):
    try:
        fichero = open(nombre_fichero, 'w')
        yield fichero
    finally:
        fichero.close()


with gestor_fichero('file.txt') as fichero:
    print(fichero.read())
```

Como puedes ver, el contenido del `try` sería el equivalente al contenido del `__enter__` y el `finally` al del `__exit__`. Una vez tenemos definida nuestra función, podemos usarla de la misma forma que hemos visto anteriormente. Para finalizar podemos ver que se hace uso del generador `yield` este lo utilizamos para almacenar el archivo abierto en esta variable, pero sin producir un desbordamiento de memoria en caso de que el fichero abierto sea muy grande.





