"""
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def max_de_dos(a,b):
    if a > b:
        return a
    else:
        return b

print(max_de_dos(10,99))

"""
2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""



"""
3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud(string):
    largo = 0
    for i in string:
        largo += 1
    return largo

"""
4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def es_vocal(letra):
    voales = ['a', 'e', 'i', 'o', 'u']
    for i in voales:
        if letra == i:
            return True
    return False


"""
5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una 
lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def suma_in_list(lista):
    for i in lista:
        suma += i
    return suma

def multip(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

"""
6 - Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(string):
    reversed_string = ''
    for i in range(len(string)):
        reversed_string += string[-i]
    return reversed_string

"""
7 - Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(string1, string2):
    reversed_string = ''
    for i in range(len(string1)):
        reversed_string += string1[-i]
    if reversed_string == string2:
        return True
    else:
        return False

print(es_palindromo('Python'))

"""
8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""

def superposicion(l1, l2):
    for i1 in l1:
        for i2 in l2:
            if i1 == i2:
                return True
    return False


"""
9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n):
    return '#' * n

"""
10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un 
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente.
"""
def procedimiento(lista):
    for i in lista:
        print('#' * i)

procedimiento([1,2,3,4,5,6,7,8,9])

"""
11- La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""
# NO FUCIONA CORRECTAMENTE
# lista = [1,2,3,4,5,6,7,8,9]
# def max_in_list(lista):
#     for i in lista:
        

"""
12- Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 
"""

lista = ['Python', 'Javascript', 'Ruby']
def mas_larga(lista):
    largo = 0
    lista_mas_larga = []
    for i in lista:
        for k in i:
            largo += 1
        lista_mas_larga.append(i)
    for i in lista_mas_larga:
        anterior = i
        if anterior > i:
            anterior = i
        else:
            anterior = anterior
    return anterior

"""
13- Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres. 
"""

lista = ['Python', 'Javascript', 'Ruby']
n = int(input('Ingrese un número: '))

def filtrar_palabras(lista, n):
    # Iteramos sobre los elementos de la lista.
    for i in lista:
        # Iteramos sobre cada sub-string de cada elemento de la lista
        largo_palabra = 0
        for k in i:
            largo_palabra += 1
        if largo_palabra < n:
            pass
        else:
            return i

print(filtrar_palabras(['Python', 'Javascript', 'Ruby'], 9))

""" 
14- Construir un pequeño programa que convierta números binarios en enteros. 
"""



""" 
15- Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""

""" 
16- Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

edades = (10,23,14,18,25,32,40,50,20,25)

def mayor_20(edades):
    personas = 0
    for i in edades:
        if i > 20:
            personas += 1
    return personas

""" 
17- Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""
# FALTA DE TERMINAR
def vowels_counter(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_counter = []
    for i in word:
        if i == vowels[0]:
            vowels_counter.insert(0, +1)
        if i == vowels[1]:
            vowels_counter.insert(1, +1)
        if i == vowels[2]:
            vowels_counter.insert(2, +1)
        if i == vowels[3]:
            vowels_counter.insert(3, +1)
        if i == vowels[4]:
            vowels_counter.insert(4, +1)
    print(vowels, vowels_counter)

"""
18- Determinar la cantidad de dígitos de un numero (1- 100000)
"""

def cantidad(n):
    cantidad = 0
    for i in str(n):
        cantidad += 1
    return cantidad

"""
19- Para un numero N menor de 100. Mostrar la suma de los cuadrados de los números que están separados entre si cuatro posiciones.
"""

def cuadrados(n):
    suma = 0
    if n > 100:
        exit
    else:
        for i in range(0, n, 4):
            suma += i ** 2
    return suma

"""
20- Imprimir 10 veces la serie de números de 1 a 10.
"""

def serie():
    for i in range(1,11):
        for k in range(1,11):
            print(k)

""" 
21- Para un número N imprimir su tabla de multiplicar.
"""

def tabla_multiplicar(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')

"""
22- Solicitar un número e imprimir los dígitos pares de este.
"""

def numeros_pares(n):
    for i in str(n):
        if int(i)%2 == 0:
            print(i)

"""
23- Los números de las claves de dos cajas fuertes están mezcladas en un
número entero llamado clave maestra. Determine ambas claves, la primera
clave se construye con los dígitos impares de la clave maestra y la
segunda con los pares. Ejemplo: Clave Maestra= 12345, clave1=135,
clave2=24.
"""

def claves(n):
    clave_par = ''
    clave_impar = ''
    for i in str(n):
        if int(i)%2 == 0:
            clave_par += str(i)
        else:
            clave_impar += str(i)
    return clave_par, clave_impar

"""
24- Mostrar la sumatoria de 1 al 100.
"""

def sumatoria():
    sumatoria = 0
    for i in range(1,101):
        sumatoria += i
    return sumatoria

"""
25- Identificar si la suma de los dígitos de un numero es par o impar. Retorne True si es par y False si es impar.
"""

def par_impar(n1, n2):
    if (n1+n2)%2 == 0:
        return True
    else:
        return False

"""
26- Crea un juego que consista en adivinar un número aleatorio
"""

import random

def guest_number():
    boolean = True
    while boolean == True:
        n = random.random(1,10)
        input_number = int(input('Introduce un número del 1 al 10: '))
        if input_number == n:
            boolean = False
    print(f'Has adivinado el número: {n}')

"""
27- Crea un generador de contraseñas que reciba como input las características que el ususario quiere para su contraseña. 
"""
# FALTA TERMINAR PARA DEJARLO A PUNTO

import random
# import pyperclip as pc

def password_generator(length):
    lower = 'abcdefghijklmnñopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    numbers = '123456789'
    simbols = '!"#$%&/()=?¡¿*,.-;:_{|°][}'
    characters = lower+upper+numbers+simbols
    password = random.choices(length, characters)
    # print(f'Contraseña: {password} {pc.copy(password)}')

"""
28- Crea un programa en el cual el usuario ingrese como dato la cantidad de minutos que quiere para su temporizador
"""

import time

def temporizador(t):
    for i in range(1, t):
        time.sleep(1)
        print(f'Tiempo restante:  = {i}')

temporizador(t=int(input('Ingrese cantidad de minutos: ')*60+1))

"""
29- Crea un programa que imprima una pirámide de asteriscos '*' de esta manera:

"""


"""
30- Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman.
"""

def rimar(word1, word2):
    if word1[-3] == word2[-3]:
        print('Riman')
    if word1[-2] == word2[-2]:
        print('Riman un poco')
    else:
        print('No riman')

"""
31- Convertr una cadena de caracteres en minúsculas y pasarlas a mayúsculas sin el método upper().
"""

"""
32- Verficar si un número es primo o no.
"""

def primo(n):
    if n%n = 0:
        return True
    else:
        return False

"""
33- 
"""