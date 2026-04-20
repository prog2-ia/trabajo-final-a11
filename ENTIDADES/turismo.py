from vehiculos import Vehiculo
class Turismo(Vehiculo):
    def __init__(self,matricula:str,precio_base_dia:int|float,num_plazas:int):
        super().__init__(matricula,precio_base_dia)
        self.num_plazas = num_plazas # Aquí ponemos una futura restricción para que si pide un coche de 7 plazas no darle una de 5
    #tarifa distinta, aquí vamos a cobrar más por cada plaza superior a 5, un abono de 5€ por plaza
    def calcular_tarifa(self,dias:int) -> int|float:
        tarifa_base = super().calcular_tarifa(dias)

        # Si tiene más de 5 plazas, le sumamos el recargo
        if self.num_plazas > 5:
            return tarifa_base + ((self.num_plazas - 5) * 5)

        #Si tiene 5 o menos, simplemente devolvemos la tarifa base normal
        return tarifa_base

    def __str__(self):
        return f"Turismo Matricula: {self.matricula}, Plazas: {self.num_plazas}"

