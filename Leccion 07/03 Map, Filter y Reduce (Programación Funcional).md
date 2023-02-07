# Map, Filter y Reduce

Estas tres funciones utilizadas en Python y muchos lenguajes es utilizado para el manejo de iterables. Con estas tres funciones podemos ahorrarnos bastante código y hacerlo más legible, entendible.

# Map

La función de Map de Python es una función que te permite transformar un iterable completo usando otra función.

**Sintaxis**:
```python
map(<function>, <iterable>)
```

**Ejemplo**:
```python
prices = ['$10', '$20', '$5', '$37', '$90']

# Utilizando un ciclo for
prices_to_integrer_for = []
for price in prices:
    prices_to_integrer_for.append(int(price[1:]))

# Utilizando la función map
prices_to_integrer_map = list(map(lambda price: int(price[1:]), prices))


print(prices_to_integer_for, prices_to_integrer_map)
# [10, 20, 5, 37, 90] [10, 20, 5, 37, 90]
```

En este ejemplo se ejemplifica la manera manual de realizar una conversión de una lista de precios en formato de cadena de carácter. En el primer caso se utiliza la manera que uno haría intuitivamente que es utilizar un bucle for. En el segundo caso utilizamos el método `map()`. Como el método map recibe como parámetros una función y luego el iterable sobre el cual ejecutar la función. 

NOTA: map retorna una llamada al objeto y no un iterable. Por lo que si queremos obtener un resultado coherente debemos utilizar funciones como list() que nos permitirán convertir el retorno de la función en una lista.

## Implementación propia de un map

```python
def own_map(function, iterable):
    new_iterable = []
    for i in iterable:
        new_iterable.append(function(i))
    return new_iterable
```

# Filter

La función filter en Python permite filtrar una lista a partir de una condición. 

**Sintaxis**:
```python
filter(<function>, <iterable>)
```

**Ejemplo**:
```python
prices = ['$10', '$20', '$5', '$37', '$90']

# Utilizando un ciclo for
for price in prices:
    if int(price[1:]) >= 25:
        print(price)

# Utilizando la función filter
expensive_prices = list(filter(lambda price: int(price[1:]) >= 20, prices))
print(expensive_prices)

# '$37' 
# '$90'
# ['$37', '$90']
```

Como vemos tenemos dos casos de comparación. El primero es una implementación de un filtrado de una lista por medio de una condición, si la condición es verdadera imprimimos el elemento del iterable. En el segundo caso utilizamos la función filter. Esta función al igual que map recibe como parámetros una función y luego el iterable. En este caso hemos filtrado los elementos de la función que sean mayores a 25.

## Implementación propia de un filter

```python
prices = ['$10', '$20', '$5', '$37', '$90']

def own_filter(function, iterable):
    filtered_list = []
    for i in iterable:
        if function(i):
            filtered_list.append(i)
    return filtered_list

print(own_filter(lambda price: int(price[1:]) >= 20, prices))

# ['$20', '$37', '$90']
```

# Reduce

La función reduce aunque no está implementada en el lenguaje se puede utilizar importando la función del módulo functools.

```python
from functools import reduce
```

La función reduce en Python reduce el iterable pasado como argumento a un solo elemento. Es decir, que por ejemplo de una lista de números podría calcular la suma de todos ellos, por lo que el resultado sería la suma, un solo elemento. 

**Sintaxis**:
```python
reduce(<function>, <iterable>, [acumulator])
```
Reduce se basa en un acumulador en donde agregará todos los elementos del iterable para retornar uno solo. El acumulador se debe pasar como parámetro de la función. El parámetro del acumulador es opcional, por defecto es 0 pero se le puede asignar cualquier otro valor.

**Ejemplo**:
```python
from functools import reduce

prices = ['$10', '$20', '$5', '$37', '$90']

# Utilizando un bucle for
suma = 0
for price in prices:
    acum += int(price[1:])
print(suma)


# Utilizando la función reduce
suma = reduce(lambda acum, price: acum + int(price[1:]), prices, 0)
print(suma)

# 162 
# 162
```

En el ejemplo anterior se ven dos casos, el primero implementandolo manualmente y el segundo utilizando la función reduce. En el primer caso recorremos el iterable para sumar los elementos del iterable. En el segundo caso utilizando la función reduce vemos como pasamos la función y le indicamos que le sume al acumulador el precio convertido a entero. Como es de esperar en los dos casos nos retorna le mismo resultado, pero el el segundo caso nos hemos ahorrado 3 líneas de código, es más legible el código y eficiente. 

## Implentación propia de un reduce

```python
def own_reduce(function, iterable, acum):
    for i in iterable:
        acum = function(acum, i)
    return acum

print(own_reduce(lambda acum, price: acum + int(price[1:]), prices, 0))
# 162
```
