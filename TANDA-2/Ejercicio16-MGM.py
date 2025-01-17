palabras = []

for i in range(4):
    palabras.append(input("Bro dame una palabrita\n"))

palabras.sort()
print("Palabras ordenadas: ",",".join(palabras))