from vehiculos import Vehiculo


class Furgoneta(Vehiculo):
    def __init__(self,matricula:str,precio_base_dia: int|float ,carga:int,num_plazas:int):
        super().__init__(matricula,precio_base_dia)
        self.carga = carga
        self.num_plazas=num_plazas

    def calcular_tarifa(self, dias:int) -> int|float:
        return super().calcular_tarifa(dias) + ((self.carga / 100) * 2)

    def __str__(self):
        return f"Furgoneta Matricula: {self.matricula}, Plazas: {self.num_plazas}, Carga: {self.carga}"