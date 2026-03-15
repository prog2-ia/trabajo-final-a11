from datetime import date
from vehiculos import Vehiculo
class Reserva:
    def __init__(self,id_reserva,vehiculo,dni_cliente,fecha_inicio,fecha_fin,,tipo_licencia,destino):
        # Encapsulamos el id de la reserva
        self.__id_reserva = id_reserva
        self.vehiculo = vehiculo
        self.dni_cliente = dni_cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo_licencia = tipo_licencia
        self.destino = destino
        #Calculamos el precio total y lo encapsulamos
        self.__precio_total = self.calcular_precio_total()

    @property
    def id_reserva(self):
        return self.__id_reserva

    '''En este método calculamos el número de dias de la reserva'''
    def calcular_dias(self):
        diferencia = self.fecha_fin - self.fecha_inicio
        return diferencia.days
    '''En este método calculamos el coste total de la reserva'''
    def calcular_precio_total(self):
        dias = self.calcular_dias()
        '''aquí llamamos al método de vehículo'''
        return self.vehiculo.calcular_Tarifa(dias)

    def generar_contrato_txt(self):
        nombre_archivo = f"contrato_{self.id_reserva}.txt"

        # Aquí diseñamos el contrato
        contenido = f"""
        --- CONTRATO DE ALQUILER ---
        Reserva ID: {self.id_reserva}
        DNI Cliente: {self.dni_cliente}
        Fechas: {self.fecha_inicio} a {self.fecha_fin}
        Precio Total: {self.precio_total} €
        ----------------------------
        """

        '''Aquí abrimos el archivo y escribimos todo el bloque de texto de una vez'''
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            file.write(contenido)

        print(f"Contrato generado: {nombre_archivo}")


class ReservaGrupal(Reserva):
    def calcular_precio_total(self):
        precio_original = super().calcular_precio_total()
        # Aquí aplicamos un descuento de 10% para reservas en grupo
        precio_con_descuento = precio_original * 0.90
        return precio_con_descuento



