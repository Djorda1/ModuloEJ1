numero_inicial = 2
numero_final = 8
lista=[]
while numero_inicial < numero_final:
    if numero_inicial % 2:
        lista.append(numero_inicial)
    numero_inicial= numero_inicial+1
print(lista)