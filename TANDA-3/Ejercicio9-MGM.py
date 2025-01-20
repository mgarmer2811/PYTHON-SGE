inventario = {}

def agregar_producto():
    nombre = input("Introduce el nombre del producto\n")
    cantidad = int(input("Introduce la cantidad del producto\n"))
    precio = float(input("Introduce el precio del producto\n"))
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print("Producto: ",nombre," añadido al sistema\n")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar\n")
    if nombre in inventario:
        nueva_cantidad = int(input("Introduce la nueva cantidad del producto\n"))
        inventario[nombre]['cantidad'] = nueva_cantidad
        print("Cantidad de ",nombre," actualizada")
    else:
        print("El producto ",nombre," no existe en el sistema\n")

def valor_producto():
    nombre = input("Introduce el nombre del producto para ver su valor total\n")
    if nombre in inventario:
        cantidad = inventario[nombre]['cantidad']
        precio = inventario[nombre]['precio']
        valor_total = cantidad * precio
        print("El valor total del producto: ",nombre," es: ",valor_total,"€\n")
    else:
        print("El producto: ",nombre," no existe en el inventario\n")

def valor_total_inventario():
    valor_total = 0
    for producto in inventario.values():
        valor_total += producto['cantidad'] * producto['precio']
    print("El valor total del inventario es: ",valor_total,"€\n")

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.\n")
    else:
        print("Inventario actual:")
        for nombre, datos in inventario.items():
            print("Producto: ",nombre,"\nCantidad: ",datos["cantidad"],"\nPrecio: ",datos["precio"],"€\n")

while True:
    print("\nOpciones disponibles:")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Valor del inventario de un producto")
    print("4. Valor del inventario total")
    print("5. Mostrar inventario")
    print("6. Salir")

    opcion = input("Elige una opción (1-6)\n")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        actualizar_producto()
    elif opcion == '3':
        valor_producto()
    elif opcion == '4':
        valor_total_inventario()
    elif opcion == '5':
        mostrar_inventario()
    elif opcion == '6':
        print("Gracias por usar el programa. ¡Hasta luego!\n")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 6.\n")
