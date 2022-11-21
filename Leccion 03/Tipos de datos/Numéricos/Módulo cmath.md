# Módulo cmath

Este módulo se encuentra especializado para el cálculo de números complejos. Se encunetran muchas de las funcionalidades del módulo math y funciones extras para el trabajo con números complejos. La funcionalidad de este módulo se encuentra drectamente especializado en números complejos, incluso cuando el resultado de una función sea un número real se retornará un número complejo. 

### Importación del módulo

```python
import cmath
```

### Funciones de números complejos

* **cmath.fase( < x > )**: calcula la fase de x, es el equivalente a sacar el arctg del número complejo. 
  ```python
  cmath.phase(2+3j)
  # 0.982793723247329
  ```
* **cmath.polar( < x > )**: retorna la forma polar de un número complejo, polar = (r, phi).
  ```python
  cmath.polar(2+3j)
  # (3.605551275463989, 0.982793723247329)
  ```
* **cmath.rect( < x >, < y >)**: retorna el número complejo x con coordenadas polares r y phi.
  ```python
  cmath.rect(2, 3)
  # (2+2.9999999999999996j)
  ```

### Funciones logartimicas y potencias

* **cmath.exp( < x > )**: retorna *e* elevado a la x.
  ```python
  cmath.exp(2)
  # (7.38905609893065+0j)
  ```
* **cmath.log( < x >, [ base ])**: retorna el logaritmo de x en [ base ].
  ```python

  ```
* **cmath.log10( < x > )**: retorna el logaritmo de x en base 10.
  ```python
  cmath.log(10, 2)
  # (3.3219280948873626+0j)
  ```
* **cmath.sqrt( < x > )**:  retorna la raíz cuadrada de x.
  ```python
  cmath.sqrt(-1)
  # 1j
  ```

### Funciones trigonométricas 

* **cmath.sin( < x > )**: retorna el seno de x.
  ```python
  cmath.sin(2-4j)
  # (24.83130584894638+11.356612711218174j)
  ```
* **cmath.cos( < x > )**: retorna el coseno de x.
  ```python
  cmath.cos(2-4j)
  # (-11.36423470640106+24.814651485634187j)
  ```
* **cmath.tan( < x > )**: retorna la tangente de x.
  ```python
  cmath.tan(2-4j)
  # (-0.0005079806234700387-1.0004385132020523j)
  ```
* **cmath.asin( < x > )**: retorna el arcoseno de x.
  ```python
  cmath.asin(2-4j)
  # (0.4538702099631225-2.198573027920936j)
  ```
* **cmath.acos( < x > )**: retorna el arcocoseno de x.
  ```python
  cmath.acos(2-4j)
  # (1.1169261168317741+2.198573027920936j)
  ```
* **cmath.atan( < x > )**: retorna el arcotangente de x.
  ```python
  cmath.atan(2-4j)
  # (1.4670482135772953-0.20058661813123432j)
  ```

### Funciones hiperbólicas


* **cmath.acosh( < x > )**: retorna el inverso del coseno hiperbólico de x.
  ```python
  cmath.acosh(4+9j)
  # (2.9822307095329315+1.1544751810028089j)
  ```
* **cmath.asinh( < x > )**: retorna el inverso del seno hiperbólico de x.
  ```python
  cmath.asinh(4+9j)
  # (2.9787766619541034+1.1506489896356062j)
  ```
* **cmath.atanh( < x > )**: retorna el inverso de la tangente hiperbólica de x.
  ```python
  cmath.atanh(4+9j)
  # (0.04090735594545052+1.4781223517970492j)
  ```
* **cmath.cosh( < x > )**: retorna el coseno hiperbólico de x.
  ```python
  cmath.cosh(4+9j)
  # (2.9822307095329315+1.1544751810028089j)
  ```
* **cmath.sinh( < x > )**: retorna el seno hiperbólico de x.
  ```python
  cmath.sinh(4+9j)
  # (2.9787766619541034+1.1506489896356062j)
  ```
* **cmath.tanh( < x > )**: retorna la tangente hiperbólica de x.
  ```python
  cmath.tanh(4+9j)
  # (0.04090735594545052+1.4781223517970492j)
  ```

### Funciones de clasificación 


* **cmath.isfinite( < x > )**: retorna True si tanto la parte imaginaria como real de x son finitas, y False en cualquier otro caso.
  ```python
  cmath.isfinite(cmath.inf)
  # False
  ```
* **cmath.isinf( < x > )**: retorna True si la parte real o la imaginaria de x es un infinito, y False en el caso contrario.
  ```python
  cmath.isinf(cmath.inf)
  # True
  ```
* **cmath.isnan( < x > )**: retorna True tanto si la parte real o imaginaria de x es NaN, y Falso en cualquier otro caso.
  ```python
  cmath.isnan(2+3j)
  # False
  ```
* **cmath.isclose( a, b, *, rel_tol= < n >, abs_tol= < n > )**: retorna True si los valores a y b son cercanos el uno al otro y Falso de otro modo. 
  ```python
  cmath.isclose(2e-9, 2e-8, rel_tol=1e-9, abs_tol=1e-9)
  # False
  ```
  * `rel_tol` es la tolerancia relativa – es el máximo valor permitido de la resta entre a y b, relativo al valor absoluto más grande de a o b. Por ejemplo, para fijar una tolerancia del 5%, usar rel_tol=0.05. El valor de tolerancia por defecto es 1e-09, lo que asegura que los dos valores son los mismos en aproximadamente 9 dígitos decimales. rel_tol debe ser mayor que cero. 
  * `abs_tol` es la tolerancia mínima absoluta – útil a la hora de hacer comparaciones cercanas al cero. abs_tol debe ser al menos cero. Si no ocurren errores, el resultado será: `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`.

### Constantes 


* **cmath.pi**: la constante matemática π, como número de coma flotante.
```python
cmath.pi
# 3.141592653589793
```
* **cmath.e**: la constante matemática e, como número de coma flotante.
```python
cmath.
# 2.718281828459045
```
* **cmath.tau**: la constante matemática τ, como número de coma flotante.
```python
cmath.
# 6.283185307179586
```
* **cmath.inf**: números de coma flotante de +infinito. Equivalente a float('inf').
```python
cmath.
# inf
```
* **cmath.infj**: números complejos con la parte real cero y números positivos infinitos como la parte imaginaria. Equivalente a complex(0.0, float('inf')).
```python
cmath.
# infj
```
* **cmath.nan**: el valor del número de coma flotante «not a number» (NaN) . Equivalente a float('nan').
```python
cmath.
# nan
```
* **cmath.nanj**: números complejos con parte real cero y como parte imaginaria NaN. Equivalente a complex(0.0, float('nan')).
```python
cmath.
# nanj
```
