try:
    archivo = open("log.txt","r",encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    lineasSinRepetidos = set(lineas)

    archivo = open("no_repetidos.txt","w",encoding="utf-8")
    archivo.writelines(lineasSinRepetidos)
    archivo.close()

    print("Se ha completado la depuracion correctamente!")

except Exception as e:
    print("Ha ocurrido un error: ",e)