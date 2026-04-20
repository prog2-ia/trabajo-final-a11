from datetime import date
from vehiculos import Vehiculo,Turismo, Furgoneta, Electrico
from reserva import Reserva
def main():
 print("INICIANDO PRUEBAS DEL SISTEMA DE ALQUILER ")
 # En primer lugar, creamos nuestra flota de prueba
 print("Creando vehículos...")
 coche_normal = Turismo("1111-AAA", precio_base_dia=50, num_plazas=5)
 furgoneta_carga = Furgoneta("2222-BBB", precio_base_dia=60, carga=1000, num_plazas=3)
 coche_electrico = Electrico("3333-CCC", precio_base_dia=80, nivel_bateria=100, autonomia_maxima=400, num_plazas=5)
 print("Flota creada correctamente.")


 # En segundo lugar, definimos algunas fechas para probar tus descuentos
 hoy = date(2026, 3, 15)
 fecha_3_dias = date(2026, 3, 18)  # Sin descuento
 fecha_10_dias = date(2026, 3, 25)  # 10% de descuento
 fecha_40_dias = date(2026, 4, 24)  # 25% de descuento




 # Primera prueba reserva corta. Sin descuento + Turismo
 print("PRUEBA 1: Alquiler Corto (Turismo)")
 reserva1 = Reserva("RES-001", coche_normal, "12345678A", hoy, fecha_3_dias, "B", "Madrid")
 reserva1.vehiculo.alquilar()  # Cambiamos disponibilidad
 print(f"Días de alquiler: {reserva1.calcular_dias()}")
 reserva1.generar_contrato_txt()
 print()


 # Segunda prueba reserva Media. 10% descuento + Furgoneta
 print("PRUEBA 2: Alquiler Medio con 10% Dto (Furgoneta)")
 reserva2 = Reserva("RES-002", furgoneta_carga, "87654321B", hoy, fecha_10_dias, "C1", "Valencia")
 reserva2.vehiculo.alquilar()
 print(f"Días de alquiler: {reserva2.calcular_dias()}")
 reserva2.generar_contrato_txt()
 print()


 #  Reserva Larga. 25% descuento + Eléctrico
 print("PRUEBA 3: Alquiler Largo con 25% Dto (Eléctrico)")
 reserva3 = Reserva("RES-003", coche_electrico, "55555555C", hoy, fecha_40_dias, "B", "Barcelona")
 reserva3.vehiculo.alquilar()
 print(f"Días de alquiler: {reserva3.calcular_dias()}")
 reserva3.generar_contrato_txt()
 print()
 print("Todas las pruebas finalizadas. Revisa los archivos .txt generados.")

if __name__ == "__main__":
 main()
