# -----------------------------Descripción ciclo for-----------------------------
# Python utiliza bucles for para iterar sobre una lista de elementos. A
# diferencia de C o Java,  que utilizan el bucle for para cambiar un valor (una variable) en cada iteración y así poder acceder a los elementos de un arreglo (array) utilizando ese valor.
# En Python los bucles for iteran sobre estructuras de datos basadas en colecciones como listas, tuplas y/o diccionarios.

# -----------------------------Sintáxis del ciclo-----------------------------
# Palabra reserada de 'for' + varaible que contendra cada uno de los elementos de nuestro arreglo + palabara de reservada de 'in' + variable que interaremos o recorrerremos.

cadena = 'Hola'

for letra in cadena:
    print(letra)

# -----------------------------Iterar con la función range()-----------------------------
# En lugar de ser una función, range() en realidad es un tipo de secuencia inmutable. La secuencia resultante tendrá una lista desde el límite inferior, p. ej. cero, hasta el límite superior menos uno.
# Por defecto el límite inferior o índice inicial será cero.
# La función range tiene varios parámetros que se pueden pasar. PARÁMETROS POSIBLES --> range(incio, fin, pasos)
# range(10) --> Irá desde el 0 hasta el 9.
# ragnge(2, 10) --> Irá desde el 2 hasta el 9.
# range(0, 11, 2) --> Irá desde el 0 hasta el 10 de 2 en 2.

for i in range(10):
    print(i)

# -----------------------------Iterar listas y tuplas-----------------------------
# Las listas o tuplas se pueden iterar de una manera muy sencilla.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for valor in lista:
    print(valor)

# Iterar dos listas de un mismo tamaño en un solo bucle con la función zip()

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for lista1, lista2 in zip(lista1, lista2):
    print(lista1, lista2)

# Iterarar sobre una lista y obtener el índice correspondiente con la función enumerate()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for indice, valor in enumerate(lista):
    print(indice, valor)


# ----------------------------Iterar diccionarios-----------------------------
# Iterar diccionarios, de esta manera solo se mostraran las keys del diccionario pero no se value
diccionario = {
    "manzana": "roja",
    "arandano": "morado",
    "banana": "amarilla",
}

for valor in diccionario:
    print(valor)

# Iterar sobre claves en un diccionario (también conocido como hashmap). Esto nos devolverá la Key y su value
diccionario = {
    "manzana": "roja",
    "arandano": "morado",
    "banana": "amarilla",
}

for key in diccionario:
    print(key, diccionario[key])

# -----------------------------Iterar sets-----------------------------
set = {"manzana", "banana", "frutilla"} 

for valor in set:
    print(valor)

# ----------------------------- Senstencias for/else-----------------------------
# En Python es posible el uso de else en bucles for, elsees ejecutado si ninguna condición dentro del bucle for se cumplió. Para poder hacer uso de elsetendremos que utilizar una sentencia break(terminar, interrumpir) y asi interrumpir el bucle for si una condición se cumple. Si el bucle for no es interrumpido la sentencia else se ejecutara 

# Este programa analiza cada día de la semana y lo compara con el día de hoy, en caso de ser cierta la condición se frenará el ciclo for y mostrará un mensaje por consola. En caso de no ser cierta la condición se ejecutará el condicional else mostrando otro mensaje.
dias_semana = ['Lunes','Martes','Miercoles','Jueves','Viernes']
hoy = 'Sabado'
for dia in dias_semana:
  if dia == hoy:
    print('Hoy es un dia laborable')
    break
else:
  print('Hoy no es un dia laborable')

# ----------------------------- Break -----------------------------
# La palabra reservada break permite detener la ejerucción del ciclo.

# Este programa lo que hace es detenerse si la condición es falsa y ejecutar el condicional else que contiene un mensaje.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if 1 > 2:
        print('1 es mayor que 2')
        break
else:
    print('1 es menor que 2')


# ----------------------------- Continue -----------------------------
# continue es una palabra clave que se utiliza para finalizar la iteración actual en un for bucle (o un while bucle) y continúa con la siguiente iteración.

# Este programa itera una lista en caso de la condición ser verdadera se dejará de ejecutar el ciclo for, en caso de ser falsa se continuará ejecutando el ciclo for
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero <= 1:
        print('1 es menor que 2')
        continue
else:
    print('Fin del ciclo for')

# -----------------------------Ejemplos-----------------------------
# Este programa imprime numeros del 1 al 10 de manera asendente. Basicamente lo que hace el programa es imprimir numeros  en un rango del 1 al 10

for i in range(1,10):
    print(i)

# -----------------------------Ejemplos-----------------------------
# Este programa imprime numeros del 1 al 10 de manera descendente. Basicamente lo que hace el programa es ir restando de 1 en 1 la variable num.
# En cada vuelta del ciclo
#     | num - i  | impresión
#  i=1    10-1        9
#  i=2    10-2        8
#  i=3    10-3        7
#  i=4    10-4        6
#  i=5    10-5        5
#  i=6    10-6        4
#  i=7    10-7        3
#  i=8    10-8        2
#  i=9    10-9        1
#  i=10   10-10       0

num=10
for i in range(1,num+1):
    print(num-i)