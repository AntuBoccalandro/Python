# Documentation

La documentación es muy importante para cualquier proyecto ya que facilita en el caso de los desarrolladores, la lectura del código y el entendimiento del mismo.

## Tipos de documentación
* **Documentación interna**: la constituyen los comentarios dentro del programa. La documentación interna está hecha para mejorar el entendimiento y lectura del código para los desarrolladores.
* **Documentación externa**: la constituyen manuales de la aplicación, guías de uso, etc. Básciamente está hecho para que tanto los usuarios como otros desarrolladores sepan como utilizar la aplicación.

### Comentarios en Python

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

## Uso de Docstrings

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
