try:
    numero = int(input('Bro dame un numero entero positivo porfa\n'))
    contador = 0

    for i in range(1,numero+1):
        if numero % i == 0:
            contador += 1
    
    if contador == 2:
        print('El numero que has metio es primo')
    else:
        print('El numero que has metio NO es primo')

except ValueError:
    print('No me has dao un numero entero positivo cabezon')