# Imprimir texto por consola
print('Hola Mundo') 

# Imprimir variables por consola
mi_variable = 'Hola Mundo'
print(mi_variable)

# Imprimir operaciones con variables
a = 10
b = 20
print(a + b)

# Imprimir concadenaciones de Strings 
a = 'Hola '
b = 'Mundo'
print(a + b)

# Imprimir varios valores a la vez
a = 1
b = 2
c = 3
print(a, b, c)

# Imprimir variables entre texto
edad = 18

# Opcion 1
print(f'Para trabajar debes ser mayor de {edad} años')

# Opcion 2
print('Para trabajar debes ser mayor de', edad, 'años')

# Opcion 3
print('Para trabajar debes ser mayor de ' + str(edad) + ' años')


def construye_tabla_formatos():
    for estilo in range(8):
        for colortexto in range(30,38):
            cad_cod = ''
            for colorfondo in range(40,48): 
                fmto = ';'.join([str(estilo), 
                                 str(colortexto),
                                 str(colorfondo)]) 
                cad_cod+="\033["+fmto+"m "+fmto+" \033[0m" 
            print(cad_cod)
        print('\n')

construye_tabla_formatos()


from colorama import init, Fore, Back, Style

# Para restablecer colores después de cada impresión inicializar 
# el módulo con init(autoreset=True) en lugar de init().

init()
print(Fore.RED+"Texto color rojo")
print(Back.WHITE+"Texto color rojo sobre fondo blanco")
print(Back.WHITE+Style.BRIGHT+"Txt rojo brill.s/blanco"+Back.RESET)
print(Style.RESET_ALL + "Texto con valores por defecto")
print(Fore.WHITE+Back.BLUE+"Texto blanco sobre azul"+Back.RESET)
print("Texto blanco sobre fondo negro")

# Niveles de intensidad

print(Style.DIM + Fore.WHITE + "Intensidad baja")
print(Style.NORMAL + "Intensidad normal")
print(Style.BRIGHT + "Intensidad alta")



from time import sleep
from colorama import Cursor, init, Fore
init()
print("Copiando archivos... ")
for arch in ["111", "222", "333", "444", "555"]:
    sleep(1)
    print(Cursor.UP(1)+Cursor.FORWARD(20)+Fore.YELLOW+str(arch))
       
print(Cursor.POS(25,2) + Fore.GREEN + ">>> Proceso finalizado")

# Correspondencias con secuencias de Escape ANSI:

# "\033[númA" - Línea arriba
# "\033[númB" - Línea abajo
# "\033[númC" - avanzar caracter
# "\033[númD" - retroceder caracter
# "\033[x;yf" - desplazar cursor a coordenada de pantalla


