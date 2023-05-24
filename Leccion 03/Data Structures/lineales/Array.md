# Array o arrays

En Python una array es una secuencia de datos ordenada y mutable. Es decir que los datos se guardan de manera que podemos acceder a ellos mediante índices (como en los strings). Con mutable nos referimos a que podemos modificar los datos que esta contiene. Las arrays pueden contener múltiples tipos de datos: números enteros, complejos, reales; secuencias: otras arrays, strings, tuplas; valores booleanos: False, True; diccionarios y set.

### Definir una array

Las arrays se asignan a una variable como cualquier otro tipo de dato. El rango de elementos será delimitados por corchetes `[]`. Los diferentes datos de la array los separaremos mediante comas.

```python
array = [1,2,'Hola',True]
print(array)

# [1,2,'Hola',True]
```

arrays dentro de otras arrays:
```python
array = [1,2,'Hola',True], [True, False, [1, 23, 9]]
print(array)

# [1,2,'Hola',True], [True, False, [1, 23, 9]]
```

**Determinar el tipo de dato**
```python
array = [1,2,'Hola',True]
print(type(array))

# <class 'list'>
```

### Operaciones con arrays

**Operadores artiméticos** 

Los operadores artiméticos en las arrays son importantes ya que nos permitirán modificar a la secuencia de datos.
* **Suma**: al sumar dos arrays mediante el operador de suma `+` los elemenos de una array se unirán a la de la otra desde el final de la primera. 
    ```python
    colors1 = ['Blue', 'Red', 'Orange']
    colors2 = ['Green', 'White', 'Black']
    total_colors = colors1 + colors2
    print(total_colors)

    # ['Blue', 'Red', 'Orange','Green', 'White', 'Black']
    ```
* **Multiplicación**: al multiplicar arrays los elementos de estas se multiplicarán por el número de veces que se indique.
    ```python
    colors = ['Blue', 'Red', 'Orange']
    print(colors * 3)

    # ['Blue', 'Red', 'Orange', 'Blue', 'Red', 'Orange', 'Blue', 'Red', 'Orange']
    ```
El resto de operadores aritméticos como resta o división no son soportados por este tipo de dato.

**Operadores de relación**

Nos permiten realizar comparaciones con las arrays. Es importante que las dos arrays a comparar deben ser del mismo tipo de dato.
**Comparaciones numéricas**: a la hora de hacer la comprobación de los elementos de las arrays a comprar no se comparan la cantidad de elementos que estas posean si no la suma que resulta de todos los elementos de la array, así: `list1=[1,2,3]` es menos que `list2=[9,9,9]` ya que a pesar de tener la misma cantidad de elementos cada array la suma de los elementos internos de la `array2` es mayor que los de la `array2`.
```python
array1 = [1,2,3]
array2 = [9,9,9]
print(list1 > list2)

# False
```

