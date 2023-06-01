# **Testing**

A la hora de testear una aplicación se pueden tener dos tipos de pruebas. Por un lado las pruebas de integración son aquellas que verifican si la aplicación como tal funciona correctamente, el problema de estas es que si algo falla no puedes saber que es, para eso existen las pruebas unitarias, que permiten testear por separado cada parte, al testear una sola parte, función, clase, etc, se puede saber cual fue el problema que directamente ejecutado la aplicación y viendo que funciona y que no.


# **Librerías utilizadas en testing**

Las más utilizadas son: 
* pytest
* unittest
* nose2

Todos son muy buenos, pero utilizaremos el módulo ya incluido por Python llamado unittest.

# **Consideraciones a tener en cuenta con la escritura de tests**

Antes de sumergirse en la escritura de pruebas, primero querrá tomar un par de decisiones:

**¿Qué quieres probar?**
* ¿Está escribiendo una prueba unitaria o una prueba de integración?
* Entonces, la estructura de una prueba debería seguir este flujo de trabajo:

**Crea tus entradas**
* Ejecutar el código que se está probando, capturando la salida
* Comparar la salida con un resultado esperado

**Para esta aplicación, está probando sum(). Hay muchos comportamientos en los que sum()podría verificar, tales como:**

* ¿Puede sumar una lista de números enteros (enteros)?
* ¿Puede sumar una tupla o un conjunto?
* ¿Puede sumar una lista de flotadores?
* ¿Qué sucede cuando le proporciona un valor incorrecto, como un solo número entero o una cadena?

# **Creación de tests en Python**

Dependiendo del tamaño de la aplicación hay varias maneras de incluir los tests dentro de una aplicación de Python. 
* Si la aplicación es grande se suele crear una carpeta llamada tests, dentro hay otras subcarpetas y dentro de estás finalmente los archivos con los tests. 
* Si la aplicación es pequeña o mediana se puede crear simplemente una carpeta tests y dentro un archivo con los tests. En caso de que se requiera se puede utilizar la función `__import__()` para importar archivos con los tests pero sin necesidad de crear un paquete con un archivo `__init__ `, etc.

**Primer test**:
```python
# Importación de la librería de testing
import unittest
# Importación de la funcióna testear
from my_sum import sum


# Creacmos clase que contendrá el test 
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        # Si el resultado es igual a 6 daremos como correcto el test
        self.assertEqual(result, 6)

# Ejecutamos el test
if __name__ == '__main__':
    unittest.main()
```

## **Métodos de aserción**

Existen varios métodos de aserción que nos permiten crear nuestros tests, estos son:

| **Método**                    | **Equivalente a**      |
| ------------------------- | ------------------ |
| `.assertEqual(a, b)`      | `a == b`           |
| `.assertTrue(x)`          | `bool(x) is True`  |
| `.assertFalse(x)`         | `bool(x) is False` |
| `.assertIs(a, b)`         | `a is b`           |
| `.assertIsNone(x)`        | `x is None`        |
| `.assertIn(a, b)`         | `a in b`           |
| `.assertIsInstance(a, b)` | `isinstance(a, b)` |

`.assertIs()`, `.assertIsNone()`, `.assertIn()` y `.assertIsInstance()`todos tienen métodos opuestos, denominados `.assertIsNot()`, y así sucesivamente.

## **Puntos a tener en cuenta**

Los datos que crea como entrada se conocen como accesorios . Es una práctica común crear accesorios y reutilizarlos.

Si ejecuta la misma prueba y pasa diferentes valores cada vez y espera el mismo resultado, esto se conoce como parametrización .

## **Escenarios más complejos**

Si quiere ejecutar un test pero el valor con el cual quiere testear la unidad sabe que generará un error puede utilizar la sentencia with junto a el context manager Assert Raises. Al utilizar esto solo se pasará el test si la asersión es correcta. 

```python
import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()
```

Hay algunas técnicas simples que puede usar para probar partes de su aplicación que tienen muchos efectos secundarios, recuerda que los efectos secundarios son las acciones que hacen una implementación de una clase o función:

