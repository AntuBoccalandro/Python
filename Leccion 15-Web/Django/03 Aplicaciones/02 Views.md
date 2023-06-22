# Views

Las vistas son partes de la aplicación que se verán como resultado luego de acceder a las url definidas. Básicamente el contenido de las distintas urls.

### Creación de vistas

Se debe crear una función que reciba el parámetro request* y opcionalmente los parámetros de las urls. 


**Retornar respuestas HTTP**: En este ejemplo se retorna una respuesta Http con un texto. Este argumento puede ser una variable.
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home page')
```

**Retornar archivos HTML**: retornamos archivos HTML mediante la función `render`. Recibe como argumentos request y el nombre del archivo html que debe encontrarse en una carpeta templates. 
```python
mkdir templates
cd templates
touch home.html
```

```python
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```
