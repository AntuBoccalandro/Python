# Métodos de Strings

string = 'En inglés hola se dice Hello o Hi, así que ya sabes decir hola en inglés'

string.find('hola') # Cada uno retorna la posición en la que se encuentre la substring. La diferencia entre los dos, es que find() retorna la posición de la primera similitud de la substring y rfind() retorna la última posición de la similitud de la substring.

string.rfind('hola') # Cada uno retorna la posición en la que se encuentre la substring. La diferencia entre los dos, es que find() retorna la posición de la primera similitud de la substring y rfind() retorna la última posición de la similitud de la substring. Si es substring no es encintrado el método retornará -1

print(':'.join(['Python', 'es', 'un lenguaje'])) # El método str.join(iterable)  es usado para unir todos los elementos de un iterable con un espefico string str in Python. Si, el iterable no contiene ningún valor en los strings, Esto conduce a un TypeError exception.

print(' y '.join(['A', 'B', 'C'])) # Concadena ' y ' entre los elementos de la tupla

print(' '.join('Python')) # Concadena ' ' entre cada substring de Python
lista = ['P', 'y', 't', 'h', 'o', 'n']
print(''.join(lista))

lista = ['P', 'y', 't', 'h', 'o', 'n']
coma = ', '
print(coma.join(lista))

string = 'Hola como te va ?'
nuevo_string  = string.replace('va', 'fue')  # El método replace en su primer parámetro recive el substring que se quiere modificar y como segundo parámetro su reeplazo
print(nuevo_string)

string = 'Para mi esto es muy bonito'
nuevo_string = string.replace('es', 'ES', 2)  # El método replace en su primer parámetro recive el substring que se quiere modificar y como segundo parámetro su reeplazo y como tercer parámetro la cantidad de ocurrencias que se qiuera modificar 
print(nuevo_string)

# La estructura de este método es la siguiente:
# nombre_de_la_string[inicio:fin:pasos]

string = 'Python es un exelente lenguaje'

string[2:4]   # nombre_de_la_string[inicio:fin]
string[1:]    # nombre_de_la_string[inicio:]
string[:2]    # nombre_de_la_string[:fin]
string[0:4:2] # nombre_de_la_string[inicio:fin:pasos]