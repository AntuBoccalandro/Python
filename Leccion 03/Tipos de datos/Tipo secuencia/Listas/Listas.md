# Tipos de datos > Tipo secuencia > Listas

En Python una lista es una secuencia de datos ordenada y mutable. Es decir que los datos se guardan de manera que podemos acceder a ellos mediante índices (como en los strings). Con mutable nos referimos a que podemos modificar los datos que esta contiene. Las listas pueden contener múltiples tipos de datos: números enteros, complejos, reales; secuencias: otras listas, strings, tuplas; valores booleanos: False, True; diccionarios y set.

### Definir una lista

Las listas se asignan a una variable como cualquier otro tipo de dato. El rango de elementos será delimitados por corchetes `[]`. Los diferentes datos de la lista los separaremos mediante comas.

```python
lista = [1,2,'Hola',True]
print(lista)

# [1,2,'Hola',True]
```

Listas dentro de otras listas.
```python
lista = [1,2,'Hola',True], [True, False, [1, 23, 9]]
print(lista)

# [1,2,'Hola',True], [True, False, [1, 23, 9]]
```

**Determinar el tipo de dato**
```python
lista = [1,2,'Hola',True]
print(type(lista))

# <class 'list'>
```

### Comparativa Listas Vs Tuplas

**Similitudes entre listas y tuplas**:
*Son considerados objetos (instancias de una clase).*
*Son contenedores de colecciones de datos, pudiendo ser estos de cualquier tipo.*
*Son colecciones ordenadas*
*Tanto en tuplas como en listas puedes acceder a un elemento en particular mediante su índice*
**Diferencias entre listas y tuplas**:
* *Una tupla es inmutable*
* *Una lista es mutable*

### Operaciones con listas

**Operadores artiméticos** 

Los operadores artiméticos en las listas son importantes ya que nos permitirán modificar a la secuencia de datos.

**Operadores de relación**

Nos permiten realizar comparaciones con las listas.

**Operadores lógicos**

Nos permiten realizar comprobaciones lógicas con los datos.

**Operador in**

Permiten saber si un dato se encuentra o no dentro de la secuencia.

**Operador not in**

Permite saber si no hay un dato dentro de una secuencia. Es el contrario a not in.


### Índices

**Acceder a los elementos por su índice**
**Acceder a los elementos por rango de índice**
**Reemplazar valores con índices**

### Métodos de listas

Las listas son mutables por lo que son modificables, por ello existen varios métodos
que nos permiten operar con ellas. En el caso de las tuplas al ser inmutables la manera
de implementar métodos de listas es convertirla a una para modificarla y luego
convertirla a una tupla para retornar como output.

**Índices**:
Antes de comenzar a ver los distintos métodos que existen es necesario conocer qué son los índices. Los índices sirven para ubicar o valores dentro de una lista, en Python este índice comienza desde el 0 en adelante. 

Es decir que en una lista de 4 elementos los índices serían: 

| Índice |  Elementos  |
| :----: | :---------: |
|   0    | 1° Elemento |
|   1    | 2° Elemento |
|   2    | 3° Elemento |
|   3    | 4° Elemento |

![](https://i.imgur.com/akqYYq5.png)

## **Métodos de listas**:

**<Nombre_de_la_lista>[inicio:fin]**
* Devuelve los elementos de la lista situados entre los índices 2 al 4.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista[2:4])

# OUTPUT
[3, 4]
```

**<Nombre_de_la_lista>[inicio:]**
* Devuelve los elementos de la lista situados entre los índices 1 al 9.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista[1:])

# OUTPUT
[2, 3, 4, 5, 6, 7, 8, 9, 0]
```

**<Nombre_de_la_lista>[:fin]**
* Devuelve los elementos de la lista situados entre los índices 0 al 2.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista[:2])

# OUTPUT
[1, 2]
```

**<Nombre_de_la_lista>[inicio:fin:pasos]**
* Devuelve los elementos de la lista situados entre los índices 0 al 4 pasando de a 2 elementos.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista[0:4:2])

# OUTPUT
[1, 3]
```

