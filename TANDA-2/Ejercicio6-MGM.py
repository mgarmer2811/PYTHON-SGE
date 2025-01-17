numero = 0

try:
    numero = int(input('Bro dame un numero entero positivo porfa\n'))
    if numero >= 0:
        impares = ''

        for i in range(numero):
            if i % 2 != 0:
                impares = impares + str(i) + ','
                
        print(impares)
    else:
        raise ValueError
except ValueError:
    print('No me has dao un numero entero positivo melon >:0')