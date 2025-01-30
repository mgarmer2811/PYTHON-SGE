palabraBuscar = input("Introduce la palabra a buscar\n")
palabraSustituta - input("Introduce la palabra sustituta\n")

contenidoArchivo = ""

try:
    archivo = open("texto.txt","r",encoding="utf-8")
    while True:
        linea = archivo.readline()
        if not linea:
            break
        contenidoArchivo += linea

    archivo.close()
    contenidoArchivo = contenidoArchivo.replace(palabraBuscar,palabraSustituta)
    archivo.open("modificado.txt","w",encoding="utf-8")
    archivo.write(contenidoArchivo)
    print("Se ha terminado el proceso correctamente")

except Exception as e:
    print("Ha ocurrido un error: ",e)