**Comparaciones de strings**: cuando comparamos arrays que contienen strings cambia la situación que con los números. Ya que si se comprara la cantidad de elementos como el orden alfabético de estos.
```python
array1 = ['a', 'b', 'c']
array2 = ['c', 'b', 'a']
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

Como ya hemos dicho las arrays son secuencias de datos ordenados accesibles por índices. Un índice es un número por el cual podemos identificar a los datos dentro de la array. Colocando el número de índice podemos recuperar el dato dentro de todos los demás. En las arrays los índices empiezan desde el número 0 hasta el n. También se puede acceder a los elementos de derecha a izquierda mediante índices negativos tales como -1, -9, etc.

![](https://files.realpython.com/media/t.c11ea56e8ca2.png)

**Acceder a los elementos por su índice**: 

* **list[<índice>]**
    ```python
    array = ['Python', 'Django', 'Flask']
    print(array[0])
    print(array[2])
    print(array[-2])

    # 'Python'
    # 'Flask'
    # 'Django'
    ```

**Acceder a los elementos por rango de índice**
* **list[ < índice inicial> : < índice final > ]**: se retornarán los elementos compredidos en el rango de índices especificado. Ten en cuenta que al acceder a los elementos por medio de rangos en argumento de índice final tienen una toleracia de 1, por lo que si se quiere acceder hasta el índice 5 se deberá colocar el número 6.
    ```python
    array = ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
    print(array[0:1])
    print(array[0:6])
    print(array[:3])
    print(array[1:])

    # 'Python'
    # ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
    # ['Python', 'Django', 'Flask']
    # ['Django', 'Flask', 'Javascript', 'React', 'PyQT']
    ```

**Acceder a los elementos por rangos por pasos**
* **list[ < índice inicial> : < índice final > : < pasos >]**: se retornarán los elementos compredidos en el rango de índices espceificado accediendo cada < paso >. Ten en cuenta que siempre se empezará por el índice de inicio sin ninguna tolerancia.
    ```python
    array = ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
    print(array[0:6:2])
    print(array[::4])

    # ['Python', 'Flask', 'React']
    # ['Python', 'React']
    ```
**Acceder a elementos de arrays dentro de otras arrays**
Cuando tenemos una array dentro de otra array y queremos acceder a esta cuando escribimos su índice accedemos a toda la array, cuando quizá lo que queremos es acceder a los elementos de la array dentro de la otra array.

![](https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/t.08554d94a1e5.png&w=1150&sig=dd460296ea6940e0ea6e809b7d98b1272708da03)

```python
array = ['Python', ['Javascript', 'React']]
print(array[1])

# ['Python', ['Javascript', 'React']]
```

Para ello se puede acceder a los índices de manera "escalonada", es decir, para acceder a los elementos de una array dentro de otra array podemos seguir colocando corchetes para acceder a ellos.
```python
array = ['Python', ['Javascript', 'React']]
print(array[1][1])

# 'React'
```
Otro ejemplo más grande:
```python
array = ['Python', ['Django', ['Flask', ['PyQt']]]]
print(array[1][1][1])

# ['PyQt']
```

**Reemplazar valores mediante el uso de los índices**
Pdemos reasignarle valores a rangos de elementos o reasignar valores a indices específicos de una array.
```python
array = ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
array[1:4] = ['C++']

