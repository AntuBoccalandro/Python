# Constructores

Un constructor se utiliza para instanciar un objeto. Los constructores es inicializar a los miembros de datos de la clase cuando se crea un objeto de la clase. Es decir, se encarga de asignar los valores a los diferentes atributos. Los constructores nos permiten crear objetos que tengan diferentes atributos y no siempre los mismos, que es la característica que hace útil a las clases.

```python
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
```

## Self

Self hace referencia al nombre del objeto en el que se encuentra escrito. Lo podrías reemplazar por el nombre de la clase como vemos a continuación.

```python
class Person:
    def __init__(Person, name, lastname, age):
        Person.name = name
        Person.lastname = lastname
        Person.age = age
```
Este código se ejecuta perfectamente, pero al escribir el parámetro self si cambiamos el nombre de la clase nos evitamos tener que cambiar el nombre en las demás partes del código.
