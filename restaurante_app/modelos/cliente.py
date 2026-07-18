"""Modulo que contiene la clase Cliente."""


class Cliente:
    """Representa a un cliente registrado en el restaurante.

    """

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        edad: int,
        cliente_frecuente: bool = False,
    ) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo
        self.edad: int = edad
        self.cliente_frecuente: bool = cliente_frecuente

    def mostrar_informacion(self) -> str:
        """Devuelve una cadena con la informacion del cliente."""
        return (
            f"Identificación: {self.identificacion} | Nombre: {self.nombre} | "
            f"Edad: {self.edad} | Cliente frecuente: {self.cliente_frecuente}"
        )
