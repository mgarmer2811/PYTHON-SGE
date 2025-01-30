ARCHIVO_NOTAS = "notas.txt"

def agregarNota():
    nota = input("Escribe la nota\n")
    try:
        with open (ARCHIVO_NOTAS,"a",encoding="utf-8") as archivo:
            archivo.write(nota + "\n")
        print("Nota agregada correctamente\n")

    except Exception as e:
        print("Ha ocurrido un error: ",e)

def leerNotas():
    notas = []
    try:
        with open(ARCHIVO_NOTAS,"r",encoding="utf-8") as archivo:
            notas = archivo.readlines()
        
        for nota in notas:
            print(nota)
        
    except Exception as e:
        print("Ha ocurrido un error: ",e)

def buscarPorPalabra():
    palabra = input("Escribe la palabra por la que buscar")
    notas = []
    try:
        with open(ARCHIVO_NOTAS,"r",encoding="utf-8") as archivo:
            notas = archivo.readlines()
        
        for i in range(len(notas)):
            if palabra in notas[i]:
                print(notas[i])

    except Exception as e:
        print("Ha ocurrido un error: ",e)

def borrarNota():
    nota = input("Escribe la nota a borrar")
    notas = []
    try:
        with open(ARCHIVO_NOTAS,"r",encoding="utf-8") as archivo:
            notas = archivo.readlines()
        
        if nota not in notas:
            raise Exception("La nota introducida no existe en el fichero")

    except Exception as e:
        print("Ha ocurrido un error: ",e)

def menu():
    print("")
    print("")
    print("1. Añadir nuevas notas")
    print("2. Leer notas almacenadas")
    print("3. Buscar nota por palabra clave")
    print("4. Borrar una nota especifica")
    print("5. Salir")
    opcion = input("Escoja opcion: ")
    print("")
    print("")

    return opcion

while True:
    opcion = menu()

    if opcion == "1":
        agregarNota()
    elif opcion == "2":
        leerNotas()
    elif opcion == "3":
        buscarPorPalabra()
    elif opcion == "4":
        borrarNota()
    else:
        break