
from facultad import Facultad, FacultadError
from estudiante import Estudiante
from curso import Curso


def mostrarMenu() -> None:
    print(
        "\n"
        " 0: Salir\n"
        " 1: Agregar Estudiante\n"
        " 2: Agregar Curso\n"
        " 3: Inscribir Estudiante a Curso\n"
        " 4: Dar Baja de Curso\n"
        " 5: Mostrar Todos los Cursos\n"
        " 6: Mostrar Todos los Estudiantes\n"
    )


def pedirOpcion() -> int:
    while True:
        try:
            return int(input("Selecciona una opción del munu: "))
        except ValueError:
            print("Error: ingrese un número válido en el menu de opciones.")


def pedirTexto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: el campo no puede estar vacío.")


def pedirEnteroPositivo(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: el número debe ser mayor a cero.")
        except ValueError:
            print("Error: ingrese un número entero válido.")


def main() -> None:
    facultad = Facultad()

    mostrarMenu()
    opcion = pedirOpcion()

    while opcion != 0:

        if opcion == 1:
            nombre    = pedirTexto("Nombre del estudiante: ")
            apellido  = pedirTexto("Apellido del estudiante: ")
            matricula = pedirTexto("Número de matrícula: ")
            carrera   = pedirTexto("Carrera: ")
            try:
                facultad.agregarEstudiante(Estudiante(nombre, apellido, matricula, carrera))
                print("Estudiante agregado correctamente.")
            except FacultadError as e:
                print(f"Error: {e}")

        elif opcion == 2:
            nombre    = pedirTexto("Nombre del curso: ")
            codigo    = pedirTexto("Código del curso: ")
            profesor  = pedirTexto("Profesor encargado: ")
            capacidad = pedirEnteroPositivo("Capacidad máxima de estudiantes: ")
            try:
                facultad.agregarCurso(Curso(nombre, codigo, profesor, capacidad))
                print("Curso agregado correctamente.")
            except FacultadError as e:
                print(f"Error: {e}")

        elif opcion == 3:
            matricula = pedirTexto("Matrícula del estudiante: ")
            codigo    = pedirTexto("Código del curso: ")
            try:
                facultad.inscribir(matricula, codigo)
            except FacultadError as e:
                print(f"Error: {e}")

        elif opcion == 4:
            matricula = pedirTexto("Matrícula del estudiante: ")
            codigo    = pedirTexto("Código del curso: ")
            try:
                facultad.darBaja(matricula, codigo)
            except FacultadError as e:
                print(f"Error: {e}")

        elif opcion == 5:
            facultad.mostrarCursos()

        elif opcion == 6:
            facultad.mostrarEstudiantes()

        else:
            print("Opción inválida. Intente nuevamente.")

        mostrarMenu()
        opcion = pedirOpcion()

    print("\nFin del programa.")


if __name__ == "__main__":
    main()
