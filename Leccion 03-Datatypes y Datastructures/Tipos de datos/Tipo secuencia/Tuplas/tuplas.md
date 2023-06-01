# Tipos de datos > Tipo secuencia > Tuplas

Una tupla es una secuencia de datos ordenada accesible por índices, la diferencias contra las listas reside en que este tipo de dato es inmutable. Sus datos no pueden ser modificados libremente como en las listas, si no que se deberá convertir la tupla a una lista para poder modificarla, aunque no tienen mucho sentido ya que para ello existen las listas. Las tuplas sirven para almacener colecciones de datos constantes, que son necesarios pero no queremos modifcarlos.

### Comparativa Tuplas Vs Listas

**Similitudes entre tuplas y listas**:

* *Son considerados objetos (instancias de una clase).*
* *Son contenedores de colecciones de datos, pudiendo ser estos de cualquier tipo.*
* *Son colecciones ordenadas*
* *Tanto en tuplas como en listas puedes acceder a un elemento en particular mediante su índice*

**Diferencias entre tuplas y listas**:
* *Una tupla es inmutable*
* *Una lista es mutable*

### Definición de una tupla

Las tuplas se asignan a una variabe como cualquier otro tipo de dato, para indicar que se trata de una tupla se encerrarán los datos separados por camas entre paréntesis `()`. Las tuplas pueden almacenar cualquier tipo dato, inclusive una tupla dentro de otra tupla.

```python
tupla = (1,2,'Hola',True)
print(tupla)

# (1,2,'Hola',True)
```

Tuplas dentro de otras tuplas:
```python
tupla = (1,2,'Hola',True), (True, False, (1, 23, 9))
print(tupla)

# (1,2,'Hola',True), (True, False, (1, 23, 9))
```

**Determinar el tipo de dato**
```python
tupla = (1,2,'Hola',True)
print(type(tupla))

# <class 'tuple'>
```

### Operaciones con tuplas

**Operadores artiméticos** 

Los operadores artiméticos en las tuplas son importantes ya que nos permitirán modificar a la secuencia de datos.
* **Suma**: al sumar dos tuplas mediante el operador de suma `+` los elemenos de una tupla se unirán a la de la otra desde el final de la primera. 
    ```python
    colors1 = ('Blue', 'Red', 'Orange')
    colors2 = ('Green', 'White', 'Black')
    total_colors = colors1 + colors2
    print(total_colors)

    # ('Blue', 'Red', 'Orange','Green', 'White', 'Black')
    ``` 
* **Multiplicación**: al multiplicar tuplas los elementos de estas se multiplicarán por el número de veces que se indique.
    ```python
    colors = ('Blue', 'Red', 'Orange')
    print(colors * 3)

    # ('Blue', 'Red', 'Orange', 'Blue', 'Red', 'Orange', 'Blue', 'Red', 'Orange')
    ```
El resto de operadores aritméticos como resta o división no son soportados por este tipo de dato.

**Operadores de relación**

Nos permiten realizar comparaciones con las tuplas. Es importante que las dos tuplas a comparar deben ser del mismo tipo de dato.
**Comparaciones numéricas**: a la hora de hacer la comprobación de los elementos de las tuplas a comprar no se comparan la cantidad de elementos que estas posean si no la suma que resulta de todos los elementos de la lista, así: `tuple1=(1,2,3)` es menos que `tuple2=(9,9,9)` ya que a pesar de tener la misma cantidad de elementos cada tupla la suma de los elementos internos de la `tuple2` es mayor que los de la `tuple1`.
```python
tupla1 = (1,2,3)
tupla2 = (9,9,9)
print(tupla1 > tupla2)

# False
```

**Comparaciones de strings**: cuando comparamos tuplas que contienen strings cambia la situación que con los números. Ya que si se comprara la cantidad de elementos como el orden alfabético de estos.
```python
tupla1 = ('a', 'b', 'c')
tupla1 = ('c', 'b', 'a')
print(list1 < list2)

# True
```

