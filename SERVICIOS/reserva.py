from datetime import date
import os
from    ENTIDADES.vehiculos import Vehiculo
class Reserva:
    def __init__(self,id_reserva,vehiculo,dni_cliente,fecha_inicio,fecha_fin,tipo_licencia,destino):
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
    def calcular_dias(self) -> int:
        diferencia = self.fecha_fin - self.fecha_inicio
        return diferencia.days

    '''En este método calculamos el coste total de la reserva'''
    def calcular_precio_total(self)->float:
        dias = self.calcular_dias()
        # Obtenemos la tarifa base desde el objeto vehículo
        precio_base = self.vehiculo.calcular_tarifa(dias)

        porcentaje_descuento = 0

        if dias >= 30:
            porcentaje_descuento = 0.25  # 25% de descuento
        elif dias >= 7:
            porcentaje_descuento = 0.10  # 10% de descuento

        precio_final = precio_base * (1 - porcentaje_descuento)
        return round(precio_final, 2)  # Redondeamos a 2 decimales

    def __add__(self, suplemento: int | float) -> 'Reserva':
        #Sobrecarga de + para poder cobrar un suplemento extra
        if isinstance(suplemento, (int, float)):
            # Sumamos el suplemento directamente al precio total
            self._Reserva__precio_total += suplemento
            return self
        else:
            raise TypeError("El suplemento a añadir debe ser un número (entero o decimal).")
    def generar_contrato_txt(self):
        if not os.path.exists("CONTRATOS"):
            os.makedirs("CONTRATOS")

        nombre_archivo = f"CONTRATOS/contrato_{self.id_reserva}.txt"

        # Aquí diseñamos el contrato
        contenido = f"""
        --- CONTRATO DE ALQUILER ---
        Reserva ID: {self.id_reserva}
        DNI Cliente: {self.dni_cliente}
        Vehículo: {self.vehiculo}
        Fechas: {self.fecha_inicio} a {self.fecha_fin}
        Precio Total: {self._Reserva__precio_total} €
        ----------------------------
        """

        '''Aquí abrimos el archivo y escribimos todo el bloque de texto de una vez'''
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            file.write(contenido)

        print(f"Contrato generado: {nombre_archivo}")






