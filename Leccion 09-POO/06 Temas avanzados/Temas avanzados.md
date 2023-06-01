# **Sobrecarga de operadores**

La sobrecarga de operadores consiste en utilizar la programación orientada a objetos para crear clases en las que definamos que va a hacer cada operador. Esto nos permite ahorrar mucho tiempo en proyectos, sobre todo grandes. Por ejemplo podríamos sobrecargar el operador de suma para que reste dos objetos de nuestra clase, esto resultaría contraintuitivo pero nos permite realizar operaciones personalizadas con los objetos de una clase propia.

```python
class Vector:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector (self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector (self.x - v.x, self.y - v.y)

    def __mul__(self, s):
        return Vector (self.x * s, self.y * s)

    def __repr__(self):
        return f'<Vector ({self.x}, {self.y})>'


a = Vector (3, 5)
b = Vector (2, 7)
print(a + b)
# <Vector (5, 12)>

print(b – a)
# <Vector (-1, 2)>

print(b * 1.3)
# <Vector (2.6, 9.1)>
```
Como vemos hemos creado una clase Vector en la cual hemos definido una serie de métodos que nos permiten utilizar los operadores de suma, resta y multiplicación para realizar operaciones específicas con los objectos de tipo Vector.

## **Tabla de operadores**

Existen otros operadores, básicamente todos los que ofrece Python. Todos estos operadores los podríamos sobrecargar en nuestros programas.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*hg0oywDt__rvkBDeEeov7Q.png)



# **Métodos mágicos**

Los métodos mágicos o dunder-methods son métodos definidos con dos guiones bajos al principio y al final del nombre del método. Estos métodos vienen integrados en Python, como el método `__init__`.

## **Lista de dunder-methods**

