
from modulos.estudiante import Estudiante
from modulos.curso import Curso


class FacultadError(Exception):
    pass


class Facultad:

    def __init__(self) -> None:
        self.__estudiantes: list[Estudiante] = []
        self.__cursos: list[Curso] = []


    def buscarEstudiante(self, matricula: str) -> Estudiante | None:
        return next((e for e in self.__estudiantes if e.getMatricula() == matricula), None)

    def buscarCurso(self, codigo: str) -> Curso | None:
        return next((c for c in self.__cursos if c.getCodigo() == codigo), None)


    def agregarEstudiante(self, estudiante: Estudiante) -> None:
        if self.buscarEstudiante(estudiante.getMatricula()):
            raise FacultadError(f"Ya existe el estudiante con matrícula {estudiante.getMatricula()}.")
        self.__estudiantes.append(estudiante)

    def agregarCurso(self, curso: Curso) -> None:
        if self.buscarCurso(curso.getCodigo()):
            raise FacultadError(f"Ya existe el curso con código {curso.getCodigo()}.")
        self.__cursos.append(curso)


    def inscribir(self, matricula: str, codigo: str) -> None:
        estudiante = self.buscarEstudiante(matricula)
        curso      = self.buscarCurso(codigo)

        if estudiante is None:
            raise FacultadError("Estudiante no encontrado.")
        if curso is None:
            raise FacultadError("Curso no encontrado.")
        if any(c.getCodigo() == codigo for c in estudiante.getCursos()):
            raise FacultadError(f"{estudiante.getNombreCompleto()} ya está inscripto en '{curso.getNombre()}'.")
        if not curso.hayLugar():
            raise FacultadError(f"El curso '{curso.getNombre()}' no tiene cupos disponibles.")

        curso.agregarEstudiante(estudiante)
        estudiante.inscribirCurso(curso)
        print(f"{estudiante.getNombreCompleto()} inscripto en '{curso.getNombre()}'.")

    def darBaja(self, matricula: str, codigo: str) -> None:
        estudiante = self.buscarEstudiante(matricula)
        curso      = self.buscarCurso(codigo)

        if estudiante is None:
            raise FacultadError("Estudiante no encontrado.")
        if curso is None:
            raise FacultadError("Curso no encontrado.")
        if not any(c.getCodigo() == codigo for c in estudiante.getCursos()):
            raise FacultadError(f"{estudiante.getNombreCompleto()} no está inscripto en '{curso.getNombre()}'.")

        curso.quitarEstudiante(matricula)
        estudiante.darBajaCurso(codigo)
        print(f"{estudiante.getNombreCompleto()} dado de baja de '{curso.getNombre()}'.")


    def mostrarCursos(self) -> None:
        if not self.__cursos:
            print("No hay cursos registrados.")
            return
        for curso in self.__cursos:
            print(f"  {curso}")

    def mostrarEstudiantes(self) -> None:
        if not self.__estudiantes:
            print("No hay estudiantes registrados.")
            return
        for estudiante in self.__estudiantes:
            print(f"  {estudiante}")
