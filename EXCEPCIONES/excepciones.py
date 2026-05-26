class ExcepcionBase(Exception):
    pass
class SolapeExcepcion(ExcepcionBase):
    pass
class VehiculoEnRevisionExcepcion(ExcepcionBase):#Excepción para no entregar un vehículo que esta en revisión
    pass
class PlazasInsuficientesExcepcion(ExcepcionBase):#Excepción para no entregar un coche de menos plazas de las necesarias
    pass
class KilometrajeImposibleExcepcion(ExcepcionBase):#Excepción para manejar errores en el kilometraje
    pass
class BateriaBajaExcepcion(ExcepcionBase):#Excepción para no entregar un vehículo eléctrico con batería baja
    pass

class UsuarioNoEncontrado(ExcepcionBase):#Excepción por si no se encuentra un usuario en la base de datos
    pass

class FechasInvalidasExcepcion(ExcepcionBase):#Excepción para manejar fechas
    pass

class DniValido(ExcepcionBase):# Excepción para controlar si el dni es válido
    pass
