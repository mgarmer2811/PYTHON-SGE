try:
    archivo1 = open("archivo1.txt", "r", encoding="utf-8")
    archivo2 = open("archivo2.txt", "r", encoding="utf-8")

    lineas1 = archivo1.readlines()
    lineas2 = archivo2.readlines()

    archivo1.close()
    archivo2.close()

    combinado = open("combinado.txt", "w", encoding="utf-8")

    max_lineas = max(len(lineas1), len(lineas2))
    for i in range(max_lineas):
        if i < len(lineas1):
            combinado.write(lineas1[i])
        if i < len(lineas2):
            combinado.write(lineas2[i])

    combinado.close()
    print("El archivo combinado ha sido creado correctamente.")

except Exception as e:
    print("Ha ocurrido un error:", e)
