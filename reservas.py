from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio):

        if cliente is None:
            raise ReservaError("El cliente no existe")

        if servicio is None:
            raise ReservaError("El servicio no existe")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

    def cancelar(self):

        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return f"""
╔════════════════════════════╗
        RESERVA GENERADA
╠════════════════════════════╣

👤 Cliente:
{self.cliente.obtener_nombre()}

🛠️ Servicio:
{self.servicio.descripcion()}

📌 Estado:
{self.estado}

╚════════════════════════════╝
"""
