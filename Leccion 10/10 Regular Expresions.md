# Expresiones regulares

Las expresiones regulares son patrones utilizados para encontrar una determinada combinación de caracteres dentro de una cadena de texto.


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


