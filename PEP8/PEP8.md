# PEP8

PEP8 es una guía de estilo de código de Python para escribir código con un estilo estandarizado que lo haga legible y entendible a la vez que visualmente limpio. Esta guía fue escrita por Guido Van Rossum. La idea de PEP8 es que al estandarizar la manera en la cuál se escribe código de Python esto hace que cualquier desarrollador pueda entender el código así como el propio desarrollador. 

### Nombres de objetos de Python

Cualquier tipo de nombre de función, variable u objeto tiene una serie de reglas a seguir.

| Tipo       | Convención de nombres                                                                | Ejemplos                |
| ---------- | ------------------------------------------------------------------------------------ | ----------------------- |
| Funciones  | Estilo snake_case. Todas las letras en minúsculas separadas por guiones bajos.       | `my_fun`, `my_function` |
| Variables  | Estilo snake_case. Todas las letras en minúsculas separadas por guiones bajos.       | `my_var`, `my_variable` |
| Constantes | Todas las letras en mayúsculas, las palabras deben estar separadas por guiones bajos | `PI`, `MY_CONSTANT`     |
| Clases     | Primera letra en mayúsculas y el resto en mínusculas.                                | `User`, `Admin`         |
| Métodos    | Estilo snake_case. Todas las letras ene minúsculas separadas por guiones bajos.      | `method`, `get_data`    |
| Módulos    | No más de una palabra, esta debe ser corta y todo en minúsculas.                     | `package`, `mypackage`. |
| Paquetes   |

NOTA: cabe aclarar que los nombres que se utilizan en funciones, clases, objetos, etc, deben ser significativos para que describa el dato que se va a guardar o la acción que realiza un método o función. 

### Espacios en blanco

* **Clases**: se deben dejar 2 espacios en blanco cuando se define una clase.
    ```python
    class User:
        def __init__(self):
            pass


    user = User()
    ```
* **Métodos**: se deben separar con 1 espacio entre los métodos de la función.
    ```python
    class User:
        def __init__(self, name):
            self.name = name
        
        def get_name(self, name):
            return self.name


user = User('Jhon')
    ```
* **Funciones**: se deben separar con 1 espacio, en caso de que en la función se realizen muchas acciones, las diferentes partes de la función y el retorno.
    ```python
    from math import sqrt

    def estandar_desviation(data):
        sum1 = 0
        for value in values:
            sum1 += (value - median) ** 2
        
        radic = sum1 / (len(values) - 1)

        sum2 = 0
        for value in values:
            sum2 += value
        
        return sum2 / len(values), sqrt(radic)
    ```

### Lines break

El máximo de caracteres en una línea puede ser de 79 caracteres, un número al que usualmente no llegaremos. Las rupturas de línea solo se podrán realizar si las expresiones se encuentran encerradas entre algún tipo de paréntesis, llaves o corchetes. 

```python
def (arg1, arg2, 
    arg3, arg4)
```
```python
data = [1, 2, 3, 4, 
        5, 6, 7, 9]
```

Si se realizan operaciones entre las expresiones siempre los operadores deben estar del lado izquierdo para mejorar la legibilidad y seguir la línea de identación.

```python
lista = [var1
        - var2
        + var3]
```
### Identación

* **La identación en las rupturas de líneas**
