tienda = {}
carrito = []

def agregar_producto():
    nombre = input("Introduce el nombre del producto\n")
    cantidad = int(input("Introduce la cantidad del producto\n"))
    precio = float(input("Introduce el precio del producto\n"))
    tienda[nombre] = {"cantidad": cantidad, "precio": precio}
    print("Producto:", nombre, "añadido al sistema\n")

def actualizar_producto():
    clave_admin = "admin123"
    clave = input("Introduce la clave de administrador para actualizar productos\n")
    
    if clave == clave_admin:
        nombre = input("Introduce el nombre del producto a actualizar\n")
        if nombre in tienda:
            nueva_cantidad = int(input("Introduce la nueva cantidad del producto\n"))
            nuevo_precio = float(input("Introduce el nuevo precio del producto\n"))
            tienda[nombre]['cantidad'] = nueva_cantidad
            tienda[nombre]['precio'] = nuevo_precio
            print("Producto:", nombre, "actualizado correctamente\n")
        else:
            print("El producto", nombre, "no existe en la tienda\n")
    else:
        print("Clave incorrecta. No tienes permisos para actualizar productos\n")

def mostrar_tienda():
    if not tienda:
        print("La tienda está vacía.\n")
    else:
        print("Productos disponibles:")
        for nombre, datos in tienda.items():
            print("Producto:", nombre, "\nCantidad disponible:", datos["cantidad"], "\nPrecio:", datos["precio"], "€\n")

def agregar_carrito():
    nombre = input("Introduce el nombre del producto a añadir al carrito\n")
    if nombre in tienda:
        cantidad_disponible = tienda[nombre]["cantidad"]
        if cantidad_disponible > 0:
            cantidad_a_agregar = int(input("¿Cuántos " + nombre + " deseas agregar al carrito? (Stock disponible: " + str(cantidad_disponible) + ")\n"))
            if cantidad_a_agregar <= cantidad_disponible:
                carrito.append({"nombre": nombre, "cantidad": cantidad_a_agregar, "precio": tienda[nombre]["precio"]})
                tienda[nombre]["cantidad"] -= cantidad_a_agregar
                print(cantidad_a_agregar, nombre, "añadido(s) al carrito\n")
            else:
                print("No hay suficiente stock para agregar esa cantidad al carrito\n")
        else:
            print("El producto", nombre, "está agotado\n")
    else:
        print("El producto no existe en la tienda\n")

def retirar_carrito():
    nombre = input("Introduce el nombre del producto a retirar del carrito\n")
    for item in carrito:
        if item["nombre"] == nombre:
            carrito.remove(item)
            print("Producto", nombre, "retirado del carrito\n")
            return
    print("El producto", nombre, "no está en el carrito\n")

def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.\n")
    else:
        print("Contenido del carrito:")
        for item in carrito:
            print("Producto:", item['nombre'], "- Cantidad:", item['cantidad'], "- Precio unitario:", item['precio'], "€")

def coste_total_carrito():
    total = 0
    for item in carrito:
        total += item["cantidad"] * item["precio"]
    print("El coste total del carrito es:", total, "€\n")
    return total

def realizar_compra():
    if not carrito:
        print("El carrito está vacío. No puedes realizar la compra.\n")
    else:
        coste = coste_total_carrito()
        confirmacion = input("¿Confirmas la compra por un total de " + str(coste) + "€? (Si/No)\n").lower()
        if confirmacion == 'si':
            print("Compra realizada con éxito\n")
            carrito.clear()
        else:
            print("Compra cancelada\n")

while True:
    print("\nOpciones disponibles:")
    print("1. Agregar producto")
    print("2. Actualizar producto (requiere clave de administrador)")
    print("3. Mostrar productos disponibles")
    print("4. Agregar producto al carrito")
    print("5. Retirar producto del carrito")
    print("6. Ver carrito")
    print("7. Ver coste total del carrito")
    print("8. Realizar compra")
    print("9. Salir")

    opcion = input("Elige una opción (1-9)\n")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        actualizar_producto()
    elif opcion == '3':
        mostrar_tienda()
    elif opcion == '4':
        agregar_carrito()
    elif opcion == '5':
        retirar_carrito()
    elif opcion == '6':
        mostrar_carrito()
    elif opcion == '7':
        coste_total_carrito()
    elif opcion == '8':
        realizar_compra()
    elif opcion == '9':
        print("Gracias por usar el programa. ¡Hasta luego!\n")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 9.\n")
