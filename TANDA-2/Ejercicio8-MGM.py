palabra = input('Bro dame una palabra porfa\n')

palabraInvertida = ''
for letra in palabra[::-1]:
    palabraInvertida += letra

print(palabraInvertida)