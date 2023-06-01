# **Manejo de archivos CSV con Python**

Los archivos CSV (Comma Separated Values) es un tipo de archivo en el cual se presenta normalmente gran cantidad de datos.

**Los archivos CSV tienen esta fisonomía:**
```txt
column 1 name,column 2 name, column 3 name
first row data 1,first row data 2,first row data 3
second row data 1,second row data 2,second row data 3
...
```

Este tipo de archivos son similares a un Excel, podemos contabilizar, realizar cálculos y analizar archivos CSV con Python con su librería integrada y algunas extras.

# **Lectura de archivos CSV**

**Contenido del archivo CSV de ejemplo:**
```csv
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
```


```python
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
```

