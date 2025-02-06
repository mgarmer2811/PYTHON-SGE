def esTexto(texto):
    try:
        float(texto)
        return False
    except:
        return True  ## si al convertir salta error, es que es una string

def funcion(texto):
    if esTexto(texto):
        dicPalabras = {}
        dicPalabrasOrdenado = {}
        
        palabras = texto.strip().split()
        for palabra in palabras:
            if palabra not in dicPalabras:
                veces = palabras.count(palabra)
                dicPalabras[palabra] = veces
        listaClaveValor = list(dicPalabras.items())
        dicPalabrasOrdenado = dict(sorted(listaClaveValor,key=lambda x: x[1],reverse=True))
        print("El diccionario ordenado segun frecuencia es el siguiente:\n",dicPalabrasOrdenado)
        
    else:
        print("NO has introducido texto")
        return
    
texto = input("Introduce un texto\n")
funcion(texto)
    


