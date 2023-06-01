# Tipos de datos > Set

Los sets son secuencias de elementos: 
 * Los sets no están ordenados.
 * Los elementos del set son únicos. No se permiten elementos duplicados.
 * Un set puede ser modificado, pero los elementos contenidos en el set deben ser de un tipo inmutable.

### Definir un set

Un set se define mediante llaves `{}` o mediante la función incorporada `set()`, está función convierte una secuancia de datos a un set con las características que estos poseen.

```python
s = {'foo', 'bar'}
```
Verificar el tipo de dato:
```python
s = {'foo', 'bar'}
type(s)

# <class 'set'>
```
Definir un set mediante la función incorporada `set()`:
```python
s = set(['foo', 'bar'])
print(s)

# {'foo', 'bar'}
```
### Operaciones con set

**Operador de resta**: devuelve el conjunto de todos los elementos que están en el set1 pero no en el set2.
```python
s1 = {'foo', 'bar', 'baz'}
s2 = {'foo', 'python', 'django'}
print(s1 - s2)

# {'bar', 'baz}   
```

**Operador in**: permite saber si un elemento se encuentra en el set
```python
s1 = {'foo', 'bar', 'baz'}
'foo' in s1

# True
```
**Operador not in**: permite saber si no se encuentra un elemento dentro del set.
```python
s1 = {'foo', 'bar', 'baz'}
'foo' not in s1

# False
```
**operador  |**: este operador permite unir dos set.
```python
s1 = {'foo', 'bar', 'baz'}
'foo' in s1

# True
```python
s1 = {'foo', 'bar', 'baz'}
s2 = {'foo', 'python', 'django'}
print(s1 | s2)

# {'bar', 'django', 'foo', 'python', 'baz'}
```

### Métodos de sets

* **set1.union( < set2 >, [set3, set4, set n])**: une dos sets al igual que el operador `|`.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'foo', 'python', 'django'}
    print(s1.union(s2))

    # {'bar', 'django', 'foo', 'python', 'baz'}
    ```
* **set1.intersection( < set2 > , [set3, set4, set n])**: devuelve el set de elementos comunes entre el set1 y el set2.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'foo', 'python', 'django'}
    print(s1.intersection(s2))

    # {'foo'}    
    ```
* **set1.difference( < set2 > , [set3, set4, set n])**: devuelve el conjunto de todos los elementos que están en el set1 pero no en el set2.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'foo', 'python', 'django'}
    print(s1.difference(s2))

    # {'bar', 'baz'}    
    ```
* **set1.symmetric_difference( < set2 > )**: devuelve el conjunto de todos los elementos del set1 o set2, pero no de ambos. Básicamente la suma de los elementos de los dos set menos los elementos que sean iguales.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'foo', 'python', 'django'}
    print(s1.symmetric_difference(s2))

    # {'baz', 'django', 'python', 'bar'}    
    ``` 
    NOTA: el operador `^` realiza la misma operación y es mejor en ciertas situaciones ya que permite realizar esta operación con más de 2 set.


* **set1.isdisjoint( < set2 > )**: determina si dos set tienen o no elementos en común. Retorna True si no hay elementos en común y False en caso contrario.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'javascript', 'python', 'django'}
    print(s1.isdisjoint(s2))

    # True
    ``` 

* **set1.issubset( < set2 > )**: determina si un set se encuentra dentro de otro set. En teoría de conjuntos, metemáticas, se considera que un subconjunto se encuentra en un conjunto si algunos de sus elementos coinciden.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'foo', 'bar', 'baz', 'python', 'javascript}
    print(s1.issubset(s2))

    # True
    ``` 
    NOTA: el opeardor <= se comporta de la misma manera que el método.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'foo', 'bar', 'baz', 'python', 'javasrscript}
    print(s1 <= s2)

    # True
    ```

* **set1.issuperset( < set2 > )**: un superset es el reverso de un set. Un set se considera un superset de otro set si el set1 y el set2 tienen todos los elementos iguales.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'foo', 'bar', 'baz'}
    print(s1.issuperset(s2))

    # True  
    ```
    NOTA: el operador > se comporta de la misma manera.
    ```python
    s1 = {'foo', 'bar', 'baz'}
    s2 = {'foo', 'bar', 'baz'}
    print(s1 >= s2)

    # True
    ```

