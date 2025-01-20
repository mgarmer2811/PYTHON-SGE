class Persona:

    def __init__(self,nombre,edad,altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    
    def saludar(self):
        print("Nombre: ",self.nombre," Edad: ",self.edad)
    
    def informacion(self):
        print("Altura: ",self.altura)

manuel = Persona("Manuel",21,183)
manuel.saludar()
manuel.informacion()