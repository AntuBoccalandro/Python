# **PEP8**

# **Porque usar PEP8**

> “La legibilidad cuenta”.
> 
> — El Zen de Python

PEP8 es una guía de estilo de código de Python para escribir código con un estilo estandarizado que lo haga legible y entendible a la vez que visualmente limpio. Esta guía fue escrita por Guido Van Rossum. La idea de PEP8 es que al estandarizar la manera en la cuál se escribe código de Python esto hace que cualquier desarrollador pueda entender el código así como el propio desarrollador. 

# **Convenciones de nombres**

> Explícito es mejor que implícito".
> 
> — El Zen de Python

Cualquier tipo de nombre de función, variable u objeto tiene una serie de reglas a seguir.

| **Tipo**       | **Convención de nombres**                                                                | **Ejemplos**                |
| ---------- | ------------------------------------------------------------------------------------ | ----------------------- |
| Funciones  | Estilo snake_case. Todas las letras en minúsculas separadas por guiones bajos.       | `my_fun`, `my_function` |
| Variables  | Estilo snake_case. Todas las letras en minúsculas separadas por guiones bajos.       | `my_var`, `my_variable` |
| Constantes | Todas las letras en mayúsculas, las palabras deben estar separadas por guiones bajos | `PI`, `MY_CONSTANT`     |
| Clases     | Primera letra en mayúsculas y el resto en mínusculas.                                | `User`, `Admin`         |
| Métodos    | Estilo snake_case. Todas las letras ene minúsculas separadas por guiones bajos.      | `method`, `get_data`    |
| Módulos    | No más de una palabra, esta debe ser corta y todo en minúsculas.                     | `package`, `mypackage`. |
| Paquetes   |

NOTA: cabe aclarar que los nombres que se utilizan en funciones, clases, objetos, etc, deben ser significativos para que describa el dato que se va a guardar o la acción que realiza un método o función. 


# **Diseño de código**

> “Hermoso es mejor que feo”.
> 
> — El Zen de Python

## **Espacios en blanco**

* **Clases**: se deben dejar 2 espacios en blanco cuando se define una clase.
    ```python
    class User:
        def __init__(self):
            pass


    user = User()
    ```
* **Métodos**: se deben separar con 1 espacio entre los métodos de la función.
    ```python
    class User:
        def __init__(self, name):
            self.name = name
        
        def get_name(self, name):
            return self.name


user = User('Jhon')
    ```
* **Funciones**: se deben separar con 1 espacio, en caso de que en la función se realizen muchas acciones, las diferentes partes de la función y el retorno.
    ```python
    from math import sqrt

    def estandar_desviation(data):
        sum1 = 0
        for value in values:
            sum1 += (value - median) ** 2
        
        radic = sum1 / (len(values) - 1)

        sum2 = 0
        for value in values:
            sum2 += value
        
        return sum2 / len(values), sqrt(radic)
    ```

## **Longitud máxima de líneas y saltos de líneas**

PEP 8 sugiere que las líneas deben limitarse a 79 caracteres. 

## **Lines break**

El máximo de caracteres en una línea puede ser de 79 caracteres, un número al que usualmente no llegaremos. Las rupturas de línea solo se podrán realizar si las expresiones se encuentran encerradas entre algún tipo de paréntesis, llaves o corchetes. 

```python
def (arg1, arg2, 
    arg3, arg4)
```
```python
data = [1, 2, 3, 4, 
        5, 6, 7, 9]
```

Si se realizan operaciones entre las expresiones siempre los operadores deben estar del lado izquierdo para mejorar la legibilidad y seguir la línea de identación.

```python
lista = [var1
        - var2
        + var3]
```
# **Identación**

> “Debería haber una, y preferiblemente solo una, forma obvia de hacerlo”.
> 
> — El Zen de Python

Se deben utilizar una tabulación de 4 espacios, no se debe utilizar un caracter de tablación. Esto es fácilmente configurable desde el editor de código o IDE que se esté utilizando.

## **Sangría después de saltos de línea**

En este caso, PEP 8 ofrece dos alternativas para ayudar a mejorar la legibilidad:

Agregue un comentario después de la condición final. Debido al resaltado de sintaxis en la mayoría de los editores, esto separará las condiciones del código anidado:

