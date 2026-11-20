
import re
from entidades import Entidad


class Cliente(Entidad):
    """
    Clase que representa a los clientes del sistema Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificacion, nombre, correo, telefono):
        # Inicializar los datos de la clase padre
        super().__init__(identificacion)

        # Validar que los datos no estén vacíos
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio.")

        if not correo or not correo.strip():
            raise ValueError("El correo electrónico es obligatorio.")

        if not telefono or not telefono.strip():
            raise ValueError("El teléfono es obligatorio.")

        # Encapsular los datos personales
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

        # Ejecutar las validaciones
        self.validar()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        # Validar que el nombre tenga al menos dos caracteres
        if len(self.__nombre) < 2:
            raise ValueError("El nombre debe tener al menos dos caracteres.")

        # Validar el formato del correo electrónico
        patron = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'

        if not re.match(patron, self.__correo):
            raise ValueError("El correo electrónico no es válido.")

        # Validar que el teléfono contenga entre 7 y 15 dígitos
        if not self.__telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números.")

        if not 7 <= len(self.__telefono) <= 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 dígitos.")

        return True

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
