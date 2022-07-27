from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    def __str__(self):
        return f'Alto: {self._alto} Ancho: {self._ancho}'

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @abstractmethod # Este decorador nos permite crear un método abstracto lo que hace que toda la clase se convierta en una clase abstracta, por ende al crear una clase con métodos o atributos abstractos la clase entera se convierte en abstracta. Además si heredamos el método o atributo abstracto a otra clase y esta no tiene definido dicho atributo y/o método está también se convertirá en abstracta.
    def calcular_area(self):
        pass