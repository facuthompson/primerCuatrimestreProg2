class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str) -> None:
        self.__titulo   = titulo
        self.__autor    = autor
        self.__isbn     = isbn
        self.__prestado = False

    def getTitulo(self) -> str:   return self.__titulo
    def getAutor(self)  -> str:   return self.__autor
    def getIsbn(self)   -> str:   return self.__isbn
    def getPrestado(self) -> bool: return self.__prestado

    def setPrestado(self, estado: bool) -> None:
        self.__prestado = estado

    def __str__(self) -> str:
        estado = "Prestado" if self.__prestado else "Disponible"
        return (f"Título: {self.__titulo} | Autor: {self.__autor} "
                f"| ISBN: {self.__isbn} | Estado: {estado}")
