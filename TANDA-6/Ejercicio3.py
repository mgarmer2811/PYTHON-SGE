import json

archivo = open("estudiantes.json","r")
estudiantes = json.load(archivo)

suma = 0
maxCalificacion = -1
mejorEstudiante = ""
media = 0

for estudiante in estudiantes:
    calificacion = estudiante["calificacion"]
    suma += calificacion

    if calificacion > maxCalificacion:
        maxCalificacion = calificacion
        mejorEstudiante =  estudiante["nombre"]

media = suma / len(estudiantes)

print("La media de calificaciones es: ",media)
print("El estudiante con la nota mas alta es: ",mejorEstudiante," con una calificacion de: ",maxCalificacion)