* Código de refactorización para seguir el principio de responsabilidad única
* Burlarse de cualquier método o llamada de función para eliminar los efectos secundarios
* Uso de pruebas de integración en lugar de pruebas unitarias para esta parte de la aplicación

Hasta ahora, ha estado aprendiendo principalmente sobre pruebas unitarias. Las pruebas unitarias son una excelente manera de crear código predecible y estable. Pero al final del día, ¡su aplicación debe funcionar cuando se inicia!

La prueba de integración es la prueba de múltiples componentes de la aplicación para verificar que funcionan juntos. Las pruebas de integración pueden requerir actuar como un consumidor o usuario de la aplicación al:

* Llamar a una API REST de HTTP
* Llamar a una API de Python
* Llamar a un servicio web
* Ejecutar una línea de comando
* 
Cada uno de estos tipos de pruebas de integración se puede escribir de la misma manera que una prueba unitaria, siguiendo el patrón Entrada, Ejecución y Afirmación. 

Es por eso que es una buena práctica separar las pruebas unitarias y las pruebas de integración. La creación de accesorios necesarios para una integración, como una base de datos de prueba y los casos de prueba en sí mismos, a menudo tarda mucho más en ejecutarse que las pruebas unitarias, por lo que es posible que solo desee ejecutar pruebas de integración antes de pasar a producción en lugar de una vez en cada confirmación.

Una forma sencilla de separar las pruebas unitarias y de integración es simplemente ponerlas en carpetas diferentes:

```bash
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    ├── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        ├── __init__.py
        └── test_integration.py
```

Si se quieren ejecutar todas las pruebas creadas en tests/integratios se deberá utilizar el siguiente comando:
```bash
python -m unittest discover -s tests/integration
```

## **Pruebas de aplicaciones basadas en datos**

Una buena técnica para usar es almacenar los datos de prueba en una carpeta dentro de su carpeta de prueba de integración llamada fixturespara indicar que contiene datos de prueba. Luego, dentro de sus pruebas, puede cargar los datos y ejecutar la prueba.

Aquí hay un ejemplo de esa estructura si los datos consisten en archivos JSON:

```bash
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    └── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        |
        ├── fixtures/
        |   ├── test_basic.json
        |   └── test_complex.json
        |
        ├── __init__.py
        └── test_integration.py
```

En un caso como este podríamos tener un test como este:

```python
import unittest


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Org XYZ")
        self.assertEqual(customer.address, "10 Red Road, Reading")


class TestComplexData(unittest.TestCase):
    def setUp(self):
        # load test data
        self.app = App(database='fixtures/test_complex.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10000)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer.name, u"バナナ")
        self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")

if __name__ == '__main__':
    unittest.main()
```
## **Pruebas en múltiples entornos**

Si se quiere probar una aplicación en mútiples entornos, como por ejemplo, en diferentes versiones de Python. 

**Instalación de tox:**
```bash
pip install tox
```

**Configuración:**
Tox se configura a través de un archivo de configuración en el directorio de su proyecto. El archivo de configuración Tox contiene lo siguiente:

* El comando ejecutar para ejecutar pruebas.
* Cualquier paquete adicional requerido antes de ejecutar
* Las versiones de destino de Python para probar contra

Creamos el archivo tox.ini gracias al comando tox-quickstart.
```bash
tox-quickstart
```

El archivo generado es algo como esto:
```ini
[tox]
envlist = py27, py36

[testenv]
deps =

commands =
    python -m unittest discover
```

**Comandos de la CLI de TOX**

Ejecute solo un único entorno, como Python 3.6:

$ tox -e py36
Vuelva a crear los entornos virtuales, en caso de que sus dependencias hayan cambiado o los paquetes del sitio estén corruptos:

$ tox -r
Ejecute Tox con una salida menos detallada:

$ tox -q
Ejecutando Tox con una salida más detallada:

$ tox -v
Puede encontrar más información sobre Tox en el sitio web de documentación de Tox .



  