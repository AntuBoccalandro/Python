# **Tipos de datos > Diccionarios**

Dentro de los tipos de datos numéricos encontramos a los número enteros. Los números enteros son todo aquel número comprendido entre el +∞ y -∞. Muchos de los lenguajes de programación tienen límites de números a almacenar en las variables de tipo entero, pero en Python no hay límite, el límite es la memoria de la computadora; por ejemplo: si la memoria disponible es de 4GB en Python puede haber una variable que almacene un número que llene esa cantidad de memoria, esto es muy improbable pero es interesante saber que el límite lo define lo físico.

### **Nomenclaturas**

Los dccionarios se conocen en inglés como dictionary. Su abreviatura es `dict`, y siempre que se quiera hacer referencia a un diccionario se utilizará la abreviatura de `dict`.

### **Definir un diccionario**

Para definir un diccionario se utiliza la siguiente sintaxis

**Sintaxis:**
```python
d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
```

**Ejemplo:**
```python
d = {
    'name': 'Juan', 
    'lastname': 'Perez'
}
```

Para saber o asegurarnos el tipo de dato podemos utilizar la función `type()`.

```python
d = {
    'name': 'Juan', 
    'lastname': 'Perez'
}

print(type(d))

# <class type "dict">
```

### **Accediendo a los valores del diccionario**

Como hemos visto los diccionarios se componen de una clave y un valor, para poder acceder a los valores basta con colocar entre corchetes el nombre de la calve y como resultado obtendremos su respectivo valor.

```python
user = {
    'name': 'Juan', 
    'lastname': 'Perez',
    'age': 19
}

print(user['name'])

# 'Juan'
```

**Agregar nuevos valores al diccionario**: si se desea agregar un nuevo valor al diccionario se puede simplemente acceder al diccionario y mediante el uso de corchetes añadir una nueva clave y valor.

```python
user = {
    'name': 'Juan', 
    'lastname': 'Perez',
    'age': 19
}

user['nickname'] = 'Juanse'
print(user)

# {'name': 'Juan', 'lastname': 'Perez', 'age': 29, 'nickname': 'Juanse'}
```

**Reasignación de valores**: se puede cambiar el valor de una clave simplemente refiriendonos a la clave y asignando un nuevo valor.

```python
user = {
    'name': 'Juan', 
    'lastname': 'Perez',
    'age': 19
}

user['age'] = 29
print(user)

# {'name': 'Juan', 'lastname': 'Perez', 'age': 29}
```

NOTA: Cuando se eliminan elementos o añaden al diccionario este conserva su orden inicialmente definido. Además los métodos de listas no funcionan con este tipo de dato ya que se trata de otra estrcutura completamente diferente.

Los diccionarios no tienen restricciones respecto a los tipos de datos que peuden contener, pueden contener listas, número enteros, reales, valores booleanos, inclusive otros diccionarios.

### **Accediendo a los elementos de un diccionario**

Si se tiene un diccionario con ya sean claves o valores que sean un tipo de dato de secuencia se pueden acceder a ellos mediante su clave o valor y luego acceder a los índices de cada secuencia.

```python
electronic = {
    'computer': {'cpu': 'Ryzen 5900X', 'gpu': 'Nvidia 4090'},
    'memory': 1.5,
    'phone': 'Iphone 14'
}

print(elcetronic['computer']['cpu'])

# 'Ryzen 5900X'
```

### **Restricciones para las claves**

Los valores de las claves pueden ser datos de cualquier tipo, pero no sucede lo mismo con las claves. Las claves solo pueden ser tipos de datos inmutables. Por lo que utilizar diccionarios o listas como claves de un diccionario no es posible. Esto es porque los datos inmutables pueden ser hasheables, mientras que los datos mutables no, es por ello que si intentamos utilizar un tipo de dato mutable para la clave de un diccionario obtendremos un error de tipo: `TypeError: unhashable type: 'list'`.

