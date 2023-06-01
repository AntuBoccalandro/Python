# Operadores de unpacking

Estos operadores nos permiten descomponer una secuencia de elementos o una secuencia de elementos de clave-valor.

## Con secuencias 

El operador de unpacking `*` sirve para descomponer o desarmar una lista, tupla o secuencia de elementos como los strings.

```python
# desempaquetar
numeros = [1,2,3]
print(numeros)
# [1,2,3]
print(*numeros)
# 1 2 3
print(*numeros, sep=' - ')
# 1 - 2 - 3

# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')

sumar(*numeros)
# Resultado suma: 6

# Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a, *b, c, d = mi_lista
print(a,b,c,d)
# 1 [1, 2, 3] 4 5 6 

# Unir lista
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
# Lista de listas: [[1, 2, 3], [4, 5, 6]]
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')
# Unir listas: [1, 2, 3, 4, 5, 6]

# Construir una lista a partir de un str
lista = [*'HolaMundo']
print(lista)
# ['H', 'o', 'l', 'a', 'M', 'u', 'n', 'd', 'o']
print(*lista, sep='')
# HolaMundo
```

## Con diccionarios

Para el caso de los diccionario el operador de unpacking `*` no funcionará, para este tipo de sentencias será necesario el uso de dos asteríscos `**`. Pero la lógica es la misma que con el operador de unpacking.

```python
# Unir diccionarios
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'Unir diccionarios: {dic3}')
# Unir diccionarios: {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
```


