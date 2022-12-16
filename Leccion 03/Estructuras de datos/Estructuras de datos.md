# Estructuras de datos

Conocer las diferentes estrcuturas de datos nos permite diferentes soluciones a los problemas y maneras más indicadas y eficientes de resolverlos. El uso de las estrcuturas de datos correcta según la situación es fundamental para resolver un problema de la mejor manera.


# Dictionaries, Maps, and Hash Tables

Los diccionarios también suelen denominarse mapas, hashmaps, tablas de búsqueda o matrices asociativas. Permiten buscar, insertar y eliminar de forma eficiente cualquier objeto asociado a una clave determinada.

![](https://pythondiario.com/wp-content/uploads/2016/12/dictionary2Bimage.png)

## dict

Definición de un diccionario:
```python
dictionary = {
    "number": 10,
    "boolean": [True, False],
    "string": "Hello World",
    "tuple": (1, 2, 3, 4, 5),
    "dict": {"sub_key1": "sub_value1", "sub_key2": "sub_value2"}
}
```

**Los diccionarios**:
* Utilizar los diccionarios de la librería estándar de Python es recomendable y para la mayoría de los casos no será necesario utilizar librerías externas
* Las claves de los diccionarios tienen que ser tipos de datos hasheables, es decir tienen que ser tipos de datos inmutables como tuplas o strings, pero no números o listas.

## Ordered Dict
