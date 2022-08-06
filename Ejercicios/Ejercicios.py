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

print(longitud('Juan'))

"""
4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def es_vocal(letra):
    voales = ['a', 'e', 'i', 'o', 'u']
    for i in voales:
        if letra == i:
            return True
    return False

print(es_vocal('a'))

# 5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una 
# lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def suma_in_list(lista):
    for i in lista:
        suma += i
        return suma

print(suma_in_list([1,2,3,4,5,6,7,8,9]))


def multiplicacion_in_lista(lista):
    for i in lista:
        largo *= i

print(suma_in_list([1,2,3,4,5,6,7,8,9]))

"""6 - Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(string):
    reversed_string = string[::-1]
    return reversed_string

print(inversa('Python'))

"""7 - Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(string):
    reversed_string = string[::-1]
    if reversed_string == string:
        return True

print(es_palindromo('Python'))


# 8 - Definir una función superposicion() que tome dos listas y devuelva True 
# si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(l1, l2):
    for i1 in l1:
        for i2 in l2:
            if i1 == i2:
                return True
    return False

print(superposicion([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]))


# 9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(n):
    return '#' * n

print(generar_n_caracteres(9))

# 10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un 
# histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente.

def procedimiento(lista):
    for i in lista:
        print('#' * i)

procedimiento([1,2,3,4,5,6,7,8,9])