# **La función zip**

La función incorporada (o built-in) `zip()` toma como argumento dos o más objetos iterables (idealmente cada uno de ellos con la misma cantidad de elementos) y retorna un nuevo iterable cuyos elementos son tuplas que contienen un elemento de cada uno de los iteradores originales.

```python
paises = ["China", "India", "Estados Unidos", "Indonesia"]
poblaciones = [1391, 1364, 327, 264]
list(zip(paises, poblaciones))
# OUTPUT: [('China', 1391), ('India', 1364), ('Estados Unidos', 327), ('Indonesia', 264)]
```
Como vemos tenemos la lista generada por la función `zip()` retorna una lista de tuplas en la que el primer elemento es el de la lista de paisesw (lista uno) y el segundo elemento es de la lista de poblaciones (la segunda lista). 

## **¿Qué pasa si la cantidad de elementos da cada iterable es diferente?**

Si se da el caso de tener varios iterables pero que tengan diferente cantidad de elementos el largo del iterable retornado por esta función se limitará al iterable de menos elementos de los iterables pasados como parámetros.

```python
numeros = (1,2,3)
letras = ['a','b','c','d']
indentificadores = 321, 322, 323, 324, 325
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros, letras, indentificadores, conjunto)

print(list(mezcla))
# [(1, 'a', 321, 0), (2, 'b', 322, 4), (3, 'c', 323, 6)]
``` 
Como vemos el resultado es una lista de 3 tuplas, el iterable obtenido es de 3 elementos ya que corresponde al largo del iterable de menos elementos, en este caso la tupla de `numeros`, que de los iterables es el más pequeño.

## **Iterar con la función zip**

Esta función es útil para iterar sobre varios iterables en un ciclo for o algún otro iterador.

```python
numeros = (1,2,3)
letras = ['a','b','c','d']
indentificadores = 321, 322, 323, 324, 325
conjunto = {6,4,0,9,8,15,10}

for numero, letra, id, aleatorio in zip(numeros, letras, indentificadores, conjunto):
    print(f'Número: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}')

# Número: 1, Letra: a, Id: 321, Aleatorio: 0
# Número: 2, Letra: b, Id: 322, Aleatorio: 4
# Número: 3, Letra: c, Id: 323, Aleatorio: 6
```

## **Unzip**

Aunque no existe un método `unzip` se puede emular mediante el uso del operador de unpacking.

```python
mezcla = [(1,'a'),(2,'b'),(3,'c')]
numeros, letras = zip(*mezcla)

print(f'Números: {numeros}, Letras: {letras}')
# Números: (1, 2, 3), Letras: ('a', 'b', 'c')
```
Como vemos es la operación inversa de realizar un zip. Es decir que a partir de una lista de tuplas (generadas o no por la función zip) se pódrá recuperar los valores de los iterables iniciales.

## **Ordenar iterables generados por zip**

Mediante el método `sorted()` podemos ordenar iterables generados por la función zip. Cabe aclarar que el orden de este iterable será definido por el primer iterable pasado a la función zip.

```python
numeros = [3, 1, 2]
letras = ['c','b','a']
print(sorted(list(zip(numeros, letras))))
# [(1, 'a'), (2, 'b'), (3, 'c')]

print(sorted(list(zip(letras, numeros))))
# [('a', 1), ('b', 2), ('c', 3)]
```
Como vemos el orden de la primera lista es con respecto a los números, en cambio en la segunda lista al ser el primer iterable que le pasamos a la función zip el orden es teniendo en cuenta las letras.
