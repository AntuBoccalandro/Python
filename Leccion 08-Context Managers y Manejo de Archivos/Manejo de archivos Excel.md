# **Manejo de archivos de Excel con Python**

```bash
pip install openpyxl
```

# Crear un archivo Excel

El primer paso para trabajar con openxlsx es crear un archivo Excel. Podemos hacer esto utilizando la función Workbook de la librería openxlsx:

```python
from openpyxl import Workbook

# Crear un nuevo libro de Excel
libro = Workbook()

# Crear una hoja de cálculo
hoja = libro.active

# Escribir datos en la hoja de cálculo
hoja["A1"] = "Nombre"
hoja["B1"] = "Apellido"
hoja["A2"] = "Juan"
hoja["B2"] = "Pérez"

# Guardar el libro
libro.save("ejemplo.xlsx")
```

En este ejemplo, creamos un nuevo libro de Excel y una hoja de cálculo activa. Luego, escribimos datos en la hoja de cálculo y guardamos el libro en un archivo llamado "ejemplo.xlsx".
Leer datos de un archivo Excel

Para leer datos de un archivo Excel existente, podemos utilizar la función load_workbook de la librería openxlsx:

```python
from openpyxl import load_workbook

# Cargar el libro de Excel
libro = load_workbook("ejemplo.xlsx")

# Seleccionar la hoja de cálculo
hoja = libro.active

# Leer datos de la hoja de cálculo
nombre = hoja["A2"].value
apellido = hoja["B2"].value

print(nombre, apellido)
```

En este ejemplo, cargamos el libro "ejemplo.xlsx" utilizando la función load_workbook. Luego, seleccionamos la hoja de cálculo activa y leemos los datos de las celdas A2 y B2.
Modificar datos de un archivo Excel

Para modificar datos de un archivo Excel existente, podemos utilizar la misma función load_workbook y acceder a las celdas de la hoja de cálculo de la misma manera que lo hicimos para leer datos:

```python
from openpyxl import load_workbook

# Cargar el libro de Excel
libro = load_workbook("ejemplo.xlsx")

# Seleccionar la hoja de cálculo
hoja = libro.active

# Modificar datos de la hoja de cálculo
hoja["A2"] = "Pedro"
hoja["B2"] = "García"

# Guardar el libro
libro.save("ejemplo.xlsx")
```

En este ejemplo, cargamos el libro "ejemplo.xlsx" utilizando la función load_workbook. Luego, seleccionamos la hoja de cálculo activa y modificamos los datos de las celdas A2 y B2. Finalmente, guardamos el libro con los cambios realizados.
Agregar una hoja de cálculo archivo Excel existente, podemos utilizar la función create_sheet de la librería openxlsx:

```python
from openpyxl import load_workbook

# Cargar el libro de Excel
libro = load_workbook("ejemplo.xlsx")

# Crear una nueva hoja de cálculo
nueva_hoja = libro.create_sheet("Nueva Hoja")

# Escribir datos en la nueva hoja de cálculo
nueva_hoja["A1"] = "Producto"
nueva_hoja["B1"] = "Precio"
nueva_hoja["A2"] = "Camisa"
nueva_hoja["B2"] = 25.99

# Guardar el libro
libro.save("ejemplo.xlsx")
```

En este ejemplo, cargamos el libro "ejemplo.xlsx" utilizando la función load_workbook. Luego, creamos una nueva hoja de cálculo llamada "Nueva Hoja" utilizando la función create_sheet. Finalmente, escribimos datos en la nueva hoja de cálculo y guardamos el libro con los cambios realizados.
Modificar formato de celdas

Para modificar el formato de las celdas de una hoja de cálculo, podemos utilizar la propiedad number_format de las celdas de la librería openxlsx:

```python
from openpyxl import load_workbook

# Cargar el libro de Excel
libro = load_workbook("ejemplo.xlsx")

# Seleccionar la hoja de cálculo
hoja = libro.active

# Modificar el formato de las celdas
hoja["B2"].number_format = "$0.00"

# Guardar el libro
libro.save("ejemplo.xlsx")
```

En este ejemplo, cargamos el libro "ejemplo.xlsx" utilizando la función load_workbook. Luego, seleccionamos la hoja de cálculo activa y modificamos el formato de la celda B2 para que se muestre en formato de moneda. Finalmente, guardamos el libro con los cambios realizados.
Agregar un gráfico

Para agregar un gráfico a una hoja de cálculo, podemos utilizar la función add_chart de la librería openxlsx:

```python
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference

# Cargar el libro de Excel
libro = load_workbook("ejemplo.xlsx")

# Seleccionar la hoja de cálculo
hoja = libro.active

# Crear un gráfico de barras
datos = Reference(hoja, min_col=2, min_row=1, max_row=2)
grafico = BarChart()
grafico.add_data(datos)

# Agregar el gráfico a la hoja de cálculo
hoja.add_chart(grafico, "C1")

# Guardar el libro
libro.save("ejemplo.xlsx")
```

En este ejemplo, cargamos el libro "ejemplo.xlsx" utilizando la función load_workbook. Luego, seleccionamos la hoja de cálculo activa y creamos un gráfico de barras utilizando la función BarChart y la clase Reference de la librería openxlsx. Finalmente, agregamos el gráfico a la hoja de cálculo en la celda C1 y guardamos el libro con los cambios realizados.


# **Fórmulas**

Con openxlsx es posible aplicar funciones a los datos en una hoja de cálculo utilizando la clase Formula de la librería. Para hacerlo, podemos utilizar la siguiente sintaxis:

```python
from openpyxl import load_workbook
from openpyxl.utils import FORMULAE

# Cargar el libro de Excel
libro = load_workbook("ejemplo.xlsx")

# Seleccionar la hoja de cálculo
hoja = libro.active

# Aplicar una función a los datos de la hoja de cálculo
hoja["C2"] = Formula("SUM(B2:B5)")

# Guardar el libro
libro.save("ejemplo.xlsx")
```

En este ejemplo, utilizamos la clase Formula para aplicar la función SUM a los datos en el rango B2:B5 de la hoja de cálculo. Luego, guardamos el libro con los cambios realizados.

También podemos utilizar variables en las fórmulas utilizando la sintaxis de llaves {} para indicar los valores que deben ser reemplazados. Por ejemplo:

```python
from openpyxl import load_workbook
from openpyxl.utils import FORMULAE

# Cargar el libro de Excel
libro = load_workbook("ejemplo.xlsx")

# Seleccionar la hoja de cálculo
hoja = libro.active

# Definir variables
precio_unitario = 2.99
cantidad = 10

# Aplicar una función a los datos de la hoja de cálculo
hoja["C2"] = Formula("ROUND({}*{},2)".format(precio_unitario, cantidad))

# Guardar el libro
libro.save("ejemplo.xlsx")
```

En este ejemplo, definimos dos variables (precio_unitario y cantidad) y las utilizamos en una fórmula para calcular el valor total de una compra. La función ROUND se utiliza para redondear el resultado a dos decimales. Luego, guardamos el libro con los cambios realizados.

Es importante tener en cuenta que openxlsx utiliza la sintaxis de fórmulas de Excel para aplicar funciones, por lo que es necesario conocer la sintaxis y la estructura de las fórmulas en Excel para poder utilizarlas adecuadamente con esta librería.
