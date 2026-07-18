""" Sistema de Restaurante.
Trabajo realizado por: Danny Betancourt
Este sistema restaurante_app utilizando Programación Orientada a Objetos en Python.
El sistema deberá permitir registrar y listar productos, bebidas y clientes 
mediante un menú interactivo ejecutado desde consola.
"""

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_encabezado(restaurante: Restaurante) -> None:
    """Imprime el encabezado con el nombre del restaurante."""
    print("=" * 35)
    print(" SISTEMA DE GESTIÓN DE RESTAURANTES ")
    print("=" * 35)
    print(f"Nombre: {restaurante.nombre}")


def cargar_datos_iniciales(restaurante: Restaurante) -> None:
    """Precarga productos y clientes de ejemplo en el sistema."""
    restaurante.registrar_producto(
        Producto(restaurante.generar_codigo_producto(), "Humitas", "Comida", 1.50, disponible=True)
    )
    restaurante.registrar_producto(
        Producto(restaurante.generar_codigo_producto(), "Jugo de tomate", "Bebida", 1.50, disponible=True)
    )
    restaurante.registrar_cliente(
        Cliente("1101234567", "Danny Betancourt", "danny@correo.com", 40, cliente_frecuente=True)
    )
    restaurante.registrar_cliente(
        Cliente("1107654321", "Carlos Pérez", "carlos@correo.com", 31, cliente_frecuente=False)
    )


def mostrar_menu() -> None:
    """Imprime el menu principal del sistema."""
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE SABOR LOJANO")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Tomar orden")
    print("7. Listar órdenes")
    print("-" * 40)
    print("8. Salir")


def solicitar_float(mensaje: str) -> float:
    """Solicita un numero decimal al usuario validando la entrada."""
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("Valor invalido. Ingrese un numero (ej: 4.50).")


def solicitar_entero(mensaje: str) -> int:
    """Solicita un numero entero al usuario validando la entrada."""
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print("Valor invalido. Ingrese un numero entero (ej: 25).")


def solicitar_bool(mensaje: str) -> bool:
    """Solicita una respuesta s/n al usuario y la convierte a booleano."""
    while True:
        valor = input(mensaje).strip().lower()
        if valor in ("s", "si", "sí"):
            return True
        if valor in ("n", "no"):
            return False
        print("Valor invalido. Responda 's' o 'n'.")


def registrar_producto(restaurante: Restaurante) -> None:
    """Solicita los datos de un producto y lo registra en el servicio.

    El codigo del producto se genera automaticamente, por lo que no se
    solicita al usuario.
    """
    print("\n--- Registrar producto ---")
    nombre: str = input("Nombre: ").strip()
    categoria: str = input("Categoria: ").strip()
    precio: float = solicitar_float("Precio: ")
    disponible: bool = solicitar_bool("Disponible (s/n): ")

    codigo: str = restaurante.generar_codigo_producto()
    producto = Producto(codigo, nombre, categoria, precio, disponible)
    restaurante.registrar_producto(producto)
    print(f"Producto registrado correctamente con el código '{codigo}'.\n")


def registrar_bebida(restaurante: Restaurante) -> None:
    """Solicita los datos de una bebida y la registra en el servicio.

    El codigo de la bebida se genera automaticamente, por lo que no se
    solicita al usuario.
    """
    print("\n--- Registrar bebida ---")
    nombre: str = input("Nombre: ").strip()
    categoria: str = input("Categoria: ").strip()
    precio: float = solicitar_float("Precio: ")
    tamano: str = input("Tamaño (ej: 350ml): ").strip()
    tipo_envase: str = input("Tipo de envase (ej: lata, vidrio, plastico): ").strip()
    disponible: bool = solicitar_bool("Disponible (s/n): ")

    codigo: str = restaurante.generar_codigo_producto()
    bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase, disponible)
    restaurante.registrar_producto(bebida)
    print(f"Bebida registrada correctamente con el código '{codigo}'.\n")


