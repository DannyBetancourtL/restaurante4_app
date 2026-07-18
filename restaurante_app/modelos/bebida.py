"""Modulo que contiene la clase Bebida, especializacion de Producto."""

from modelos.producto import Producto


class Bebida(Producto):
    """Representa una bebida del restaurante.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        tipo_envase: str,
        disponible: bool = True,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio, disponible)
        self.tamano: str = tamano
        self.tipo_envase: str = tipo_envase

    def mostrar_informacion(self) -> str:
        """Devuelve la informacion del producto extendida con datos de bebida."""
        info_base = super().mostrar_informacion()
        return (
            f"{info_base} | Tamaño: {self.tamano} | Envase: {self.tipo_envase}"
        )
