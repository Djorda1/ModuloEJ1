import numpy
def areaTriangulo(base,altura):
    return base*altura
def radioCirculo(radio):
    return numpy.pi*float(radio)**2


radio = input("agregar radio ")
base = input("agregar base")
altura = input("agregar altura")
print(areaTriangulo(float(base),float(altura)))
print(radioCirculo(radio))