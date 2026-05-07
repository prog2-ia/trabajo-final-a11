from datetime import date

class Cliente:
    def __init__(self, dni: str, nombre: str, apellidos: str, tipo_licencia: str, 
                 fecha_nacimiento: date, fecha_licencia: date, email: str):
        self.__dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.tipo_licencia = tipo_licencia
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_licencia = fecha_licencia
        self.email = email
        self.esta_bloqueado = False  # Para clientes con deudas o incidentes
        self.historial_reservas = []

    @property
    def dni(self):
        return self.__dni

    @property
    def edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    @property
    def años_experiencia(self):
        hoy = date.today()
        return hoy.year - self.fecha_licencia.year - ((hoy.month, hoy.day) < (self.fecha_licencia.month, self.fecha_licencia.day))

    def mostrar_ficha_tecnica(self):
        print("\n" + 30 * "=")
        print(f"FICHA TÉCNICA DEL CLIENTE")
        print(30 * "=")
        print(f"Nombre completo: {self.nombre} {self.apellidos}")
        print(f"DNI:             {self.dni}")
        print(f"Licencia:        {self.tipo_licencia}")
        print(f"Email:           {self.email}")
        print(f"Fecha Nac.:      {self.fecha_nacimiento.strftime('%d/%m/%Y')}")
        print(f"Antigüedad Lic.: {self.fecha_licencia.strftime('%d/%m/%Y')}")
        print(f"Reservas totales: {len(self.historial_reservas)}")
        print(30 * "=" + "\n")

    def es_conductor_novel(self):
        """Se considera novel si tiene menos de 2 años de carnet."""
        return self.años_experiencia < 2

    def puede_alquilar(self):
        """Validación básica de seguridad."""
        if self.esta_bloqueado:
            return False, "El cliente está bloqueado por el sistema."
        if self.edad < 25:
            return False, "El cliente debe ser mayor de 25 años."
        return True, "Apto para alquilar."

    def __str__(self):
        estado = "ACTIVO" if not self.esta_bloqueado else "BLOQUEADO"
        return (f"[{estado}] {self.nombre} {self.apellidos} ({self.dni}) | "
                f"Experiencia: {self.años_experiencia} años | Puntos: {self.puntos_fidelidad}")