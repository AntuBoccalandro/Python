# **Structs**

Un struct es un tipo de dato en programación que permite combinar diferentes tipos de variables en una sola unidad lógica. Es utilizado para agrupar datos relacionados y tratarlos como una entidad única. Se podría decir que es como si crearas un nuevo tipo de dato pero no necesariamente de la misma forma que lo haces con la Programación Orientada a Objetos.

Cabe aclarar que Python no incluye una sintaxis propia del lenguaje como C o C++ que permita definir sus propios structs, pero si hay maneras de "emular" su funcionamiento.

# **Definición de un struct**

```python
# El nombre struct no es necesario para crearlo
class Struct:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
```

En este código, definimos el método especial `__init__`, que es el constructor de la clase. Acepta argumentos clave-valor y utiliza la función `setattr()` para establecer los atributos de la instancia de clase.

# **Crear una instancia de la estructura**
Ahora que tenemos la clase `Struct`, podemos crear una instancia de una estructura. Para hacerlo, simplemente creamos un objeto `Struct` y proporcionamos los valores para cada campo de la estructura. Aquí hay un ejemplo:

```python
persona = Struct(nombre='Juan', edad=30, ciudad='Madrid')
```

En este ejemplo, hemos creado una instancia llamada `persona` con tres campos: `nombre`, `edad` y `ciudad`.

# **Acceder a los campos de la estructura**
Una vez que tengamos una instancia de la estructura, podemos acceder a los campos utilizando la sintaxis de punto.

```python
print(persona.nombre)
print(persona.edad)
print(persona.ciudad)
```

# **Codificar los campos de la estructura**
Si deseas modificar el valor de un campo en una estructura, simplemente asigna un nuevo valor a ese campo utilizando la sintaxis de punto. Aquí hay un ejemplo:

```python
persona.edad = 31
```

En este caso, hemos actualizado el campo `edad` de la estructura `persona` a 31.

# **Agregar métodos a la estructura**
Además de los campos, podemos agregar métodos a nuestras estructuras. Estos métodos pueden realizar operaciones o cálculos basados en los campos de la estructura. Aquí hay un ejemplo:

```python
class Persona(Struct):
    def es_mayor_de_edad(self):
        return self.edad >= 18

persona = Persona(nombre='Juan', edad=30, ciudad='Madrid')
print(persona.es_mayor_de_edad())
```

En este ejemplo, hemos creado una clase llamada `Persona` que hereda de la clase `Struct`. La clase `Persona` tiene un método `es_mayor_de_edad()` que devuelve `True` si la persona tiene 18 años o más.

# **Utilizar la estructura en tu código**
Una vez que hayas definido tu estructura y creado instancias de ella, puedes utilizarla en tu código como cualquier otro objeto. Puedes almacenar estructuras en listas, diccionarios u otras estructuras de datos según sea necesario.

```python
for persona in personas:
    print(f"Nombre: {persona.nombre}, Edad: {persona.edad}, Ciudad: {persona.ciudad}")
    print(f"¿Es mayor de edad?: {persona.es_mayor_de_edad()}")
```

¡Claro! Disculpa la interrupción. Aquí tienes la continuación del tutorial:

```python
for persona in personas:
    print(f"Nombre: {persona.nombre}, Edad: {persona.edad}, Ciudad: {persona.ciudad}")
    print(f"¿Es mayor de edad?: {persona.es_mayor_de_edad()}")
    print()
```

En este ejemplo, hemos creado una lista llamada `personas` que contiene instancias de la clase `Persona` con diferentes valores para cada campo. Luego, iteramos sobre la lista e imprimimos los valores de los campos y el resultado del método `es_mayor_de_edad()` para cada persona.

# **Utilizar estructuras anidadas**
Una ventaja de utilizar clases para simular estructuras en Python es que puedes tener estructuras anidadas. Esto significa que puedes tener campos que son a su vez instancias de otras clases. Aquí hay un ejemplo:

```python
class Dirección(Struct):
    def __init__(self, calle, ciudad, código_postal):
        self.calle = calle
        self.ciudad = ciudad
        self.código_postal = código_postal

class Persona(Struct):
    def __init__(self, nombre, edad, dirección):
        self.nombre = nombre
        self.edad = edad
        self.dirección = dirección

dirección = Dirección(calle='Calle Principal', ciudad='Madrid', código_postal='28001')
persona = Persona(nombre='Juan', edad=30, dirección=dirección)

print(f"Nombre: {persona.nombre}")
print(f"Dirección: {persona.dirección.calle}, {persona.dirección.ciudad}, {persona.dirección.código_postal}")
```

En este ejemplo, hemos creado una clase `Dirección` que representa la dirección de una persona, y la clase `Persona` que tiene un campo `dirección` que es una instancia de `Dirección`. Luego, creamos una instancia de `Persona` llamada `persona` con valores para todos los campos, incluida la dirección.

# **Añadir más funcionalidades a las estructuras**
Puedes agregar más funcionalidades a tus estructuras según tus necesidades. Por ejemplo, puedes definir métodos para realizar cálculos o manipulaciones de datos específicos. También puedes sobrescribir métodos especiales como `__str__` para controlar cómo se representa una instancia de la estructura como una cadena. Esto te brinda flexibilidad para personalizar el comportamiento de tus estructuras según tus requisitos.

