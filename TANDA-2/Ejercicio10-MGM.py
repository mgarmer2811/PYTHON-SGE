try:
    altura = int(input('Bro dame un numerito entero positivo porfa\n'))

    for y in range(altura):
        print('*' * y)
except ValueError:
    print('No me has dao un numero entero positivo melon')