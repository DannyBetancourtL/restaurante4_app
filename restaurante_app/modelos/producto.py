"""Modulo que contiene la clase base Producto."""


class Producto:
    """Representa un producto general del restaurante.

    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        disponible: bool = True,
    ) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio
        self.disponible: bool = disponible

    def mostrar_informacion(self) -> str:
        """Devuelve una cadena con la informacion basica del producto."""
        return (
            f"Código: {self.codigo} | Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | Disponible: {self.disponible}"
        )
