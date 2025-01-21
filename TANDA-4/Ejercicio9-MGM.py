class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

def existe(libros, libro):
    for i in range(len(libros)):
        if libro.getTitulo() == libros[i].getTitulo() and libro.getAutor() == libros[i].getAutor():
            return i
    return -1

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self):
        titulo = input("Introduzca el título del nuevo libro:\n")
        autor = input("Introduzca el nombre del autor:\n")
        libro = Libro(titulo, autor)
        if existe(self.libros, libro) == -1:
            self.libros.append(libro)
            print("El libro '",titulo,"' del autor '",autor,"' se ha añadido correctamente")
        else:
            print("El libro ya existe en el sistema.")

    def eliminar(self):
        titulo = input("Introduzca el título del libro a eliminar:\n")
        autor = input("Introduzca el nombre del autor:\n")
        libro = Libro(titulo, autor)
        index = existe(self.libros, libro)
        if index != -1:
            self.libros.pop(index)
            print("El libro '",titulo,"' del autor '",autor,"' se ha eliminado correctamente")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def listar(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Listado de libros en la biblioteca:")
            for libro in self.libros:
                print("Titulo: '",libro.getTitulo(),"' \tAutor: ",libro.getAutor())


biblioteca = Biblioteca()
fin = False
while not fin:
    print("\nMenú de Biblioteca")
    print("1. Agregar un libro")
    print("2. Eliminar un libro")
    print("3. Listar libros")
    print("4. Salir")
    opcion = input("Seleccione una opción:\n")

    if opcion == "1":
        biblioteca.agregar()
    elif opcion == "2":
        biblioteca.eliminar()
    elif opcion == "3":
        biblioteca.listar()
    elif opcion == "4":
        fin = True
        print("Has salido del programa!")
    else:
        print("Opción no válida. Intente de nuevo.")
