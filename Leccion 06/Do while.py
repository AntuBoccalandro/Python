palabra_secreta = "python"
contador= 0

while True:
    palabra= input("Ingrese su palabra secreta: ").lower()
    contador = contador+1
    if palabra== palabra_secreta:
        break
    if palabra != palabra_secreta and contador > 7: 
        break