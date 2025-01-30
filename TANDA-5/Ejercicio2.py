entradaUser = input("Introduce el texto que quieres guardar en salida.txt: ")

try:
    archivo = open("salida.txt","w",encoding="utf-8")
    archivo.write(entradaUser)
    print("Texto guardado con exito!")

except Exception as e:
    print("Ha ocurrido un error: ",e)