```python
x = 5
if (x > 3 and
    x < 10):
    # Both conditions satisfied
    print(x)
```

Agregue sangría adicional en la continuación de la línea:

```python
x = 5
if (x > 3 and
        x < 10):
    print(x)
```

Agrega un sangría extra cuando tiene varios argumentos y una sentencia de return:
```python
def function(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_one
```

## **Donde colocar las llaves de cierre**

Las continuaciones de línea le permiten romper líneas dentro de paréntesis, corchetes o llaves. Es fácil olvidarse de la llave de cierre, pero es importante colocarla en un lugar sensato. De lo contrario, puede confundir al lector. PEP 8 proporciona dos opciones para la posición de la llave de cierre en continuaciones de línea implícitas:

Alinee la llave de cierre con el primer carácter que no sea un espacio en blanco de la línea anterior:

```python
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]
```

Alinee la llave de cierre con el primer carácter de la línea que inicia la construcción:

```python
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
```

# **Comentarios**

> “Si la implementación es difícil de explicar, es una mala idea”.
> 
> — El Zen de Python

Debe usar comentarios para documentar el código tal como está escrito. Es importante documentar su código para que usted y sus colaboradores puedan entenderlo. 

Aquí hay algunos puntos clave para recordar al agregar comentarios a su código:
* Limite la longitud de línea de los comentarios y las cadenas de documentación a 72 caracteres.
* Usa oraciones completas, comenzando con una letra mayúscula.
* Asegúrate de actualizar los comentarios si cambias tu código.

## **Comentarios en bloque**

PEP 8 proporciona las siguientes reglas para escribir comentarios en bloque:
* Aplique sangría a los comentarios del bloque al mismo nivel que el código que describen.
* Comience cada línea con un #seguido de un solo espacio.
* Separe los párrafos por una línea que contenga un solo #.

```python
# Example 1
for i in range(0, 10):
    # Loop over i ten times and print out the value of i, followed by a
    # new line character
    print(i, '\n')


# Example 2
def quadratic(a, b, c, x):
    # Calculate the solution to a quadratic equation using the quadratic
    # formula.
    #
    # There are always two solutions to a quadratic equation, x_1 and x_2.
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)
    return x_1, x_2
```
## **Comentarios en línea**

PEP 8 tiene que decir sobre ellos:
* Utilice los comentarios en línea con moderación.
* Escriba comentarios en línea en la misma línea que la declaración a la que se refieren.
* Separe los comentarios en línea con dos o más espacios de la declaración.
* Comience los comentarios en línea con #un solo espacio, como comentarios de bloque.
* No los use para explicar lo obvio.

```
x = 5  # This is an inline comment
```

## **Documentation strings**

