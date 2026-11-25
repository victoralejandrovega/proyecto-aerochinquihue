# VISTA: aquí solo se muestran cosas por pantalla (print).

def mostrar_destinos(destinos):
    print("\n=== DESTINOS ===")
    for d in destinos:
        print(f"{d.nombre:15} Pasaje: ${d.precio_pasaje:,}  Encomienda x kg: ${d.precio_kg:,}")


def mostrar_aviones(aviones):
    print("\n=== AVIONES ===")
    for a in aviones:
        print(f"{a.modelo:20} Pasajeros: {a.capacidad_pasajeros:2}  Carga: {a.capacidad_kg} kg")


def mostrar_vuelos(vuelos):
    print("\n=== VUELOS ===")
    for v in vuelos:
        print(f"{v.codigo}  {v.fecha} {v.hora}  {v.destino.nombre:15} {v.avion.modelo:20} "
              f"Asientos libres: {v.asientos_disponibles()}")


def mostrar_venta(venta):
    print("\n=== VENTA REGISTRADA ===")
    print("Cliente:", venta.servicio.cliente.nombre)
    print("Destino:", venta.servicio.vuelo.destino.nombre)
    print("Medio de pago:", venta.medio_pago)
    print(f"Descuento: {venta.descuento}%")
    print(f"Total a pagar: ${venta.total:,.0f}")
