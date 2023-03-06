# **Barra de progreso**

Las barras de progreso sirven para indicar la descarga de un archivo, subida de un documento o proceso que lleve un lapso de tiempo suficiente como para mostrarle al usuario una barra de progreso que se vaya completando con el tiempo de ejecución de un proceso. 


# **Módulo progress**

## Instalación 

```shell
pip install progress 
```

## Importanción

```python
from progress.bar import Bar, ChargingBar, FillingCirclesBar, FillingSquaresBar, IncrementalBar, PixelBar, ShadyBar
from progress.spinner import Spinner, PieSpinner, MoonSpinner, LineSpinner, PixelSpinner
from progress.counter import Stack, Pie, Counter, Countdown
```

## Tipos de progress-bars

![](https://camo.githubusercontent.com/38a0d4bf4f3a998b17dd032ee7778501a96d736074e0d9761da35b29518a0734/68747470733a2f2f7261772e6769746875622e636f6d2f7665726967616b2f70726f67726573732f6d61737465722f64656d6f2e676966)

**Bars**:
* Bar
* ChargingBar
* FillingCirclesBar
* FillingSquaresBar
* IncrementalBar
* PixelBar
* ShadyBar
  
**Spinners**:
* Spinner
* PieSpinner
* MoonSpinner
* LineSpinner
* PixelSpinner

**Counters**:
* Stack
* Pie
* Counter
* Countdown


## Implementación de las progress-bars

**Parámetros**
```python
my_bar = Bar('Text', fill='character', suffix='%(percent)d%%', index=start_value, max=max_value)
```
* **Text**: es el texto que acompaña a la barra. Este se sitúa en la izquierda de la barra.
* **Fill**: relleno de la barra. 
* **Suffix**: formateo del progreso de la derecha.
* **Index**: valor inicial
* **Max**: valor máximo

```python
example_bar = Bar('Installing:', max=100)

for i in range(100):
    time.sleep(0.2)
    example_bar.next()
example_bar.finish()

# Installing: |############################    | 100/100
```

## Ejemplos de todos los tipos de barras

```python
# Installing: |############################    | 100/100
example_bar = Bar('Installing:', max=100)
for i in range(100):
    time.sleep(0.2)
    example_bar.next()

example_bar.finish()


# Installing:  ███████████████████████████∙∙∙∙∙ 85%
example_bar = ChargingBar('Installing: ', max=100)
for i in range(100):
    time.sleep(0.2)
    example_bar.next()

example_bar.finish()


# Installing:  ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢ 51%
example_bar = FillingSquaresBar('Installing: ', max=100)
for i in range(100):
    time.sleep(0.2)
    example_bar.next()

example_bar.finish()


# Installing:  ◉◉◉◉◉◉◉◉◉◉◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯ 32%
example_bar = FillingCirclesBar('Installing: ', max=100)
for i in range(100):
    time.sleep(0.2)
    example_bar.next()

example_bar.finish()


# Installing:  |██████████████████████▌         | 70/100
example_bar = IncrementalBar('Installing: ', max=100)
for i in range(100):
    time.sleep(0.2)
    example_bar.next()

example_bar.finish()


# Installing:  |⣿⣿⣿⣿⣿⣿⣿⡆                        | 23/100
example_bar = PixelBar('Installing: ', max=100)
for i in range(100):
    time.sleep(0.2)
    example_bar.next()

example_bar.finish()


# Installing:  |█████████▒                      | 30/100
example_bar = ShadyBar('Installing: ', max=100)
for i in range(100):
    time.sleep(0.2)
    example_bar.next()

example_bar.finish()


# Installing: \
# Installing: |
# Installing: /
# Installing: -
example_bar = Spinner('Installing: ', max=100)
for i in range(100):
    time.sleep(1)
    example_bar.next()

example_bar.finish()


# Installing: 1
example_bar = Counter('Installing: ', max=100)
for i in range(100):
    time.sleep(1)
    example_bar.next()

example_bar.finish()


# Installing: 99
example_bar = Countdown('Installing: ', max=100)
for i in range(100):
    time.sleep(1)
    example_bar.next()

example_bar.finish()


# Installing: -
example_bar = Spinner('Installing: ', max=100)
for i in range(100):
    time.sleep(0.05)
    example_bar.next()

example_bar.finish()


# Installing: ◷
example_bar = PieSpinner('Installing: ', max=100)
for i in range(100):
    time.sleep(0.05)
    example_bar.next()

example_bar.finish()


# Installing: ◑
example_bar = MoonSpinner('Installing: ', max=100)
for i in range(100):
    time.sleep(0.05)
    example_bar.next()

example_bar.finish()


# Installing: ⎼
example_bar = LineSpinner('Installing: ', max=100)
for i in range(100):
    time.sleep(0.05)
    example_bar.next()

example_bar.finish()


# Installing: █
example_bar = Stack('Installing: ', max=100)
for i in range(100):
    time.sleep(0.05)
    example_bar.next()

example_bar.finish()


# Installing: ●
example_bar = Pie('Installing: ', max=100)
for i in range(100):
    time.sleep(0.05)
    example_bar.next()

example_bar.finish()
```

## Ejemplo de implementación en lectura de archivos

```python
from progress.spinner import Spinner
import time


character = input('Enter any character to count in the file: ')
spinner = Spinner('Leyendo: ')
counter = 0

archivo = open('file.txt', "r")

while True: 
    linea = archivo.readline()
    if linea:
        counter += linea.count(character)
    else:
        break
    time.sleep(0.1)
    spinner.next()
    
print(counter)

archivo.close

# Enter any character to count in the file: a
# 34
```

# **Módulo tqdm**

Este módulo requiere de algo más de configuraciones pero a su vez es más simple.

## Instalación 

```shell
pip install tqdm 
```

## Importanción

```python
from tqdm import tqdm, trange
```

## Implementación de las progress-bars

```python

# 100%|██████████████████████████████| 100/100 [00:01<00:00, 91.16it/s]
for num in tqdm(range(100)):
    time.sleep(0.01)


# 100%|██████████████████████████████| 100/100 [00:01<00:00, 91.16it/s]
for num in trange(100):
    time.sleep(0.01)


# Procesando d: 100%|██████████████████████████████| 4/4 [00:02<00:00,  1.99it/s]
example_bar = tqdm(['a', 'b', 'c', 'd'])
for caracter in example_bar:
    example_bar.set_description(f'Installing {caracter}')
    time.sleep(0.1)


# Procesando d: 100%|#############################| 4/4 [00:02<00:00,  1.99it/s]
for caracter in tqdm(range(100), total=100, ascii=True):
    time.sleep(0.1)
```


