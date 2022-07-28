# Condicionales en Python

# Condicional if
# -------------------- Descripción --------------------

# Si la expresión evaluada, resulta ser verdadera(True), entonces ejecuta una vez el código en la expresión. Si sucede el caso contrario y la expresión es falsa, entonces No ejecutes el código que sigue

# -------------------- Sintaxis --------------------

# La palabra reservada if , da inicio al condicional if .
# [+]   La siguiente parte es la condición. Esta puede evaluar si la declaración es verdadera o falsa. En Python estas son definidas por las palabras reservadas (True or False).  
# [+]   Paréntesis (()) Los paréntesis son opcionales, no obstante, ayudan a mejorar la legibilidad del código cuando más de una condición está presente.
# [+]   Dos puntos : cuya función es separar la condición de la declaración de ejecución siguiente.
# [+]   Una nueva línea.
# [+]   Un nivel de indentación de cuatro espacios, que es una convención en Python. El nivel de indentación es asociado con la estructura de la declaración que sigue.
# [+]   Finalmente, la estructura de la sentencia. Este es el código que será ejecutado, únicamente si la sentencia a ser evaluada es verdadera. Es posible tener múltiples líneas en la estructura de código que pueden ser ejecutadas; en este caso es necesario tener cautela en cuanto a que todas las líneas tengan el mismo nivel de indentación.

# -------------------- Ejemplo --------------------
# Este programa pasará sobre el condicioanl if, si la condición es verdadera ejecutará un mensaje, en caso de ser falsa ejeuctará la sentencia else que contiene un mensaje difer ente.

condicion = True

if condicion == True:
    print('La condicion es verdadera')

# Opción 1
if condicion == True:
    print('La condición es verdadera')
# Opción 2
if condicion == True: print('La condición es verdadera')

# Condicional else
# -------------------- Descripción --------------------

# Cuando la expresión if se evalúa como True, entonces ejecuta el código que le sigue. Pero si se evalúa como False, entonces ejecuta el código que sigue después de la sentencia else. Es explicitamente necesario tener una sentencia if antes de una sentencia else de lo contrario nos arrojará un error el programa.

# -------------------- Sintaxis --------------------

# if condición:
#   sentencia 1
# else:
#   sentencia 2


# La palabra reservada else , da inicio al condicional.
# [+]   Dos puntos : cuya función es separar la condición de la declaración de ejecución siguiente.
# [+]   Una nueva línea.
# [+]   Un nivel de indentación de cuatro espacios, que es una convención en Python. El nivel de indentación es asociado con la estructura de la declaración que sigue.
# [+]  uando la expresión if se evalúa como True, entonces ejecuta el código que le sigue. Pero si se evalúa como False, entonces ejecuta el código que sigue después de la sentencia else.

# -------------------- Ejemplo --------------------
# Este programa pasará sobre el condicioanl if, si la condición es verdadera ejecutará un mensaje, en caso de ser falsa ejeuctará la sentencia else que contiene un mensaje diferente.

a = 10
b = 20

if a == b:
    print(f'{a}  es igual a {b} ')
else:
    print(f'{a} es diferente a {b} ')

# Opción 1
if a == b:
    print(f'{a}  es igual a {b} ')
else:
    print(f'{a} es diferente a {b} ')
# Opción 2
print("A") if a > b else print("B") 

# Condicional elif
# -------------------- Descripción --------------------

# Si la primera condición es verdadera, realiza esto, si no, realiza esto otro", ahora le indicamos al programa, "Si esto no es verdadero, intenta esto otro, y si todas las condiciones fallan en ser verdaderas, entonces haz esto. 

# -------------------- Sintaxis --------------------

# if condición:
#   sentencia 1
# elif:
#   sentencia 2


# La palabra reservada elif , da inicio al condicional .
# [+]   Dos puntos : cuya función es separar la condición de la declaración de ejecución siguiente.
# [+]   Una nueva línea.
# [+]   Un nivel de indentación de cuatro espacios, que es una convención en Python. El nivel de indentación es asociado con la estructura de la declaración que sigue.
# [+]  Cuando la condición del condicional if sea falsa se ejecutará esta sentencia.

# -------------------- Ejemplo --------------------
# En este programa se revisa la primera condición, al ser falsa se ejecuta la sentencia elif que contiene una secuencia de código.

a = 1
b = 2

if a > b:
    print(f'{a} es mayor que {b}')
elif a < b:
    print(f'{a} es menor que {b}')