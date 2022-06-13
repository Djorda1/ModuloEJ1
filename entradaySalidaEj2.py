import pickle
class vehiculo:
    marca = ""
    velocidad = 0
    precio = 0

    def __init__(self,marca, velocidad ,precio):
        self.marca=marca
        self.velocidad=velocidad
        self.precio=precio

a1 = vehiculo("Audi",200,20000)

f=open('ficheroEjercio.bin','wb')
pickle.dump(a1,f)
f.close()
f=open('ficheroEjercio.bin','rb')
datos=pickle.load(f)
print(datos)
f.close()



