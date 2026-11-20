
from abc import abstractmethod
from entidades import Entidad


class Servicio(Entidad):
    """
    Clase abstracta que representa los servicios
    ofrecidos por Software FJ.
    """

    def __init__(self, identificacion, nombre, costo_base):
        super().__init__(identificacion)

        if not nombre or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if costo_base <= 0:
            raise ValueError("El costo debe ser mayor que cero.")

        self.__nombre = nombre.strip()
        self.__costo_base = costo_base

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_base(self):
        return self.__costo_base

    @abstractmethod
    def calcular_costo(self, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def validar(self):
        pass

    @abstractmethod
    def describir(self):
        pass

    def mostrar_informacion(self):
        return self.describir()


class ReservaSala(Servicio):
    """Servicio para reservar salas."""

    def __init__(self, identificacion, nombre, costo_base, capacidad):
        super().__init__(identificacion, nombre, costo_base)
        self.capacidad = capacidad
        self.validar()

    def validar(self):
        if self.capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")
        return True

    def calcular_costo(self, impuesto=0, descuento=0):
        total = self.costo_base + (self.costo_base * impuesto / 100)
        total -= total * descuento / 100
        return round(total, 2)

    def describir(self):
        return (
            f"Reserva de sala: {self.nombre}. "
            f"Capacidad: {self.capacidad} personas."
        )


class AlquilerEquipo(Servicio):
    """Servicio para alquilar equipos."""

    def __init__(self, identificacion, nombre, costo_base, cantidad):
        super().__init__(identificacion, nombre, costo_base)
        self.cantidad = cantidad
        self.validar()

    def validar(self):
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        return True

    def calcular_costo(self, impuesto=0, descuento=0):
        subtotal = self.costo_base * self.cantidad
        total = subtotal + (subtotal * impuesto / 100)
        total -= total * descuento / 100
        return round(total, 2)

    def describir(self):
        return (
            f"Alquiler de equipos: {self.nombre}. "
            f"Cantidad: {self.cantidad}."
        )


class AsesoriaEspecializada(Servicio):
    """Servicio de asesorías especializadas."""

    def __init__(self, identificacion, nombre, costo_base, horas):
        super().__init__(identificacion, nombre, costo_base)
        self.horas = horas
        self.validar()

    def validar(self):
        if self.horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")
        return True

    def calcular_costo(self, impuesto=0, descuento=0):
        subtotal = self.costo_base * self.horas
        total = subtotal + (subtotal * impuesto / 100)
        total -= total * descuento / 100
        return round(total, 2)

    def describir(self):
        return (
            f"Asesoría especializada: {self.nombre}. "
            f"Duración: {self.horas} horas."
        )
