# **Análisis de rendimiento de aplicaciones Python**
El análisi de rendimiento de una aplicación es sumamente importante para verifican la eficiencia de la misma, ver que no esté utilizando más memoria de la necesaria o haciendo un mal uso de la CPU.

## **Medir el tiempo de ejecución de un programa**
A través del módulo integrado time. Medimos cuando empieza a ejecutarse la función, y luego cuando termina de ejecutarse y restamos estos dos tiempos. Cabe aclarar que a continuación se muestran dos funciones. La primera como se ve en los resultados por consola no continuene un tiempo de ejecución en CPU ya que no está realizando ninguna operación que demande de la misma. En cambio, en la segunda función se ve que la función además de tardar, casi el mismo tiempo que la primer función, si demanda CPU.
```python
import time

def sleeper():
    time.sleep(1.75)


def spinlock():
    for _ in range(100_000_000):
        pass


for function in sleeper, spinlock:
    t1 = time.perf_counter(), time.process_time()
    function()
    t2 = time.perf_counter(), time.process_time()
    print(f"{function.__name__}()")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
    print()

# sleeper()
#  Real time: 1.75 seconds
#  CPU time: 0.00 seconds

# spinlock()
#  Real time: 1.77 seconds
#  CPU time: 1.77 seconds
```

## **Usando cProfile**
```python
from cProfile import Profile
from pstats import SortKey, Stats

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


with Profile() as profile:
    print(f"{fib(35) = }")
    (
        Stats(profile)
        .strip_dirs()
        .sort_stats(SortKey.CALLS)
        .print_stats()
    )

# fib(35) = 9227465
#          29860712 function calls (10 primitive calls) in 9.624 seconds

#    Ordered by: call count

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 29860703/1    9.624    0.000    9.624    9.624 <stdin>:1(fib)
#         1    0.000    0.000    0.000    0.000 pstats.py:118(init)
#         1    0.000    0.000    0.000    0.000 pstats.py:137(load_stats)
#         1    0.000    0.000    0.000    0.000 pstats.py:108(__init__)
#         1    0.000    0.000    0.000    0.000 cProfile.py:50(create_stats)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}


# <pstats.Stats object at 0x7fbbd6d47610>
```
Note: You use a separate module called pstats to format, sort, and print the collected runtime statistics. This module becomes even more useful when you dump the statistics into a binary file. In that case, you can run pstats as an interactive program to browse the file’s content in the terminal.

## **Uso de line_profiler**
```python
# Importamos la función a decorar y line_profiler
from line_profiler import LineProfiler

# Definimos la función que deseamos analizar
def mi_funcion():
    total = 0
    for i in range(1000):
        total += i
    return total

# Definimos un decorador que utilizará LineProfiler para perfilar nuestra función
def perfilador(func):
    def wrapper(*args, **kwargs):
        profiler = LineProfiler()
        profiler.add_function(func)
        profiler.enable_by_count()
        result = func(*args, **kwargs)
        profiler.disable_by_count()
        profiler.print_stats()
        return result
    return wrapper

# Decoramos nuestra función con el decorador que acabamos de definir
@perfilador
def funcion_decorada():
    return mi_funcion()

# Llamamos a nuestra función decorada para que se ejecute y se analice su rendimiento
funcion_decorada()

# Timer unit: 1e-07 s

# Total time: 0.0006791 s
# File: C:\Users\antub\Downloads\a.py
# Function: funcion_decorada at line 24

# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     24                                           @perfilador
#     25                                           def funcion_decorada():
#     26         1       6791.0   6791.0    100.0      return mi_funcion()
```
References:
* **Line number**
* **Hits:** the number of times the line is run
* **Time:** the total amount of time this line executed across all hits
* **Per Hit:** the average amount of time
% **Time:** The percentage of time spent on that line relative to the total amount of recorded time spent in the function.
