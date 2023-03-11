# Expresiones regulares

Las expresiones regulares son patrones utilizados para encontrar una determinada combinación de caracteres dentro de una cadena de texto.

# Módulo re

Este es un módulo que nos permite trabajar con expresiones regulares con Python. Este ya se encuentra incluido por lo que no hace falta instalarlo.

## Importar el módulo

```python
import re
```

## Método match
## Método search
## Método findall


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


## Verificar url https
## Verificar contraseña


