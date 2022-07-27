# Métodos de listas

lista = [1, 3, 5, 10, 4, 5]
lista.append(8) #Agrega elemento
lista.clear() # Limpia los valores internos de la lista
lista2 = lista.copy() # Copia la lista en una nueva variable
print(lista.count(5)) # count cuenta la cantidad de veces que hay un elemento
lista.remove(5) # remove elimina un elemento de la lista
añadir = [6, 7, 8] 
lista.extend(añadir) # Añade los elementos de una lista a otra
print(lista.index(3)) # Devuelve el índce de la primera aparición del elemento
print(lista.index(5, 3)) # Devuelve el índice de la segunda aparición del elemento
lista.insert(5, 20) # Inserta un elemeneto en un indice especificado en el primer parámetro
lista.pop(5) # Elimina un elemnto por su índice
lista.remove(10) # Elimina un elemnto por su valor
lista.reverse() # Reversa todos los elementos de la lista
lista.sort() # Ordena los elementos de una manera alfabética o asendente en caso de numeros.
lista.len() # Muestra el largo de un elemento, por ejemplo la palabra Hola.
print(lista)

# La estructura de este método es la siguiente:
# nombre_de_la_lista[inicio:fin:pasos]

lista[2:4] # nombre_de_la_lista[inicio:fin]
lista[1:]  # nombre_de_la_lista[inicio:]
lista[:2]  # nombre_de_la_lista[:fin]
lista[0:4:2] # nombre_de_la_lista[inicio:fin:pasos]