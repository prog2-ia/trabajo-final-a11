from abc import ABC,abstractmethod

class Vehiculo(ABC):
    def __init__(self,matricula,precio_base_dia):
        self.__matricula = matricula
        #Tarifa estándar de lo que cuesta el alquiler de vehículo
        self.precio_base_dia = precio_base_dia
        self.kilometraje_actual = 0
        self.km_ultima_revision = 0
        self.disponible = True
        self.revision = False

    @abstractmethod
    def __str__(self):
        pass

    @property
    def matricula(self):
        return self.__matricula

    def calcular_tarifa(self,dias):
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
    def calcular_tarifa(self,dias):
        tarifa_base = super().calcular_tarifa(dias)

        # Si tiene más de 5 plazas, le sumamos el recargo
        if self.num_plazas > 5:
            return tarifa_base + ((self.num_plazas - 5) * 5)

        #Si tiene 5 o menos, simplemente devolvemos la tarifa base normal
        return tarifa_base

    def __str__(self):
        return f"Turismo Matricula: {self.matricula}, Plazas: {self.num_plazas}"

class Furgoneta(Vehiculo):
    def __init__(self,matricula,precio_base_dia,carga,num_plazas):
        super().__init__(matricula,precio_base_dia)
        self.carga = carga
        self.num_plazas=num_plazas

    def calcular_tarifa(self, dias):
        return super().calcular_tarifa(dias) + ((self.carga / 100) * 2)

    def __str__(self):
        return f"Furgoneta Matricula: {self.matricula}, Plazas: {self.num_plazas}, Carga: {self.carga}"

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