**append()**
Append agrega un elemento a la lista.
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista.append(10)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
```

**clear()**
* Clear limpia todos los elementos de la misma y obteniendo como output una lista vacía.
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista.clear()
print(lista)

# OUTPUT
[]
```
**copy()**
* Copia los elementos de la lista especificada en una nueva variable.
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
nueva_lista = lista.copy()
print(f'Lista: {lista} --> Nueva lista: {nueva_lista}')

# OUTPUT
Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] --> Nueva lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```

**count(<elemento>)**
* Devuelve la cantidad de veces que se repite el elemento especificado entre paréntesis. 
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lista.count(9))

# OUTPUT
1
```

**remove()**
* Remueve el elemento especificado entre paréntesis.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.remove(8)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 9, 0]
```

**extend()**
* Añade los elementos de una lista a la otra.
```python
lista1 = [1,2,3,4,5,6,7,8,9,0]
lista1.extend(lista1)
print(lista1)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```

**index(<elemento>)**
* Devuelve el índice de la primer aparición del elemento especificado.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista.index(9))

# OUTPUT
8
```

**insert(<índice>, <nuevo elemento>)**
* Inserta un elemento en el índice especificado en el primer parámetro del método.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista)
lista.insert(5,9)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
[1, 2, 3, 4, 5, 9, 6, 7, 8, 9, 0]
```

**pop(<índice>)**
* Elimina un elemento por su índice.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.pop(5)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 7, 8, 9, 0]
```

**remove(<valor>)**
* Elimina un elemento por su valor.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.remove(8)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 9, 0]
```

**reverse()**
* Cambia el orden de la lista, invirtiendo.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.reverse()
print(lista)

# OUTPUT
[0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

**sort()**
* Ordena la lista de una manera alfabética, ascendente en caso de números y con algunos detalles en cuanto a letras se refiere. En caso de tener letras minúsculas, Python las ordenará de manera alfabética, pero si alguna de estas tiene una mayúscula al inicio, Python detecta que es más importante y la podrá al inicio.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.sort()
print(lista)

# OUTPUT
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**len()**
* Muestra el largo de una variable.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(len(lista))

# OUTPUT
10
```

## **Métodos de tuplas**
Dentro de las tuplas encontramos menos métodos, pero algo que nos provee mucha versatilidad es el de convertir una tupla a una lista y usar todos los métodos de lista. Las tuplas al ser inmutables no nos dan tanta flexibilidad, pero dependiendo del uso serán más útiles o no, ya que si debemos estar modificando sus valores y teniendo que convertir constantemente esta tupla a una lista y gastando recursos de más.

list()
List convierte una tupla en una lista.
```python
tupla = (1,2,3,4,5,6,7,8,9,0)
lista = list(tupla)
print(f'{type(tupla)} --> {type(lista)}')

# OUTPUT
<class 'tuple'> --> <class 'list'>
```

tuple()
List convierte una tupla en una lista.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
tupla = tuple(tupla)
print(f'{type(lista)} --> {type(tupla)}')

# OUTPUT
<class 'list'> --> <class 'tuple'>
```

Las listas son mutables por lo que son modificables, por ello existen varios métodos
que nos permiten operar con ellas. En el caso de las tuplas al ser inmutables la manera
de implementar métodos de listas es convertirla a una para modificarla y luego
convertirla a una tupla para retornar como output.

**Índices**:
Antes de comenzar a ver los distintos métodos que existen es necesario conocer qué son los índices. Los índices sirven para ubicar o valores dentro de una lista, en Python este índice comienza desde el 0 en adelante. 

Es decir que en una lista de 4 elementos los índices serían: 

| Índice |  Elementos  |
| :----: | :---------: |
|   0    | 1° Elemento |
|   1    | 2° Elemento |
|   2    | 3° Elemento |
|   3    | 4° Elemento |

![](https://i.imgur.com/akqYYq5.png)

## **Métodos de listas**:

**<Nombre_de_la_lista>[inicio:fin]**
* Devuelve los elementos de la lista situados entre los índices 2 al 4.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista[2:4])

# OUTPUT
[3, 4]
```

