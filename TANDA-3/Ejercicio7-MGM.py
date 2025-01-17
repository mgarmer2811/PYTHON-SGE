password = input("Mete la constraseña bro\n")

def cumpleLongitud(password):
    return len(password) > 8

def cumpleLetras(password):
    hayMayuscula = False
    hayMinuscula = False

    for letra in password:
        if letra.isupper():
            hayMayuscula = True
            break
        if letra.islower():
            hayMinuscula = True
            break
    return hayMayuscula and hayMinuscula