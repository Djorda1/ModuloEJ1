class vehiculo:
    color = "blanco"
    ruedas = 4
    puertas = 3

class coche(vehiculo):
    velocidad= 120
    cilindrada= 4000

coche1=coche()

print("nuevo coche:",coche1.color,coche1.ruedas,coche1.puertas,coche1.velocidad,coche1.cilindrada)
