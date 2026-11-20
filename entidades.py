
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades generales
    del sistema Software FJ.
    """

    def __init__(self, identificacion):
        # Validar que la identificación no esté vacía
        if not identificacion:
            raise ValueError("La identificación es obligatoria.")

        self.__identificacion = identificacion

    @property
    def identificacion(self):
        # Permite consultar la identificación
        return self.__identificacion

    @abstractmethod
    def validar(self):
        # Cada clase hija debe implementar sus validaciones
        pass

    @abstractmethod
    def mostrar_informacion(self):
        # Cada clase hija debe mostrar su información
        pass
