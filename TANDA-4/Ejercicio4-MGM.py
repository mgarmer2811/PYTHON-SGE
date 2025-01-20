class Estudiante:

    def __init__(self,nombre,calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def promedio(self):
        suma = 0
        for calificacion in self.calificaciones:
            suma += calificacion
        
        return (suma / len(self.calificaciones))

manu = Estudiante("manu",[7,9,10,9,5,10,8,9,9,8])
print("El promedio del estudiante es: ",manu.promedio())