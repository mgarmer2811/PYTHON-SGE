fin = False
numeros = []
suma = 0
cantidadNumeros = 0

while (not fin):
    numeroUser = (int(input("Bro dame un numerin. Mete '-1' para terminar\n")))
    
    if (numeroUser == -1):
        fin = True
    else:
        numeros.append(numeroUser)
        cantidadNumeros += 1

for numero in numeros:
    suma += int(numero)

promedio = suma / cantidadNumeros
print("El promedio de los numerines que has metido es: ",promedio)