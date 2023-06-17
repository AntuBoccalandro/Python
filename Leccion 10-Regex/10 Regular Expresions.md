# Expresiones regulares

Las expresiones regulares son patrones utilizados para encontrar una determinada combinación de caracteres dentro de una cadena de texto.

# Módulo re

Este es un módulo que nos permite trabajar con expresiones regulares con Python. Este ya se encuentra incluido por lo que no hace falta instalarlo.

## Importar el módulo

```python
import re
```
## Funciones Principales

### re.match()

La función `re.match()` verifica si el patrón de búsqueda se encuentra al principio de una cadena. Devuelve un objeto `Match` si se encuentra una coincidencia o `None` si no hay coincidencia.

```python
import re

texto = "Hola, ¿cómo estás?"
patron = r"Hola"

resultado = re.match(patron, texto)
if resultado:
    print("Coincidencia encontrada:", resultado.group())
else:
    print("No se encontró ninguna coincidencia.")
```

En este ejemplo, el patrón `Hola` se verifica al comienzo de la cadena `texto`. Si hay una coincidencia, se imprime el mensaje "Coincidencia encontrada" junto con la cadena coincidente. De lo contrario, se imprime "No se encontró ninguna coincidencia".

### re.search()

La función `re.search()` busca una coincidencia del patrón en toda la cadena y devuelve un objeto `Match` para la primera ocurrencia encontrada. Si no se encuentra ninguna coincidencia, devuelve `None`.

```python
import re

texto = "Hola, ¿cómo estás?"
patron = r"cómo"

resultado = re.search(patron, texto)
if resultado:
    print("Coincidencia encontrada:", resultado.group())
else:
    print("No se encontró ninguna coincidencia.")
```

En este ejemplo, el patrón `cómo` se busca en toda la cadena `texto`. Si hay una coincidencia, se imprime el mensaje "Coincidencia encontrada" junto con la cadena coincidente. De lo contrario, se imprime "No se encontró ninguna coincidencia".

### re.findall()

La función `re.findall()` busca todas las ocurrencias del patrón en la cadena y devuelve una lista de todas las coincidencias encontradas.

```python
import re

texto = "Hola, ¿cómo estás? Hola, bienvenido."
patron = r"Hola"

resultado = re.findall(patron, texto)
print("Coincidencias encontradas:", resultado)
```

En este ejemplo, el patrón `Hola` se busca en toda la cadena `texto`. Se utiliza `re.findall()` para encontrar todas las ocurrencias y se imprime la lista de coincidencias encontradas.

### re.finditer()

La función `re.finditer()` busca todas las ocurrencias del patrón en la cadena y devuelve un iterador que produce objetos `Match` para cada coincidencia encontrada.

```python
import re

texto =

 "Hola, ¿cómo estás? Hola, bienvenido."
patron = r"Hola"

resultados = re.finditer(patron, texto)
for resultado in resultados:
    print("Coincidencia encontrada:", resultado.group())
```

En este ejemplo, el patrón `Hola` se busca en toda la cadena `texto`. Se utiliza `re.finditer()` para encontrar todas las ocurrencias y se itera sobre los objetos `Match` encontrados para imprimir cada coincidencia.

### re.sub()

La función `re.sub()` reemplaza todas las ocurrencias del patrón en una cadena por un texto especificado.

```python
import re

texto = "Hola, ¿cómo estás?"
patron = r"cómo"
reemplazo = "estás"

nuevo_texto = re.sub(patron, reemplazo, texto)
print("Texto modificado:", nuevo_texto)
```

En este ejemplo, el patrón `cómo` se busca en la cadena `texto` y se reemplaza por el texto `estás`. El resultado modificado se imprime utilizando `re.sub()`.

## Patrones y Sintaxis de Expresiones Regulares

Para trabajar con expresiones regulares, necesitarás comprender la sintaxis y los patrones utilizados. Algunos de los elementos clave incluyen:

- **Metacaracteres**: Los metacaracteres son caracteres con un significado especial en las expresiones regulares, como `.`, `*`, `+`, `?`, `|`, `^`, `$`, etc.

- **Secuencias especiales**: Son combinaciones de caracteres que representan grupos de caracteres comunes, como `\d` (dígito), `\w` (carácter alfanumérico), `\s` (espacio en blanco), `\b` (límite de palabra), etc.

