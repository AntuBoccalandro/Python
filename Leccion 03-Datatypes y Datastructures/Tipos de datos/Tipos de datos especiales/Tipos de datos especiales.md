# **Tipos de datos especiales**

# **None**

El tipo None en Python representa una falta de valor. Este tipo de dato es útil para específicar que una función no retorna ningún valor definir una variable pero no asignarle un valor.

**Casos de uso**:
```python
# En funciones que no retornan ningún valor
def mostrar_datos(datos) -> None:
    print(datos)


# En variables que no querramos asignarle un valor inicialemente
lenguajes = ["C", "C++", "Python", "Java", "Go"]
posicion = None
for i, elemento in enumerate(lenguajes):
    if elemento == "Python":
        posicion = i
        break

if posicion is None:
    print("No se encontró el elemento.")
else:
    print("El elemento está en la posición:", i)
```

**Valores infinitos**:
Los valores infinitos en Python hacen referencia al número posiitivo más grande que se puede representar y el número negativo más grande que podemos representar.

```python
import math

# Utilizando el constructor float
valor_infinito_positivo = float('inf')
print(valor_infinito_positivo, math.isinf(valor_infinito_positivo))
# OUTPUT: inf True

valor_infinito_negativo = float('-inf')
print(valor_infinito_negativo, math.isinf(valor_infinito_negativo))
# OUTPUT: -inf True

# Utilizando la librería math
valor_infinito_positivo_math = math.inf
print(valor_infinito_positivo_math, math.isinf(valor_infinito_positivo_math))
# OUTPUT: inf

valor_infinito_negativo_math = -math.inf
print(valor_infinito_negativo_math, math.isinf(valor_infinito_negativo_math))
# OUTPUT: -inf
``` 

# **NaN**

NaN, Not a number, no es un número. NaN es un tipo de dato numérico indefinido. Este tipo de dato sirve para cuando queremos darle un valor inicial a una variable pero no queremos darle valores como 0 o 1 que puedan a llegar a interferir. Cuando creamos un valor NaN no hace falta escribirlo así, es solo una referencia, podríamos crear un NaN con el constructor float de la siguiente manera:
* float('nan')
* float('Nan')
* float('naN')
* float('NaN')
* float('nAn')
* Etcétera...con todas las combinaciónes que halla.
  
Cuando mostremos por pantalla el tipo de dato Nan este se mostrará todo en minúsculas, `nan`.

```python
a = float('NaN')
print(f'Es {a} (not a number)?: {math.isnan(a)}')
# nan True
```
