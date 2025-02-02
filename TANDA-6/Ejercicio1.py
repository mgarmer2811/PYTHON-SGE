import json

archivo = open("datos.json","r")
datos = json.load(archivo)
archivo.close()

print(datos["nombre"])
