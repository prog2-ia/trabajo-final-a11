class ExcepcionBase(Exception):
    pass
class SolapeExcepcion(ExcepcionBase):
    pass
class VehiculoEnRevisionExcepcion(ExcepcionBase):
    pass
class PlazasInsuficientesExcepcion(ExcepcionBase):
    pass
class KilometrajeImposibleExcepcion(ExcepcionBase):
    pass
class BateriaBajaExcepcion(ExcepcionBase):
    pass

class UsuarioNoEncontrado(ExcepcionBase):
    pass

class FechasInvalidasExcepcion(ExcepcionBase):
    pass

class DniValido(ExcepcionBase):
    pass
