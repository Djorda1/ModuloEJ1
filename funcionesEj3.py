def esBisiesto(año):
    if año % 4 ==0:
        return True
    else: return False

año=int(input("ingresar año"))
if esBisiesto(año): print("es bisieto")
else: print("no es bisiesto")
