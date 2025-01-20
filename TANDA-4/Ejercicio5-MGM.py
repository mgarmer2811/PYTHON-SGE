class Producto:

    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def agregarExistencias(self,masCantidad):
        self.cantidad += masCantidad
        print("A la cantidad actual le hemos sumado: ",masCantidad)
        print("Cantidad actual del producto: ",self.cantidad)

    def quitarExistencias(self,menosCantidad):
        self.cantidad -= menosCantidad
        print("A la cantidad actual le hemos restado: ",menosCantidad)
        print("Cantidad actual del producto: ",self.cantidad)

    def informacion(self):
        
        print("Informacion del producto:")
        print("Nombre: ",self.nombre)
        print("Precio: ",self.precio)
        print("Cantidad: ",self.cantidad)

manzana = Producto("manzana",0.15,5)
pera = Producto("pera",0.17,7)

manzana.informacion()
manzana.agregarExistencias(4)
manzana.quitarExistencias(7)
print("\n")
pera.informacion()
pera.agregarExistencias(4)
pera.quitarExistencias(3)