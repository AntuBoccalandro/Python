# **Sobre carga de operadores**

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


## **Método __str__**

Uno de los métodos mágicos más utilizados es `__str__` que permite establecer la forma en la que un objeto es representado como cadena de texto.

```python
class Player:
    def __init__(self, name, power):
        self.power = power
        self.name = name


    def __str__(self):
        return f'Name: {self.name} - Power: {self.power}'
    


player1 = Player('Player1', 200)
print(player1.__str__())
print(player1)

# Name: PLayer1 - Power: 200
# Name: PLayer1 - Power: 200
```
Como vemos cuando llamamos al método str este nos retorna la representación del objeto. Pero este método también es útil a la hora de imprimir un objeto, ya que se mostrará la representación del objeto que hemos definido en el método str y no su dirección de memoria como se ve en el siguiente ejemplo.

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

Este método funciona de la misma manera que `__str__`, retornando la representación del objeto. Pero este método es más recomendado para realizar esta acción. Pues el método `__str__` llama al método `__repr__` para mostrar la representación del objeto. 

```python
class Player:
    def __init__(self, name, power):
        self.power = power
        self.name = name


    def __repr__(self):
        return f'Name: {self.name} - Power: {self.power}'
    


player1 = Player('Player1', 200)
print(player1.__repr__())
print(player1)

# Name: PLayer1 - Power: 200
# Name: PLayer1 - Power: 200
```

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
