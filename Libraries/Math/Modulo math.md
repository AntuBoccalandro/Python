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

### Funciones trigonométricas

* **math.radians( < x >)**: transforma a grados a radianes. 
    ```python
    print(math.radians(360))
    # 6.283185307179586
    ```

* **math.degrees( < x >)**: transforma a radianes a grados. 
    ```python
    print(math.degrees(6.283185307179586))
    # 360.0
    ```

* **math.sin( < x >)**: calcula el seno de un ángulo.
    ```python
    print(math.sin(30))
    # -0.9880316240928618
    ```

* **math.cos( < x >)**: calcula el coseno de un ángulo.
    ```python
    print(math.cos(30))
    # 0.15425144988758405
    ```

* **math.tan( < x >)**: calcula la tangente de un ángulo.
    ```python
    print(math.tan(30))
    # -6.405331196646276
    ```

* **math.asin( < x >)**: calcula el arcoseno de un ángulo.
    ```python
    print(math.asin(1))
    # 1.5707963267948966
    ```

* **math.acos( < x >)**: calcula el arcocoseno de un ángulo.
    ```python
    print(math.acos(1))
    # 3.141592653589793
    ```

* **math.atan( < x >)**: calcula el arcotangente de un ángulo.
    ```python
    print(math.atan(1))
    # 0.7853981633974483
    ```
* **math.atan2( < x >)**: atan2(y, x) devuelve el valor de atan(y/x) en radianes. 
    ```python
    print(math.atan2(-0.9, -0.9))
    # -2.356194490192345
    ```

* **math.hypot( < x >)**: calcula la hipotenusa de un ángulo.
    ```python
    print(math.hypo(30))
    # 30.0
    ```
* **math.dist( < p >, < q >)**: retorna la distancia entre dos puntos p y q.
    ```python
    print(math.dist((2,4), (5,9)))
    # 5.830951894845301
    ```

### Funciones hiperbólicas

* **math.acosh( < x >)**: retorna el coseno hiperbólico inverso de x.
    ```python
    print(math.acosh(90))
    # 5.192925985263684
    ```

* **math.asinh( < x >)**: retorna el seno hiperbólico inverso de x.
    ```python
    print(math.asinh(90))
    # 5.192987713658941
    ```

* **math.atanh( < x >)**: retorna la tangente hiperbólica inversa de x.
    ```python
    print(math.atanh(0.5))
    # 0.5493061443340549
    ```

* **math.cosh( < x >)**: retorna el coseno hiperbólico de x.
    ```python
    print(math.cosh(90))
    # 6.102016471589204e+38
    ```

* **math.sinh( < x >)**: retorna el seno hiperbólico de x.
    ```python
    print(math.sinh(90))
    # 6.102016471589204e+38
    ```

* **math.tanh( < x >)**: retorna la tangente hiperbólica de x.
    ```python
    print(math.tanh(90))
    # 1.0
    ```
