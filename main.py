# Programa principal - AeroChinquihue (Avance 1)
# Integrantes: Víctor Vega, Matías Fernández, Javier Ramírez
from controlador import Aerolinea
from modelo import Cliente
import vista

aerolinea = Aerolinea()
aerolinea.cargar_destinos()
aerolinea.cargar_aviones()
aerolinea.cargar_vuelos()

vista.mostrar_destinos(aerolinea.destinos)
vista.mostrar_aviones(aerolinea.aviones)
vista.mostrar_vuelos(aerolinea.vuelos[:13])  # solo los del primer día

# Ejemplo: creamos un cliente y reservamos un pasaje
cliente = Cliente("12.345.678-9", "Cliente de Prueba")
cliente.vuelos_realizados = 12  # más de 10 vuelos -> 10% de descuento
aerolinea.clientes.append(cliente)

vuelo = aerolinea.buscar_vuelo("AC012")  # Chaitén
venta = aerolinea.reservar_pasaje(cliente, vuelo, 3, "Tarjeta")
if venta:
    vista.mostrar_venta(venta)