**Operador in**

Permiten saber si un dato se encuentra o no dentro de la secuencia.
```python
colors = ('Blue', 'Red', 'Orange')
print('Blue' in colors2)

# True
```

**Operador not in**

Permite saber si no hay un dato dentro de una secuencia. Es el contrario a not in.
```python
colors = ('Blue', 'Red', 'Orange')
print('Green' not in colors2)

# True
```

### Índices

Como ya hemos dicho las tuplas son secuencias de datos ordenados accesibles por índices. Un índice es un número por el cual podemos identificar a los datos dentro de la tupla. Colocando el número de índice podemos recuperar el dato dentro de todos los demás. En las listas los índices empiezan desde el número 0 hasta el n. También se puede acceder a los elementos de derecha a izquierda mediante índices negativos tales como -1, -9, etc.

**Acceder a los elementos por su índice**: 

* **tuple(<índice>)**
    ```python
    tupla = ('Python', 'Django', 'Flask')
    print(tupla[0])
    print(tupla[2])
    print(tupla[-2])

    # 'Python'
    # 'Flask'
    # 'Django'
    ```

**Acceder a los elementos por rango de índice**
* **tuple( < índice inicial> : < índice final > )**: se retornarán los elementos compredidos en el rango de índices especificado. Ten en cuenta que al acceder a los elementos por medio de rangos en argumento de índice final tienen una toleracia de 1, por lo que si se quiere acceder hasta el índice 5 se deberá colocar el número 6.
    ```python
    tupla = ('Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT')
    print(tupla[0:1])
    print(tupla[0:6])
    print(tupla[:3])
    print(tupla[1:])

    # 'Python'
    # ('Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT')
    # ('Python', 'Django', 'Flask')
    # ('Django', 'Flask', 'Javascript', 'React', 'PyQT')
    ```

**Acceder a los elementos por rangos por pasos**
* **tuple( < índice inicial> : < índice final > : < pasos >)**: se retornarán los elementos compredidos en el rango de índices espceificado accediendo cada < paso >. Ten en cuenta que siempre se empezará por el índice de inicio sin ninguna tolerancia.
    ```python
    tupla = ('Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT')
    print(tupla[0:6:2])
    print(tupla[::4])

    # ('Python', 'Flask', 'React')
    # ('Python', 'React')
    ```
**Acceder a elementos de listas dentro de otras listas**
Cuando tenemos una lista dentro de otra lista y queremos acceder a esta cuando escribimos su índice accedemos a toda la lista, cuando quizá lo que queremos es acceder a los elementos de la lista dentro de la otra lista.

!()(https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/t.08554d94a1e5.png&w=1150&sig=dd460296ea6940e0ea6e809b7d98b1272708da03)

```python
tupla = ('Python', ('Javascript', 'React'))
print(tupla[1])

# ('Python', ('Javascript', 'React'))
```

Para ello se puede acceder a los índices de manera "escalonada", es decir, para acceder a los elementos de una lista dentro de otra lista podemos seguir colocando corchetes para acceder a ellos.
```python
tupla = ('Python', ('Javascript', 'React'))
print(tupla[1][1])

# 'React'
```
Otro ejemplo más grande:
```python
tupla = ('Python', ('Django', ('Flask', ('PyQt'))))
print(tupla[1][1][1])

# ('PyQt')
```

**Reemplazar valores mediante el uso de los índices**
No se pueden reasignar valores a los elementos de una tupla ya que no es una propiedada que estas posean la de ser mutables como las listas. Como resultado de intentar reasignarle un valor obtendremos un error de tipo: `TypeError: 'tuple' object does not support item assignment`.
```python
tupla = ('Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT')
tupla(1:4) = ('C++')

# Error
```
Otro ejemplo:
```python
tupla = ('Python', 'Django', 'Flask', 'Javascript', 'React', 'PyQT')
tupla(0) = ('Bash')

# Error
```
