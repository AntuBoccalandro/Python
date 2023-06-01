# Built-in funtions

Las funciones incorporadas son aquellas que ya vienen inluidas en el propio lenguaje, es decir, que no hace falta importar las funciones para poder trabajar con ellas. A las funciones incorporadas también se las conocen como built-in functions. 

## Abs
**Definición**: retorna el valor absoluto de un número. El valor absoluto de un número es la parte positiva de este.

**Entrada**: int | float

**Salida**: int | float

```python
abs(-10)

# 10 <class 'int'>
```

## All
**Definición**: se introduce una secuencia, si esta contiene algun elemento Empty | Zero | False retornará False, en caso contrario retornará True.

**Entrada**: sequence => list | tuple | dict | set | str

**Salida**: bool

```python
all([1,2,''])
all([1,2, True])

# False <class 'bool'>
# True <class 'bool'>
```

## Any

**Definición**: se introduce una secuencia, si esta contiene algun elemento Empty | Zero | False retornará True, solo retornará False si todos sus elementos son de tipo Empty | Zero | False .

**Entrada**: sequence => list | tuple | dict | set | str

**Salida**: bool

```python
any([1,2,''])
all([False, '', 0])

# True <class 'bool'>
# False <class 'bool'>
```

## Ascii

**Definición**: Esta función devuelve la forma imprimible de cualquier objeto pasado como argumento. Si damos cualquier carácter no ascii, el intérprete añade una barra invertida( \ ) y la escapa usando otra barra invertida( \ ). 

**Entrada**: any type

**Salida**: str  

```python
ascii('r')
ascii('\t')
ascii('Hello \n world!')
ascii([3,'/'])

# “‘r'” <class 'str'>
# “‘\\t'” <class 'str'>
# “‘Hello \\n world!'” <class 'str'>
# “[3, ‘/’]” <class 'str'>
```

## Bin
**Definición**: toma como parámetro solamente números enteros y retorna su forma binaria. Si recibe un parámetro que no sea un número retornará un error.

**Entrada**: int

**Salida**: str

```python
bin(10)
bin(10.0)
bin('Hola'

# '0b1010' <class 'str'>
# TypeError: 'float' object cannot be interpreted as an integer
# TypeError: 'str' object cannot be interpreted as an integer
```

## Bool
**Definición**: toma como argumento cualquier tipo de dato, si este contiene un dato de tipo Empty | Zero | False retorná False, en caso contrario retorna True. Si se ingresa False retornará False, si se ingresa True retornará True.

**Entrada**: any type

**Salida**: bool

```python
bool('a')
bool(False)
bool([])
bool(0)

# True
# False
# False
# False
```

## Bytearray
**Definición**: toma un número entero desde el 0 hasta el 256 como argumento y retorná un array de elementos de dicha longitud. A dicho array se le pueden aplicar todas las operaciones de arrays ya conocidas.

**Entrada**: int 

**Salida**: bytearray

```python

# bytearray(b'\x00\x00\x00\x00\x00\x00') <class 'bytearray'>
```

## Breakpoint

**Definición**: permite crear un breakpoint dentro del código, y es una alternativa al módulo ipdb.

**Entrada**: ----

**Salida**: ----

```python
message='Hello'
breakpoint()
print(message)

# –Return–
# None
# > <ipython-input-1-ce49f3863458>(2)<module>()
# 1 message=’Hello’
# —-> 2 breakpoint()
# 3 print(message)ipdb> message
# ‘Hello’ipdb>
```

## Bytes

**Definición**: es similar a la función bytearray pero esta retorná un objeto no mutable.

**Entrada**: int

**Salida**: bytes

```python
obj=bytes(5)

# b’\x00\x00\x00\x00\x00′ <class 'bytes'>
```

## Callable

* **Definición**: toma como argumento un objeto y retorna True si este es llamable o False si este no es llamable.
* 
**Entrada**: object

**Salida**: bool

```python
callable(9)

def fun():
    return 10

x = fun
callable(x)

# False <class 'bool'>
# True <class 'bool'>
```

## Chr

**Definición**: toma como argumento un número entero y retorná su equivalente caracter unicode

**Entrada**: int

**Salida**: str

```python
chr(45)
chr(100)

# '-' <class 'str'>
# 'd' <class 'str'>
```
## Classmethod

**Definición**: Este método devuelve el método de la clase tomando la entrada como las funciones dentro de una clase. Esto nos ayuda a llamar al método de la forma en que llamamos a cualquier otra función.

**Entrada**: 

**Salida**:

```python
class geeks:
	course = 'DSA'

	def purchase(obj):
		print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()
```

## Compile
**Definición**: Este método devuelve el objeto código del código dado como entrada en forma de cadena. Recibe 3 parámetros:
* 1°→ Código en forma de cadena 
* 2°→ Nombre del archivo que se va a ejecutar el código, si el código proviene del mismo archvo se coloca una cadena en blanco ''.
* 3°→ Instrucción, en este caso queremos ejecutar el código así que colocamos 'exec' que proviene de excecute.
  
**Entrada**: str, str, str

**Salida**: object

```python
compile('x=4\ny=6\nprint(x*y)','','exec')

# 24 <class 'int'>
```

## Complex

**Definición**: toma como argumento un número entero, decimal o complejo y retorna su forma compleja. Puede recibir dos parámetros:
* 1°→ número que será la parte real del número complejo.
* 2°→ número que será la parte inmaginaria del número complejo.

**Entrada**: int | float | complex

**Salida**: complex

```python
complex(2)
complex(9j)
complex(2+3j)
complex(3, 4)

# 2+0j <class 'complex'>
# 9j <class 'complex'>
# 2+3j <class 'complex'>
# 3+4j <class 'complex'>
```

## Delattr

**Definición**: elimina el atributo de un objeto específico, recibe dos parámetros:
* 1° -> objeto del que queremos eliminar un atributo
* 2° -> nombre del atributo que queremos eliminar del objeto

**Entrada**: object 

**Salida**: ---- 

```python
class course:
	name = 'Python full-course'
	duration_months = 6
	price = 150
	rating = 5


print(course.rating)

delattr(course, 'rating')

try:
	print(course.rating)
except Exception as e:
	print(e)

# 5
# type object 'course' has no attribute 'rating'
```

## Dict

**Definición**: convierte una secuencia de datos de clave valor en un diccionario.

**Entrada**: key-value pairs

**Salida**: dict

```python
print(dict(a=1, b=2, c=3, d=4))

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## Dir

**Definición**: devuelve una lista de los atributos y métodos de cualquier objeto. 
* Para Class Objects, devuelve una lista de nombres de todos los atributos válidos y atributos base también. 
* Para los objetos Módulos/Biblioteca, intenta devolver una lista de nombres de todos los atributos contenidos en ese módulo. 
* Si no se pasan parámetros, devuelve una lista de nombres en el ámbito local actual. 

**Entrada**: object

**Salida**: list

```python
import random


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __dir__(self):
        return ['name', 'email', 'password']


user = User('Jhony', 'jhon@gmail.com', 'jhony1234')

print(dir(random))
print(dir(int))
print(dir(user))

# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# ['email', 'name', 'password']
```

## Divmod

**Definición**: retorna un par de números en el que el primer es el cociente y el segundo el resto.

**Entrada**: int | float 

**Salida**: tuple

```python
print(divmod(10, 5))

# (2, 0)
```

