# Obtener valores del usuario

Cuando hablamos de obtener valores nos referimos a darle al usuario un campo donde podrá escribir una serie de datos que los almacenaremos en una variable. Para ello utilizamos la función input().

```python
numero = input("Ingrese un número: ")

# Ingrese un número:  
```

Por defecto cualquier dato que introducimos en la función es de tipo string (str) por lo que si queremos hacer que el dato introducido por el usuario se convierta a otro en cerraremos la función input() en una función de conversión de dato.

```python
numero = int(input("Ingrese un número: "))
type(numero)

# Ingrese un número: 99
# <class 'int'>
```

### Obtener contraseñas del usuario

Si se quiere realizar alguna aplicación que requiera de ingresar una contraseña es necesario utilizar una librería de Python que nos permite hacer una recolección de estos datos de una manerae específica. El modulo `getpass` que ya viene instalado con Python nos premite obtener valores del usuario de la misma manera solo que al escribir caracteres no se ve lo que estamos escribirendo, esto para mayor seguridada a la hora de ingresar contraseñas, además de que le da a la aplicación una funcionalidad bastante profesional.

```python
from getpass import getpass

password = getpass(prompt='Ingrese su contraseña: ')
print(password)

# Ingrese su contraseña: 
# 12349
```
