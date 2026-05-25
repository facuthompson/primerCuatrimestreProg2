
from libro import Libro

class Miembro:
    def __init__(self, dni: str, nombre: str) -> None:
        self.__dni           = dni
        self.__nombre        = nombre
        self.__librosSacados: list[Libro] = []

    def getNombre(self) -> str: return self.__nombre
    def getDni(self)    -> str: return self.__dni

    def agregarLibro(self, libro: Libro) -> None:
        self.__librosSacados.append(libro)

    def quitarLibro(self, isbn: str) -> None:
        self.__librosSacados = [
            l for l in self.__librosSacados if l.getIsbn() != isbn
        ]

    def getLibros(self) -> list[Libro]:
        return self.__librosSacados

    def __str__(self) -> str:
        titulos = ", ".join(l.getTitulo() for l in self.__librosSacados) or "Ninguno"
        return (f"Miembro: {self.__nombre} | DNI: {self.__dni} "
                f"| Libros prestados: {titulos}")
