from Persona import Persona

print('Creación de objetos'.center(50, '-')) #La función center nos permite colocar el texto centrado en la consola. El primer parámetro que recive esta funcion es la cantidad de caracteres con la cuál queremos centrar el texto y el segundo parámetro es el de el caracter. En este caso se centrará el texto en la consola con 25 guiones (-) por cada lado
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminación de objetos'.center(50,'-'))
del persona1 # Mediante la keyword del y el método __del__ podemos eleminar un objeto. Este método __del__ creado en el la clase del archivo __main__ nos permite destruir este objeto y mostrar ejecutar un cierto código por la consola.