from datetime import datetime


def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        fecha = datetime.now()

        archivo.write(f"{fecha} -> {mensaje}\n")
