
import logging


# Configuración del archivo donde se guardarán los registros
logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("SoftwareFJ")


class ErrorSoftwareFJ(Exception):
    """Excepción general del sistema Software FJ."""
    pass


class ClienteInvalidoError(ErrorSoftwareFJ):
    """Se genera cuando los datos del cliente no son válidos."""
    pass


class ServicioInvalidoError(ErrorSoftwareFJ):
    """Se genera cuando un servicio presenta datos incorrectos."""
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Se genera cuando una reserva no cumple las condiciones."""
    pass


def registrar_evento(mensaje):
    """Registra un evento informativo en el archivo de logs."""

    logger.info(mensaje)


def registrar_advertencia(mensaje):
    """Registra una advertencia del sistema."""

    logger.warning(mensaje)


def registrar_error(mensaje):
    """Registra un error sin detener la aplicación."""

    logger.error(mensaje)


def registrar_excepcion(mensaje):
    """Registra una excepción con información del error."""

    logger.exception(mensaje)


def validar_cliente(cliente):
    """Comprueba que el objeto recibido sea un cliente válido."""

    try:
        if cliente is None:
            raise ClienteInvalidoError(
                "No se recibió información del cliente."
            )

        cliente.validar()

    except ClienteInvalidoError as error:
        registrar_error(str(error))
        raise

    except Exception as error:
        registrar_error(
            f"Error al validar el cliente: {error}"
        )

        raise ClienteInvalidoError(
            "No fue posible validar el cliente."
        ) from error

    else:
        registrar_evento("Cliente validado correctamente.")
        return True

    finally:
        registrar_evento(
            "Finalizó el proceso de validación del cliente."
        )


def validar_servicio(servicio):
    """Comprueba que el servicio recibido sea válido."""

    try:
        if servicio is None:
            raise ServicioInvalidoError(
                "No se recibió información del servicio."
            )

        servicio.validar()

    except ServicioInvalidoError as error:
        registrar_error(str(error))
        raise

    except Exception as error:
        registrar_error(
            f"Error al validar el servicio: {error}"
        )

        raise ServicioInvalidoError(
            "No fue posible validar el servicio."
        ) from error

    else:
        registrar_evento("Servicio validado correctamente.")
        return True

    finally:
        registrar_evento(
            "Finalizó el proceso de validación del servicio."
        )


def validar_reserva(reserva):
    """Comprueba que la reserva recibida sea válida."""

    try:
        if reserva is None:
            raise ReservaInvalidaError(
                "No se recibió información de la reserva."
            )

        reserva.validar()

    except ReservaInvalidaError as error:
        registrar_error(str(error))
        raise

    except Exception as error:
        registrar_error(
            f"Error al validar la reserva: {error}"
        )

        raise ReservaInvalidaError(
            "No fue posible validar la reserva."
        ) from error

    else:
        registrar_evento("Reserva validada correctamente.")
        return True

    finally:
        registrar_evento(
            "Finalizó el proceso de validación de la reserva."
        )
