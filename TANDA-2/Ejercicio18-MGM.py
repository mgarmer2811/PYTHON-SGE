numero = input("Introduce un numero de al menos 4 cifras\n")

while (len(numero) < 4) and (numero.isdigit()):
    numero = input("Numero invalido. Introduce un numero de al menos 4 cifras\n")

suma = 0
for digito in numero:
    suma += int(digito)

print("La suma de los digitos es: ",suma)