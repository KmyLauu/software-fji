from excepciones import ClienteError


class Cliente:

    def __init__(self, nombre, correo):

        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ClienteError("El correo no es válido")

        self.__nombre = nombre
        self.__correo = correo

    def obtener_nombre(self):
        return self.__nombre

    def obtener_correo(self):
        return self.__correo

    def mostrar_info(self):

        return f"""
Nombre: {self.__nombre}
Correo: {self.__correo}
"""
