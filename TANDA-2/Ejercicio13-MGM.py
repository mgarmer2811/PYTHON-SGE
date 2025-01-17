anyo1 = int(input('Bro dame un año porfa\n'))
anyo2 = int(input('Bro dame otro año porfi\n'))

for anyo in range(anyo1,anyo2+1):
    if (anyo % 10 == 0) and (((anyo % 4 == 0) and (anyo % 100 != 0)) or (anyo % 400 == 0)):
        print(anyo)

