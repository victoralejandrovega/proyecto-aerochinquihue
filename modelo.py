# Proyecto AeroChinquihue - Avance 1 (RA II)
# Integrantes: Víctor Vega, Matías Fernández, Javier Ramírez
# MODELO: aquí están las clases con los datos del programa.


class Destino:
    def __init__(self, nombre, precio_pasaje, precio_kg):
        self.nombre = nombre
        self.precio_pasaje = precio_pasaje
        self.precio_kg = precio_kg


class Avion:
    def __init__(self, modelo, capacidad_pasajeros, capacidad_kg):
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.capacidad_kg = capacidad_kg


class Vuelo:
    def __init__(self, codigo, destino, avion, fecha, hora, extraordinario=False):
        self.codigo = codigo
        self.destino = destino
        self.avion = avion
        self.fecha = fecha
        self.hora = hora
        self.extraordinario = extraordinario
        self.asientos_ocupados = []  # números de asiento ya reservados
        self.kg_ocupados = 0

    def asientos_disponibles(self):
        return self.avion.capacidad_pasajeros - len(self.asientos_ocupados)


class Cliente:
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre
        self.vuelos_realizados = 0


class Pasaje:
    def __init__(self, cliente, vuelo, asiento):
        self.cliente = cliente
        self.vuelo = vuelo
        self.asiento = asiento
        self.precio = vuelo.destino.precio_pasaje


class Encomienda:
    def __init__(self, cliente, vuelo, peso_kg):
        self.cliente = cliente
        self.vuelo = vuelo
        self.peso_kg = peso_kg
        self.precio = peso_kg * vuelo.destino.precio_kg


class Venta:
    def __init__(self, servicio, medio_pago, descuento=0):
        self.servicio = servicio      # puede ser un Pasaje o una Encomienda
        self.medio_pago = medio_pago
        self.descuento = descuento    # porcentaje (0 a 100)
        self.total = servicio.precio - servicio.precio * descuento / 100


class Gerente:
    def __init__(self, nombre):
        self.nombre = nombre
