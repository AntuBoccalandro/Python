# Closures

Un Closure (cierre) es un objeto de función que recuerda los valores en los ámbitos incluídos, incluso si no están presentes en la memoria. Es decir, si tenemos una función externa podemos retornar la referencia a la función interna que esta contenga para que podamos acceder a ella desde fuera de la función externa que la contiene.


**Ejemplo**:
```python
def external_function(message):
    def internal_function():
        print(message)
    return internal_function

instance = external_function('Hi!')
instance()

# Hi!
```
Como vemos en este ejemplo retornando la referencia a la función interna podemos crear una instancia de esta función y luego ejecutarla aunque la internal_function no se encuentre definida fuera del programa.



