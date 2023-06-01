# **Algoritmos**

Un algoritmo es una serie de pasos que indican como se va a resolver un determinado problema. 

# **Principales algoritmos de ordenamiento**



## **Ordenamiento por inserción (Isertion Sort)**
## **Ordenamiento por selección (Selection Sort)**
## **Ordenamiento Burbuja (Bubble Sort) [ANIMACIÓN](https://visualgo.net/en/sorting)**

El algoritmo funciona comparando pares adyacentes de elementos en la lista y, si están en el orden incorrecto, los intercambia. Este proceso se repite hasta que la lista esté completamente ordenada. La idea principal es que los elementos más grandes "floten" lentamente hacia el final de la lista, al igual que las burbujas en un líquido. 

Aquí tienes una descripción paso a paso del algoritmo de Bubble Sort:

1. Comenzando desde el principio de la lista, compara el primer elemento con el siguiente elemento.
2. Si el primer elemento es mayor que el siguiente elemento, intercámbialos de posición.
3. Avanza al siguiente par de elementos adyacentes y repite el paso anterior.
4. Continúa realizando estos pasos hasta llegar al final de la lista. Al final de la primera pasada, el elemento más grande estará en su posición correcta al final de la lista.
5. Repite los pasos 1-4 para el resto de los elementos de la lista, pero excluyendo los elementos ya colocados en su posición final.
6. Continúa realizando estas pasadas hasta que no se realicen más intercambios en una pasada completa. Esto indica que la lista está completamente ordenada.

```python
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(f'Ordered array: {bubbleSort([1, 6, 9, 3, 2, 4, 0, 4, 10])}')
# Ordered array: [0, 1, 2, 3, 4, 4, 6, 9, 10]
```

## **Ordenamiento rápido (Quick Sort)**
## **Ordenamiento por conteo (Counting Sort)**
## **Radix Sort**


