# Tipos de datos > Tipo secuencia > Listas

En Python una lista es una secuencia de datos ordenada y mutable. Es decir que los datos se guardan de manera que podemos acceder a ellos mediante índices (como en los strings). Con mutable nos referimos a que podemos modificar los datos que esta contiene. Las listas pueden contener múltiples tipos de datos: números enteros, complejos, reales; secuencias: otras listas, strings, tuplas; valores booleanos: False, True; diccionarios y set.

### Comparativa Listas Vs Tuplas

**Similitudes entre listas y tuplas**:

* *Son considerados objetos (instancias de una clase).*
* *Son contenedores de colecciones de datos, pudiendo ser estos de cualquier tipo.*
* *Son colecciones ordenadas*
* *Tanto en tuplas como en listas puedes acceder a un elemento en particular mediante su índice*

**Diferencias entre listas y tuplas**:
* *Una tupla es inmutable*
* *Una lista es mutable*

### Definir una lista

Las listas se asignan a una variable como cualquier otro tipo de dato. El rango de elementos será delimitados por corchetes `[]`. Los diferentes datos de la lista los separaremos mediante comas.

```python
lista = [1,2,'Hola',True]
print(lista)

# [1,2,'Hola',True]
```

Listas dentro de otras listas:
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

### Operaciones con listas

**Operadores artiméticos** 

Los operadores artiméticos en las listas son importantes ya que nos permitirán modificar a la secuencia de datos.
* **Suma**: al sumar dos listas mediante el operador de suma `+` los elemenos de una lista se unirán a la de la otra desde el final de la primera. 
    ```python
    colors1 = ['Blue', 'Red', 'Orange']
    colors2 = ['Green', 'White', 'Black']
    total_colors = colors1 + colors2
    print(total_colors)

    # ['Blue', 'Red', 'Orange','Green', 'White', 'Black']
    ```
* **Multiplicación**: al multiplicar listas los elementos de estas se multiplicarán por el número de veces que se indique.
    ```python
    colors = ['Blue', 'Red', 'Orange']
    print(colors * 3)

    # ['Blue', 'Red', 'Orange', 'Blue', 'Red', 'Orange', 'Blue', 'Red', 'Orange']
    ```
El resto de operadores aritméticos como resta o división no son soportados por este tipo de dato.

**Operadores de relación**

Nos permiten realizar comparaciones con las listas. Es importante que las dos listas a comparar deben ser del mismo tipo de dato.
**Comparaciones numéricas**: a la hora de hacer la comprobación de los elementos de las listas a comprar no se comparan la cantidad de elementos que estas posean si no la suma que resulta de todos los elementos de la lista, así: `list1=[1,2,3]` es menos que `list2=[9,9,9]` ya que a pesar de tener la misma cantidad de elementos cada lista la suma de los elementos internos de la `lista2` es mayor que los de la `lista2`.
```python
lista1 = [1,2,3]
lista2 = [9,9,9]
print(list1 > list2)

# False
```

**Comparaciones de strings**: cuando comparamos listas que contienen strings cambia la situación que con los números. Ya que si se comprara la cantidad de elementos como el orden alfabético de estos.
```python
lista1 = ['a', 'b', 'c']
lista2 = ['c', 'b', 'a']
print(list1 < list2)

# True
```

**Operador in**

Permiten saber si un dato se encuentra o no dentro de la secuencia.
```python
colors = ['Blue', 'Red', 'Orange']
print('Blue' in colors2)

# True
```

**Operador not in**

Permite saber si no hay un dato dentro de una secuencia. Es el contrario a not in.
```python
colors = ['Blue', 'Red', 'Orange']
print('Green' not in colors2)

# True
```

### Índices

Como ya hemos dicho las listas son secuencias de datos ordenados accesibles por índices. Un índice es un número por el cual podemos identificar a los datos dentro de la lista. Colocando el número de índice podemos recuperar el dato dentro de todos los demás. En las listas los índices empiezan desde el número 0 hasta el n. También se puede acceder a los elementos de derecha a izquierda mediante índices negativos tales como -1, -9, etc.

