import json

productos = {
    "productos": [
        {
            "nombre": "Laptop",
            "precio": 1200.99,
            "cantidad": 5
        },
        {
            "nombre": "Smartphone",
            "precio": 799.49,
            "cantidad": 10
        },
        {
            "nombre": "Tablet",
            "precio": 450.00,
            "cantidad": 7
        },
        {
            "nombre": "Auriculares",
            "precio": 150.00,
            "cantidad": 20
        }
    ]
}

archivo = open("productos.json","w")
json.dump(productos,archivo,indent=3)
archivo.close()

print("Se han guardado los productos correctamente en 'productos.json'")