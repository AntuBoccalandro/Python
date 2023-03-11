# Métodos

Son las funcionalidades o comportamiento que tendrá el objeto, es decir que nos permite controlar los atributos. Por ejemplo, tenemos una persona con un name (el atributo) y si la persona quiere cambiar este nombre podríamos llamar al método change_name() por lo que los métodos van a cambiar el comportamiento del objeto y de sus atributos, este método podría permitirle a la persona que ingrese un nuevo nombre así que lo que estamos haciendo es modificar el atributo name. Como este ejemplo existen muchísimos más, así que te invito a que pienses en otros más. Para crear un método es necesario 

```python
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    # Método mostrar_detalles()
    def mostrar_detalles(self):
        print(f'Person: {self.name} {self.lastname} {self.edad}')

person = Person('John', 'Williams', 1234, 29)
person.see_datails()

# Person: John Williams 29
```
El método creado (see_details) imprimirá en la consola todos los valores de los atributos del objeto person. Entre los parentesis especificamos el objeto del cual queremos ejecutar el método.

# **Métodos de instancia, de clase y estáticos**

## Métodos de instancia

Los métodos de instancia son los clásicos de siempre. Se definen creando una función, pasandole `self` como parámetro de la función, además de otros parámetros si se requiere. Se pueden llamar desde el objeto.

**Los métodos de instancia**
* Pueden acceder y modificar los atributos del objeto.
* Pueden acceder a otros métodos.
* Dado que desde el objeto self se puede acceder a la clase con ` self.class`, también pueden modificar el estado de la clase

```python
class MyClass:
    def __init__(self, atr1, atr2):
        self.atr1 = atr1
        self.atr2 = atr2

    def instance_method(self):
        return (self.atr1, self.atr2)


obj = MyClass()
obj.instance_method()
```

## Métodos de clase

A diferencia de los métodos de instancia, los métodos de clase reciben como argumento `cls`, que hace referencia a la clase. Por lo tanto, pueden acceder a la clase pero no a la instancia. Se pueden llamar desde el objeto o la clase. Los métodos de clase se definen mediante el decorador `@classmethod`.

**Los métodos de clase**
* No pueden acceder a los atributos de la instancia.
* Pero si pueden modificar los atributos de la clase.

```python
class MyClass:
    atr1 = 'Atributo inicial de clase'

    def __init__(self, atr1):
        self.atr1 = atr1

    @classmethod
    def get_atr(cls):
        print(cls.atr1)


obj = MyClass(9)
print(obj.atr1)
obj.get_atr()

# 9
# Atributo inicial de la clase
```
Como vemos mediante el decorador classmethod convertimos un método de instancia en uno de clase. Este método no puede acceder a los atributos de la instancia pero si a los de la clase. En este caso tenemos definido un atributo de nuestra clase al que podemos acceder mediante el método de clase utilizando cls.nombre_del_atributo. Si mostramos el atributo del objeto creado vemos que se muestra 9, pero si llamamos al método `get_atr` nos retorna "Atributo inicial de la clase" ya que estamos accediendo a los atributos de la clase y no de la instancia.

## Métodos estáticos


Los métodos estáticos se pueden definir con el decorador `@staticmethod` y no aceptan como parámetro ni la instancia ni la clase. Es por ello por lo que no pueden modificar el estado ni de la clase ni de la instancia. Pero por supuesto pueden aceptar parámetros de entrada.

Por lo tanto el uso de los métodos estáticos pueden resultar útil para indicar que un método no modificará el estado de la instancia ni de la clase. Es cierto que se podría hacer lo mismo con un método de instancia por ejemplo, pero a veces resulta importante indicar de alguna manera estas peculiaridades, evitando así futuros problemas y malentendidos.


```python
class Math:

    @staticmethod
    def sumar(num1, num2):
        return num1 + num2

    @staticmethod
    def restar(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicar(num1, num2):
        return num1 * num2

    @staticmethod
    def dividir(num1, num2):
        return num1 / num2

print(Math.sumar(5, 7))
print(Math.restar(9, 3))
print(Math.multiplicar(15, 9))
print(Math.dividir(10, 2))

# 12
# 6
# 135
# 5
```
