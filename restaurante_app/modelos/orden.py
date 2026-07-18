"""Modulo que contiene la clase Orden."""

from typing import List, Tuple

from modelos.producto import Producto
from modelos.cliente import Cliente


class Orden:
    """Representa una orden (pedido) realizada por un cliente.

    """

    def __init__(self, numero: str, cliente: Cliente) -> None:
        self.numero: str = numero
        self.cliente: Cliente = cliente
        self.detalle: List[Tuple[Producto, int]] = []

    def agregar_item(self, producto: Producto, cantidad: int) -> None:
        """Agrega un producto con su cantidad al detalle de la orden."""
        self.detalle.append((producto, cantidad))

    def calcular_total(self) -> float:
        """Calcula el total de la orden sumando precio * cantidad de cada item."""
        return sum(producto.precio * cantidad for producto, cantidad in self.detalle)

    def mostrar_informacion(self) -> str:
        """Devuelve una cadena con el resumen de la orden."""
        encabezado = (
            f"Orden N°: {self.numero} | Cliente: {self.cliente.nombre} "
            f"({self.cliente.identificacion})"
        )
        lineas = [encabezado]
        for producto, cantidad in self.detalle:
            subtotal = producto.precio * cantidad
            lineas.append(
                f"    - {producto.nombre} x{cantidad} = ${subtotal:.2f}"
            )
        lineas.append(f"    Total: ${self.calcular_total():.2f}")
        return "\n".join(lineas)
