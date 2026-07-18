Sistema de Restaurante — restaurante_app

              SABOR LOJANO

Estudiante: DANNY BETANCOURT
Semana: 8
Tema: Programación Orientada a Objetos 


Sistema restaurante_app utilizando Programación Orientada a Objetos en Python. El sistema deberá permitir registrar y listar productos, bebidas y clientes mediante un menú interactivo ejecutado desde consola.

La actividad deberá evidenciar una correcta distribución de responsabilidades entre las clases. La incorporación de la clase Bebida deberá ampliar el sistema mediante herencia, sin modificar innecesariamente el funcionamiento general del servicio principal.

El proyecto docente de la Semana 8 utiliza un sistema de biblioteca para demostrar la aplicación de los principios SOLID. En esta tarea, el estudiante deberá utilizarlo únicamente como referencia metodológica y adaptar los conceptos al contexto de un restaurante. No se debe copiar literalmente el código docente.

Sistema propuesto: restaurante
El sistema representará la gestión básica de productos, bebidas y clientes de un restaurante. La finalidad principal es demostrar que un proyecto puede mantenerse organizado cuando cada clase cumple una responsabilidad concreta y las relaciones de herencia conservan un comportamiento coherente.

Entidades mínimas solicitadas:

Producto: clase base que representa un producto general del restaurante.
Bebida: clase hija de Producto que incorpora información específica de una bebida.
Cliente: clase que representa a un cliente registrado.
Restaurante: clase de servicio encargada de administrar las colecciones y operaciones del sistema.
Importante: la actividad debe demostrar que Producto y Bebida pueden utilizarse mediante un comportamiento común, sin que el servicio necesite preguntar constantemente qué tipo concreto de objeto está procesando.
Estructura obligatoria del proyecto
El proyecto deberá organizarse respetando la siguiente estructura:

Estructura mínima:
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
Responsabilidad de cada archivo
modelos/producto.py: debe contener la clase Producto. Esta clase representará los datos comunes de los productos y definirá el método mostrar_informacion().
modelos/bebida.py: debe contener la clase Bebida, que heredará de Producto e incorporará atributos propios, como tamaño o tipo de envase.
modelos/cliente.py: debe contener la clase Cliente, encargada únicamente de representar la información de un cliente.
servicios/restaurante.py: debe contener la clase Restaurante, encargada de registrar, validar y listar productos y clientes.
main.py: debe ser el punto de arranque del programa. Desde este archivo se mostrará el menú, se solicitarán los datos y se llamará a los métodos del servicio.