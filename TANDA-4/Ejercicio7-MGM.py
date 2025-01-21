class Rectangulo:
    
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
rect = Rectangulo(3,7)
print("El area del rectangulo es: ",rect.area())