totalLineas = 0

try:
    archivo = open("datos.txt","r",encoding="utf-8")
    while True:
        linea = archivo.readline()
        if not linea:
            break
        print(linea)
        totalLineas += 1
    print("\nTotal lineas del archivo: ",totalLineas)

except Exception as e:
    print("Ha ocurrido un error: ",e)