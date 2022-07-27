class Persona:
    # self es una variable es la que nos permite acceder a los atributois
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def mostrar_detalle(self): # El parámetro de self es obligatorio ponerlo
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez',28)  # Creamos el primer objeto con los valores definidos entre los parentesis 

persona1.mostrar_detalle()  # Llamamos al método mostrar detalle, este ejeutar´pa una serie de acciones predefinidas

Persona.mostrar_detalle(persona1)   # Esta es otra manera de llamar al método mostrar detalle() auque esta manera no es muy utilizada ya que es algo rebuscada. Lo que hacemos es posicionarnos el la clase 'Persona' y luego de ello nos ubicamos en el método mostrar_detalle() como no estamos refiriendonos a ningún objeto en particular es necesario pasar el objeto en el cual queremos ejecutar este método en los parámetros de la función.

persona1.nuevoAtributo = '940192041923' # Python al ser dinámico (se lo conoce como dinamismo) nos permite crear un nuevo atributo desde fuera de la clase, eso sí hay que tener en cuenta que dicho atributo creado será solo para el objeto al que se le está asociando este atributo. Por lo que si queremos mostrar por consola el atributo nuevo creado pero en otro objeto tendremos un error ya que este no existrá para este objeto solo para el objeto en el que especificamente hemos creado este atributo.

persona2 = Persona('Karla', 'Gomez',40) # Creamos el primer objeto con los valores definidos entre los parentesis 
persona2.mostrar_detalle()  # Llamamos al método mostrar detalle, este ejeutar´pa una serie de acciones predefinidas

"""
Más sobre self:
1- La variale self no tiene porque llamarse self, puede llamarse this o cualquier otro nombre. Auque según la documentación oficial recomienda utilizar el nombre de self.
"""