# **NamedTuples**

La Named Tuple tendrá un nombre, una serie de atributos con tipo y nombre y viene de serie con varios dunders ya implementados por nosotros, como `__repr__` o `__eq__`. Esto nos ahorra mucho tiempo y código comparado con una clase. Además, ocupan menos memoria. Las namedtuples se caracterizan porque los valores de sus atributos asignados al instanciar un objeto de esa clase son inmutables y no se pueden modificar.

## Formas de definir una namedtuple

**Sintaxis**: recibe como parámetros el nombre de la clase (namedtuple) que usualmente es el mismo nombre que la variable a la cual se asigna la namedtuple. Luego recibe los nombres de los atributos de la clase, estos separados por espacios o directamente pasándole una lista de strings separados por comas.
```python
# Forma 1
namedtuple('<className>', '[atribute1 atribute2...atributeN]')

# Forma 2
namedtuple('<className>', [['atribute1', 'atribute2'...'atributeN']])
```

**En código**:
```python
from collections import namedtuple

Persona1 = namedtuple('Persona1', 'nombre appellido edad')
Persona2 = namedtuple('Persona2', ['nombre', 'appellido', 'edad'])
```

## **Crear un objeto a partir de una namedtuple**

```python
persona1 = Persona1('Juan', 'Cervera', 16)
``` 

## **Acceder a los atributos de una namedtuple**
Al igual que en las tuplas o las listas en una namedtuple podemos acceder a los atributos de una instancia mediante índices.

```python
from collections import namedtuple


persona1 = Persona1('Juan', 'Cervera', 16)

for i in range(len(persona1)):
    print(persona1[i])

# Juan
# Cervera
# 16
```

## **Manejo de atributos de las namedtuples**
```python
# Mostrar atributos de una namedtuple
print(persona1.nombre)
print(persona1.appellido)
print(persona1.edad)


# Crear una clase que herede de una namedtuple
class Persona2(Persona1):
    def to_uppercase(self):
        return self.nombre.upper(), self.appellido.upper()


persona2 = Persona2('Antú', 'Boccalandro', 29)
print(persona2.to_uppercase())


# Extención de atributos de una namedtuple
persona4 = namedtuple('Persona1', Persona2._fields + ('email',))
print(persona4._fields)

# Modificación de valores de un atributo. Esto nos retornará un error.
persona1.edad = 18
```
