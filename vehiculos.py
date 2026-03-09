

class Vehiculo:
    def __init__(self,matricula,precio_base_dia):
        self.matricula = matricula
        #Tarifa estándar de lo que cuesta el alquiler de vehículo
        self.precio_base_dia = precio_base_dia
        self.kilometraje_actual = 0
        self.km_ultima_revision = 0
        self.disponible = True
        self.revision = False

    def calcular_Tarifa(self,dias):
        tarifa = self.precio_base_dia * dias
        return tarifa

    def alquilar(self):
        if self.disponible==False and not self.revision:
            print('Este coche no esta disponible') #Aqui excepcion solape(clase)
        else:
            self.disponible=False

    def devolver(self,km_recorridos):

        if self.disponible==True:
            print('Ya ha sido devuelto') #Aqui excepcion solape(clase)
        else:
            self.disponible=True
            self.kilometraje_actual+=km_recorridos

            if self.kilometraje_actual-self.km_ultima_revision>=15000:
                print('Necesita hacer una revisión') # Llamar a funcion
                self.revision = True

    def realizar_revision(self):
        if self.revision == True:
            self.revision= False
            print('Revisión realizada correctamente')
        else:
            print('Este coche no necesita revisión')

#class Turismo:
class Turismo(Vehiculo):
    def __init__(self,matricula,precio_base_dia,num_plazas):
        super().__init__(matricula,precio_base_dia)
        self.num_plazas = num_plazas # Aquí ponemos una futura restricción para que si pide un coche de 7 plazas no darle una de 5
    # tarifa distinta, aquí vamos a cobrar más por cada plaza superior a 5, un abono de 5€ por plaza
    def calcular_Tarifa(self,dias):
        if self.num_plazas>5:
            return super().calcular_Tarifa(dias) + ((self.num_plazas - 5)*5)

class Furgoneta(Vehiculo):
    def __init__(self,matricula,precio_base_dia,carga):
        super().__init__(matricula,precio_base_dia)
        self.carga = carga

    def calcular_Tarifa(self, dias):
        return super().calcular_Tarifa(dias) + ((self.carga / 100) * 2)

#class Electrico:

class Electrico(Vehiculo):
    def __init__(self, matricula, precio_base_dia, nivel_bateria, autonomia_maxima):
        super().__init__(matricula, precio_base_dia)
        self.nivel_bateria = nivel_bateria
        self.autonomia_maxima = autonomia_maxima

    def alquilar(self):
        if self.nivel_bateria < 20:
            print('Error: Batería demasiado baja.')  # Aquí excepción

        else:
            super().alquilar()

    def cargar(self):
        self.nivel_bateria = 100
        print(f'Vehículo {self.matricula} cargado al 100%')