numero = 0

try:
    numero = int(input('Bro dame un numero entero positivo porfa\n'))
    if numero >= 0:
        numeros = ''

        for i in range(numero,-1,-1):
            numeros += str(i) + ','

        print(numeros)
    else:
        raise ValueError
except ValueError:
    print('No me has dao un numero entero positivo melon >:0')