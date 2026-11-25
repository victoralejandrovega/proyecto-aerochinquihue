# CONTROLADOR: crea los objetos y conecta el modelo con la vista.
from modelo import Destino, Avion, Vuelo, Cliente, Pasaje, Venta


class Aerolinea:
    def __init__(self):
        self.destinos = []
        self.aviones = []
        self.vuelos = []
        self.clientes = []
        self.ventas = []

    # ---- Poblamiento de datos ----
    def cargar_destinos(self):
        datos = [
            ("Cochamó", 20000, 5000), ("Puelo Bajo", 20000, 5000), ("Contao", 20000, 5000),
            ("Rio Negro", 25000, 6000), ("Pupelde", 25000, 6000),
            ("Chepu", 30000, 8000), ("Ayacara", 30000, 8000),
            ("Pillán", 40000, 12000), ("Reñihue", 40000, 12000),
            ("Isla Quenac", 40000, 12000), ("Palqui", 40000, 12000),
            ("Chaitén", 50000, 15000), ("Santa Bárbara", 50000, 15000),
        ]
        for nombre, pasaje, kg in datos:
            self.destinos.append(Destino(nombre, pasaje, kg))

    def cargar_aviones(self):
        self.aviones.append(Avion("CESSNA 310", 5, 910))
        self.aviones.append(Avion("CESSNA 208 CARAVAN", 9, 1315))
        self.aviones.append(Avion("LET 410 UVP-E20", 19, 1800))

    def cargar_vuelos(self):
        # Un vuelo diario a cada destino durante 3 días.
        # Destinos baratos -> avión chico, destinos caros -> avión grande.
        fechas = ["2026-11-26", "2026-11-27", "2026-11-28"]
        numero = 1
        for fecha in fechas:
            for destino in self.destinos:
                if destino.precio_pasaje <= 25000:
                    avion = self.aviones[0]
                elif destino.precio_pasaje <= 40000:
                    avion = self.aviones[1]
                else:
                    avion = self.aviones[2]
                codigo = f"AC{numero:03}"
                self.vuelos.append(Vuelo(codigo, destino, avion, fecha, "09:00"))
                numero += 1

    # ---- Operaciones ----
    def buscar_vuelo(self, codigo):
        for v in self.vuelos:
            if v.codigo == codigo:
                return v
        return None

    def reservar_pasaje(self, cliente, vuelo, asiento, medio_pago):
        if asiento in vuelo.asientos_ocupados:
            print("Ese asiento ya está ocupado")
            return None
        descuento = 10 if cliente.vuelos_realizados > 10 else 0
        pasaje = Pasaje(cliente, vuelo, asiento)
        vuelo.asientos_ocupados.append(asiento)
        venta = Venta(pasaje, medio_pago, descuento)
        self.ventas.append(venta)
        return venta