```python
electronic = {
    {'cpu': 'Ryzen 5900X', 'gpu': 'Nvidia 4090'}: 'computer':,
    'memory': 1.5,
    'phone': 'Iphone 14'
}

print(electronic)

# TypeError: unhashable type: 'list'
```

### **Restricciones para los valores **

No existen las restricciones para los valores de un diccionario. Se pueden utilizar todo objeto existente en Python.

### **Operadores**

**Operadores de pertenencia**: los operadores como in y not in pueden ser utilizados para la comprobación de claves o valores de uno o más diccionarios.

```python
user1 = {
    'name': 'Juan', 
    'lastname': 'Perez',
    'age': 19
}

user2 = {
    'name': 'Ramirez', 
    'lastname': 'Esteban',
    'age': 29
}

print(user1['name'] in user2['name'])

# False
```

### **Métodos de diccionarios**

* **d.clear()**: borra todo el contenido del diccionario dejándolo vacío.

    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    d.clear()
    print(d)

    # {}
    ```

* **d.get(<key>, [<default>])**: retorna el valor de una clave, esto si la clave existe dentro del diccionario. 

    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    print(d.get('a'))

    # 10
    ```
    El argumento opcional <default> sirve para especificar el retorno en caso de que no se encuentre esa clave, si no se especifica dicho argumento por defecto el valor que retornará la función será None.


    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    print(d.get('d', 'No se encuentra la clave'))

    # 'No se encuentra la clave'
    ```

* **d.items()**: retorna una lista de tuplas compuesta por una estructura de clave-valor a partir de un diccionario.

    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    print(d.items())
    
    # [('a', 10), ('b', 20), ('c', 30)]
    ```

* **d.keys()**: retorna una lista de las claves del diccionario.

    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    print(d.keys())

    # ['a', 'b', 'c']
    ```

* **d.values()**: retorna una lista de los valores del diccionario.

    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    print(d.values())

    # [10, 20, 30]
    ```

* **d.pop(<key>, [<default>])**: elimina la clave especificada del diccionario y retorna su valor asociado. 

    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    d.pop('a')
    print(d)

    # 10
    ```
    El argumento opcional <default> sirve para que en caso de no encontrarse la clave a eliminar se retorne una valor definido por el programador en vez de una excepción.

    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    d.pop('d', 'No se encuentra la clave')
    print(d)

    # 'No se encuentra la clave'
    ```

* **d.popitem()**: elimina el último par de clave-valor del diccionario.

    ```python
    d = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    d.popitem()
    print(d)

    # {'a': 10, 'b': 20}
    ```

* **d.update(<obj>)**: fusiona un diccoinario con otro. En caso de haber claves repetidas se actualiarán sus valores por las del nuevo diccionario. 

    ```python
    d1 = {
        'a': 10,
        'b': 20,
        'c': 30,
    }

    d2 = {
        'c': 40,
        'd': 50,
        'e': 60,
    }

    d1.update(d2)
    print(d1)

    # {'a': 10, 'b': 20, 'c': 40, 'd': 50, 'e': 60}
    ```

## **Generación de diccionarios**

Parar generar diccionarios podemos utilizar expresiones como esta. Como vemos esta expresión es parecido a lo utilizado en list-comprehension.

```python
valores_al_cuadrado = {x: x**2 for x in range(5)}
print(valores_al_cuadrado)

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

# **Diccionarios ordenados**

Los `OrderedDict` en Python son una subclase del tipo `dict` que mantienen el orden de inserción de los elementos. En un diccionario estándar de Python, el orden de los elementos no se mantiene y los elementos se pueden devolver en cualquier orden.

La ventaja de utilizar un OrderedDict es que se puede garantizar el orden en el que los elementos fueron agregados al diccionario. Esto puede ser útil en situaciones en las que se necesita mantener un orden específico de los elementos, como por ejemplo en la generación de informes o en la creación de gráficos.


```python
from collections import OrderedDict

# crear un nuevo OrderedDict
od = OrderedDict()

