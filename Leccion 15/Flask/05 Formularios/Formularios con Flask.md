# **Formularios con Flask**

Primero empezaremos viendo como obtener los datos enviados por un formulario creado en html pero luego veremos como hacer esto mediante una librería llamada `flask wtf`. 

# **Obtener datos de formularios**

Lo primero es definir la ruta a la cual llegarán los datos del formulario.

**Archivo index.html**:
```html
<form action="/forms" method="POST">
    <input type="text" name="formText">
    <input type="email" name="formEmail">
    <input type="submit">
</form>
```

**Archivo form.html**:
```html
<h2>{{ data['name'] }}</h2>
<h2>{{ data['email'] }}</h2>
```

**Archivo app.py**:
```python
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_view():
    return render_template('index.html')


@app.route('/form', methods=['POST'])
def form():
    name = request.form['NAME']
    email = request.form['EMAIL']

    return render_template('form.html', data={
        'name': name,
        'email': email
    })


if __name__ == '__main__':
    app.run(debug=True)
```
Cuando rellenemos el formulario los datos de este serán enviados a la función `/form` y esta nos retornará un archivo html con los datos enviados por el formulario.

