
class Reserva:
    def __init__(self,id_reserva,vehiculo,dni_cliente,fecha_inicio,fecha_fin,precio_total,tipo_licencia,destino):
        self.id_reserva = id_reserva
        self.vehiculo = vehiculo
        self.dni_cliente = dni_cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = precio_total
        self.tipo_licencia = tipo_licencia
        self.destino = destino

    def calcular_dias(self):
        dias = self.fecha_fin - self.fecha_inicio
        return dias

class ReservaGrupal(Reserva):
    pass




