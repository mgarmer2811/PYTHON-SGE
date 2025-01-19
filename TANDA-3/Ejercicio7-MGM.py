password = input("Mete la constraseña bro\n")

def cumpleLongitud(password):
    return len(password) > 8

def cumpleLetras(password):
    hayMayuscula = False
    hayMinuscula = False

    for caracter in password:
        if caracter.isupper():
            hayMayuscula = True
        if caracter.islower():
            hayMinuscula = True
    return hayMayuscula and hayMinuscula

def cumpleDigitos(password):
    hayDigito = False
    
    for caracter in password:
        if caracter.isdigit():
            hayDigito = True
            break
    return hayDigito

def cumpleEspecial(password):
    hayEspecial = False
    caracteresEspeciales = "!@#$%^&*()-_+=/\\,.:;"

    for caracter in password:
        if caracter in caracteresEspeciales:
            hayEspecial = True
            break
    return hayEspecial

def testPassword(password):
    if not cumpleLongitud(password):
        print("La contraseña debe tener mas de 8 caracteres\n")
    
    if not cumpleLetras(password):
        print("La contraseña no tiene al menos 1 mayuscula y 1 minuscula\n")

    if not cumpleDigitos(password):
        print("La contraseña no tiene al menos 1 digito\n")
    
    if not cumpleEspecial(password):
        print("La contraseña no tiene al menos 1 caracter especial\n")

testPassword(password)