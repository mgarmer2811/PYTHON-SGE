palabra = input("Bro dame una palabra porfa\n")

mitad = len(palabra) / 2
iterador1 = 0
iterador2 = len(palabra) - 1
noEsPalindromo = False

while (iterador1 < mitad) and (iterador2 > mitad):
    if(palabra[iterador1] == palabra[iterador2]):
        iterador1 += 1
        iterador2 -= 1
    else:
        print("La palabra introducida NO es un palindromo")
        noEsPalindromo = True
        break

if (not noEsPalindromo):
    print("La palabra ingresada ES un palindromo")