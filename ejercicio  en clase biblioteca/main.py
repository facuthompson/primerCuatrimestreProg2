from biblioteca import Biblioteca, BibliotecaError
from libro import Libro
from miembro import Miembro


def mostrarMenu() -> None:
    print(
        "\n"
        " 0: Salir\n"
        " 1: Agregar Libro\n"
        " 2: Agregar Miembro\n"
        " 3: Mostrar Libros\n"
        " 4: Mostrar Miembros\n"
        " 5: Prestar Libro\n"
        " 6: Devolver Libro\n"
        " 7: Consultar Estado de un Libro\n"
        " 8: Consultar Libros de un Miembro\n"
    )


def pedirOpcion() -> int:
    while True:
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: ingresa un número del menu de opciones.")


def pedirTexto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: el campo no puede estar vacío, por favor volve a intentarlo.")


def validar_isbn(isbn: str) -> bool:
    return isbn.isdigit() and len(isbn) in (10, 13)


def main() -> None:
    biblioteca = Biblioteca()
    mostrarMenu()
    opcion = pedirOpcion()
    while opcion != 0:

        if opcion == 1:
            titulo = pedirTexto("Título del libro: ")
            autor  = pedirTexto("Autor del libro: ")
            while True:
                isbn = pedirTexto("ISBN del libro: ")
                if validar_isbn(isbn):
                    break
                print("Error: el ISBN debe tener 10 o 13 dígitos numéricos, intenta nuevamente.")
            try:
                biblioteca.agregarLibro(Libro(titulo, autor, isbn))
                print("El Libro se agrego correctamente.")
            except BibliotecaError as e:
                print(f"Error: {e}")

        elif opcion == 2:
            dni    = pedirTexto("DNI del miembro: ")
            nombre = pedirTexto("Nombre del miembro: ")
            try:
                biblioteca.agregarMiembro(Miembro(dni, nombre))
                print("el nuevo miembro se agrego correctamente.")
            except BibliotecaError as e:
                print(f"Error: {e}")

        elif opcion == 3:
            biblioteca.getLibros()

        elif opcion == 4:
            biblioteca.getMiembros()

        elif opcion == 5:
            dni  = pedirTexto("DNI del miembro: ")
            isbn = pedirTexto("ISBN del libro: ")
            try:
                biblioteca.prestarLibro(isbn, dni)
            except BibliotecaError as e:
                print(f"Error: {e}")

        elif opcion == 6:
            isbn = pedirTexto("ISBN del libro: ")
            dni  = pedirTexto("DNI del miembro: ")
            try:
                biblioteca.devolverLibro(isbn, dni)
            except BibliotecaError as e:
                print(f"Error: {e}")

        elif opcion == 7:
            isbn = pedirTexto("ISBN del libro: ")
            biblioteca.consultaEstadoLibro(isbn)

        elif opcion == 8:
            dni = pedirTexto("DNI del miembro: ")
            biblioteca.consultaLibrosMiembro(dni)

        else:
            print("Opción inválida. Intenta nuevamente.")

        mostrarMenu()
        opcion = pedirOpcion()

    print("\nFin del programa.")


if __name__ == "__main__":
    main()
