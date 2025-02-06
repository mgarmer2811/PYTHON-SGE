import json

def LibrosEuro():
    libros = [
        {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "año": 1605, "precio": 19.99},
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967, "precio": 15.50},
        {"titulo": "1984", "autor": "George Orwell", "año": 1949, "precio": 12.80},
        {"titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "año": 2001, "precio": 18.40},
        {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "año": 1985, "precio": 17.20}
    ]

    archivo = open("libros.json","w",encoding="utf-8")
    json.dump(libros,archivo,indent=3)
    archivo.close()

    