# Funciones
# Def define una función para hacerlo se debe colocar def + nombre de la variable + parámetreos entre () Nota: No hace falta siempre poner un parámetro
# Las funciones sirven para crear bloques de código y luego llamar a estas funciones que realizan una acción para ahorrar líneas de código y desarrollar más rápido. 
# Las funciones en Python funcionan como los condicioanles o loops es decir que todo lo que esté dentro de loa tabulación será parte de la función y lo que no esté tabulado no.

# ---- Ejemplo Básio sin parámetros---
# def mi_funcion():
#     print('Saludos desde mi función') # Código que se ejecutará

# mi_funcion() # Llamamos a la función mi_funcion

# ---- Ejemplo Básico con parámetros---
# def mi_funcion(nombre, apellido):
#     print(f'Nombre: {nombre}, Apellido: {apellido}')

# mi_funcion('Karla', 'Lara') # Llamamos a la función y le pasamos los parámetros de nombre y apellido entre los paréntesis.

# def sumar(a, b):
#     return a + b

# resultado = sumar(5, 3) # Guardamos el return o resultado de la función en una variable llamada 'resultado'. Dentro de la variable en vez de asignarle un valor llamamos a la función sumar y le pasamos los parámetros entre ().
# print(f'Resultado de la suma: {resultado}')  # Forma 1
# print(f'Resultado de la suma: {sumar(5, 3)}') # Forma 2

# def sumar(a = 0, b = 0) -> int: # Al colocar el valor de a y b se dice que se están colocando valores por default para que la función se ejecute correctamente. También podemos específicar el tipo de dato que retornará la función, esto mediante -> datatype EJEMPLO: def fuction(a, b) -> int: . Al colocar el tipo de dato que retornará la función solo estamos dando indicios pero en verdad puede retornar cualquier otro tipo de dato.
#     return a + b

# resultado = sumar()
# print(f'Resultado de la suma: {resultado}')  
# print(f'Resultado de la suma: {sumar(2, 8)}')

# Esta es una función de argunmentos variables. Al colocar el * en sección de los parámetros se está indicando que la cantidad de parámetros o argumentos es varaible, al hacer esto los datos se convierten en tuplas por lo que son inmutables, al tratar con los valores dentro de la función hay que saber que es una tupla. Lo bueno de los argumentos variable es que podemos pasar una cantidad de argumentos indefinida.
# def listarNombres(*nombres): 
#     for nombre in nombres:
#         print(nombre)

# listarNombres('Juan', 'Karla', 'maría', 'Ernesto')

# Distintos tipos de datos como argumentos en Python

# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)

# nombres = ['Juan', 'Karla', 'Guillermo']
# desplegarNombres(nombres)
# desplegarNombres((10, 11))


# Funciones de argumentos variables por medio de diccionarios

# Funciones recursivas
# Descripción: uyna función reduriva en una función q que se manda a llamar a si misma para completar una cierta tarea

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

resultado = factorial(5)
print(f'El factoriala de 5 es {resultado}')

