altura = float(input("Bro dame la altura del triangulo\n"))
base = float(input("Bro dame la base del triangulo\n"))

def area(altura,base):
    return altura * base

def perimetro(altura,base):
    return (2 * altura) + (2 * base)

print("El area del rectangulo es: ",area(altura,base))
print("El perimetro del rectangulo es: ",perimetro(altura,base))