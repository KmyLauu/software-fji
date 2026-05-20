from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import *
from logs import registrar_log


print("\n===== SISTEMA SOFTWARE FJ =====\n")


# OPERACIÓN 1
try:

    cliente1 = Cliente("Laura", "laura@gmail.com")

    sala1 = ReservaSala("Sala VIP", 50000)

    costo = sala1.calcular_costo(3)

    reserva1 = Reserva(cliente1, sala1)

    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

    print(f"Costo total: {costo}")

    registrar_log("Reserva realizada correctamente")

except Exception as error:

    print(error)

    registrar_log(str(error))

finally:

    print("Operación finalizada\n")


# OPERACIÓN 2
try:

    cliente2 = Cliente("", "correo@gmail.com")

except ClienteError as error:

    print("Error:", error)

    registrar_log(str(error))


# OPERACIÓN 3
try:

    cliente3 = Cliente("Carlos", "correoinvalido")

except ClienteError as error:

    print("Error:", error)

    registrar_log(str(error))


# OPERACIÓN 4
try:

    equipo = AlquilerEquipo("Portátil", 80000)

    print("Costo equipo:", equipo.calcular_costo(2))

except Exception as error:

    print(error)

    registrar_log(str(error))


# OPERACIÓN 5
try:

    equipo2 = AlquilerEquipo("VideoBeam", 60000)

    print(equipo2.calcular_costo(-1))

except ServicioError as error:

    print("Error:", error)

    registrar_log(str(error))


# OPERACIÓN 6
try:

    asesoria = Asesoria("Asesoría Python", 100000)

    print("Costo asesoría:", asesoria.calcular_costo(2))

except Exception as error:

    print(error)

    registrar_log(str(error))


# OPERACIÓN 7
try:

    asesoria2 = Asesoria("Asesoría Java", 120000)

    print(asesoria2.calcular_costo(0))

except ServicioError as error:

    print("Error:", error)

    registrar_log(str(error))


# OPERACIÓN 8
try:

    reserva_error = Reserva(None, sala1)

except ReservaError as error:

    print("Error:", error)

    registrar_log(str(error))


# OPERACIÓN 9
try:

    numero = int("hola")

except ValueError as error:

    nuevo_error = ServicioError("Error al convertir el dato")

    print(nuevo_error)

    registrar_log(str(nuevo_error))


# OPERACIÓN 10
try:

    cliente10 = Cliente("María", "maria@gmail.com")

    sala10 = ReservaSala("Sala Ejecutiva", 70000)

    reserva10 = Reserva(cliente10, sala10)

    reserva10.cancelar()

    print(reserva10.mostrar_reserva())

    registrar_log("Reserva cancelada correctamente")

except Exception as error:

    print(error)

    registrar_log(str(error))
