# Tipos de datos > Numéricos > Módulo math

Los operadores artiméticos nos permiten hacer operaciones matemáticas con números enteros, reales y complejos pero si se quiere realizar cálculos más complejos o simplemente sacar la raíz cuadrada de un número o utilizar funciones trigonométricas el propio lenguaje exige una limitación, para ello existe el módulo math o librería math. Esta librería provee de funcionalidades matemáticas que nos permiten realizar una gran variedad de cálculos, siempre manteniendonos desde lo básico y no matemáticas avanzadas, para ello Python tiene otras librerías que nos permiten realizar otro tipo de cálculos.
 
Consideraciones a tener en cuenta es que el módulo math no soporta realizar operaciones con números complejos, para ello existe el módulo cmath.

### Importar el módulo math

```python
import math
```

### Constantes

Las constantes matemáticas son muy importantes para operaciones matemáticas. Math incluye:
* **Pi**
* **Tau**
* **Euler's number**
* **Infiniti**
* **Not a Number(NaN)**

Para acceder a cada una de ellas solo basta con acceder a la constante que se quiere saber.

```python
print(math.pi)
# 3.141592653589793

print(math.tau)
# 6.283185307179586

print(math.e)
# 2.718281828459045

print(math.inf)
# 'Positive Infinity = inf'

print(-math.inf)
# 'Negative Infinity = -inf'

print(math.nan)
# nan
```

### Funciones artiméticas

* **math.factorial(< n >)**: retorna el factorial de un número, esta alternativa es 10 veces más rápida que hacerla por recursividad o loops.
    ```python
    print(math.factorial(7))
    # 5040
    ```
* **math.ceil(< n >)**: devolverá el menor valor entero que sea mayor o igual que el número dado. La utilidad de esta función radica en pasar como parámetro números decimales ya que con números enteros retornará el mismo número introducido.
    ```python
    print(math.ceil(9.2))
    # 10

    print(math.ceil(10))
    # 10
    ```
* **math.floor(< n >)**: devolverá el valor entero más cercano que sea menor o igual que el número dado. Básicamente se comporta de la manera opuesta a la función ceil().
    ```python
    print(math.floor(9.2))
    # 9

    print(math.floor(10))
    # 10
    ```
* **math.trunc(< n >)**: trunca los decimales de un número.
    ```python
    print(math.trunc(9.289))
    # 9

    print(math.trunc(10))
    # 10
    ```
* **math.isclose()**: retorna True si se cumple la siguiente condición: *abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)*. 
    ```python
    print(math.isclose(8, 9))
    # False

    print(math.isclose(8.99999999999, 9))
    # True
    ```
    Esta función puede recibir como tercer parámetro la tolerancia mediante un argumento de clave-valor. 
    ```python
    print(math.isclose(8, 9, rel_tol=0.5))
    # True
    ```
* **math.pow()**: calcula la potencia de un número x eleveado a la n. Estos dos números se pasan como parámetros
    ```python
    print(math.pow(2, 2))
    # 4
    ```
* **math.log()**: calcula el logaritmo natural de un n número.
    ```python
    print(math.log(4))
    # 1.3862943611198906
    ```
    * **Con dos argumentos, puede calcular el logaritmo del primer argumento a la base del segundo.**
    ```python
    print(math.log(math.pi, 2))
    # 1.651496129472319
    ```
    * **math.log2()**: se calcula el logaritmo natural en base 2 de un número.
    * **math.log10()**: se calcula el logaritmo natural en base 10 de un número.

* **math.fsum()**: calcula la suma de un iterable. 
    ```python
    print(math.fsum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # 45
    ```
* **math.gcd()**: calcula el máximo común divisor entre dos números.
  ```python
    print(math.gcd(5, 25))
    # 5
    ```
* **math.sqrt()**: calcula la raíz cuadrada de un número.
    ```python
    print(math.sqrt(4))
    # 2
    ```

### Trigonometría 

* **math.radians()**: transforma a radianes grados. 
* **math.degrees()**: transforma a grados radianes. 
* **math.sin()**: calcula el seno de un ángulo.
* **math.cos()**: calcula el coseno de un ángulo.
* **math.tan()**: calcula la tangente de un ángulo.
* **math.asin()**: calcula el arcoseno de un ángulo.
* **math.acos()**: calcula el arcocoseno de un ángulo.
* **math.atan()**: calcula el arcotangente de un ángulo.
* **math.hypot()**: calcula la hipotenusa de un ángulo.
