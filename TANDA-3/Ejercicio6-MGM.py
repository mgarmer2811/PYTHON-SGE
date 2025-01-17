numero = 0
numeros = []
fin = False

def pedirNumeros():
    global numero,numeros,fin

    while(not fin):
        try:
            numero = float(input("Bro dame un numerin {Mete '-1' para terminar}\n"))
            
            if numero == -1:
                fin = True
            else:
                numeros.append(numero)

        except ValueError:
            print("Eso que me has dao no era un numerin\n")
    
    return numeros

def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    
    return promedio

def maximo(lista):
    return max(lista)

def minimo(lista):
    return min(lista)

pedirNumeros()
print("El promedio de los numeros es: ",promedio(numeros))
print("El maximo de la lista es: ",maximo(numeros))
print("El minimo de la lista es: ",minimo(numeros))