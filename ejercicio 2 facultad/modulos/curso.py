
class Curso:
    def __init__(self, nombre: str, codigo: str, profesor: str, capacidad: int) -> None:
        self.__nombre     = nombre
        self.__codigo     = codigo
        self.__profesor   = profesor
        self.__capacidad  = capacidad
        self.__inscriptos = []

    def getNombre(self)     -> str:  return self.__nombre
    def getCodigo(self)     -> str:  return self.__codigo
    def getProfesor(self)   -> str:  return self.__profesor
    def getCapacidad(self)  -> int:  return self.__capacidad
    def getInscriptos(self) -> list: return self.__inscriptos

    def getCuposDisponibles(self) -> int:
        return self.__capacidad - len(self.__inscriptos)

    def hayLugar(self) -> bool:
        return self.getCuposDisponibles() > 0

    def agregarEstudiante(self, estudiante) -> None:
        self.__inscriptos.append(estudiante)

    def quitarEstudiante(self, matricula: str) -> None:
        self.__inscriptos = [e for e in self.__inscriptos if e.getMatricula() != matricula]

    def __str__(self) -> str:
        return (f"Curso: {self.__nombre} | Código: {self.__codigo} "
                f"| Profesor: {self.__profesor} | Inscriptos: {len(self.__inscriptos)}"
                f"/{self.__capacidad} | Cupos libres: {self.getCuposDisponibles()}")
