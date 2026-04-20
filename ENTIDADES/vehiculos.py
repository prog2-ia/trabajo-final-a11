from abc import ABC,abstractmethod

class Vehiculo(ABC):
    def __init__(self,matricula:str,precio_base_dia:int|float):
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

    def devolver(self,km_recorridos:int|float):

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

