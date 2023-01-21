# Las clases pueden tener varios argumentos y estos pueden ser variables como en las funciones. Veamos un ejemplo:

class clase:
    def __init__(self, *args, **kwargs):
        pass

"""
*args --> Este parámetro recive una tupla
**kwargs --> Este parámetro recive un diccionario
"""