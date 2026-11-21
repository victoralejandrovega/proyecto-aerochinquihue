# AeroChinquihue

Sistema en Python para gestionar los vuelos, pasajes y encomiendas de **AeroChinquihue**, una empresa aeronáutica con sede en Puerto Montt que conecta comunidades apartadas de la región de Los Lagos desde el Aeródromo La Paloma.

Proyecto del ramo **Programación Orientada a Objetos**, Universidad de Los Lagos.

## Integrantes

- Víctor Vega
- Matías Fernández
- Javier Ramírez

## Qué hace

- Maneja 13 destinos con su precio de pasaje y de encomienda por kilo.
- Maneja 3 tipos de avión (Cessna 310, Cessna 208 Caravan y LET 410 UVP-E20).
- Crea los vuelos diarios de la aerolínea.
- Reserva pasajes, elige el asiento y registra la venta.
- Aplica un 10 % de descuento a clientes con más de 10 vuelos.

## Estructura (patrón MVC)

| Archivo | Descripción |
|---|---|
| `modelo.py` | Clases con los datos: Destino, Avion, Vuelo, Cliente, Pasaje, Encomienda, Venta y Gerente |
| `vista.py` | Muestra la información por pantalla |
| `controlador.py` | Crea los objetos y carga los datos de los vuelos |
| `main.py` | Programa principal |

## Cómo ejecutar

Requiere Python 3.

    python main.py

## Avances

- **Avance 1:** diagrama de clases, maquetas de interfaces, creación de objetos y poblamiento de datos de los vuelos.
