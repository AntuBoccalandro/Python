# Manejo de tiempo y fechas

## Importar módulo datetime

```python
import datetime
```

## Crear objeto time

```python
import datetime

hora = datetime.time(14,30,20,656)

print(hora.hour)
print(hora.minute)
print(hora.second)
print(hora.microsecond)
# 14
# 30
# 20
# 656
```

## Crear objeto date

```python
import datetime

fecha = datetime.date(2027,12,20)

print(fecha.year)
print(fecha.month)
print(fecha.day)
# 2023
# 12
# 20
```

## Obtener la fecha actual

```python
import datetime

fecha_hoy = datetime.date.today()

print(fecha_hoy)
# 2022-12-20
```

## Obtener la hora actual

```python
import datetime

hora_actual = datetime.datetime.now()

print(hora_actual)
# 2022-12-20 16:48:26.396251
```

## Cambiar localización de la fecha

Importar módulo `locale`
```python
import locale

# Establece el idioma a español
locale.setlocale(locale.LC_ALL, "es")

# Establece el idioma a español
locale.setlocale(locale.LC_ALL, "es_ES")

# Establece el idioma a español
locale.setlocale(locale.LC_ALL, "es_MX")
```


# Formateo de fechas y horas

El formateo de fechas y horas consiste en cambiar el modo de presentación de los datos, eligiendo entre número de mes, nombre del mes, etc. Para conocer los formateadores de este módulo se presenta la siguiente tabla.

| **Código** | **Significado**                          | **Ejemplos**                     |
| ---------- | ---------------------------------------- | -------------------------------- |
| %a         | Día de la semana abreviado               | lu., ma., ...                    |
| %A         | Día de la semana completo                | lunes, martes, ...               |
| %w         | Día de la semana como número decimal     | 0, 1, ... 6                      |
| %d         | Día del mes como número decimal con cero | 01, 02, ..., 31                  |
| %b         | Mes abreviado                            | ene., feb., ...                  |
| %B         | Mes completo                             | enero, febrero, ...              |
| %m         | Mes como número decimal con cero         | 01, 02, ...12                    |
| %Y         | Año en formato de cuatro dígitos         | 0001, 0002, ..., 2020, 2021, ... |
| %H         | Hora en formato 24h. con dos dígitos     | 00, 01, ..., 23                  |
| %I         | Hora en formato 12h. con dos dígitos     | 01, 02, ..., 12                  |
| %M         | Minutos en formato de dos dígitos        | 00, 01, ..., 59                  |
| %S         | Segundos en formato de dos dígitos       | 00, 01, ..., 59                  |


## Formatear la fecha 

```python
import datetime

fecha_ahora = datetime.date.now()

fecha_formateada = fecha_ahora.strftime("%A, %d de %B de %Y a las %H:%M")
print(fecha_formateada)
# Saturday, 24 de December de 2022 a las 09:33
```

## Formatear la hora

```python
import datetime


hora_actual = datetime.time.now()

hora_formateada = hora_actual.strftime("%I:%M:%S")
print(hora_formateada)
# 12:34:59
```

# Operaciones

## Sumar dos días a una fecha

```python
from datetime import datetime, timedelta

now = datetime.now()
new_date = now + timedelta(days=2)
```
También podemos utilizar keywords como: years, weeks, months, days, para sumar o restar estas unidades de tiempo a las fechas.

También se puede utilizar el operador de suma (`+`).

## Restar horas

Supongamos que quermos saber la edad de una persona, pero no nos basta con el año, quermos tener exactitud utilizando días y meses.
```python
from datetime import datetime

fecha1 = datetime(2001, 5, 5)  # Primera fecha
fecha2 = datetime(2023, 5, 23)  # Segunda fecha

# Calcula la diferencia total en meses
diferencia_meses = (fecha2.year - fecha1.year) * 12 + (fecha2.month - fecha1.month)

# Calcula los años y meses
anios = diferencia_meses // 12
meses = diferencia_meses % 12

print(f'{anios} años y {meses} meses')
```


