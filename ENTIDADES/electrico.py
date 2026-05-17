from    ENTIDADES.vehiculos import Vehiculo
from EXCEPCIONES.excepciones import BateriaBajaExcepcion


#class Electrico:
class Electrico(Vehiculo):
    def __init__(self, matricula: str, precio_base_dia: int|float, nivel_bateria: int|float, autonomia_maxima: int|float, num_plazas: int,disponible:bool):
        super().__init__(matricula, precio_base_dia,disponible)
        self.nivel_bateria = nivel_bateria
        self.autonomia_maxima = autonomia_maxima
        self.num_plazas=num_plazas



    def alquilar(self):
        if self.nivel_bateria < 20:
            raise BateriaBajaExcepcion(f'Error: Batería del vehículo {self.matricula} demasiado baja ({self.nivel_bateria}%).')

        else:
            super().alquilar()

    def cargar(self): #funcion para cargar.
        self.nivel_bateria = 100
        print(f'Vehículo {self.matricula} cargado al 100%')

    def __str__(self):
        return f"Eléctrico => Matricula: {self.matricula}, Plazas: {self.num_plazas}, Autonomía: {self.autonomia_maxima}, Batería: {self.nivel_bateria}, Disponible: {self.disponible}"