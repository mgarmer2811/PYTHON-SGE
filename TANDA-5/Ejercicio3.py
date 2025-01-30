nombreArchivo = input("Introduce el nombre del archivo a leer\n")

try:
    archivo = open(nombreArchivo,"r",encoding="utf-8")
    contenido = archivo.read()
    palabras = contenido.split()
    totalPalabras = len(palabras)
    print("El archivo contiene un total de: ",totalPalabras)

except Exception as e:
    print("Ha ocurrido un error: ",e)