![](https://aprendepython.es/_images/magic-methods-list.jpg)

A partir de todos estos métodos podemos realizar comparaciónes y operaciones con objetos. Por ejemplo comparar el atributo fuerza de dos objetos.

```python
class Player:
    def __init__(self, name, power):
        self.power = power
        self.name = name


    def __eq__(self, obj):
        return True if self.power == obj.power else False

    def __ne__(self, obj):
        return True if self.power != obj.power else False

    def __lt__(self, obj):
        return True if self.power < obj.power else False

    def __gt__(self, obj):
        return True if self.power > obj.power else False

    def __le__(self, obj):
        return True if self.power <= obj.power else False

    def __ge__(self, obj):
        return True if self.power >= obj.power else False
    


player1 = Player('Player1', 200)
player2 = Player('Player2', 200)
print(player1.__eq__(player2))
print(player1.__ne__(player2))
print(player1.__lt__(player2))
print(player1.__gt__(player2))
print(player1.__le__(player2))
print(player1.__ge__(player2))

# True
# False
# False
# False
# True
# True
```


# **Representación de objetos**

La representación de objetos consiste en definir un dunder-method que nos permita mostrar la forma en la cual se muestra el objeto para el programador.

**Existen dos métodos de representación de objetos:**
* `__str__` su objetivo es que la informacion sea legible para el usuario
* `__repr__` su objetivo es que la informacion no sea ambigua
  
Es más recomendable utilizar el método `__repr__` ya que es más robusto, nos permite representar mayor cantidad de objetos. Además cuando llamamos al método str no se encuentra definido se llamará (por defecto) al método `__repr__`.

## **Método __str__**

Uno de los métodos mágicos más utilizados es `__str__` que permite establecer la forma en la que un objeto es representado como cadena de texto.

```python
class Player:
    def __init__(self, name, power):
        self.power = power
        self.name = name


    def __str__(self):
        return f'Name: {self.name} - Power: {self.power}'
    


print(player1.__str__())
print(player1)
print(str(player1))
print(f'{player1!s}')

# Name: PLayer1 - Power: 200
# Name: PLayer1 - Power: 200
# Name: PLayer1 - Power: 200
# Name: PLayer1 - Power: 200
```
Las maneras de llamar al método str son varias. Se puede llamar como método de instancia, imprimiendo el objeto, pasando el objeto como parámetro de la función str o con un f-string con un signo de exclamación y una s que llama explícitamente al método str. Como vemos cuando llamamos al método str este nos retorna la representación del objeto. Pero este método también es útil a la hora de imprimir un objeto, ya que se mostrará la representación del objeto que hemos definido en el método str y no su dirección de memoria como se ve en el siguiente ejemplo.

```python
class Player:
    def __init__(self, name, power):
        self.power = power
        self.name = name


player1 = Player('Player1', 200)
print(player1)

# <__main__.Player object at 0x000001b8379b9bd0>
```

## **Método __repr__**

Este método funciona de la misma manera que `__str__`, retornando la representación del objeto. Pero este método es más recomendado para realizar esta acción. Pues el método `__str__` llama al método `__repr__` para mostrar la representación del objeto. Además es utilizado más que para representar información del objeto es utilizado para retornar la información de tipo constructor de la clase, como el nombre de la clase y los nombres de los atributos que tiene la clase y no los valores de los atributos que un objeto tiene, como sucedía con el método str.

```python
class My_class:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color


    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.marca!r}, {self.modelo}, {self.color!r})')
    


obj = My_class('Marca', 'Modelo', 'Color')
print(obj.__repr__())
print(obj)
print(repr(obj))
print(f'{obj!r}')

# My_class('Marca', Modelo, 'Color')
# My_class('Marca', Modelo, 'Color')
# My_class('Marca', Modelo, 'Color')
# My_class('Marca', Modelo, 'Color')
```
Como vemos esto muestra el nombre de la clase y luego mostramos la representación de cada uno de los atributos de la clase.

# **Gestores de contexto con clases**

Los gestores de contexto nos permiten ahorrarnos código. Por ejemplo al abrir un archivo, etc. En Python existen los métodos `__enter__` y `__exit__` que nos permiten trabajar con este tipo de funcionalidad.

Primero veamos la teoría:
* **__init__(self, params)**: la función init
* **__enter__(self)**: se ejecuta automáticamente se entra al bloque with.
* **__exit__(self, exc_type, exc_value, traceback)**: se ejecuta siempre al final del bloque with, aunque ocurra una excepción este método se ejecutará.
  * exc_type: Tipo de excepción que fue lanzada. En nuestro ejemplo sería <class 'Exception'>
  * exc_value: Valor de la excepción en el caso de que fuera proporcionado.
  * traceback: Objecto traceback con más información acerca de la excepción.

**Creando nuestro propia clase que permita al uso del context manager with**:
```python
class MiClaseFichero:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def __enter__(self):
        self.fichero = open(self.nombre_fichero, 'w')
        return self.fichero

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichero:
            self.fichero.close()


with MiClaseFichero('file.txt') as fichero:
    print(fichero.read())
```
Lo que está sucediendo es lo siguiente:
* En el `__init__` guardamos el nombre del fichero que queremos crear, nada nuevo.
* En el `__enter__` creamos un fichero, lo almacenamos en nuestra clase, y devolvemos la referencia que será usada dentro del with.
* Por último en el `__exit__` cerramos el fichero si estaba abierto.

## **Gestores de contexto con decoradores**

Si no queremos utilizar programación orientada a objetos o simplemente implementar esta solución implica crear código innesesario o que se podría reducir, podemos utilizar el decorador `@contextmanager`.

```python
from contextlib import contextmanager

@contextmanager
def gestor_fichero(nombre_fichero):
    try:
        fichero = open(nombre_fichero, 'w')
        yield fichero
    finally:
        fichero.close()


with gestor_fichero('file.txt') as fichero:
    print(fichero.read())
```

Como puedes ver, el contenido del `try` sería el equivalente al contenido del `__enter__` y el `finally` al del `__exit__`. Una vez tenemos definida nuestra función, podemos usarla de la misma forma que hemos visto anteriormente. Para finalizar podemos ver que se hace uso del generador `yield` este lo utilizamos para almacenar el archivo abierto en esta variable, pero sin producir un desbordamiento de memoria en caso de que el fichero abierto sea muy grande.

# **Agregación y composición**

![](https://aprendepython.es/_images/aggregation-composition.jpg)

## **Agregación**

La agregación es un tipo de asociación que indica que una clase es parte de otra clase (composición débil). Los componentes pueden ser compartidos por varios compuestos (de la misma asociación de agregación o de varias asociaciones de agregación distintas). Es importante saber que cuando agregamos un componente a nuestra clase este es independiente, por lo que si eliminarmos la clase que tiene ese componente este no se eliminará como pasa en la composición. 

**Ejemplo**:
```python
class Computer:
    def __init__(self, case = 'ofimatic model'):
        self.cpu = Cpu('AMD', 32, 16, 5600)
        self.gpu = Gpu('Nvidia', 10000, 3500)
        self.ram = Ram('Hyperx', 32, 3200)
        self.ssd = Ssd('Kingston', 1000, 7600, 7600)
        self.psu = Psu('Redragon', 850, True)
        self.case = case


    def __repr__(self):
        return f'Computer -> Cpu: {self.cpu} - Gpu: {self.gpu} - Ram: {self.ram} - Ssd: {self.ssd} - Psu: {self.psu} - Case: {self.case}'


class Cpu:
    def __init__(self, brand, threads, cores, frecuency):
        self.brand = brand
        self.threads = threads
        self.cores = cores
        self.frecuency = frecuency

    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - Threads: {self.threads} - Cores: {self.cores} - Frecuency: {self.frecuency}'


class Gpu:
    def __init__(self, brand, cores, frecuency):
        self.brand = brand
        self.cores = cores
        self.frecuency = frecuency

    def __repr__(self):
        return f'GPU -> Brand: {self.brand} - Cores: {self.cores} - Frecuency: {self.frecuency}'


class Ram:
    def __init__(self, brand, capacity, frecuency):
        self.brand = brand
        self.capacity = capacity
        self.frecuency = frecuency

    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - Capacity: {self.capacity}GB - Frecuency: {self.frecuency}'


class Ssd:
    def __init__(self, brand, capacity, read_speed, write_speed):
        self.brand = brand
        self.capacity = capacity
        self.read_speed = read_speed
        self.write_speed = write_speed

    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - Capacity: {self.capacity}GB - ReadSpeed: {self.read_speed} - WriteSpeed: {self.write_speed}'

 
class Psu:
    def __init__(self, brand, power, is_certificated):
        self.brand = brand
        self.power = power
        self.is_certificated = is_certificated


    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - PowerCapacity: {self.power} - IsCertificated: {self.is_certificated}'
    

class Case:
    def __init__(self, brand, dimentions):
        self.brand = brand
        self.dimentions = dimentions


    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - Dimentions: {self.dimentions[0]} x {self.dimentions[1]}cm'
    



case = Case('Msi', (40, 65))
my_computer = Computer(case)
print(my_computer)
```
Como vemos tenemos una clase que implementa composición pero a su vez también agregación. El atributo case de la clase Computer no es necesario para que la computadora funcione ya que esta puede hacerlo sin necesidad de un gabinete. Lo mismo podríamos hacer agregandole otras propiedades como ventiladores, refrigeración líquida, etc.


## **Composición**

Es el mecanismo en el cual una clase se construye a partir de otros objetos de igual o distinto tipo, pudiéndolos combinar para obtener la funcionalidad deseada. Es importante saber que cuando componemos un componente a otra clase este depende totalmente de esta clase, por lo que si la eliminasemos todo la instancia se eliminaría ya que depende del otro componente para funcionar.

**Ejemplo**:
```python
class Computer:
    def __init__(self):
        self.cpu = Cpu('AMD', 32, 16, 5600)
        self.gpu = Gpu('Nvidia', 10000, 3500)
        self.ram = Ram('Hyperx', 32, 3200)
        self.ssd = Ssd('Kingston', 1000, 7600, 7600)
        self.psu = Psu('Redragon', 850, True)


    def __repr__(self):
        return f'Computer -> Cpu: {self.cpu} - Gpu: {self.gpu} - Ram: {self.ram} - Ssd: {self.ssd} - Psu: {self.psu}'


class Cpu:
    def __init__(self, brand, threads, cores, frecuency):
        self.brand = brand
        self.threads = threads
        self.cores = cores
        self.frecuency = frecuency

    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - Threads: {self.threads} - Cores: {self.cores} - Frecuency: {self.frecuency}'


class Gpu:
    def __init__(self, brand, cores, frecuency):
        self.brand = brand
        self.cores = cores
        self.frecuency = frecuency

    def __repr__(self):
        return f'GPU -> Brand: {self.brand} - Cores: {self.cores} - Frecuency: {self.frecuency}'


class Ram:
    def __init__(self, brand, capacity, frecuency):
        self.brand = brand
        self.capacity = capacity
        self.frecuency = frecuency

    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - Capacity: {self.capacity}GB - Frecuency: {self.frecuency}'


class Ssd:
    def __init__(self, brand, capacity, read_speed, write_speed):
        self.brand = brand
        self.capacity = capacity
        self.read_speed = read_speed
        self.write_speed = write_speed

    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - Capacity: {self.capacity}GB - ReadSpeed: {self.read_speed} - WriteSpeed: {self.write_speed}'

 
class Psu:
    def __init__(self, brand, power, is_certificated):
        self.brand = brand
        self.power = power
        self.is_certificated = is_certificated


    def __repr__(self):
        return f'CPU -> Brand: {self.brand} - PowerCapacity: {self.power} - IsCertificated: {self.is_certificated}'
    


my_computer = Computer()
print(my_computer)
```
Como vemos tenemos una clase llamada Computer la cual tiene como propiedades a las instancias de las clases de cada componente, las cuales tienen a su vez sus propias propiedades. 


# **Creación de un nuevo tipo de dato**

Como todo en Python es un objeto podemos crear una clase cuyos objetos sean un nuevo tipo de dato. Para ello tenemos que aplicar muchos de los conocimiento aprendidos hasta ahora, como los dunder-methods.

```python
class Vector:
    def __init__(self, *v):
        self.v = list(v)

    @classmethod
    def fromlist(cls, v):
        if not isinstance(v, list):
            raise TypeError
        inst = cls()
        inst.v = v
        return inst

    def __repr__(self):
        args = ', '.join(repr(x) for x in self.v)
        return 'Vector({})'.format(args)

    def __len__(self):
        return len(self.v)

    def __getitem__(self, i):
        return self.v[i]

    def __add__(self, other):
        # Adición de elementos
        v = [x + y for x, y in zip(self.v, other.v)]
        return Vector.fromlist(v)

    def __sub__(self, other):
        # Sustracción de elementos
        v = [x - y for x, y in zip(self.v, other.v)]
        return Vector.fromlist(v)

    def __mul__(self, scalar):
        # Multiplicación por escalas
        v = [x * scalar for x in self.v]
        return Vector.fromlist(v) 


a = Vector(1,2,3,4)
b = Vector(5,6,7,8)
print("\n")

# Tipo de dato
print("Tipo de dato: %s" % type(a))

# Longitud del Vector
n = len(a)
print("Numero de Elementos en el vector: %s" % n)
print("\n")

# Elementos de los vectores
for x in a:
	print(x**2)
print("\n")

# Multiplicación de Vectores por escala.
mult = a * 5
print(mult)
print("\n")

# Adición de vectores
suma = a + b
print(suma)
print("\n")

# Sustracción de Vectores
res = a - b
print(res)
```

# **Decoradores con clases**

Ya se ha explicado a fondo la creación de decoradores por medio de funciones por lo que esta sección será bastante práctica y solo se explicarán los nuevos conceptos.

## **Definir un decorador**

```python
class Decorator(object):
  """Clase de decorador simple."""
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print('Antes de ser llamada la función.')
    retorno = self.func(*args, **kwargs)
    print('Despues de ser llamada la función.')
    print(retorno)
    return retorno

@Decorator
def function():
  print('Dentro de la función.')
  return "Retorno"

function()
# Antes de ser llamada la función.
# Dentro de la función.
# Despues de ser llamada la función.
# 'Retorno'
```
En este ejemplo notamos que el decorador se ejecutan en el método sobrecargado def `__call__(self, *args, **kwargs)` de la clase, este método se ejecuta siempre que se instancia y se hace una llamada a la clase.

## **Decorando métodos**

Para decorar el método de una clase es necesario agregar un método adicional, este es el método `__get__(self)`.

```python
from types import MethodType

class Decorator(object):

  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print('Dentro del Decorador.')
    return self.func(*args, **kwargs)

  def __get__(self, instance, cls):
    # Retorna un método si se llama en una instancia
    return self if instance is None else MethodType(self, instance)

class Test(object):
  @Decorator
  def __init__(self):
    print("Dentro de la función decorada")

a = Test()
# Dentro del Decorador.
# Dentro de la función decorada
```
Como se observa creamos una clase Decorador con tres métodos obligatorios `__init_(self)`, `__call__(self)` y `__get__(self)`, esta es la estructura de la clase decoradora para poder decorar métodos de clases.


## **Decorador con parámetros**

```python
class MyDec(object):
  def __init__(self, flag):
    self.flag = flag


  def __call__(self, original_func):
    decorator_self = self
    def wrappee(*args, **kwargs):
      print('en decorador antes de wrapee ', decorator_self.flag)
      original_func(*args,**kwargs)
      print('en decorador despues de wrapee', decorator_self.flag)
    return wrappee


@MyDec(flag='foo de fa fa')
def bar(a,b,c):
  print('En bar(...) : ',a,b,c)

if __name__ == "__main__":
  bar(1, "Hola", True)


# en decorador antes de wrapee  foo de fa fa
# en bar 1 Hola True
# en decorador despues de wrapee foo de fa fa
```
Inicialmente creamos una clase MyDec que va a ser el decorador, y en el constructor recibe todos los argumentos que sean necesarios en este caso agregamos el algumento flag. En el metodo `__call__(self)` que es el que se ejecuta cuando agregamos el decorador `@MyDec(flag='foo de fa fa')` en la funcion. Dentro de los argumentos de `__call__` esta original_func que es la funcion a la cual se le a colocado el decorador. Y dentro de `wrappee()` recibimos los argumentos de la funcion y posteriormente ejecutamos la funcion original_func(*args,**kwargs) y le pasamos los argumentos y los kwargs.

# **Identidad de objetos**

Mediante el operador `is` e `==` parecen ser lo mismo pero son muy diferentes.
* El operador `==` compara el contenido de dos objetos 
* Operador `is` revisa si dos objetos son iguales (objetos son identicos). Si apuntan al mismo objeto.

**Ejemplo**:
```python
lista_a = [1,2,3]
lista_b = [1, 2, 3]
lista_c = lista_a


print(lista_a == lista_b)
print(lista_a is lista_b)
print(lista_a is lista_c)

# True
# False
# True
```
El primer resultado es True porque al comparar el contenido de las dos listas es igual. En el segundo resultado obtenemos False porque si bien las dos listas tienen el mismo contenido apuntan a direcciones diferentes de memoria. Por último obtenemos True porque la lista_a y la lista_c apuntan a la misma dirección de memoria.

# **Clonación de objetos**

La clonación de objetos consiste en copiar el contenido de un objeto a partir de otro. Existen dos tipos de copiado de objetos:
* Copia superficial o simplemente copia. Copiamos el objeto pero todavía sigue teniendo referencias de memoria hacia el otro objeto.
* Copia prodnda o deepcopy. Copiamos el objeto pero rompemos con toda referencia a memoria.

## **Copia superficial**

Ya explicamos de que se trata, ahora veremos un ejemplo en código.
```python
import copy


lista_a = [[1,2],[3,4],[5,6]]
lista_b = copy.copy(lista_a)

print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

lista_a[0][1] = 'A' 

print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')



# Lista a: [[1, 2], [3, 4], [5, 6]]
# Lista b: [[1, 2], [3, 4], [5, 6]]
# Lista a: [[1, 'A'], [3, 4], [5, 6]]
# Lista b: [[1, 'A'], [3, 4], [5, 6]]
```
Como vemos el índice 0 y en el elemento 1 de las dos listas ha sido modificado ya que el objeto copiado (la lista_b) todavía tiene direcciones de memoria que apuntan al contenido del otro objeto (la lista_a).

**También podemos copiar un objeto utilizando el constructor original que creo ese objeto, como se presenta en este ejemplo:**
```python
lista_a = [[1,2],[3,4],[5,6]]
lista_b = list(lista_a)
```
En este ejemplo obtenemos el mismo resultado que utilizando el método copy.copy() de la librería copy.

## **Copia produnda**

Ya explicamos de que se trata, ahora veremos un ejemplo en código.
```python
import copy


lista_a = [[1,2],[3,4],[5,6]]
lista_b = copy.deepcopy(lista_a)

print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

lista_a[0][1] = 'A' 

print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')



# Lista a: [[1, 2], [3, 4], [5, 6]]
# Lista b: [[1, 2], [3, 4], [5, 6]]
# Lista a: [[1, 'A'], [3, 4], [5, 6]]
# Lista b: [[1, 2], [3, 4], [5, 6]]
```
Como vemos hemos modificado el elemento 1 del índice 0 de la primer lista y como resultado no se ha modificado el valor en la segunda lista. Esto sucede de esta manera porque hemos realizado una copia profunda y se crea un nuevo objeto en vez de referenciarlo a otro.


**Comparación**:

![](https://i.stack.imgur.com/AWKJa.jpg)
![](https://www.techiedelight.com/wp-content/uploads/Deep-Copy.png)

Estos conocimientos se aplican también a clases definidas por el programador.

# **Dataclases**

Esta librería

## **Definir una clase por medio del decorador dataclass**

```python
from dataclasses import dataclass


@dataclass
class User:
    identifier: int
    name: str
    lastname: str
    email: str
    password: str


persona1 = Persona(1, 'Juan', 'Perez', 'juan@gmail.com', '1234')
print(persona1.__repr__())
```

# **Diferencias entre variables de clase y variables de instancia**

La diferencia es simple:
* Las variables de clase son aquellas variables definidas fuerda del método init (constructor) y el igual para cada instancia.
* Las variables de instancia son aquellas variables definidas dentro del método init (constructor) y dicho valor es independiente de cada instancia.

**NOTA:**Básicamente son conocidos como atributos de la clase y atributos de instancia

## **Atributos de clase**
```python
class Perro:
	tipo_de_animal = 'Mamífero' #se define la variable de clase
```


## **Atributos de instancia**
```python
class Perro:
    def __init__(self, nombre):
		self.nombre = nombre #se define la variable de instancia
```

## Uso de los dos tipos de atributos en una clase

```python
class Perro:
	tipo_de_animal = 'Mamífero' #se define la variable de clase

	def __init__(self, nombre):
		self.nombre = nombre #se define la variable de instancia
```

# **Funciones útiles**

Hay algunas funciones útiles que sirven para manejar errores o haccer comprobaciones como debugear.

Claro, aquí tienes una descripción y un ejemplo de cada una de las funciones que mencionaste:

# **Método super():**
El método `super()` se utiliza para llamar a un método de la clase padre desde una clase hija en la programación orientada a objetos. Proporciona una forma de acceder y llamar a los métodos y atributos de la clase padre desde la clase hija. Se utiliza principalmente en casos en los que la clase hija necesita extender o modificar el comportamiento del método de la clase padre.

**Ejemplo:**
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("¡Hola! Soy un animal.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def saludar(self):
        super().saludar()
        print("¡Soy un perro y me llamo", self.nombre, "!")

mi_perro = Perro("Max", "Labrador")
mi_perro.saludar()
```

En este ejemplo, la clase `Perro` hereda de la clase `Animal`. Al utilizar `super().__init__(nombre)` dentro del método `__init__` de la clase `Perro`, se llama al método `__init__` de la clase padre `Animal` para inicializar el atributo `nombre`. Luego, al utilizar `super().saludar()` dentro del método `saludar` de la clase `Perro`, se llama al método `saludar` de la clase padre `Animal`, mostrando el saludo genérico de un animal. Después, se imprime un mensaje específico para un perro.

# **Función isinstance():**
La función `isinstance()` se utiliza para verificar si un objeto es una instancia de una clase dada. Retorna `True` si el objeto es una instancia de la clase especificada, y `False` en caso contrario. Esta función es útil para realizar comprobaciones de tipo en Python.

**Ejemplo:**
```python
class Persona:
    pass

class Estudiante(Persona):
    pass

persona = Persona()
estudiante = Estudiante()

print(isinstance(persona, Persona))  # True
print(isinstance(estudiante, Persona))  # True
print(isinstance(persona, Estudiante))  # False
```

En este ejemplo, se define una clase `Persona` y una clase `Estudiante` que hereda de la clase `Persona`. Se crean dos objetos, `persona` y `estudiante`. Al utilizar la función `isinstance()` con estos objetos y las clases correspondientes, se puede verificar si el objeto es una instancia de la clase. En este caso, el objeto `persona` es una instancia de la clase `Persona` y también de la clase `Estudiante`, ya que `Estudiante` hereda de `Persona`. El objeto `estudiante` también es una instancia de la clase `Persona`, pero no de la clase `Estudiante` directamente.

# **Método __mro__**
El método `__mro__` es un atributo especial que muestra el orden de resolución de métodos (Method Resolution Order) utilizado por una clase en la herencia múltiple en Python. Proporciona una tupla que especifica el orden en el que se buscarán los métodos en caso de que existan métodos con el mismo nombre en diferentes clases en la jerarquía de herencia.

**Ejemplo:**
```python
class A:


    def saludar(self):
        print("Hola desde A")

class B:
    def saludar(self):
        print("Hola desde B")

class C(A, B):
    pass

objeto = C()
objeto.saludar()

print(C.__mro__)
```

En este ejemplo, se definen las clases `A`, `B` y `C`. La clase `C` hereda de las clases `A` y `B` en ese orden. Al crear un objeto `objeto` de la clase `C` y llamar al método `saludar()`, se imprimirá "Hola desde A" porque el método `saludar()` de la clase `A` se resuelve primero según el orden especificado en `C.__mro__`.

# **Método __bases__**
El método `__bases__` es un atributo especial que muestra las clases base directas de una clase en Python. Proporciona una tupla que contiene las clases de las cuales la clase actual hereda directamente.

**Ejemplo:**
```python
class Vehiculo:
    pass

class Coche(Vehiculo):
    pass

class Camion(Vehiculo):
    pass

print(Coche.__bases__)  # (Vehiculo,)
print(Camion.__bases__)  # (Vehiculo,)
print(Vehiculo.__bases__)  # (object,)
```

En este ejemplo, se definen las clases `Vehiculo`, `Coche` y `Camion`. La clase `Coche` y la clase `Camion` heredan directamente de la clase `Vehiculo`. Al imprimir `Coche.__bases__` y `Camion.__bases__`, se obtiene `(Vehiculo,)` como resultado, lo que indica que ambas clases heredan de la clase `Vehiculo`. La clase `Vehiculo` no tiene ninguna clase base directa, por lo que `Vehiculo.__bases__` retorna `(object,)`, ya que todas las clases en Python heredan de la clase base `object` de forma implícita.

# **hasattr():**
La función `hasattr()` se utiliza para verificar si un objeto tiene un atributo o un método con un nombre específico. Retorna `True` si el objeto tiene el atributo o método, y `False` en caso contrario.

**Ejemplo:**
```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("¡Hola!")

persona = Persona("Juan")

print(hasattr(persona, "nombre"))  # True
print(hasattr(persona, "saludar"))  # True
print(hasattr(persona, "edad"))  # False
```

En este ejemplo, se define la clase `Persona` con un atributo `nombre` y un método `saludar()`. Se crea un objeto `persona` de la clase `Persona`. Al utilizar la función `hasattr()` con este objeto y los nombres de atributos o métodos correspondientes, se puede verificar si el objeto tiene ese atributo o método. En este caso, el objeto `persona` tiene el atributo `nombre` y el método `saludar()`, por lo que `hasattr(persona, "nombre")` y `hasattr(persona, "saludar")` retornarán `True`. Sin embargo, el objeto `persona` no tiene un atributo llamado `edad`, por lo que `hasattr(persona, "edad")` retornará `False`.

# **Metaclases**

Una metaclase es una clase cuyas instancias son clases en lugar de objetos. Es decir, si para construir un objeto usas una clase, para construir una clase usas una metaclase.

La "función" `type` se utiliza a menudo para determinar el tipo de un objeto. Pero `type` no es una función, esesna metaclase y por tanto se puede heredar de ella. Y como `type` es una metaclase: cualquier subclase de `type` es una metaclase (algo parecido a lo que pasa con las clases abstractas). 

## **Método `__new__`**
`__new__` es un método peculiar. Es estático (staticmethod), es decir, existe con independencia de las instancias de la clase y por tanto no tiene un argumento self. En su lugar, lo que se le pasa como argumento es la propia clase, normalmente nombrado como cls.

El proceso de creación de un objeto (instancia) de una clase es más o menos así (después lo refinamos):
* Se invoca la clase con los argumentos requeridos
* Se ejecuta el método `__new__` pasándose la clase a sí misma como primer argumento, y a continuación los argumentos que indicó el usuario en la “invocación” original.
* `__new__` retorna una nueva instancia (esto es obligatorio).
* Se ejecuta el método __init__ pasando como primer argumento la instancia creada por `__new__` y también todos los argumentos de la invocación original.

**Ejemplo**:
```python
>>> class Title(str):
...    def __new__(cls, val):
...       print 'construyendo un nuevo objeto'
...       return str.__new__(cls, val.title())

>>> Title('transparencias adiós')
construyendo un nuevo objeto
'Transparencias Adiós'
```

## **Creando una metaclase**

```python
class MyMetaclase(type):
    pass
```
Sabiendo que:
* `__new__` sirve para crear clases
* `__init__` sirve para inicializar/modificar clases

Lo interesante aquí es que, “modificar una clase” incluye cosas como añadir o modificar métodos, sus implementaciones, sus nombres, argumentos y número, atributos, etc, etc, las posibilidades son infinitas.


Ya toca escribir una metaclase que haga algo útil por poco que sea. Esta metaclase crea automáticamente métodos que se llaman `not_[método]` para cada método de la clase. Estos métodos devuelven el valor lógico negado de la función original.
```python
import types

class AutoNot(type):
    def __init__(cls, name, bases, dct):
       type.__init__(cls, name, bases, dct)
       methods = [x for x in dct if isinstance(dct[x], types.FunctionType)]
       for m in methods:
           setattr(cls, 'not_%s' % m, lambda self: not dct[m](self))

class A:
    __metaclass__ = AutoNot

    def yes(self):
        return True

a = A()

print a.yes()
print a.not_yes()
```
Supongo que eso de crear clases pasando el nombre, la lista de clases base y el diccionario de métodos te parecerá tan ortopédico como a mí. No hay problema, afortunadamente hay una forma mucho más estilosa de usar una metaclase. Consiste en usar un atributo de clase especial llamado `__metaclass__` y asignarle la metaclase que quieras usar para crear esa clase. Lo siguiente es equivalente al ejemplo anterior pero modificado para usar `__metaclass__`.

# **Interfaces**

A un alto nivel, una interfaz actúa como modelo para el diseño de clases. Al igual que las clases, las interfaces definen métodos. A diferencia de las clases, estos métodos son abstractos. Un método abstracto es aquel que la interfaz simplemente define. No implementa los métodos. Esto lo hacen las clases, que luego implementan la interfaz y dan un significado concreto a los métodos abstractos de la interfaz.

Las interfaces en Python se implementan de manera bastante diferente a otros lenguajes como Java o C++, ya que en verdad es una herencia de clases abstractas.

## **Interfaces Informales**

En determinadas circunstancias, es posible que no necesite las reglas estrictas de una interfaz Python formal. La naturaleza dinámica de Python le permite implementar una interfaz informal . Una interfaz informal de Python es una clase que define métodos que se pueden anular, pero no hay una aplicación estricta.

**Creación de la interface**:
```python
# Interface diseñada para dos implementaciones de extracción de datos de PDFs y Emails.
class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass
```

**Ahora implementemos la inteface**:
```python
class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass


class EmailParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    # Atentos al método definido a continuación
    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass
```

Como vemos en las dos implementaciones de la interfaz en la primera se cumplen los dos métodos definidos en la interfaz, pero en la segunda implemenetación (EmailParser) no se respetan todos los métodos, es por eso que las interfaces informales son buenas para proyectos pequeños, pero para intermedios y grandes proyectos es necesario para evitar errores, el utilizar interfaces formales. Una interfaz formal nos arrojaría un error en caso de que no haya sido implementada estrictamente.

## **Interfaces formales**

Las interfaces formales garantizan la implementación exacta de la interfaz, cumpliendo con la implemenetación de todos los métodos que define la interfaz.

```python
import abc


class FormalParserInterface(metaclass=abc.ABCMeta):
    # El fragmento de código que has mostrado es una implementación de un método especial llamado __subclasshook__ en una clase en Python. Este método se utiliza para establecer la relación de subclase entre dos clases y se utiliza principalmente para verificar si una clase es una subclase válida de otra.
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)

    # Creación de un método abstracto
    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    # Creación de un método abstracto
    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError


# Implementación de una iterfaz
class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


# Implementación de una iterfaz incorrectamente. Ya que a tiempo de ejecución se tendrá un error porque no han sido implementados todos los métodos que define la interface.
class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass
```
