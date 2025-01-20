class Vehiculo:
    cantidad_total = 0

    def __init__(self,ruedas,color,marca):
        self.ruedas = ruedas
        self.color = color
        self.marca = marca
        Vehiculo.cantidad_total += 1
    
    def informacion(self):
        print("Informacion del vehiculo:")
        print("*************************")
        print("Numero de ruedas: ",self.ruedas)
        print("Color: ",self.color)
        print("Marca: ",self.marca)
    
    @classmethod
    def numeroVehiculos(cls):
        print("El numero total de vehiculos asciende a: ",cls.cantidad_total)
    
porsche911 = Vehiculo(4,"Plateado","Porsche")
skylineGTR = Vehiculo(4,"Azul","Nissan")

porsche911.informacion()
skylineGTR.informacion()
Vehiculo.numeroVehiculos()
