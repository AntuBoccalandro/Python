# Tkinter

Tkinter es una de las librearías de Python para crear interfaces gráficas más conocidas, no significa que sea la mejor pero si una buena opción para desarrollar aplicaciones sencillas y que no necesiten de una gran cantidad de diseño.


## Instalación

Se instala mediante pip:
```
pip install tkinter
```

# La aplicación

Siempre deberemos primero:
```python
# Importamos la librería
import tkinter as tk

# Creamos una ventana
window = tk.Tk()

# Mantenemos esta ventana abierta para que no se cierre instantaneamente
window.mainloop()
```

# Widgets

La librería cuenta con múltiples componentes ya definidos que podremos utilizar directamente.

NOTA: para agregar los widgets a la ventana creada se debe utilizar la función `.pack()`

## Label

Simplemente texto que se muestra en la ventana

```python
label = tk.Label(
    # *
    text='Hello World',
    # opcional
    foreground='white',
    # opcional
    background='black',
    # opcional
    width=10,
    # opcional
    height=10
                )
```


## Button

Un botón

```python
button = tk.Button(
    # *
    text="Click me!",
    # opcional
    width=25,
    # opcional
    height=5,
    # opcional
    bg="blue",
    # opcional
    fg="yellow",
)
```

## Obtener datos del usuario

Existen tres operaciones que se pueden hacer con los campos de entrada:
* Obtener datos
* Eliminar datos
* Insertar datos


**Crear una entrada**:
```python
entrada = tk.Entry()
```
