import random

numeroSecreto = random.randint(1,51)
adivinado = False
intentos = 0
MAX_INTENTOS = 7

while (intentos < MAX_INTENTOS) and (not adivinado):
    intentoUser = int(input("Intenta adivinar el numero\n"))
    intentos += 1

    if intentoUser == numeroSecreto:
        print("Felicidades! Has adivinado el numero secreto\n")
        adivinado = True
        break
    elif intentoUser < numeroSecreto:
        print("El numero secreto es mayor\n")
    else:
        print("El numero secreto es menor\n")

if not adivinado:
    print("Has perdido!")