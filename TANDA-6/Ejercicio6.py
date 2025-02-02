import json

nombre_archivo = 'archivo.json'

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = json.load(archivo)
    print("El archivo JSON es válido. Contenido:", contenido)
except json.JSONDecodeError as e:
    print("Error de decodificación JSON:", e)
except FileNotFoundError:
    print("El archivo", nombre_archivo, "no se encontró.")
except Exception as e:
    print("Ocurrió un error:", e)