# clase libro
class Libro():
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_categoria(self):
        return self.categoria

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_categoria(self, categoria):
        self.categoria = categoria

    def __str__(self):
        return "Título: {}, Autor: {}, Categoría: {}".format(self.titulo, self.autor, self.categoria)


# clase libreria, que contiene una lista de libros
class Libreria():
    def __init__(self):
        self.libros = []

    def get_libros(self):
        return self.libros

    def set_libros(self, libros):
        self.libros = libros

    def agregar_libro(self):
        titulo = input("Introduce el título:")

        if self.buscar_libro_titulo(titulo) is None:
            autor = input("Introduce el nombre del autor:")
            categoria = input("Introduce la categoría:")
            self.libros.append(Libro(titulo, autor, categoria))
        else:
            print("El libro ya existe.")
##Por aqui
    def eliminar_libro(self, titulo):
        if self.buscar_libro_titulo(titulo) is None:
            autor = input("Introduce el nombre del autor:")
            categoria = input("Introduce la categoría:")
            self.libros.append(Libro(titulo, autor, categoria))
        else:
            print("El libro ya existe.")

    def buscar_libro_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro


    def buscar_libro_autor(self, autor):


    def buscar_libro_categoria(self, categoria):


    def mostrar_libro(self, libro):


    # cargar los libros desde un archivo en formato csv separados por ;
    # gestionando las excepciones
    def cargar_libros(self):


    # grabar los libros desde un archivo en formato csv separados por ;
    # gestionando las excepciones
    def grabar_libros(self):


    # introduciendo el titulo original lo cambia por el titulo modificado
    def modificar_titulo(self, titulo_original, titulo_nuevo):



    def modificar_categoria(self, categoria_original, categoria_nuevo):



    def modificar_autor(self, autor_original, autor_nuevo):



    # Devuelve la cantidad de libros totales
    def cantidad_libros(self):



# si este es el main se ejecuta el siguiente codigo
if __name__ == "__main__":
    l1=Libreria()
    opcion = 0
    while opcion != 8:
        print("1. Cargar Libros")
        print("2. Grabar Libros")
        print("3. Introducir Libros")
        print("4. Modificar Libros")
        print("5. Eliminar Libro")
        print("6. Cantidad de libros registrados")
        print("7. Mostrar libros")
        print("8. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            l1.cargar_libros()
        elif opcion == 2:
            l1.grabar_libros()
        elif opcion == 3:
            l1.agregar_libro()
        elif opcion == 4: # modificar libro
            opcion_modificar = 0
            while opcion_modificar != 4:
                print("1. Modificar Titulo")
                print("2. Modificar Autor")
                print("3. Modificar Categoria")
                print("4. Salir")

            # —----------------
            # Falta código aquí
            # —----------------

        elif opcion == 5: # eliminar libro
            titulo = input("Ingrese el titulo del libro a eliminar: ")
            if l1.eliminar_libro(titulo):
                print("El libro se elimino correctamente")
            else:
                print("El libro no se pudo eliminar")
        elif opcion == 6: # cantidad de libros
            print("La cantidad de libros es: " + str(l1.cantidad_libros()))
        elif opcion == 7: # mostrar libros
            opcion_modificar = 0
            while opcion_modificar != 7:
                print("1. Todos los titulos")
                print("2. Todas las categorías")
                print("3. Todos los autores")
                print("4. Un título")
                print("5. Una categoría")
                print("6. Un autor")
                print("7. Salir")
                opcion_modificar = int(input("Ingrese una opcion: "))

            # —----------------
            # Falta código aquí
            # —----------------

        elif opcion == 8:
            print("Saliendo del programa")
        else:
            print("Opcion incorrecta")
