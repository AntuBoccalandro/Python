# **Generadores**

Los generadores en Python son una función especial que permite generar una secuencia de valores. Los generadores devuelven un objeto iterable. Su diferencia radica en que no guardan en memoria los valores, ya que esto en algún punto genera un error de tipo MemoryError. Los generadores los consumiremos cuando nosostros querramos y no es necesario utilizar toda la secuencia. El usos de los generadores es para 

# **Definir un generador**

La keyword `yield` define un generador. 

```python
def generador():
    yield 1
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda la ejecución')
    yield 3

# Consumimos el generador a demanda
gen = generador()

# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))

# Si tratamos de consumir más valores de los que produce el generador
# lanza un error de StopIteration
print(next(gen))
# StopIteration

# Consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Número generado: {valor}')
```

## **Generar números del 1 al 5**

```python
# Generador de números del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero


# Ahora podremos consumir (iterar) este generador
for numero in generador_numeros():
    print(numero, end='-')

# 1-2-3-4-5
```

## **Generadores anónimos**

```python
# Expresión generadora (es un generador anónimo)
multiplicacion = (valor*valor for valor in range(4))
```

## **Aplicación en lectura de archivos**

Si queremos leer un archivo que es muy grande y almacenar su contenido de una sola vez (en vez de repartirlo en diferentes variables) podemos utilizar los generadores como se ve en este ejemplo.

```python
def file_openner(file_name):
    try:
        content_file = open(file_name)
        yield content_file
    finally:
        content_file.close()

with file_openner('data.txt') as archive:
    print(archive.read())
```
Podemos abrir el archivo y guardar todo el contenido pero evitando un erro de tipo MemoryError.


