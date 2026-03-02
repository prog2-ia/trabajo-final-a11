
class Vehiculo:
    def __init__(self,matricula,precio_base_dia):
        self.matricula = matricula
        #Tarifa estándar de lo que cuesta el alquiler de vehículo
        self.precio_base_dia = precio_base_dia
        self.kilometraje_actual = 0
        self.km_ultima_revision = 0
        self.disponible = True

    def calcular_Tarifa(self,dias):
        tarifa = self.precio_base_dia * dias
        return tarifa


#class Turismo:
class Furgoneta(Vehiculo):
    def __init__(self,matricula,precio_base_dia,carga):
        super().__init__(matricula,precio_base_dia)
        self.carga = carga

#class Electrico: