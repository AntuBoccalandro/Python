# Tipos de datos > Booleanos 

Los tipos de datos booleanos son aquellos que solo tienen dos posibles valores: `True` o `False`. 

### Definir un booleano

```python
boolean = True
print(type(boolean))
# <class 'bool'>

print(boolean)
# True

boolean = False
print(type(boolean))
# <class 'bool'>

print(boolean)
# False
```
### Booleanos en verdad son números

Se dice que los tipos de datos booleanos son en realidad números ya que lo que hace Python (y muchos lenguajes más) es convertir, a la hora de realizar las operaciones lógicas, los valores de True y False por unos y ceros, por lo que en verdad hablamos de los tipos de datos booleanos como unos y ceros para afirmar que algo es cierto o no.

```python
print(True == 1)
# True

print(False == 0)
# True
```
Otra manera de comprobar que los valores booleanos en verdad son números

```python
print(int(True))
# 1

print(int(False))
# 0
```
### Operadores not 

El operador not niega al valor booleano. Por ejemplo: si definimos a una variable con el valor de True y luego realizamos una comparación de igualdad contra un valor not False nos retornará el valor de True ya que se niega el valor de False. Básicamente se invierte al valor booleano opuesto. 

```txt
not <expresion>
```
```python
print(not True)
# False

print(not False)
# True

print(not False == True)
# True

print(not True == False)
# True
```

El funcionamiento del operador not se puede reducir a esta tabla:
| **A** | **B** | **a not b** |
| ----- | ----- | ----------- |
| True  | False | True        |
| False | True  | False       |

### Operador and

El operador and nos permite realizar varias expresiones lógicas. Es decir que nos permite unir varias expresiones booleanas, esto con la finalidad de ahorrar líneas de código además de hacer comprobaciones inecesarias. 

```txt
<expresion1> and <expresion2> and <expresionN>
```
```python
print(True and True)
# True

print(True and False)
# False
```

Los resultados que se esperan según el operador and se pueden ver en la siguente tabla:
| **A** | **B** | **a and b** |
| ----- | ----- | ----------- |
| True  | True  | True        |
| True  | False | False       |
| False | True  | False       |
| False | False | False       |


### Operador or

Este operador significa o, básicamente este operador nos permite realizar comparaciones lógicas en las cuales el resultado será True si una de las dos condiciones o expresiones son True. 

```txt
<expresion1> or <expresion2> or <expresionN>
```
```python
print(True or False)
# True

print(True or True)
# True
```

El funcionamiento de este operador se resume en la siguiente tabla:
| **A** | **B** | **a or b** |
| ----- | ----- | ---------- |
| True  | True  | True       |
| True  | False | True       |
| False | True  | True       |
| False | False | False      |


