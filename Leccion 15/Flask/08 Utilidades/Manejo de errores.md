# **Manejo de errores en Flask**

Controlar los errores de la aplicación es clave para el buen funcionamiento de la misma. Existe un decorador en flask llamado `errorhandler` el cual se le pasa como parámetro el código de error HTTP, estas funciones cuando se ejecutan retornan un valor, puede ser un JSON o una página HTML con el error y el código de error.

```python
from flask import Flask, render_template

app = Flask(__name__)


# En caso de haber un error 404 se ejecutará esta función.
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
```

**También hay otra manera de realizar esta misma tarea:**

```python
def pagina_no_encontrada(error):
    return render_template('index.html', error=error)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
```

En este caso al registrar un manejador de errores a la aplicación esta función recibirá el código de estado HTTP y luego la función que se ejecuta en caso del error handler.
