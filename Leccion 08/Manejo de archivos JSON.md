# **Manejo de archivos JSON con Python**

JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos. Se utiliza para representar datos estructurados en forma de objetos y arrays en texto plano, que pueden ser fácilmente interpretados y manipulados por programas.

La sintaxis de JSON es algo como esto:
```json
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 16
        },
        {
            "firstName": "Bob",
            "age": 18
        }
    ]
}
```

Python tiene un módulo ya incorporado llamado `json` que permite trabajar con este tipo de información.

## **Importamos json**

```python
import json
```

# **Serialización**

La serialización de documentos json hace referencia a las cadenas de bytes, que es la manera en la que se envían documentos de este tipo a través de la red (y la mayoría de documentos también). La deserialización en cambio hace referencia al proceso en el cual convetimos estos bytes a estructuras de datos de Python, o el lenguaje que estemos utilizando.

## **Tabla de conversiones**

| **Python**             | **JSON** |
| ---------------------- | -------- |
| `dict`                 | `object` |
| `list`, `tuple`        | `array`  |
| `str`                  | `string` |
| `int`, `long`, `float` | `number` |
| `True`                 | `true`   |
| `False`                | `false`  |
| `None`                 | `null`   |

## **Método dump**

Este método nos permite volcar estos bytes a un archivo que podamos trabajar de manera cómoda.

```python
import json

# Datos
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# Abrimos el archivo y escribimos los datos en él
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
```

Si abrimos el archivo .json veremos que el contenido es el mismo que la variable data.

## **Método dumps**

Sirve para lo mismo que `dump` pero este no guarda datos en un archivo, si no que un string

```python
import json

# Datos
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

json_string = json.dumps(data)
print(json_string)
# {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}
json_string = json.dumps(data)
print(json_string, indent=4)
# {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
```
El parámetro opcional de indent nos permite identar el string, esto hace que se vea mucho mejor la información.

# **Deserialización**

Ya dijimos que la deserialización es el proceso en el cual convertimos objetos JSON a objetos de Python, ahora veremos como hacerlo.

## **Tabla de conversiones**

| **JSON** | **Python**               |
| ---------- | ---------------------- |
| `object`   | `dict`                 |
| `array`    | `list`, `tuple`        |
| `string`   | `str`                  |
| `number`   | `int`, `long`, `float` |
| `true`     | `True`                 |
| `false`    | `False`                |
| `null`     | `None`                 |

## **Método load**

Este método nos permite deserializar un archivo json.

```python
import json

# Abrimos el archivo y escribimos los datos en él
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)
# {'president': {'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian'}}
```
Como vemos recuperamos los datos del archivo data_file.json y asignamos dichos datos en una variable llamada data.

## **Método loads**

Al igual que con el método dumps este método es para realizar la deserialización de strings y no de archivos.

```python
import json

# Json data in to string
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

data = json.loads(json_string)
print(data)
# {'researcher': {'name': 'Ford Prefect', 'species': 'Betelgeusian', 'relatives': [{'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian'}]}}
```

# **Codificando y descodificando objetos complejos**

Si queremos codificar o descodificar objetos que sean más complejos que arrays, strings o integeres, como lo son los números complejos podemos realizar las siguientes prácticas.

```python
# Creamos el encoder que eredará de json.JSONEncoder
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)


# 
data = json.dumps(2 + 5j, cls=ComplexEncoder)
print(data)
# OUTPUT: '[2.0, 5.0]'
```

# **Codificando y descodificando objetos complejos**

```python
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct


with open("complex_data.json") as complex_data:
    data = complex_data.read()
    numbers = json.loads(data, object_hook=decode_complex)
    print(numbers)

# OUTPUT: [(42+36j), (64+11j)]
```
