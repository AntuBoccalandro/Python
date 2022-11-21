# -------------------- Datos numéricos --------------------

# Integrer --> int Descripción: números enteros.
a = 10
print(type(a))

# Float --> float Descripción: números con coma o decimales.
a = 10
print(type(a))

# Complex --> complex Descripción: parte real + inmagginaria
a = 10j
print(type(a))

# -------------------- Tipo de secuencia--------------------

# String --> Str Descripción: cadena de caracteres
a = "Hola" 
a = 'Hola'
print(type(a))

# List --> list Descripción: una secuencia ordenada de datos mutables.
lista = [1, 'Hola', 10j, 5.8,]
print(type(lista))

# Tuple --> Tuple Descripción: secuencia ordenada de datos inmutables.
tupla = (1, 'Hola', 10j, 5.8)
print(type(tupla))

# -------------------- Diccionarios--------------------

# Dictionary --> dict Descripción: Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento por una clave (Key) y un valor (value).
diccionario = {
    'Nombre': 'Juan', 
    'Apellido': 'Perez', 
    'Edad': 18, 
}
print(type(diccionario))

# -------------------- Set--------------------

# Set --> set Descripción: Un conjunto es una colección desordenada , inmutable* y no indexada .
set = {1, 'Hola', 10j, 5.8}
print(type(set))


# -------------------- Booleanos-------------------- 
# Boolean --> boll Descripción: los valores boolenaos solo son dos True y False, estos nos permiten hacer operaciones lógicas mediante el álgebnra booleana.
a = True
b = False
print(type(a))

# -------------------- Conversión de datos --------------------

# Int a String
valor = 1
print(str(valor))

# Float a Int
valor = 1.0
print(int(valor))

# Int a Float
valor = 1
print(float(valor))

# Listas a Tupla
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(lista))

# Tupla a Lista
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(lista))

# Set a lista
set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(list(set))

# Lista a Set
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(set(lista))