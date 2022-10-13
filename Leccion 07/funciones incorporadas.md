# Funciones incorporadas 

Las funciones incorporadas son aquellas que ya vienen inluidas en el propio lenguaje, es decir, que no hace falta importar las funciones para poder trabajar con ellas. A las funciones incorporadas también se las conocen como built-in functions. 

#### ABS
**Definición**: retorna el valor absoluto de un número. El valor absoluto de un número es la parte positiva de este.
**Entrada**: int | float
**Salida**: int | float
**Código**:
```python
abs(-10)

# 10 <class 'int'>
```

#### ALL
**Definición**: se introduce una secuencia, si esta contiene algun elemento Empty | Zero | False retornará False, en caso contrario retornará True.
**Entrada**: sequence => list | tuple | dict | set | str
**Salida**: bool
**Código**: 
```python
all([1,2,''])
all([1,2, True])

# False <class 'bool'>
# True <class 'bool'>
```

#### ANY
**Definición**: se introduce una secuencia, si esta contiene algun elemento Empty | Zero | False retornará True, solo retornará False si todos sus elementos son de tipo Empty | Zero | False .
**Entrada**: sequence => list | tuple | dict | set | str
**Salida**: bool
**Código**: 
```python
any([1,2,''])
all([False, '', 0])

# True <class 'bool'>
# False <class 'bool'>
```

#### ASCII
**Definición**: Esta función devuelve la forma imprimible de cualquier objeto pasado como argumento. Si damos cualquier carácter no ascii, el intérprete añade una barra invertida( \ ) y la escapa usando otra barra invertida( \ ). 
**Entrada**: any type
**Salida**: str  
**Código**:
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

#### BIN
**Definición**: toma como parámetro solamente números enteros y retorna su forma binaria. Si recibe un parámetro que no sea un número retornará un error.
**Entrada**: int
**Salida**: str
**Código**:
```python
bin(10)
bin(10.0)
bin('Hola'

# '0b1010' <class 'str'>
# TypeError: 'float' object cannot be interpreted as an integer
# TypeError: 'str' object cannot be interpreted as an integer
```

#### BOOL
**Definición**: toma como argumento cualquier tipo de dato, si este contiene un dato de tipo Empty | Zero | False retorná False, en caso contrario retorna True. Si se ingresa False retornará False, si se ingresa True retornará True.
**Entrada**: any type
**Salida**: bool
**Código**:
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

#### BYTEARRAY
**Definición**: toma un número entero desde el 0 hasta el 256 como argumento y retorná un array de elementos de dicha longitud. A dicho array se le pueden aplicar todas las operaciones de arrays ya conocidas.
**Entrada**: int 
**Salida**: bytearray
**Código**:
```python

# bytearray(b'\x00\x00\x00\x00\x00\x00') <class 'bytearray'>
```

#### BREAKPOINT
**Definición**: permite crear un breakpoint dentro del código, y es una alternativa al módulo ipdb.
**Entrada**: ----
**Salida**: ----
**Código**:
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

#### BYTES
**Definición**: es similar a la función bytearray pero esta retorná un objeto no mutable.
**Entrada**: int
**Salida**: bytes
**Código**:
```python
obj=bytes(5)

# b’\x00\x00\x00\x00\x00′ <class 'bytes'>
```

#### CALLABLE
**Definición**: toma como argumento un objeto y retorna True si este es llamable o False si este no es llamable.
**Entrada**: object
**Salida**: bool
**Código**:
```python
callable(9)

def fun():
    return 10

x = fun
callable(x)

# False <class 'bool'>
# True <class 'bool'>
```

#### CHR
**Definición**: toma como argumento un número entero y retorná su equivalente caracter unicode
**Entrada**: int
**Salida**: str
**Código**:
```python
chr(45)
chr(100)

# '-' <class 'str'>
# 'd' <class 'str'>
```
#### CLASSMETHOD
**Definición**: Este método devuelve el método de la clase tomando la entrada como las funciones dentro de una clase. Esto nos ayuda a llamar al método de la forma en que llamamos a cualquier otra función.
**Entrada**: 
**Salida**:
**Código**:
```python
class geeks:
	course = 'DSA'

	def purchase(obj):
		print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()
```

#### COMPILE
**Definición**: Este método devuelve el objeto código del código dado como entrada en forma de cadena. Recibe 3 parámetros:
1°→ Código en forma de cadena 
2°→ Nombre del archivo que se va a ejecutar el código, si el código proviene del mismo archvo se coloca una cadena en blanco ''.
3°→ Instrucción, en este caso queremos ejecutar el código así que colocamos 'exec' que proviene de excecute.
**Entrada**: str, str, str
**Salida**: object
**Código**:
```python
exec(compile('x=4\ny=6\nprint(x*y)','','exec'))

# 24 <class 'int'>
```

#### COMPLEX
**Definición**: toma como argumento un número entero, decimal o complejo y retorna su forma compleja. Puede recibir dos parámetros:
1°→ número que será la parte real del número complejo.
2°→ número que será la parte inmaginaria del número complejo.
**Entrada**: int | float | complex
**Salida**: complex
**Código**:
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

#### DELATTR
**Definición**:
**Entrada**:
**Salida**:
**Código**:
```python
delattr
```

#### DICT
**Definición**: convierte una secuencia de datos en un diccionario.
**Entrada**: sequence => str | list | tuple | set | dict
**Salida**: dict
**Código**: 
```python

```