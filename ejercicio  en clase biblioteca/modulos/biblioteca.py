from modulos.libro import Libro
from modulos.miembro import Miembro


class BibliotecaError(Exception):
    pass


class Biblioteca:
    def __init__(self) -> None:
        self.__libros:   list[Libro]   = []
        self.__miembros: list[Miembro] = []


    def buscarLibro(self, isbn: str) -> Libro | None:
        return next((l for l in self.__libros if l.getIsbn() == isbn), None)

    def buscarMiembro(self, dni: str) -> Miembro | None:
        return next((m for m in self.__miembros if m.getDni() == dni), None)


    def agregarLibro(self, libro: Libro) -> None:
        if self.buscarLibro(libro.getIsbn()):
            raise BibliotecaError(f"Ya existe un libro con ISBN {libro.getIsbn()}.")
        self.__libros.append(libro)

    def agregarMiembro(self, miembro: Miembro) -> None:
        if self.buscarMiembro(miembro.getDni()):
            raise BibliotecaError(f"Ya existe un miembro con registrado con ese DNI {miembro.getDni()}.")
        self.__miembros.append(miembro)


    def getLibros(self) -> None:
        if not self.__libros:
            print("No hay libros registrados.")
            return
        for libro in self.__libros:
            print(f"  {libro}")

    def getMiembros(self) -> None:
        if not self.__miembros:
            print("No hay miembros registrados.")
            return
        for miembro in self.__miembros:
            print(f"  {miembro}")


    def prestarLibro(self, isbn: str, dni: str) -> None:
        libro   = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        if libro is None:
            raise BibliotecaError("Libro no encontrado.")
        if miembro is None:
            raise BibliotecaError("Miembro no encontrado.")
        if libro.getPrestado():
            raise BibliotecaError(f"El libro '{libro.getTitulo()}' ya está prestado.")

        libro.setPrestado(True)
        miembro.agregarLibro(libro)
        print(f"Libro '{libro.getTitulo()}' prestado a {miembro.getNombre()}.")

    def devolverLibro(self, isbn: str, dni: str) -> None:
        libro   = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        if libro is None:
            raise BibliotecaError("Libro no encontrado.")
        if miembro is None:
            raise BibliotecaError("Miembro no encontrado.")
        if not libro.getPrestado():
            raise BibliotecaError(f"El libro '{libro.getTitulo()}' no está prestado.")

        libro.setPrestado(False)
        miembro.quitarLibro(isbn)
        print(f"El libro '{libro.getTitulo()}' lo devolvio {miembro.getNombre()} gracias por venir.")


    def consultaEstadoLibro(self, isbn: str) -> None:
        libro = self.buscarLibro(isbn)
        if libro is None:
            print("No encontramos ese libro.")
            return

        if libro.getPrestado():
            for miembro in self.__miembros:
                if any(l.getIsbn() == isbn for l in miembro.getLibros()):
                    print(f"El libro '{libro.getTitulo()}' está prestado a "
                        f"{miembro.getNombre()} (DNI: {miembro.getDni()}).")
                    return
            print(f"El libro '{libro.getTitulo()}' está prestado (miembro no identificado).")
        else:
            print(f"El libro '{libro.getTitulo()}' está disponible.")

    def consultaLibrosMiembro(self, dni: str) -> None:
        miembro = self.buscarMiembro(dni)
        if miembro is None:
            print("No se encontró el miembro.")
            return

        libros = miembro.getLibros()
        if not libros:
            print(f"{miembro.getNombre()} no tiene libros prestados actualmente.")
            return

        print(f"Libros prestados a {miembro.getNombre()}:")
        for libro in libros:
            print(f"  {libro}")
