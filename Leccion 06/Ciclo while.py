# -----------------------------Descripción ciclo while-----------------------------
# El concepto detrás de un ciclo while es simple: mientras una condición es verdadera -> Ejecuta mis comandos. El bucle while comprueba la condición cada vez, y si devuelve "true", ejecutará las instrucciones dentro del bucle.

# -----------------------------Sintáxis-----------------------------
x = 1

while x <= 10:
    print(x)
    x = x + 1

# -----------------------------Ejemplos-----------------------------
# Este programa imprime numeros del 1 al 10 de manera asendente

x = 1

while x <= 10:
    print(x)
    x = x + 1

# -----------------------------While / else-----------------------------
# Puedes agregar una instrucción else para ejecutar si falla la condición de bucle. Agreguemos una condición else a nuestro código para imprimir "Fin del bucle" una vez que hayamos impreso los números del 1 al 10.

# Este programa imprimirá primero los números del 1 al 10. Cuando x es 11, la condición while fallará, desencadenando la condición else.
x = 1

while x <= 10:
	print(x)
	x = x + 1
else:
	print("Fin del bucle")

# -----------------------------Break en whiles-----------------------------
# En este programa saldremos del ciclo cuando la condición sea verdadera. En el programa, el bucle detendrá la ejecución cuando x sea 5, a pesar de que x sea mayor o igual que 1.

x = 1


while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1
    
else:
	print("Fin del bucle")

# -----------------------------Continue en whiles-----------------------------
# Aquí hay otro escenario: digamos que desea omitir el bucle si se cumple una determinada condición. Sin embargo, desea continuar con las ejecuciones posteriores hasta que la condición principal while se vuelva falsa.

# En este programa el bucle se imprimirá de 1 a 10, excepto 5. Cuando x es 5, el resto de los comandos se omiten y el flujo de control vuelve al inicio del bucle while.

x = 1
while x <= 10:
    if x == 5:
        x += 1
        continue
    print(x)