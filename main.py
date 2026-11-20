
from cliente import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reservas import Reserva
from excepciones import (
    registrar_evento,
    registrar_error,
    registrar_excepcion,
    validar_cliente,
    validar_servicio,
    validar_reserva
)


def ejecutar_simulaciones():
    print("=" * 55)
    print(" SISTEMA SOFTWARE FJ - GESTION DE RESERVAS")
    print("=" * 55)

    registrar_evento("Inicio de las simulaciones del sistema.")

    # SIMULACION 1: Crear un cliente válido
    print("\nSIMULACION 1: Registro de cliente válido")

    try:
        cliente1 = Cliente(
            "1001",
            "Miguel Bustillo",
            "miguel@gmail.com",
            "3001234567"
        )

        validar_cliente(cliente1)
        print(cliente1.mostrar_informacion())

    except Exception as error:
        print("Error:", error)
        registrar_excepcion("Error en simulación 1")

    # SIMULACION 2: Registrar un cliente con correo inválido
    print("\nSIMULACION 2: Cliente con correo inválido")

    try:
        cliente2 = Cliente(
            "1002",
            "Carlos Perez",
            "correo_incorrecto",
            "3001234568"
        )

    except ValueError as error:
        print("Error controlado:", error)
        registrar_error(str(error))

    # SIMULACION 3: Crear una reserva de sala válida
    print("\nSIMULACION 3: Reserva de sala")

    try:
        sala = ReservaSala(
            "S01", "Sala de reuniones", 100000, 20
        )

        validar_servicio(sala)
        print(sala.describir())
        print("Costo:", sala.calcular_costo(19, 5))

    except Exception as error:
        print("Error:", error)
        registrar_excepcion("Error en simulación 3")

    # SIMULACION 4: Crear una sala con capacidad inválida
    print("\nSIMULACION 4: Capacidad de sala inválida")

    try:
        sala_invalida = ReservaSala(
            "S02", "Sala pequeña", 80000, 0
        )

    except ValueError as error:
        print("Error controlado:", error)
        registrar_error(str(error))

    # SIMULACION 5: Alquiler de equipos
    print("\nSIMULACION 5: Alquiler de equipos")

    try:
        equipo = AlquilerEquipo(
            "E01", "Computadores", 50000, 3
        )

        validar_servicio(equipo)
        print(equipo.describir())
        print("Costo:", equipo.calcular_costo(19, 0))

    except Exception as error:
        print("Error:", error)
        registrar_excepcion("Error en simulación 5")

    # SIMULACION 6: Asesoría especializada
    print("\nSIMULACION 6: Asesoría especializada")

    try:
        asesoria = AsesoriaEspecializada(
            "A01", "Asesoría técnica", 60000, 2
        )

        validar_servicio(asesoria)
        print(asesoria.describir())
        print("Costo:", asesoria.calcular_costo())

    except Exception as error:
        print("Error:", error)
        registrar_excepcion("Error en simulación 6")

    # SIMULACION 7: Asesoría con horas inválidas
    print("\nSIMULACION 7: Horas de asesoría inválidas")

    try:
        asesoria_invalida = AsesoriaEspecializada(
            "A02", "Asesoría especial", 50000, 0
        )

    except ValueError as error:
        print("Error controlado:", error)
        registrar_error(str(error))

    # SIMULACION 8: Crear y procesar una reserva válida
    print("\nSIMULACION 8: Procesamiento de reserva")

    try:
        reserva1 = Reserva(
            "R001", cliente1, sala, 2
        )

        validar_reserva(reserva1)
        print(reserva1.procesar())

    except Exception as error:
        print("Error:", error)
        registrar_excepcion("Error en simulación 8")

    # SIMULACION 9: Intentar procesar una reserva cancelada
    print("\nSIMULACION 9: Procesar reserva cancelada")

    try:
        reserva2 = Reserva(
            "R002", cliente1, equipo, 1
        )

        reserva2.cancelar()
        print(reserva2.procesar())

    except ValueError as error:
        print("Error controlado:", error)
        registrar_error(str(error))

    # SIMULACION 10: Crear una reserva con duración inválida
    print("\nSIMULACION 10: Duración inválida")

    try:
        reserva3 = Reserva(
            "R003", cliente1, asesoria, 0
        )

    except ValueError as error:
        print("Error controlado:", error)
        registrar_error(str(error))

    # Ejemplo de encadenamiento de excepciones
    print("\nPRUEBA ADICIONAL: Encadenamiento de excepciones")

    try:
        try:
            int("dato incorrecto")

        except ValueError as error:
            raise RuntimeError(
                "No fue posible convertir el dato."
            ) from error

    except RuntimeError as error:
        print("Excepción encadenada:", error)
        registrar_excepcion("Prueba de encadenamiento")

    # Cierre del programa
    registrar_evento("Finalizaron las diez simulaciones.")

    print("\n" + "=" * 55)
    print("SIMULACIONES FINALIZADAS")
    print("El sistema continúa funcionando ante los errores.")
    print("Revise software_fj.log para consultar los registros.")
    print("=" * 55)


if __name__ == "__main__":
    ejecutar_simulaciones()
