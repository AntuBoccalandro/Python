"""
1- Opción A: True False, esto es así porque el operador is devuelve False al comparar dos variables porque a pesar de ser iguales sus contenidos sus objetos no son los mismos.
"""
n, m = 5.0, 10
print(m/n==2, m/n is 2)

"""
2- Opción B: [4, 9], porque se llena la lista con potencias del rango: primero elevamos el 2 a la 2 = 4 y luego el 3 a la 2 = 9, no se eleva el 4 que es el valor final especificado por el rango porque este no se toma en cuenta.
"""
lst = [i**2 for i in range(2,4)]
print(lst)

"""
3- Opción A: [2, 4, 6], porque se convierte un rango en una lista, esta compuesta de un rango que empieza desde el número 2 y termina en el 7 produciendo este rango de 2 en 2. Los elementos de la lista serán, 2, 4 y 6 y no habrá más elementos ya que superarían el límite del rango.
"""
x = list(range(2,8,2))
print(x)

"""
4- Opción B: [2, 7, 12], porque se llena una lista con un rango de elemtnos que van desde el 2 hasta el número 16 de a 5 en 5. El primer elemento i equivale a 2, el segundo elemento a la suma de 2 más 5 (7), luego al 7 se le suman 5 más (12), ya no se le pueden sumar más porque exedería el límite del rango.
"""
lst = [i for i in range(2,17,5)]
print(lst)

"""
5- Opción C: 1.0, porque al dividir de manera decimal las dos variables el resultado será un número decimal.
"""
x = 24.0
y = 24
print(x/y)

"""
6- Opción D: Error, porque no se pueden hacer operaciones matemáticas con strings y datos numéricos, si se pueden sumar strings pero no un string y un float o un int.
"""
z = int(2.0)+str(5)+float(3)
print(x)

"""
8- Repetida
"""

"""
9- Opción C: 8.0, porque se le pasa como parámetro a la función el número 4, este se le asigna a la variable x que vale 4 y se multiplica por x/2, es decir, 4/2 (2), como resultado final 4 por 2 es 8.0.
"""
def function(x):
    x *= x/2
    return x
print(function(4))

"""
10- Opción D: Error, porque se está intentando sumar un entero a un string y se está imprimiendo la variable b, variable que no se encuentra declarada.
"""
x = 2
print('Hi'+3, ':Python', x)

"""
11- Repetida
"""

"""
12- Opción C: 2.0, porque se primero se resuleven las potencias, en este caso 2 a la 2 (4) y se divide decimalmente por la variable x que vale 8, es decir, 8 dividido 4 que es 2.0.
"""
y = int('2')
x = 8
print(x/y**2)