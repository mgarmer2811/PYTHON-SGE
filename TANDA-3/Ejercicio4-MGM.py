palabras = []
palabra = ""
fin = False

def ordenarPalabras():
    global fin,palabra,palabras
    while(not fin):
        palabra = input("Bro dame una palabrita {Para terminar mete 'FIN'}\n")

        if palabra == "FIN":
            fin = True
        elif palabra not in palabras:
            palabras.append(palabra)
        else:
            print("Esa palabra ya esta en la lista my G, mete otra distinta\n")
    
    palabras = sorted(palabras)
    return palabras

print("Las palabras ordenadas son: ",ordenarPalabras())
# Las palabras que empiecen por mayuscula van Primero porque
# el codigo ASCII de las mayusculas es menor