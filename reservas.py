
from entidades import Entidad
from cliente import Cliente
from servicios import Servicio


class Reserva(Entidad):
    """
    Clase que administra las reservas del sistema Software FJ.
    Integra clientes, servicios, duración y estado.
    """

    def __init__(self, identificacion, cliente, servicio, duracion):
        super().__init__(identificacion)

        if not isinstance(cliente, Cliente):
            raise TypeError("Debe proporcionar un cliente válido.")

        if not isinstance(servicio, Servicio):
            raise TypeError("Debe proporcionar un servicio válido.")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        self.validar()

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def validar(self):
        """Verifica que los datos de la reserva sean correctos."""

        self.__cliente.validar()
        self.__servicio.validar()

        if self.__duracion <= 0:
            raise ValueError("La duración no es válida.")

        return True

    def calcular_total(self, impuesto=0, descuento=0):
        """Calcula el costo de la reserva según el servicio."""

        if impuesto < 0 or descuento < 0:
            raise ValueError("Los valores no pueden ser negativos.")

        if impuesto > 100 or descuento > 100:
            raise ValueError("Los porcentajes no pueden superar el 100.")

        costo = self.__servicio.calcular_costo(
            impuesto, descuento
        )

        return round(costo * self.__duracion, 2)

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "Pendiente":
            raise ValueError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"
        return "La reserva fue confirmada correctamente."

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.__estado == "Cancelada":
            raise ValueError("La reserva ya está cancelada.")

        self.__estado = "Cancelada"
        return "La reserva fue cancelada correctamente."

    def procesar(self):
        """Procesa una reserva y calcula su costo."""

        try:
            self.validar()

            if self.__estado == "Cancelada":
                raise ValueError(
                    "No se puede procesar una reserva cancelada."
                )

            if self.__estado == "Pendiente":
                self.confirmar()

            total = self.calcular_total()

            return (
                f"Reserva procesada correctamente.\n"
                f"Cliente: {self.__cliente.nombre}\n"
                f"Servicio: {self.__servicio.nombre}\n"
                f"Duración: {self.__duracion}\n"
                f"Estado: {self.__estado}\n"
                f"Total: ${total:,.2f}"
            )

        except (ValueError, TypeError):
            raise

    def mostrar_informacion(self):
        """Muestra los datos principales de la reserva."""

        return (
            f"Reserva: {self.identificacion}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}"
        )
