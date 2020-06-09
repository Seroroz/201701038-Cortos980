
# Secuencia de collatz

def colllatz(numero):
    while numero != 1:
        if numero %2 == 0:                      #verifica si es par
            print("%d,"%(numero),end = "")
            numero = numero/2
        else:
            print("%d,"%(numero),end = "")      #verifica si es impar
            numero = (numero*3)+1
        if numero == 1:
            print("1")

for n in range (1, 38):  #es mi terminacion de carnet
    colllatz(n)
                