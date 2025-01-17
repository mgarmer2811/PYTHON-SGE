palabras = []
palabra = ""
fin = False

def ordenarPalabras():
    global fin,palabra,palabras
    while(not fin):
        palabra = input("Bro dame una palabrita {Para terminar mete la palabra 'FIN'\n")

        if palabra == "FIN":
            fin = True
        else:
            palabras.append(palabra)
    
    palabras = sorted(palabras)
    return palabras

print("Las palabras ordenadas son: ",ordenarPalabras())
# Las palabras que empiecen por mayuscula van Primero porque
# el codigo ASCII de las mayusculas es menor