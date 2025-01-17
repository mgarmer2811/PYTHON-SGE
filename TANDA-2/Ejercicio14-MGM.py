numeros = []

try:
    for i in range(5):
        numeros.append(int(input('Bro dame un numero porfa\n')))
    numeros = sorted(numeros,reverse=True)
    print('El mayor de los numeros es: ',numeros[0])

except ValueError:
    print('Has metio alguna cosa que no es un numero melon')