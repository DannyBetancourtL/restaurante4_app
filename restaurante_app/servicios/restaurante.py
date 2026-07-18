"""Modulo que contiene la clase de servicio Restaurante."""

from typing import List, Optional, Tuple

from modelos.producto import Producto
from modelos.cliente import Cliente
from modelos.orden import Orden


class Restaurante:
    """Servicio encargado de administrar productos, clientes y ordenes.

    Mantiene una unica coleccion de productos (que admite tanto objetos
    Producto como objetos Bebida, gracias al polimorfismo), una
    coleccion independiente de clientes y una coleccion de ordenes.
    Se encarga de las validaciones de registro, de la generacion
    automatica de codigos y del listado de la informacion.
    """

    def __init__(self, nombre: str = "Restaurante Sabor Lojano") -> None:
        self.nombre: str = nombre
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []
        self._ordenes: List[Orden] = []
        self._contador_producto: int = 0
        self._contador_orden: int = 0

    # ---------------------- Gestion de productos ----------------------

    def generar_codigo_producto(self) -> str:
        """Genera automaticamente el siguiente codigo de producto."""
        self._contador_producto += 1
        return str(self._contador_producto)

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un Producto o Bebida si su codigo no esta repetido.

        Devuelve True si el registro fue exitoso, False si el codigo
        ya existia.
        """
        if self._buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self) -> List[str]:
        """Devuelve la informacion de todos los productos registrados.

        """
        return [producto.mostrar_informacion() for producto in self._productos]

    def obtener_producto(self, codigo: str) -> Optional[Producto]:
        """Devuelve el producto con el codigo indicado, o None si no existe."""
        return self._buscar_producto(codigo)

    def _buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    # ----------------------- Gestion de clientes -----------------------

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un Cliente si su identificacion no esta repetida.

        Devuelve True si el registro fue exitoso, False si la
        identificacion ya existia.
        """
        if self._buscar_cliente(cliente.identificacion) is not None:
            return False
        self._clientes.append(cliente)
        return True

    def listar_clientes(self) -> List[str]:
        """Devuelve la informacion de todos los clientes registrados."""
        return [cliente.mostrar_informacion() for cliente in self._clientes]

    def obtener_cliente(self, identificacion: str) -> Optional[Cliente]:
        """Devuelve el cliente con la identificacion indicada, o None."""
        return self._buscar_cliente(identificacion)

    def _buscar_cliente(self, identificacion: str) -> Optional[Cliente]:
        for cliente in self._clientes:
            if cliente.identificacion == identificacion:
                return cliente
        return None

    # ------------------------ Gestion de ordenes ------------------------

    def generar_numero_orden(self) -> str:
        """Genera automaticamente el siguiente numero de orden."""
        self._contador_orden += 1
        return str(self._contador_orden)

    def tomar_orden(
        self, identificacion_cliente: str, items: List[Tuple[str, int]]
    ) -> Optional[Orden]:
        """Crea y registra una orden para un cliente existente.

        """
        cliente = self._buscar_cliente(identificacion_cliente)
        if cliente is None:
            return None

        orden = Orden(self.generar_numero_orden(), cliente)
        for codigo, cantidad in items:
            producto = self._buscar_producto(codigo)
            if producto is None or not producto.disponible or cantidad <= 0:
                return None
            orden.agregar_item(producto, cantidad)

        if not orden.detalle:
            return None

        self._ordenes.append(orden)
        return orden

    def listar_ordenes(self) -> List[str]:
        """Devuelve la informacion de todas las ordenes registradas."""
        return [orden.mostrar_informacion() for orden in self._ordenes]
