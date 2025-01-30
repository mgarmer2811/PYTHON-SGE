try:
    archivo = open("grande.txt","r",encoding="utf-8")
    contadorPartes = 1
    lineasPorParte = 100
    lineas = []
        
    while True:
        linea = archivo.readline()
        if not linea:
            break
        lineas.append(linea)

        if len(lineas) == lineasPorParte:
            nombreSalida = "parte_" + str(contadorPartes) + ".txt"
            archivoSalida = open(nombreSalida,"w",encoding="utf-8")
            archivoSalida.writelines(lineas)
            archivoSalida.close()

            lineas = []
            contadorPartes += 1

    if lineas:
        nombreSalida = "parte_" + str(contadorPartes) + ".txt"
        archivoSalida = open(nombreSalida,"w",encoding="utf-8")
        archivoSalida.writelines(lineas)
        archivoSalida.close()
    
    print("Se ha completado la operacion correctamente!")

except Exception as e:
    print("Ha ocurrido un error: ",e)
