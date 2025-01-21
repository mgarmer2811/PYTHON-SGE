class Vehiculo:

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def informacion(self):
        print("Marca: ",self.marca,"\n")
        print("Modelo: ",self.modelo,"\n")
    
class Coche(Vehiculo):

    def __init__(self,marca,modelo,cv):
        super().__init__(marca,modelo)
        self.cv = cv
    
    def informacion(self):
        super().informacion()
        print("CC: ")

    def circular(self):
        print("El coche esta circulando\n")

class Moto(Vehiculo):

    def __init__(self,marca,modelo,cc):
        super().__init__(marca,modelo)
        self.cc = cc

    def informacion(self):
        super().informacion()
        print("Cv: ")
    
    def circular(self):
        print("La moto esta circulando\n")

vehiculo = Vehiculo("Xiaomi","SU07")
vehiculo.informacion()
porsche911 = Coche("porsche",911,394)
porsche911.informacion()
porsche911.circular()
ninjaH2 = Moto("Kawasaki","ninja h2",998)
ninjaH2.informacion()
ninjaH2.circular()