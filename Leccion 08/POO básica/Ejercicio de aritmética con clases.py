# Operaciones aritméticas con clases
class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc.
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA # Atributo Operando A
        self.operandoB = operandoB # Atributo Operando B
    
    def sumar(self): # Creamos un método que sumará dos numeros
        return self.operandoA + self.operandoB
    
    def restar(self): # Creamos un método que restará dos numeros
        return self.operandoA - self.operandoB
    
    def multiplicar(self): # Creamos un método que multiplicará dos números
        return self.operandoA * self.operandoB
    
    def dividir(self): # Creamos un método que multiplicará dos números
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(20,50) # Creamos un objeto y le pasamos los valores a los atributos que hemos definido (operandoA y operandoB)

print(f'Sumar: {aritmetica1.sumar()}') # Imprimimos por consola el método sumar

print(f'Resta: {aritmetica1.restar()}') # Imprimimos por consola el método restar

print(f'Multiplicación: {aritmetica1.multiplicar()}') # Imprimimos por consola el método multiplicar

print(f'División: {aritmetica1.dividir()}') # Imprimimos por consola el método dividir