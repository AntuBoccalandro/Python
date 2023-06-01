# **Atributos**

Son las caracteríticas que poseerán los objetos, por ejemplo si hablamos de una persona hablamos de atributos como name, lastname y age. Si hablamos de un auto podríamos pensar en color, velocidad, precio, etc… 

**Clase modelo Person:**
```python
class Person:
    name = 'John'
    lastname = 'Williams'
    age = 29
```

Si queremos acceder a los diferentes atributos de un objeto debemos utilzar el punto `.` seguido del nombre del atributo al cual queremos acceder.

```python
person = Person()
print(person.name, person.lastname, person.age)

# John Williams 29
```

Si queremos modificar estos atributos solo basta con referinos al objeto y a su atributo y reasignarle un nuevo valor.

```python
print(person.name, person.lastname, person.age)
# John Williams 29

person.name = 'Harry'
print(person.name, person.lastname, person.age)
# Harry Williams 29
```

