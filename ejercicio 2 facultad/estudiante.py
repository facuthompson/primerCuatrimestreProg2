
class Estudiante:

    def __init__(self, nombre: str, apellido: str, matricula: str, carrera: str) -> None:
        self.__nombre    = nombre
        self.__apellido  = apellido
        self.__matricula = matricula
        self.__carrera   = carrera
        self.__cursos    = []

    def getNombre(self)    -> str: return self.__nombre
    def getApellido(self)  -> str: return self.__apellido
    def getMatricula(self) -> str: return self.__matricula
    def getCarrera(self)   -> str: return self.__carrera
    def getCursos(self)    -> list: return self.__cursos

    def getNombreCompleto(self) -> str:
        return f"{self.__nombre} {self.__apellido}"

    def inscribirCurso(self, curso) -> None:
        self.__cursos.append(curso)

    def darBajaCurso(self, codigo: str) -> None:
        self.__cursos = [c for c in self.__cursos if c.getCodigo() != codigo]

    def __str__(self) -> str:
        nombres_cursos = ", ".join(c.getNombre() for c in self.__cursos) or "Ninguno"
        return (f"Nombre: {self.getNombreCompleto()} | Matrícula: {self.__matricula} "
                f"| Carrera: {self.__carrera} | Cursos: {nombres_cursos}")
