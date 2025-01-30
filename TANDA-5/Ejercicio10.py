try:
    direccionesIp = {}
    
    archivo = open("servidor.log","r",encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    archivo = open("errores.log","w",encoding="utf-8")
    for linea in lineas:
        partes = linea.strip().split(" ",3)
        direccionIp = partes[2]
        mensaje = partes[3]

        if direccionIp not in direccionesIp:
            direccionesIp[direccionIp] = 1
        else:
            direccionesIp[direccionIp] += 1

        if "ERROR" in mensaje:
            archivo.write(linea)
    
    print(direccionesIp)
            
except Exception as e:
    print("Ha ocurrido un error: ",e)