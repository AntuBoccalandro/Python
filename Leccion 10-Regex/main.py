import re


text = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
'''

# # Los matchs o emparejamientos son los resultados que se encuentra al aplicar la expresión regular

# # Buscar el primer match o busqueda
# print(re.search(r'\d', text))

# # Buscar todos los matchs
# # FindAll muestra todos los matchs
# print(re.findall(r'\d', text))

# # flags=re.M hace que cada línea del texto se tome como una oración independiente. Por defecto Python iterpreta a los textos de muchas líneas como si fuera un texto de una sola línea.
# print(re.findall(r'Mundo.$', text, flags=re.M))

# print(re.findall(r'Python!*', text, flags=re.M))
# print(re.findall(r'Python!+', text, flags=re.M))


# Ejemplo de verificación de correo electrónico

# Ejemplo de verificación de contraseña
# Ejemplo de verificación de url
# Ejemplo de verificación de fechas
# Ejemplo de verificación 

texto = '1234'

patron = re.compile('^\d$')
print(patron.match(texto))

