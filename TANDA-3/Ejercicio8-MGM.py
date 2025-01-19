fin = False
estudiantes = {}

def promedio(estudiantes):
    suma = 0
    for nota in estudiantes.values():
        suma += nota["nota"]
    
    media = suma / len(estudiantes) #Retorna el numero de keys del diccionario
    return media

def mejorEstudiante(estudiantes):
    maxNota = 0
    mejorEstudiante = ()

    for nombre,info in estudiantes.items(): #Retorna los pares key-value del diccionario
        if info["nota"] > maxNota:
            maxNota = info["nota"]
            mejorEstudiante = (nombre,info)
    
    return mejorEstudiante

def peorEstudiante(estudiantes):
    minNota = 100
    peorEstudiante = ()

    for nombre,info in estudiantes.items():
        if info["nota"] < minNota:
            minNota = info["nota"]
            peorEstudiante = (nombre,info)

    return peorEstudiante


def peorEstudiante(estudiantes):
    return 0

while(not fin):
    nombre = input("Bro dame el nombre del estudiante [Introduce 'FIN' para terminar]\n")

    if nombre == "FIN":
        fin = True
        break

    nota = float(input("Ahora dame la nota que ha sacado ese estudiante porfi\n"))

    if nombre not in estudiantes:
        estudiantes[nombre] = {"nota" : nota}
        print(nombre,": Estudiante añadido correctamente al sistema\n")
    else:
        print(nombre,": Estudiante NO añadido porque ya está en el sistema\n")