- **Clases de caracteres**: Permiten definir un conjunto de caracteres posibles para una posición en la expresión regular, como `[0-9]` (dígitos), `[a-z]` (letras minúsculas), `[A-Za-z]` (letras mayúsculas y minúsculas), etc.

- **Cuantificadores**: Son símbolos que indican la cantidad de repeticiones permitidas de un elemento, como `*` (cero o más), `+` (una o más), `?` (cero o una), `{n}` (exactamente n), `{n,}` (al menos n), `{n,m}` (entre n y m).

- **Grupos de captura**: Permiten agrupar elementos y capturar subcadenas coincidentes utilizando paréntesis `()`. Puedes acceder a los grupos capturados utilizando el método `group()` en un objeto `Match`.

Estos son solo algunos elementos clave de la sintaxis de expresiones regulares. Para comprender completamente todas las posibilidades y opciones, se recomienda consultar la documentación oficial de Python y explorar tutoriales y ejemplos adicionales.

## Modificadores

El módulo `re` también proporciona modificadores para ajustar el comportamiento de las expresiones regulares. Estos modificadores se pueden utilizar pasando argumentos adicionales en las funciones `re.search()`, `re.match()`, `re.findall()`, etc.

- `re.IGNORECASE` o `re.I`: Realiza coincidencias sin distinguir entre mayúsculas y minúsculas.
- `re.MULTILINE` o `re.M`:

 Permite que `^` y `$` coincidan con el inicio y el final de cada línea en lugar de solo el inicio y el final de la cadena.
- `re.DOTALL` o `re.S`: Hace que el metacarácter `.` coincida con cualquier carácter, incluidos los caracteres de nueva línea.
- `re.VERBOSE` o `re.X`: Permite escribir expresiones regulares más legibles y con comentarios utilizando múltiples líneas.

Puedes utilizar estos modificadores agregándolos como un argumento adicional en las funciones `re.search()`, `re.match()`, `re.findall()`, etc. Por ejemplo:

```python
import re

texto = "Hola, ¿cómo estás?"
patron = r"CÓMO"
resultado = re.search(patron, texto, re.IGNORECASE)
```

En este ejemplo, se utiliza el modificador `re.IGNORECASE` para realizar una coincidencia sin distinguir entre mayúsculas y minúsculas.


# Guía de keywords de expresiones regulares

**Coincidencias Basicas**
* `.`      Cualquier Caracter, excepto nueva linea
* `\d`      Cualquier Digitos (0-9)
* `\D`      No es un Digito (0-9)
* `\w`      Caracter de Palabra (a-z, A-Z, 0-9, _)
* `\W`      No es un Caracter de Palabra.
* `\s`      Espacios de cualquier tipo. (espacio, tab, nueva linea)
* `\S`      No es un Espacio, Tab o nueva linea.

**Limites**
* `\b`      Limite de Palabra
* `\B`      No es un Limite de Palabra
* `^`       Inicio de una cadena de texto
* `$`       Final de una cadena de texto

**Cuantificadores**
* `\*`       0 o Más
* `\+`       1 o Más
* `?`       0 o Uno
* `{3}`     Numero Exacto
* `{3,4}`   Rango de Numeros (Minimo, Maximo)

**Conjuntos de Caracteres**
* `[]`      Caracteres dentro de los brackets
* `[^ ]`    Caracteres que NO ESTAN dentro de los brackets

**Grupos**
* `( ) `    Grupo
* `|`       Uno u otro

# Ejemplos de expresiones regulares

## Número entero

```python
'/^\d$/'
```

## Número decimal

```python
'/^\d*\.\d+$/'
```

## Número entero o decimal

```python
'/^\d*(\.\d+)?$/'
```

## Número positivos o negativos

```python
'/^-?\d*(\.\d+)?$/'
```

## Carácter del abecedario

```python
'/^[a-zA-Z]*$/'
```

## Carácter alfanumérico

```python
'/^[a-zA-Z0-9]*$/'
```

## Verificar correo electrónico

```python
'/^([a-z0-9_\-\+-])@([0-9a-z\.-]+)\.([a-z\.]{2-6})$/'
```

## Verificar número de teléfono
Se necesita verificar un número de teléfono con el siguiente formato: 
```python

```

## Extraer los grupos de consonantes de una palabra

## Verificar url https


## Verificar contraseña


## Extraer dominio de una url


