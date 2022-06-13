f=open('textoEj.txt','x')
f.close()
f = open('textoEj.txt', 'a+')
f.write("Esta es la octava sesión, donde veremos cómo gestionar las entradas y salidas de un programa.")
f.close()
f=open('textoEj.txt', 'r')
datos=f.read()

print(datos)



