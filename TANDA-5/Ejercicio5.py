listaLineas = []

try:
    archivo = open("datos.csv", "r", encoding="utf-8")
    
    while True:
        linea = archivo.readline()
        if not linea:
            break

        linea = linea.strip().split(",")
        print(linea)
        listaLineas.append(linea)
    archivo.close()

except Exception as e:
    print("Ha ocurrido un error: ", e)

encabezados = listaLineas[0]
diccionario = []

for i in range(1, len(listaLineas)):
    fila_diccionario = {}
    for j in range(len(encabezados)):
        fila_diccionario[encabezados[j]] = listaLineas[i][j]
    diccionario.append(fila_diccionario)

print("\nDiccionario final:")
for item in diccionario:
    print(item)