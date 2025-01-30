numeros = []

try:
    archivo = open("numeros.txt","r",encoding="utf-8")
    while True:
        linea = archivo.readline()
        if not linea:
            break
        numeros.append(float(linea.strip()))
    
    suma = sum(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    media = suma / len(numeros)

    print("La suma de los numeros tiene como resultado: ",suma)
    print("El mayor de los numeros es: ",maximo)
    print("El menor de los numeros es: ",minimo)
    print("La media de los numeros es: ",media)

except Exception as e:
    print("Ha ocurrido un error: ",e)