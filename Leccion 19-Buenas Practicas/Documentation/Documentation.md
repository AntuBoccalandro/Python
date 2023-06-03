# **Documentation**

La documentación es muy importante para cualquier proyecto ya que facilita en el caso de los desarrolladores, la lectura del código y el entendimiento del mismo.

## **Tipos de documentación**
* **Documentación interna**: la constituyen los comentarios dentro del programa. La documentación interna está hecha para mejorar el entendimiento y lectura del código para los desarrolladores.
* **Documentación externa**: la constituyen manuales de la aplicación, guías de uso, etc. Básciamente está hecho para que tanto los usuarios como otros desarrolladores sepan como utilizar la aplicación.

## **Comentarios en Python**

Los comentarios en Python se definene mediante el signo `#`, el comentario según PEP 8 puede tener un máximo de 72 caracteres.

Comentario de una sola línea:
```python
# Este es un comentario de una sola línea
```

Comentario de varias líneas
```python
"""
Este es un comentario
de varias
líneas
"""
```
**Tips para escribir comentarios**:
* Los comentarios deben ser significativos y no redundantes. Se recomienda no comentar parte del código que se sobrentiende su funcionamiento. 
* Sirven para explicar las implementaciones de ciertos algoritmos.
* Como notas durante el desarrollo, se suelen utilizar etiquetas como: `bug`, `fixme` y `todo`.

## **Uso de Docstrings**

**Funciones**: para la documentación de funciones se utilizan 3 comillas triples en las que se deben serguir las siguientes reglas.

* Una línea de resumen de una línea
* Una línea en blanco antes del resumen
* Cualquier elaboración adicional para la cadena de documentación
* Otra línea en blanco

```python
def function(a, b):
    """function

    This function resive as parameters:
        - a
        - b
    
    Parameters
    ----------
    name : str
        the name of user
    
    Returns
    ----------
    int : 
        return the plus between a and b.
    """

    return a + b
```

**Clases**: las clases se deben documentar de otra manera ligeramente diferente. Se recomienda sesguir las reglas:

* Un breve resumen de su propósito y comportamiento.
* Cualquier método público, junto con una breve descripción.
* Cualquier propiedad de clase (atributos)
* Cualquier cosa relacionada con la interfaz para subclases, si la clase está destinada a ser subclasificada

Recomendaciones respecto al método constructor:

* Una breve descripción de qué es el método y para qué se utiliza.
* Todos los argumentos (tanto obligatorios como opcionales) que se pasan, incluidos los argumentos de palabras clave
* Etiquete cualquier argumento que se considere opcional o que tenga un valor predeterminado
* Cualquier efecto secundario que ocurra al ejecutar el método.
* Cualquier excepción que se plantee
* Cualquier restricción sobre cuándo se puede llamar al método

```python
class User:
    """
    This class represent a User.

    Attributes
    ----------
    name : str
        the name of user
    lastname : str
        the lastname of user
    password : str
        the password of uses
    

    Methods
    -------
    get_username(self)
        return de username of user object
    """

    def __init__(self, name, lastnam, password):
        """
        Parameters
        ----------
        name : str
            the name of user
        lastname : str
            the lastname of user
        password : str
            the password of uses)
        """

        self.name = name
        self.lastname = lastname
        serlf.password = password

    def get_username(self):
        """return de username of user object

        The unique parameter is self for access an username and return this data.

        Parameters
        ----------
        self : self.name
            for access to self.name of user.
        """

        return self.name
```

## **Estilos de DocStrings**

* **Google Docstrings Example:**
    ```python
    """Gets and prints the spreadsheet's header columns

    Args:
        file_loc (str): The file location of the spreadsheet
        print_cols (bool): A flag used to print the columns to the console
            (default is False)

    Returns:
        list: a list of strings representing the header columns
    """
    ```
* **reStructuredText Example:**
    ```python
    """Gets and prints the spreadsheet's header columns

    :param file_loc: The file location of the spreadsheet
    :type file_loc: str
    :param print_cols: A flag used to print the columns to the console
        (default is False)
    :type print_cols: bool
    :returns: a list of strings representing the header columns
    :rtype: list
    """
    ```