**<Nombre_de_la_lista>[inicio:]**
* Devuelve los elementos de la lista situados entre los índices 1 al 9.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista[1:])

# OUTPUT
[2, 3, 4, 5, 6, 7, 8, 9, 0]
```

**<Nombre_de_la_lista>[:fin]**
* Devuelve los elementos de la lista situados entre los índices 0 al 2.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista[:2])

# OUTPUT
[1, 2]
```

**<Nombre_de_la_lista>[inicio:fin:pasos]**
* Devuelve los elementos de la lista situados entre los índices 0 al 4 pasando de a 2 elementos.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista[0:4:2])

# OUTPUT
[1, 3]
```

**append()**
Append agrega un elemento a la lista.
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista.append(10)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
```

**clear()**
* Clear limpia todos los elementos de la misma y obteniendo como output una lista vacía.
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista.clear()
print(lista)

# OUTPUT
[]
```
**copy()**
* Copia los elementos de la lista especificada en una nueva variable.
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
nueva_lista = lista.copy()
print(f'Lista: {lista} --> Nueva lista: {nueva_lista}')

# OUTPUT
Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] --> Nueva lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```

**count(<elemento>)**
* Devuelve la cantidad de veces que se repite el elemento especificado entre paréntesis. 
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lista.count(9))

# OUTPUT
1
```

**remove()**
* Remueve el elemento especificado entre paréntesis.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.remove(8)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 9, 0]
```

**extend()**
* Añade los elementos de una lista a la otra.
```python
lista1 = [1,2,3,4,5,6,7,8,9,0]
lista1.extend(lista1)
print(lista1)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```

**index(<elemento>)**
* Devuelve el índice de la primer aparición del elemento especificado.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista.index(9))

# OUTPUT
8
```

**insert(<índice>, <nuevo elemento>)**
* Inserta un elemento en el índice especificado en el primer parámetro del método.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(lista)
lista.insert(5,9)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
[1, 2, 3, 4, 5, 9, 6, 7, 8, 9, 0]
```

**pop(<índice>)**
* Elimina un elemento por su índice.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.pop(5)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 7, 8, 9, 0]
```

**remove(<valor>)**
* Elimina un elemento por su valor.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.remove(8)
print(lista)

# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 9, 0]
```

**reverse()**
* Cambia el orden de la lista, invirtiendo.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.reverse()
print(lista)

# OUTPUT
[0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

**sort()**
* Ordena la lista de una manera alfabética, ascendente en caso de números y con algunos detalles en cuanto a letras se refiere. En caso de tener letras minúsculas, Python las ordenará de manera alfabética, pero si alguna de estas tiene una mayúscula al inicio, Python detecta que es más importante y la podrá al inicio.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
lista.sort()
print(lista)

# OUTPUT
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**len()**
* Muestra el largo de una variable.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
print(len(lista))

# OUTPUT
10
```

## **Métodos de tuplas**
Dentro de las tuplas encontramos menos métodos, pero algo que nos provee mucha versatilidad es el de convertir una tupla a una lista y usar todos los métodos de lista. Las tuplas al ser inmutables no nos dan tanta flexibilidad, pero dependiendo del uso serán más útiles o no, ya que si debemos estar modificando sus valores y teniendo que convertir constantemente esta tupla a una lista y gastando recursos de más.

list()
List convierte una tupla en una lista.
```python
tupla = (1,2,3,4,5,6,7,8,9,0)
lista = list(tupla)
print(f'{type(tupla)} --> {type(lista)}')

# OUTPUT
<class 'tuple'> --> <class 'list'>
```

tuple()
List convierte una tupla en una lista.
```python
lista = [1,2,3,4,5,6,7,8,9,0]
tupla = tuple(tupla)
print(f'{type(lista)} --> {type(tupla)}')

# OUTPUT
<class 'list'> --> <class 'tuple'>
```