def registrar_cliente(restaurante: Restaurante) -> None:
    """Solicita los datos de un cliente y lo registra en el servicio."""
    print("\n--- Registrar cliente ---")
    identificacion: str = input("Identificacion: ").strip()
    nombre: str = input("Nombre: ").strip()
    correo: str = input("Correo: ").strip()
    edad: int = solicitar_entero("Edad: ")
    cliente_frecuente: bool = solicitar_bool("Cliente frecuente (s/n): ")

    cliente = Cliente(identificacion, nombre, correo, edad, cliente_frecuente)
    if restaurante.registrar_cliente(cliente):
        print("Cliente registrado correctamente.\n")
    else:
        print(f"Error: ya existe un cliente con la identificacion '{identificacion}'.\n")


def listar_productos(restaurante: Restaurante) -> None:
    """Muestra en consola todos los productos y bebidas registrados."""
    print("\nPRODUCTOS REGISTRADOS")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.\n")
        return
    for info in productos:
        print(info)
    print()


def listar_clientes(restaurante: Restaurante) -> None:
    """Muestra en consola todos los clientes registrados."""
    print("\nCLIENTES REGISTRADOS")
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    for info in clientes:
        print(info)
    print()


def tomar_orden(restaurante: Restaurante) -> None:
    """Solicita los datos de una orden y la registra en el servicio.

    Pide la identificacion del cliente y, en un bucle, los codigos y
    cantidades de los productos a pedir. El numero de orden se genera
    automaticamente.
    """
    print("\n--- Tomar orden ---")
    identificacion: str = input("Identificación del cliente: ").strip()

    if restaurante.obtener_cliente(identificacion) is None:
        print(f"Error: no existe un cliente con la identificación '{identificacion}'.\n")
        return

    listar_productos(restaurante)

    items: list[tuple[str, int]] = []
    while True:
        codigo: str = input("Código del producto (Enter para finalizar): ").strip()
        if codigo == "":
            break

        producto = restaurante.obtener_producto(codigo)
        if producto is None:
            print(f"No existe un producto con el código '{codigo}'.")
            continue
        if not producto.disponible:
            print(f"El producto '{producto.nombre}' no está disponible.")
            continue

        cantidad: int = solicitar_entero(f"Cantidad de '{producto.nombre}': ")
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            continue

        items.append((codigo, cantidad))

    if not items:
        print("No se agregaron productos. Orden cancelada.\n")
        return

    orden = restaurante.tomar_orden(identificacion, items)
    if orden is None:
        print("Error: no se pudo registrar la orden. Verifique cliente y productos.\n")
        return

    print("\nOrden registrada correctamente:")
    print(orden.mostrar_informacion())
    print()


def listar_ordenes(restaurante: Restaurante) -> None:
    """Muestra en consola todas las órdenes registradas."""
    print("\nÓRDENES REGISTRADAS")
    ordenes = restaurante.listar_ordenes()
    if not ordenes:
        print("No hay órdenes registradas.\n")
        return
    for info in ordenes:
        print(info)
        print()


def main() -> None:
    """Funcion principal que ejecuta el bucle del menu interactivo."""
    restaurante = Restaurante("Sabor Lojano")
    cargar_datos_iniciales(restaurante)
    mostrar_encabezado(restaurante)

    opciones = {
        "1": lambda: registrar_producto(restaurante),
        "2": lambda: registrar_bebida(restaurante),
        "3": lambda: registrar_cliente(restaurante),
        "4": lambda: listar_productos(restaurante),
        "5": lambda: listar_clientes(restaurante),
        "6": lambda: tomar_orden(restaurante),
        "7": lambda: listar_ordenes(restaurante),
    }

    while True:
        mostrar_menu()
        opcion: str = input("Seleccione una opcion: ").strip()

        if opcion == "8":
            print("\nGracias por usar el Sistema de Restaurante. ¡Hasta pronto!")
            break

        accion = opciones.get(opcion)
        if accion is None:
            print("\nOpcion invalida. Intente nuevamente.\n")
            continue

        accion()


if __name__ == "__main__":
    main()
