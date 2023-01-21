# Constructores

Un constructor se utiliza para instanciar un objeto. Los constructores es inicializar a los miembros de datos de la clase cuando se crea un objeto de la clase. Es decir, se encarga de asignar los valores 

```python
class Usuario:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
```

## Self

Self hace referencia al nombre del objeto en el que se encuentra escrito. Lo podrías reemplazar por el nombre de la clase como vemos a continuación.

```python
class Usuario:
    def __init__(Usuario, name, lastname, age):
        Usuario.name = name
        Usuario.lastname = lastname
        Usuario.age = age
```
Este código se ejecuta perfectamente, pero al escribir el parámetro self si cambiamos el nombre de la clase nos evitamos tener que cambiar el nombre en las demás partes del código.
