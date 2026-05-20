from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas=1):

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        return self.precio * horas

    def descripcion(self):

        return "Reserva de salas empresariales"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias=1):

        if dias <= 0:
            raise ServicioError("Los días no son válidos")

        return self.precio * dias

    def descripcion(self):

        return "Alquiler de equipos tecnológicos"


class Asesoria(Servicio):

    def calcular_costo(self, sesiones=1):

        if sesiones <= 0:
            raise ServicioError("Cantidad inválida")

        return self.precio * sesiones

    def descripcion(self):

        return "Asesorías especializadas"
