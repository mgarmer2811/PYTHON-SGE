anyo1 = int(input("Bro dame un año porfa\n"))
anyo2 = int(input("Dame otro año porfi\n"))

if anyo1 > anyo2:
    aux = anyo1
    anyo1 = anyo2
    anyo2 = aux

cantidad = 0
anyos = []

def bisiestos(min,max):
    global cantidad,anyos
    for anyo in range(min,max):
        if (anyo % 10 == 0) and (((anyo % 4 == 0) and (anyo % 100 != 0)) or (anyo % 400 == 0)):
            cantidad += 1
            anyos.append(anyo)

bisiestos(anyo1,anyo2)

print("La cantidad de años bisiestos en ese rango es: ",cantidad)
print("Los años bisiestos en ese rango son: ",anyos)