class alumno():

    def __init__(self,nombre,nota):
        self.nombre=nombre
        if nota <= 10 and nota >= 0:
            self.nota=nota
        else:
            print("error en nota")
            quit()

    def aprobo(self):
        if self.nota > 7 :
            return "Estado: Aprobado"
        else:
            return "Estado: Desaprobado"

    def __str__(self):
        return "Nombre {}, Nota: {}".format(self.nombre, self.nota)

Jose = alumno("jose", 5)
Juan = alumno("juan",8)
print(Jose,Jose.aprobo())
print(Juan, Juan.aprobo())
Tomas = alumno("tomas",50)