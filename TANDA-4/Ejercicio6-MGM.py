class Animal:
    
    def __init__(self,nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace sonido")
    
class Perro(Animal):
    
    def __init__(self,nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print("El perro hace guau guau")

animal = Animal("animal")
perro = Perro("perro")

animal.hacer_sonido()
perro.hacer_sonido()