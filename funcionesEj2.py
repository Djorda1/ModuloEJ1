import numpy
def esPrimo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2 , numero):
            if numero % i == 0:
                return False
        return True

numero = int(input("ingresar numero"))
if esPrimo(numero):
    print("es primo")
else: print("No es primo")