* **NumPy/SciPy Docstrings Example:**
    ```python
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is False)

    Returns
    -------
    list
        a list of strings representing the header columns
    """
    ```

* **Epytext Docstrings Example:**
    ```python
    """Gets and prints the spreadsheet's header columns

    @type file_loc: str
    @param file_loc: The file location of the spreadsheet
    @type print_cols: bool
    @param print_cols: A flag used to print the columns to the console
        (default is False)
    @rtype: list
    @returns: a list of strings representing the header columns
    """
    ```

# **Documentación de proyectos con MkDocs**

La documentación del proyecto de Python es sumamente importante ya que permite a los demás desarrolladores o contribuidores saber como funciona el proyecto, como utilizarlo, ejemplos, como está construido, etc.

Para la construcción de la documentación del proyecto es recomendable seguir los siguientes pasos:


## **Paso 1: Configurar el entorno de desarrollo**

Antes de comenzar a trabajar en su proyecto, necesita un entorno virtual en el que pueda instalar los paquetes que necesita. Será necesario agregar algunas dependencias referente a la documentación con MkDocs.
```bash
python -m pip install mkdocs
python -m pip install "mkdocstrings[python]"
python -m pip install mkdocs-material
```
Luego de la instalación deberán estar instalados los siguientes paquetes:
1. mkdocs
2. mkdocs-material
3. mkdocstrings
4. mkdocstrings-python


## **Paso 2: Crear el paquete de Python de muestra**

Este paso es omitible si ya tiene su paquete de Python desarrollado. En este paso se desarrolla el paquete como tal, con todos sus archivos, dependencias, lógica, etc.

En nuestro paquete de ejemplo creamos un paquete que funciona como una calculadora:
```python
"""
> Package Structure
calculator/
│
├── __init__.py
└── calculations.py
"""

def add(a, b):
    return float(a + b)

def subtract(a, b):
    return float(a - b)

def multiply(a, b):
    return float(a * b)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
```

## **Paso 3: Escribir y formatear los DocStrings**
El paquete mkdocstrings puede extraer información valiosa de su base de código para ayudar a generar automáticamente partes de su documentación, por lo que es altamente importante escribir buenos DocStrings.

Nuestro paquete anterior ahora quedaría documentado así:
```python
"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""


from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Calculate the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a: A number representing the minuend in the subtraction.
        b: A number representing the subtrahend in the subtraction.

    Returns:
        A number representing the difference between `a` and `b`.
    """
    return float(a - b)

def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: A number representing the multiplicand in the multiplication.
        b: A number representing the multiplier in the multiplication.

    Returns:
        A number representing the product of `a` and `b`.
    """
    return float(a * b)

def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

    Args:
        a: A number representing the dividend in the division.
        b: A number representing the divisor in the division.

    Returns:
        A number representing the quotient of `a` and `b`.

    Raises:
        ZeroDivisionError: An error occurs when the divisor is `0`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
```

```python
# Archivo __init__.py
"""Do math with your own functions.

Modules exported by this package:

- `calculations`: Provide several sample math calculations.
"""
```

Es altamente importante agregar ejemplos a los DocStrings además de los argumentos y retornos, le dan una perspectiva clara y los resultados que debería obtener el programador sin tener que ir directamente a la página con toda la documentación. Los ejemplos agregan contexto a las funciones documentadas.

**Comprobar si son correctos los DocStrings:**
Para verificar que los DocStrings están bien escritos y tienen la suficiente cantidad de ejemplos es recomendable ejecutar el siguiente comando: este comando no retornará nada si los DocStrings están correctos, en caso contrario lanzará una excepción avisando de los errores encontrados.
```bash
python -m doctest calculator\calculations.py
```
**A tener en cuenta:**
* **Además agregar TypeHints es altamente recomendable para documentar el código, asegúrese de agregarlo en su código.**
* **Agregar documentación interna sobre el propio módulo también es altamente recomendable**
* **Agregarle documentación al archivo `__init__.py` es recomendable para que se comprenda mejor todo el paquete**


