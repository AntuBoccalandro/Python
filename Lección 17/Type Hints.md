# **Type Hints**

Los type hints son recomedaciones de tipos para las variables, funciones o clases. Por ejemplo, creamos una función que recibe dos parámetros, los type hints nos permitirán escribir el tipo de dato de cada parámetro y que tipo retorna la función. Los type hints nos ayudarán a:
* Especificar el tipo de dato que recomendamos para dicho parámetro, variable o función.
* Mostrar una recomendación en los IDEs a la hora de llamar a la función.
* Ayudar al desarrollador a la hora de pasar los parámetros de función.

Punto a aclarar. Los type hints no es que no nos permitan pasar un parámetro con un tipo diferente

# **Especificar un type hint**

Luego de una variable o parámetro de función se deben colocar dos puntos y seguido de ello un espacio y el nombre del tipo (que es una clase a fin de cuentas).

```python
x: int = 23
x: float = 23.78
x: str = 'Hello'
x: list = [1, 2, 3, 4, 5]
x: dict = {'a': 1, 'b': 2}
```

# **Especificar los parámetros de una función y su retorno**

```python
def suma(a: int, b: int) -> int:
    return a + b
```
Esta función recibe como parámetros a y b, estos deberían ser números enteros y retorna un número entero.

# Especificar interables

Gracias al módulo typing podemos especificar los tipos de los parámetros. Este módulo contiene varias clases que nos permiten especificar el tipo de una manera más específica.

```python
from typing import List

def suma(a: List[int]) -> List[int]:
    return a
```
Como vemos el parámetro a debería ser una lista de enteros. Y la función retorna una lista de enteros también.

# **Lista de tipos más utilizados del módulo Typing**

| **Tipo**                     | **Descripción**                                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `List[tipo]`                   | Lista de "Tipo"                                                                                             |
| Tuple[tipo1, Tipo2, Tipo3]   | Tupla de "tipo", "tipo2", "tipo3". En las tuplas hay que especificar los tipos de cada uno de los elementos |
| `Dict[tipo clave, tipo valor]` | En los diccionarios se debe especificar el "tipo de las claves" y el "tipo de los valores"                  |
| `Iterable[tipo]`               | Un iterable (lista, tupla, string, etc) de cierto "tipo"                                                    |  |
| `Any`                          | Cualquier tipo de dato                                                                                      |

# **Hacer opcionales los tipos**

Mediante la clase Optional[tipo] podemos hacer que el tipo de dato de un parámetro sea opcional.

```python
import typing

def suma(a: int, b: Optional[int]) -> int:
    return a + b
```
En este caso el parámetro b es opcionalmente un número entero, no necesariamente debe ser entero, podríamos pasarle un string como parámetro.

# **Tipo Callable**

El tipo Callable del módulo typing permite especificar que un parámetro es invocable (como una función) e indicar sus parámetros, si es que este tiene.

```python
from typing import Callable

def suma(a: int, b: int) -> int:
    return a + b

def wrapper(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


print(wrapper(suma, 1, 9))
```
La clase Callable recibe una lista con los tipos de datos de los parámetros y luego de ello el tipo de dato que retorna la función.

# **Aceptar varios tipos de datos: Union**

En los Type Hints de Python, Union se utiliza para indicar que un valor puede ser de uno de varios tipos posibles. Permite especificar que una variable o parámetro puede aceptar más de un tipo de datos.

```python
from typing import Callable

def suma(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b
```
En este ejemplo la función `suma` puede recibir como argumentos un tanto un número entero como float, así como también puede retornar alguno de estos dos. 

# **Crear nuestros propios Type Hints a partir de tipos de datos ya existentes**

También podemos crear nuestros propios tipos para adaptarlos a nuestros propios programas.

```python
from typing import Tuple

Vector = Tuple[int, int]

def func(a: Vector, b: Vector) -> Vector:
    return (a[0] + b[0], a[1] + b[1])
```
En este ejemplo he creado un tipo llamado Vector que equivale a una tupla de dos números enteros

# **Crear nuestros propios Type Hints a partir de nuestras propias clases**

**Type Hint sin alías a partir de clase**:
```python
from typing import List

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

def saludar(persona: Persona) -> None:
    print(f"Hola, {persona.nombre}!")
```

**Type Hint con alías a partir de clase**:
```python
from typing import List, TypeAlias

class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

ListaProductos = TypeAlias(List[Producto])
```
En este ejemplo se creó una clase llamada Producto y nuestro Type Hint a partir de ello. Nuestro Type Hint es una lista de instancias de la clase Producto. El alías nos permite utilizar otro nombre en vez del propio de la clase.

# **Alias de tipos ya existentes**

Si se quiere crear un Type Hint de un tipo de dato ya existente se puede crear un alias de ese mismo tipo para que se adapte mejor al programa que se está creando.

```python
from typing import TypeAlias

MyInt = TypeAlias(int)

def multiplicar(a: MyInt, b: MyInt) -> MyInt:
    return a * b
```

# **Verificación de tipos**

Aunque Python no es como otros lenguajes de tipado estático, este no nos arrojará un error si el tipo de dato que recibe una función no es el correcto, por ejemplo que reciba un tipo int y nosostros le pasemos un tipo de dato float. Para realizar esta comprobación de tipos para evitar posibles bugs o errores podemos utilizar módulos como `mypy`.

## **Instalación de mypy**
```bash
pip install mypy
```

## **Comprobación de tipos con mypy**
```bash
mypy <filename>.py
```

Este módulo no mostrará un mensaje si alguno de los datos establecidos por los Type Hints no es correcto. Acá tienes un ejemplo:
```bash
filename.py:10: error: Argument "align" to "headline" has incompatible
                        type "str"; expected "bool"
```