# agregar elementos al OrderedDict en un orden específico
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```
Como vemos el orden de inserción es respetado en el diccionario.

# **Diccionarios por defecto**

Un diccionario por defecto es un diccionario al cual se le asigna una función que ejecute y en caso de haber un KeyError se ejecutará está función, no retornando un error.

```python
from collections import defaultdict

# Definir un default dict. La función lambda asignada es la función que se ejecutará por defecto.
diccionario_default = defaultdict(lambda : 'Valor Erróneo')

# Asignamos valores al diccionario
diccionario_default['a'] = 1
diccionario_default['b'] = 2

# Imprimir un elemento no existente. Esto ejeutará la función lambda anteriormente definida.
print(diccionario_default['c'])
# OUTPUT: Valor Erróneo

# Podemos crear valores por default como una lista
diccionario_default_lista = defaultdict(list)

# Si accedemos a una llave no existente, la crea y los valores se asignan como una lista.
diccionario_default_lista['nombres'].append(['item1', 'item2', 'item3'])

# Mostrar los items del diccionario.
print(diccionario_default_lista.items())
# OUTPUT: dict_items([('nombres', [['item1', 'item2', 'item3']])])

# Mostrar las claves del diccionario.
print(diccionario_default_lista.keys())
# OUTPUT: dict_keys(['nombres'])

# Mostrar los valores del diccionario.
print(diccionario_default_lista.values())
# OUTPUT: dict_values([[['item1', 'item2', 'item3']]])
```
Como podemos ver las operaciones con este tipo de diccionario son semejantes a las de un diccionario normal integrado en Python.

# **Combinación o mezcla de diccionarios**

Esta acción consiste en combinar dos diccionarios, es decir, unirlos. Pero como se verá a la hora de imprimir un diccionario combinado lo que hace la clase ChainMap no es crear un diccionario solo con los valores de los diccionario que hemos combinado, si no que los separa con comas. Pero en cuanto a la búsqueda de los valores dentro de este diccionario combinado se realizará como si fuera uno solo y nos dos.

```python
from collections import ChainMap

diccionario1 = {'uno': 1, 'dos': 2, 'tres':3, 'cinco': 'A'}
diccionario2 = {'cuatro': 4, 'cinco': 5}

# Combinación de diccionarios. Podemos combinar más de 2 diccionarios si es necesario.
combinacion_diccionarios = ChainMap(diccionario1, diccionario2)
print(combinacion_diccionarios)
# OUTPUT: ChainMap({'uno': 1, 'dos': 2, 'tres': 3, 'cinco': 'A'}, {'cuatro': 4, 'cinco': 5})

# Buscamos en todos los diccionarios (de izquierda a derecha). Si una llave no existente arroja un KeyError.
print(combinacion_diccionarios['cinco'])
# OUTPUT: 4

# Arrojar un error cuando la Key no está en el diccionario.
print(combinacion_diccionarios['seis'])
# OUTPUT: KeyError
```

# **Diccionarios de solo lectura o ReadOnly**

Como el nombre indica este tipo de diccionario es de solo lectura, esto significa una vez asignado los valores al diccionario estos no se podrán modificar, solo acceder a dichos valores.

```python
from types import MappingProxyType


diccionario_modificable = {'uno': 1, 'dos': 2, 'tres': 3}
diccionario_solo_lectura = MappingProxyType(diccionario_modificable)


# Leemos el valor del diccionario.
print(diccionario_solo_lectura)
print(diccionario_solo_lectura['uno'])
# OUTPUT: {'uno':1, 'dos': 2, 'tres': 3}
# OUTPUT: 1


# Arroja error si queremos modificar el valor del diccionario de solo lectura .
diccionario_solo_lectura['uno'] = -1

# si modificamos el diccionario mutable, afecta al de solo lectura.
diccionario_modificable['dos'] = 22

# Veamos los cambios en los diccionarios.
print(diccionario_modificable)
print(diccionario_solo_lectura)
# OUTPUT: {'uno':1, 'dos': 22, 'tres': 3}
# OUTPUT: {'uno':1, 'dos': 22, 'tres': 3}
```
