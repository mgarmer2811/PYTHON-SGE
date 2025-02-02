import json

with open('estudiantes.json', 'r') as archivo_estudiantes:
    estudiantes = json.load(archivo_estudiantes)

with open('profesores.json', 'r') as archivo_profesores:
    profesores = json.load(archivo_profesores)

resultado = {
    "estudiantes": estudiantes,
    "profesores": profesores
}

with open('combinado.json', 'w') as archivo_combinado:
    json.dump(resultado, archivo_combinado, indent=4)

print("Los archivos han sido combinados y guardados en 'combinado.json'.")