# ['Python', 'C++', 'React', 'PyQT']
```
Otro ejemplo:
```python
array = ['Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
array[0] = ['Bash']

# ['Bash', 'Django', 'Flask', 'Javascript', 'React', 'PyQT']
```

### Métodos de arrays

Los métodos de arrays son funciones incorporadas que permiten trabajar con este tipo de dato pudiendo, mediante ellas, remover, modificar, agregar datos a la secuencia.

* **list()**: convierte un objeto a una array.
    ```python
    tupla = (1,2,3)
    array = llist(tupla)
    print(array, type(array))

    # [1,2,3]
    ```

* **append()**: agrega un elemento a la array.
    ```python
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    array.append(10)
    print(array)

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
    ```

* **clear()**: limpia todos los elementos de la misma y obteniendo como output una array vacía.
    ```python
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    array.clear()
    print(array)

    # []
    ```
* **copy()**: copia los elementos de la array especificada en una nueva variable.
    ```python
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    nueva_array = array.copy()
    print(f'array: {array} --> Nueva array: {nueva_array}')

    # array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] --> Nueva array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ```

* **count(<elemento>)**: devuelve la cantidad de veces que se repite el elemento especificado entre paréntesis. 
    ```python
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(array.count(9))

    # 1
    ```

* **remove()**: remueve el elemento especificado entre paréntesis.
    ```python
    array = [1,2,3,4,5,6,7,8,9,0]
    array.remove(8)
    print(array)

    # [1, 2, 3, 4, 5, 6, 7, 9, 0]
    ```

* **extend()**: añade los elementos de una array a la otra.
    ```python
    array1 = [1,2,3,4,5,6,7,8,9,0]
    array1.extend(array1)
    print(array1)

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ```

* **index(<elemento>)**: devuelve el índice de la primer aparición del elemento especificado.
    ```python
    array = [1,2,3,4,5,6,7,8,9,0]
    print(array.index(9))

    # 8
    ```

* **insert(<índice>, <nuevo elemento>)**: inserta un elemento en el índice especificado en el primer parámetro del método.
    ```python
    array = [1,2,3,4,5,6,7,8,9,0]
    print(array)
    array.insert(5,9)
    print(array)

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # [1, 2, 3, 4, 5, 9, 6, 7, 8, 9, 0]
    ```

* **pop(<índice>)**: elimina un elemento por su índice.
    ```python
    array = [1,2,3,4,5,6,7,8,9,0]
    array.pop(5)
    print(array)

    # [1, 2, 3, 4, 5, 7, 8, 9, 0]
    ```

* **remove(<valor>)**: elimina un elemento por su valor.
    ```python
    array = [1,2,3,4,5,6,7,8,9,0]
    array.remove(8)
    print(array)

    # [1, 2, 3, 4, 5, 6, 7, 9, 0]
    ```

* **reverse()**: cambia el orden de la array, invirtiendo.
    ```python
    array = [1,2,3,4,5,6,7,8,9,0]
    array.reverse()
    print(array)

    # [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ```

* **sort()**: ordena la array de una manera alfabética, ascendente en caso de números y con algunos detalles en cuanto a letras se refiere. En caso de tener letras minúsculas, Python las ordenará de manera alfabética, pero si alguna de estas tiene una mayúscula al inicio, Python detecta que es más importante y la podrá al inicio.
    ```python
    array = [1,2,3,4,5,6,7,8,9,0]
    array.sort()
    print(array)

    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

* **len()**: muestra el largo de una variable.
    ```python
    array = [1,2,3,4,5,6,7,8,9,0]
    print(len(array))

    # 10
    ```

# **List comprehesion**

Consiste en crear arrays de una manera simple (normalmente en una sola línea) a partir de ciclos, funciones generadoras y condicionales, así como demás operaciones lógicas-matemáticas.

A lo largo de este código verás la comparativa de crear arrays de la manera "tradicional" o intuitiva y luego utilizando list comprehesion.
```python
numeros = range(10)
array_pares = []

# Creamos una nueva array con los valores pares multiplicados por si mismos
for numero in numeros:
    # Revisamos si es un número par
    if numero % 2 == 0:
        array_pares.append(numero*numero)

print(f'array Pares: {array_pares}')

# Hacemos lo mismo pero con list comprehensions
# [expresion for var in coleción if condicion]
# La condición de if es opcional
array_pares = []
array_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'array Pares con list comprehensions: {array_pares}')

# Un ejemplo simila con dos condiciones (las condiciones son opcionales)
# Solo se agrega el valor a la array cuando el valor cumple ambas condiciones
# es decir, debe ser divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero%2==0 if numero%6==0]
print(f'array divisible entre 2 y 6: {pares}')

# Agregando if else
array_pares = []
array_impares = []
for numero in range(10):
    if numero%2==0:
        array_pares.append(numero)
    else:
        array_impares.append(numero)
print(f'Pares: {array_pares}')
print(f'Impares: {array_impares}')

# El mismo ejercicio usando list comprehensions
array_pares = []
array_impares = []
[array_pares.append(numero) if numero%2==0 else array_impares.append(numero) for numero in range(10)]
print(f'Pares: {array_pares}')
print(f'Impares: {array_impares}')

# array de arrays
array_arrays = [[1,2,3],[4,5,6],[7,8,9,10]]
# Convertimos la array de arrays en una sola array
array_simple = [valor
                for subarray in array_arrays
                for valor in subarray]
print(f'array simple: {array_simple}')

# Ahora creamos una array de numeros pares a partir de la array_arrays
# Sin list comprehensions, ciclos for anidados
array_pares = []
for subarray in array_arrays:
    for valor in subarray:
        if valor%2==0:
            array_pares.append(valor)
print(f'array pares: {array_pares}')

# Con list comprehensions, en una sola línea de código
# No es necesario separar las líneas, solo es para mejor lectura de código
array_pares = []
array_pares = [valor
               for subarray in array_arrays
               for valor in subarray
               if valor%2==0]
print(f'array pares: {array_pares}')
```
