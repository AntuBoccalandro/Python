# **Conceptos introductorios**

## **¿Qué es Flask?**

Flask es un micro-framework desarrollado en Python. Este micro-framework permite la creación de aplicaciones web o servicios sencillos. Aunque la gran cantidad de herramientas que se han ido añadiendo a Flask si se estructura bien la aplicación es posible crear aplicaciones grandes, aunque quizá sin la comodidad que dan frameworks como Django que dan una estructura ya hecha, bien definida y un patrón más claro a seguir.

En Flask la estructura la crea el programador, no hay una estructura definida que se cree al crear un proyecto de Flask (como sucede en Django o en otros frameworks como Laravel). 

# **Funcionamiento de Flask**

Cuando creemos aplicaciones con Flask es importante saber que 

# **Primer proyecto con Flask**

## **Instalación de Flask**

```bash
pip install flask
```

Una vez instalado no se nesesitará más que este paquete. A lo largo de las diferentes secciones se intalarán otros paquetes. 


## **Creación del proyecto**

```python
# Archivo app.py
from flask import Flask


# Creación de la aplicación
app = Flask(__name__)


# Ruta principal
@app.route('/')
def index():
    return 'Hola Mundo'


# Condición de ejecución
if __name__ == '__main__':
    app.run(debug=True)
```