Las reglas más importantes que se aplican a las cadenas de documentación son las siguientes:
* Rodee las cadenas de documentación con tres comillas dobles a cada lado, como en """This is a docstring""".
* Escríbalos para todos los módulos, funciones, clases y métodos públicos.
* Coloque el """que finaliza una cadena de documentos multilínea en una línea por sí mismo:

```python
def quadratic(a, b, c, x):
    """Solve quadratic equation via the quadratic formula.

    A quadratic equation has the following form:
    ax**2 + bx + c = 0

    There always two solutions to a quadratic equation: x_1 & x_2.
    """
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)

    return x_1, x_2
```

# **Espacio en blanco en expresiones y declaraciones**

> "Disperso es mejor que denso".
> 
> — El Zen de Python

## **Espacios en blanco en operadores binarios**

Rodee los siguientes operadores binarios con un solo espacio a cada lado:
* Operadores de asignación ( =, +=, -=, etc.)
* Comparaciones ( ==, !=, >, <. >=, <=) y ( is, is not, in,not in )
* Booleanos ( and, not,or)

**Paso por valor**:
Cuando se utiliza el signo `=` para asignar un valor predeterminado a un argumento de función, no lo rodee de espacios.

```python
# Recommended
def function(default_parameter=5):
    # ...


# Not recommended
def function(default_parameter = 5):
    # ...
```
## **Combinaciones de espaciados en operaciones**

A veces cuando realizamos operaciones combinadas hay diferente orden de resolución en las diferentes operaciones, por ello PEP8 incluye algunas reglas para que estas operaciones se vean de manera más legible.

* Agregar solo espacios en blanco alrededor de los operadores con la prioridad más baja, especialmente cuando se realizan manipulaciones matemáticas

```python
# Recommended
y = x**2 + 5
z = (x+y) * (x-y)

# Not Recommended
y = x ** 2 + 5
z = (x + y) * (x - y)

# Not recommended
if x > 5 and x % 2 == 0:
    print('x is larger than 5 and divisible by 2!')

# Recommended
if x>5 and x%2==0:
    print('x is larger than 5 and divisible by 2!')
```

**En listas**

```python
list[3:4]

# Treat the colon as the operator with lowest priority
list[x+1 : x+2]

# In an extended slice, both colons must be
# surrounded by the same amount of whitespace
list[3:4:5]
list[x+1 : x+2 : x+3]

# The space is omitted if a slice parameter is omitted
list[x+1 : x+2 :]
```

## **Cuando evitar utilizar espacios en blancos**

El lugar más importante para evitar agregar espacios en blanco es al final de una línea. Esto se conoce como espacio en blanco final . Es invisible y puede producir errores que son difíciles de rastrear.

La siguiente lista describe algunos casos en los que debe evitar agregar espacios en blanco:
* Inmediatamente dentro de paréntesis, corchetes o llaves:
    ````python
    # Recommended
    my_list = [1, 2, 3]

    # Not recommended
    my_list = [ 1, 2, 3, ]
    ```

* Antes de una coma, punto y coma o dos puntos:
    ```python
    x = 5
    y = 6

    # Recommended
    print(x, y)

    # Not recommended
    print(x , y)
    ```

* Antes del paréntesis abierto que inicia la lista de argumentos de una llamada de función:
    ```python
    def double(x):
        return x * 2

    # Recommended
    double(3)

    # Not recommended
    double (3)
    ```

* Antes del paréntesis abierto que inicia un índice o segmento:
    ```python
    # Recommended
    list[3]

    # Not recommended
    list [3]
    ```
* Entre una coma final y un paréntesis de cierre:

    ```python
    # Recommended
    tuple = (1,)

    # Not recommended
    tuple = (1, )
    ```

* Para alinear operadores de asignación:
    ```python
    # Recommended
    var1 = 5
    var2 = 6
    some_long_var = 7

    # Not recommended
    var1          = 5
    var2          = 6
    some_long_var = 7
    ```

# **Recomendaciones de programación**

> “Simple es mejor que complejo.”
> 
> — El Zen de Python

A veces se agrega sintaxis extra en condiciones, ciclos anidados, etc. Es importante saber que contra más simple es la solución posiblemente la correcta (no siempre pero suele ser habitual). A veces hacemos las cosas más complejas sin necesidad, es importante saber como realizar código que sea más simple sin sacrificar la legibilidad o entendibilidad del código.

```python
# Not recommended
my_bool = 6 > 5
if my_bool == True:
    return '6 is bigger than 5'

# Recommended, no need to add the == True. Use directly de boolean var.
if my_bool:
    return '6 is bigger than 5'
```
Otros ejemplos de situaciones son:

```python
# Not recommended
my_list = []
if not len(my_list):
    print('List is empty!')

# Recommended
my_list = []
if not my_list:
    print('List is empty!')


# Recommended
if x is not None:
    return 'x exists!'

# Not recommended
if not x is None:
    return 'x exists!'


# Not Recommended
if arg:
    # Do something with arg...

# Not Recommended
if arg:
    # Do something with arg...


# Not recommended
if word[:3] == 'cat':
    print('The word starts with "cat"')

# Recommended
if word.startswith('cat'):
    print('The word starts with "cat"')


# Not recommended
if file_name[-3:] == 'jpg':
    print('The file is a JPEG')

# Recommended
if file_name.endswith('jpg'):
    print('The file is a JPEG')
```

# **Como garantizar que nuestro código siga el estándar PEP8**

PEP8 incluye muchas recomendaciones y reglas a seguir en el código, algunas podemos recordar pero siempre se pueden pasar por alto algunas.

* El uso de linters permite verficar el código para que nos aseguremos que sigue con los estándares de PEP8, los más conocidos son:
  * `pip install pycodestyle`
  * `pip install flake8`
    
* Autoformateadores
  * `pip install black` 