![](https://files.realpython.com/media/t.c11ea56e8ca2.png)

**Acceder a los elementos por su índice**: 

* **list[<índice>]**
    ```python
    lista = ['Python', 'Django', 'Flask']
    print(lista[0])
    print(lista[2])
    print(lista[-2])

    # 'Python'
    # 'Flask'
    # 'Django'
    ```

**Acceder a los elementos por rango de índice**
* **list[ < índice inicial> : < índice final > ]**: se retornarán los elementos compredidos en el rango de índices especificado. Ten en cuenta que al acceder a los elementos por medio de rangos en argumento de índice final tienen una toleracia de 1, por lo que si se quiere acceder hasta el índice 5 se deberá colocar el número 6.
    ```python
    lista = ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
    print(lista[0:1])
    print(lista[0:6])
    print(lista[:3])
    print(lista[1:])

    # 'Python'
    # ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
    # ['Python', 'Django', 'Flask']
    # ['Django', 'Flask', 'Javascript', 'React', 'PyQT']
    ```

**Acceder a los elementos por rangos por pasos**
* **list[ < índice inicial> : < índice final > : < pasos >]**: se retornarán los elementos compredidos en el rango de índices espceificado accediendo cada < paso >. Ten en cuenta que siempre se empezará por el índice de inicio sin ninguna tolerancia.
    ```python
    lista = ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
    print(lista[0:6:2])
    print(lista[::4])

    # ['Python', 'Flask', 'React']
    # ['Python', 'React']
    ```
**Acceder a elementos de listas dentro de otras listas**
Cuando tenemos una lista dentro de otra lista y queremos acceder a esta cuando escribimos su índice accedemos a toda la lista, cuando quizá lo que queremos es acceder a los elementos de la lista dentro de la otra lista.

![](https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/t.08554d94a1e5.png&w=1150&sig=dd460296ea6940e0ea6e809b7d98b1272708da03)

```python
lista = ['Python', ['Javascript', 'React']]
print(lista[1])

# ['Python', ['Javascript', 'React']]
```

Para ello se puede acceder a los índices de manera "escalonada", es decir, para acceder a los elementos de una lista dentro de otra lista podemos seguir colocando corchetes para acceder a ellos.
```python
lista = ['Python', ['Javascript', 'React']]
print(lista[1][1])

# 'React'
```
Otro ejemplo más grande:
```python
lista = ['Python', ['Django', ['Flask', ['PyQt']]]]
print(lista[1][1][1])

# ['PyQt']
```

**Reemplazar valores mediante el uso de los índices**
Pdemos reasignarle valores a rangos de elementos o reasignar valores a indices específicos de una lista.
```python
lista = ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
lista[1:4] = ['C++']

# ['Python', 'C++', 'React', 'PyQT']
```
Otro ejemplo:
```python
lista = ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
lista[0] = ['Bash']

# ['Bash', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
```

### Métodos de listas

Los métodos de listas son funciones incorporadas que permiten trabajar con este tipo de dato pudiendo, mediante ellas, remover, modificar, agregar datos a la secuencia.

* **list()**: convierte un objeto a una lista.
    ```python
    tupla = (1,2,3)
    lista = list(tupla)
    print(lista, type(lista))

    # [1,2,3]
    ```

* **append()**: agrega un elemento a la lista.
    ```python
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lista.append(10)
    print(lista)

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
    ```

* **clear()**: limpia todos los elementos de la misma y obteniendo como output una lista vacía.
    ```python
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lista.clear()
    print(lista)

    # []
    ```
* **copy()**: copia los elementos de la lista especificada en una nueva variable.
    ```python
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    nueva_lista = lista.copy()
    print(f'Lista: {lista} --> Nueva lista: {nueva_lista}')

    # Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] --> Nueva lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ```

* **count(<elemento>)**: devuelve la cantidad de veces que se repite el elemento especificado entre paréntesis. 
    ```python
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(lista.count(9))

    # 1
    ```

* **remove()**: remueve el elemento especificado entre paréntesis.
    ```python
    lista = [1,2,3,4,5,6,7,8,9,0]
    lista.remove(8)
    print(lista)

    # [1, 2, 3, 4, 5, 6, 7, 9, 0]
    ```

* **extend()**: añade los elementos de una lista a la otra.
    ```python
    lista1 = [1,2,3,4,5,6,7,8,9,0]
    lista1.extend(lista1)
    print(lista1)

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ```

* **index(<elemento>)**: devuelve el índice de la primer aparición del elemento especificado.
    ```python
    lista = [1,2,3,4,5,6,7,8,9,0]
    print(lista.index(9))

    # 8
    ```

* **insert(<índice>, <nuevo elemento>)**: inserta un elemento en el índice especificado en el primer parámetro del método.
    ```python
    lista = [1,2,3,4,5,6,7,8,9,0]
    print(lista)
    lista.insert(5,9)
    print(lista)

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # [1, 2, 3, 4, 5, 9, 6, 7, 8, 9, 0]
    ```

* **pop(<índice>)**: elimina un elemento por su índice.
    ```python
    lista = [1,2,3,4,5,6,7,8,9,0]
    lista.pop(5)
    print(lista)

    # [1, 2, 3, 4, 5, 7, 8, 9, 0]
    ```

* **remove(<valor>)**: elimina un elemento por su valor.
    ```python
    lista = [1,2,3,4,5,6,7,8,9,0]
    lista.remove(8)
    print(lista)

    # [1, 2, 3, 4, 5, 6, 7, 9, 0]
    ```

* **reverse()**: cambia el orden de la lista, invirtiendo.
    ```python
    lista = [1,2,3,4,5,6,7,8,9,0]
    lista.reverse()
    print(lista)

    # [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ```

* **sort()**: ordena la lista de una manera alfabética, ascendente en caso de números y con algunos detalles en cuanto a letras se refiere. En caso de tener letras minúsculas, Python las ordenará de manera alfabética, pero si alguna de estas tiene una mayúscula al inicio, Python detecta que es más importante y la podrá al inicio.
    ```python
    lista = [1,2,3,4,5,6,7,8,9,0]
    lista.sort()
    print(lista)

    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

* **len()**: muestra el largo de una variable.
    ```python
    lista = [1,2,3,4,5,6,7,8,9,0]
    print(len(lista))

    # 10
    ```

# **List comprehesion**

Consiste en crear listas de una manera simple (normalmente en una sola línea) a partir de ciclos, funciones generadoras y condicionales, así como demás operaciones lógicas-matemáticas.

A lo largo de este código verás la comparativa de crear listas de la manera "tradicional" o intuitiva y luego utilizando list comprehesion.
```python
numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares multiplicados por si mismos
for numero in numeros:
    # Revisamos si es un número par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista Pares: {lista_pares}')

# Hacemos lo mismo pero con list comprehensions
# [expresion for var in coleción if condicion]
# La condición de if es opcional
lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Lista Pares con list comprehensions: {lista_pares}')

# Un ejemplo simila con dos condiciones (las condiciones son opcionales)
# Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
# es decir, debe ser divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero%2==0 if numero%6==0]
print(f'Lista divisible entre 2 y 6: {pares}')

# Agregando if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# El mismo ejercicio usando list comprehensions
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero) for numero in range(10)]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# Lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
# Convertimos la lista de listas en una sola lista
lista_simple = [valor
                for sublista in lista_listas
                for valor in sublista]
print(f'lista simple: {lista_simple}')

# Ahora creamos una lista de numeros pares a partir de la lista_listas
# Sin list comprehensions, ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor%2==0:
            lista_pares.append(valor)
print(f'Lista pares: {lista_pares}')

# Con list comprehensions, en una sola línea de código
# No es necesario separar las líneas, solo es para mejor lectura de código
lista_pares = []
lista_pares = [valor
               for sublista in lista_listas
               for valor in sublista
               if valor%2==0]
print(f'Lista pares: {lista_pares}')
```
