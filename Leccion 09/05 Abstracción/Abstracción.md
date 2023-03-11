# **Abstracción**

Las clases abstractas son clases que nunca vamos a instanciar, es decir, nunca crearemos objetos a partir de esta clase. Las clases abstractas sirven para crear estructuras para otras clases que hereden de esta.

## **Las clases abstractas:**
* No las vamos a instanciar directamente
* Contienen por lo menos un método abstracto
* Las vamos a usar de base para crear subclases más específicas

## **Métodos abstractos:**
* Debemos sobreescribirlas en cada una de las subclases
* Básicamente es un método de la clase abstacta que tendremos que reeescribirlas en las subclases. Esto es polimorfismo. Los métodos abstractos se crean sin nada de código y este código de cada método será implementado por cada clase que herede de la clase abstracta. Por último, los métodos abstractos se definen mediante el decorador `@abstractmethod`.

## Crear una clase abstracta

Para crear una clase abstracta lo que debemos hacer es importar la clase ABC desde el módulo abc. Seguido de ello cuando querramos crear una clase abstracta 

## Ejemplo de clase abstracta

Como vemos creamos una clase Animal que será nuestra plantilla, a partir de aquí podemos crear cuantas clases que pertenezcan a diferentes animales que tengan las mismas propiedades.
```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def comer(self):
        print('Animal come')

        
class Gato(Animal):
    def mover(self):
        print('Mover gato')
        
        
    def comer(self):
        super().comer()
        print('Gato come')
        

g = Gato()
g.mover()
g.comer()

# Mover gato
# Animal come
# Gato come
```
