# **Creación de datos falsos**

Cuando estamos desarrollando necesitamos probar la aplicación, esta aplicación muchas veces necesitará datos, pero escribir estos datos resulta tedioso y una pérdida de tiempo, ya que pensar 50 nombres nos tomará un rato, y todo ello para probar la aplicación 10 seugndos y ver que no funciona. Flask-faker es una extención de Flask que permite la generación aleatoria de datos de diferente tipo para testear aplicaciones.

Cabe aclarar que los datos que genera esta librería como el mismo nombre lo indica son falsos y aleatorios, por lo que son puramente para testing y no representan información real o correcta.

## **Instalación**

Se instala mediante el comando de pip:
```bash
pip install Faker
```

# **Utilización del módulo**

```python
from flask import Flask, jsonify
from flask_faker import Faker

app = Flask(__name__)
faker = Faker(app)

@app.route('/')
def index():
    data = {
        'name': faker.name(),
        'email': faker.email(),
        'address': faker.address()
    }
    return jsonify(data)
```

Esto retornará un JSON con un nombre, email y dirección.

Los métodos que provee flask-faker son para crear un solo dato, pero si necesitamos una serie de varios datos de un tipo en específico podemos generar mediante list comprenhension o ciclos for estas listas de datos.

```python
names = [fake.name() for _ in range(50)]
print(names)
```
Esta lista contendrá 50 nombres.

Los tipos de datos que podemos generar con esta librería son:
* Nombres: nombres de personas en diferentes idiomas y formatos (nombre completo, primer nombre, apellido, prefijo, sufijo, etc.)
* Direcciones: direcciones postales completas, incluyendo calle, número, ciudad, código postal y país.
* Correos electrónicos: direcciones de correo electrónico válidas con nombres aleatorios y dominios aleatorios.
* Números: números aleatorios en diferentes formatos (enteros, decimales, positivos, negativos, etc.)
* Textos: texto aleatorio, incluyendo frases completas, párrafos, palabras, etc.
* Fechas y horas: fechas y horas aleatorias en diferentes formatos (fecha completa, día, mes, año, hora, minutos, segundos, etc.)
* Teléfonos: números de teléfono aleatorios en diferentes formatos (números fijos, móviles, nacionales, internacionales, etc.)
* Empresas: nombres de empresas, direcciones, números de identificación fiscal, etc.
* Tarjetas de crédito: números de tarjeta de crédito aleatorios válidos, incluyendo tipos de tarjeta, como Visa, Mastercard, etc.
* Usuarios y contraseñas: nombres de usuario, contraseñas y hash de contraseñas.
