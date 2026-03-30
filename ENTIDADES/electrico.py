from vehiculos import Vehiculo

#class Electrico:
class Electrico(Vehiculo):
    def __init__(self, matricula, precio_base_dia, nivel_bateria, autonomia_maxima, num_plazas):
        super().__init__(matricula, precio_base_dia)
        self.nivel_bateria = nivel_bateria
        self.autonomia_maxima = autonomia_maxima
        self.num_plazas=num_plazas


    def alquilar(self):
        if self.nivel_bateria < 20:
            print('Error: Batería demasiado baja.')  # Aquí excepción

        else:
            super().alquilar()

    def cargar(self):
        self.nivel_bateria = 100
        print(f'Vehículo {self.matricula} cargado al 100%')

    def __str__(self):
        return f"Eléctrico Matricula: {self.matricula}, Plazas: {self.num_plazas}, Autoonomía: {self.autonomia_maxima}, Batería: {self.nivel_bateria}"