## **Paso 4: Prepare su documentación con MkDocs**

Ahora es cuando realmente generaremos la documentación con dicho módulo.

Ejecute el comando para que MkDocs cree la estructura de carpetas con la documentación:
```bash
mkdocs new .
```
Carpetas y archivos creados:
```bash
mkdocs-documentation/
│
├── docs/
│   └── index.md
│
└── mkdocs.yml
```

**Configuración del archivo mkdocs.yml**

```yml
# Nombre del paquete o proyecto del que se creó la documentación
site_name: Calculation Docs
# Tema del sitio generado: material otroga una interfaz bien pensada y diseñada
theme:
  name: "material"
```

Si queremos saber como va quedando el sitio podemos ejecutar el siguiente comando, esto despliega el sitio web en local en el localhost:8000:
```bash
mkdocs serve
```

**Crear páginas estáticas a partir de Markdown**

Si se desea se puede cambiar el contenido del archivo markdown generado, inclusive se pueden crear otros adicionales.


## **Paso 5: cree su documentación con MkDocs**

Cuando ya termino de configurar, editar y terminar su documentación MkDocs tiene un comando que permite "compilar" el sitio web para que pueda ser subido a un servidor y no tenerlo simplemente en local.
```bash
mkdocs build
```

Este comando creará toda una estructura de carpetas que luego podremos subir a *github pages*, *netlify* o algún otro servicio de hosting.

Quizá la mejor opción sea almacenar el sitio web generado en *github pages*. MkDocs incluye un comando que permite crear e imlmentar la documentación del proyecto en un solo paso:
```bash
mkdocs gh-deploy
``` 
Ejecutar este comando reconstruye la documentación de sus archivos Markdown y el código fuente y la envía a la `gh-pages` rama en su repositorio remoto de GitHub, esta rama es donde se alojan los sitios en github pages.

# **Personalizando Material Docs Theme**
La personalización y configuración del sitio generado por MkDocs se hace por medio de un archivo `yaml`.

**Este es un archivo de ejemplo:**
```yaml
site_name: Calculation Docs
theme:
  language: en 
  # Set the theme's name to use
  name: material
  font:
  # Set a specific font 
    text: Roboto
  # Set a main icon
  logo: assets\customlogo.png
  # To use a bootstrap icons
  icon:
    logo: bootstrap\envelope-paper
  # Set a tab icon
  favicon: assets\favicon.png
  
  features:
    - search.share    
    - search.highlight
    - search.suggest

  # Set a theme's pallets 
  palette:
    # Palette toggle for automatic mode
    - media: "(prefers-color-scheme)"
      toggle:
        icon: material/brightness-auto
        name: Switch to light mode

    # Palette toggle for light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default 
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode

    # Palette toggle for dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to system preference


# Extras aditions to page
extra:
  # Section of translations
  alternate:
    - name: English
      link: /en/ 
      lang: en
    - name: Spanish
      link: /es/
      lang: es
  # Add a custom link to the main logo
  homepage: https://www.github.com/AntuBoccalandro
  # Analytics
  analytics:
    provider: google
    property: G-XXXXXXXXXX

  # Privacy Setting
  consent:
    title: Cookie consent
    description: >
      We use cookies to recognize your repeated visits and preferences, as well
      as to measure the effectiveness of our documentation and whether users
      find what they're searching for. With your consent, you're helping us to
      make our documentation better.
    copyright: >
      Copyright &copy; 2016 - 2023 Martin Donath -
      <a href="#__consent">Change cookie settings</a>
      consent:
    # Options 
    actions:
      - accept
      - reject
      - manage
    cookies:
      analytics: Custom name

# Navegation settings
nav:
  - Home: /
  - Languages:
    - English: /en/
    - Español: /es/

plugins:
  - search:
      lang: 
        - en
        - es
```
