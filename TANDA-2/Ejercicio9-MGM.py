frase = input('Bro dame una frase porfa\n')
letra = input('Ahora dame una letrita porfa\n')

contador = 0

for let in frase:
    if let == letra:
        contador += 1

print('Numero de veces que aparece la letra "',letra,'": ',contador)