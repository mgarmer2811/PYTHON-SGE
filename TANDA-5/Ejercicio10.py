try:
    archivo = open("servidor.log","r",encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    archivo = open("errores.log","w",encoding="utf-8")
    for linea in lineas:
        partes = linea.strip().split(" ",3)
        direccionIp = partes[2]
        mensaje = partes[3]

        if "ERROR" in mensaje:
            archivo.write(linea)

    #contar direcciones ip

except Exception as e:
    print("Ha ocurrido un error: ",e)