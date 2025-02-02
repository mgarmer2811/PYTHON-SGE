import json

stringJson = '{"nombre": "Ana", "edad": 22, "ciudad": "Madrid"}'

diccionario = json.loads(stringJson)
print("Diccionario original: ",diccionario)

diccionario["ciudad"] = "Barcelona"
nuevaStringJson = json.dumps(diccionario)

print("Nueva string de json:\n")
print(nuevaStringJson)