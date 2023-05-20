# **Enums**

En Python, una enumeración (también conocida como enum) es un tipo de dato que define un conjunto de constantes con nombre. Cada constante en la enumeración tiene un nombre único y un valor asociado. Esto facilita la creación de conjuntos de opciones predefinidas y ayuda a mejorar la legibilidad del código al restringir los posibles valores de una variable.


# **Definir un enum**

```python
from enum import Enum

# Definición de la enumeración
class Color(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

# Uso de la enumeración
print(Color.ROJO)  # Imprime: Color.ROJO
print(Color.ROJO.value)  # Imprime: 1
print(Color(2))  # Imprime: Color.VERDE
```

# **Ejemplos de uso para enums**

## **Talles**
```python
class Talla(Enum):
    XS = 1
    S = 2
    M = 3
    L = 4
    XL = 5
```

## **Tamaños de fuentes**
```python
class TamanoFuente(Enum):
    PEQUENO = 'pequeno'
    MEDIANO = 'mediano'
    GRANDE = 'grande'
    EXTRA_GRANDE = 'extra grande'
```

## **Estados de tareasz**
```python
class EstadoTarea(Enum):
    PENDIENTE = 'pendiente'
    EN_PROGRESO = 'en progreso'
    COMPLETADA = 'completada'
    CANCELADA = 'cancelada'
```

# **Más funcionalidades del módulo enum**

## **Atributos personalizados**
```python
from enum import Enum

class Color(Enum):
    ROJO = ('#FF0000', 'Color rojo')
    VERDE = ('#00FF00', 'Color verde')
    AZUL = ('#0000FF', 'Color azul')

    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

# Uso de la enumeración con atributos personalizados
print(Color.ROJO.codigo)  # Imprime: '#FF0000'
print(Color.VERDE.descripcion)  # Imprime: 'Color verde'
```

## **Iteración**
```python
from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Iteración sobre las constantes de la enumeración
for dia in DiaSemana:
    print(dia)  # Imprime todos los días de la semana
```

## **Comparaciones**
```python
from enum import Enum

class Talla(Enum):
    XS = 1
    S = 2
    M = 3
    L = 4
    XL = 5

# Comparación de constantes
print(Talla.S == Talla.M)  # Imprime: False
print(Talla.XL > Talla.L)  # Imprime: True

# Ordenamiento de constantes
tallas = [Talla.M, Talla.S, Talla.XL, Talla.L, Talla.XS]
tallas_ordenadas = sorted(tallas)
print(tallas_ordenadas)  # Imprime: [Talla.XS, Talla.S, Talla.M, Talla.L, Talla.XL]
```
