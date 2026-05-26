from datetime import date
from ENTIDADES.vehiculos import  Vehiculo
from ENTIDADES.turismo import Turismo
from ENTIDADES.furgoneta import Furgoneta
from ENTIDADES.electrico import Electrico
from SERVICIOS.reserva import Reserva
from ENTIDADES.clientes import Cliente
from EXCEPCIONES.excepciones import UsuarioNoEncontrado, FechasInvalidasExcepcion, DniValido, SolapeExcepcion, VehiculoEnRevisionExcepcion
import pickle
import os
def crear_flota(): #Creamos una flota inicial de vehículos
  flota = {"1": Turismo("1111-AAA", precio_base_dia=50, num_plazas=5,disponible = True),
          "2": Furgoneta("2222-BBB", precio_base_dia=60, carga=1000, num_plazas=3,disponible=True),
          "3": Electrico("3333-CCC", precio_base_dia=80, nivel_bateria=100, autonomia_maxima=400, num_plazas=5,disponible=True)}
  return flota

#Aquí inicializamos clientes
def crear_clientes_iniciales():
    # Diccionario usando el DNI como clave
    return {"12345678A": Cliente("12345678A", "Pepe", "Pérez", "B",date(1990, 5, 12), date(2010, 8, 20), "pepe@gmail.com") }
def pedir_dni(mensaje):
    letras_validas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    while True:
        dni = input(mensaje).strip().upper()
        if len(dni) == 9:
            if dni[:8].isdigit():
                if dni[8].isalpha():
                #comprobamos que la letra sea la correcta
                    if letras_validas[int(dni[:8]) % 23] == dni[8]:
                        return dni
        print('Error: DNI inválido.')

def pedir_matricula(mensaje):
    while True:
        matricula = input(mensaje).strip().upper()
        mat_limpia = matricula.replace("-", "")
        # Comprobamos que midan 7 caracteres exactos (4 números + 3 letras)
        if len(mat_limpia) == 7:
            if mat_limpia[:4].isdigit():
                if mat_limpia[4:].isalpha():
                    return matricula
        print('Error: Matrícula inválida.')

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Error: Por favor, introduce un número entero válido.")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" Error: Por favor, introduce un número decimal válido.")

def main():
    datos = cargar_datos()
    if datos:
        flota = datos["flota"]
        clientes = datos["clientes"]
        reservas = datos["reservas"]
        contador_reservas = datos["contador_reservas"]
        contador_flota = datos["contador_flota"]
        print('Base de datos  cargada.')
    else:
         # Si no hay datos añadimos estos por defecto
         flota = crear_flota()
         clientes = crear_clientes_iniciales()
         reservas = {}
         contador_reservas = 4
         contador_flota = 3
         flota["1"].alquilar()

    usuario_registrado = False
    dni_cliente_actual = None
    while not usuario_registrado:
        print('Usuario')
        print('1.Iniciar Sesión')
        print('2.Registrarse ')
        elec = input('Escoja una opción: ')
        if elec == '1':
            try:
                dni = pedir_dni('Introduce el dni:')
                if dni not in clientes:
                    raise UsuarioNoEncontrado("Este cliente no está registrado.")  # Excepción lanzada
                print(f'Bienvenido {clientes[dni].nombre}')
                dni_cliente_actual = dni
                usuario_registrado = True
            except UsuarioNoEncontrado as e:
                print(f"Error: {e}")
        elif elec == '2':
            try:
                print("--- Registro de Cliente ---")
                dni = pedir_dni('Introduce el dni:')
                if dni in clientes:
                    raise DniValido("Este DNI ya se encuentra registrado.")  # Excepción para duplicados
                nombre = input('Introduce el nombre: ')
                apellidos = input('Introduce los apellidos: ')
                tipo_licencia = input('Introduce el tipo de licencia: ')

                str_nac = input('Introduce tu fecha de nacimiento (DD/MM/AAAA): ')
                dia_n, mes_n, anio_n = str_nac.split('/')
                fecha_nacimiento = date(int(anio_n), int(mes_n), int(dia_n))

                str_lic = input('Introduce tu fecha de licencia (DD/MM/AAAA): ')
                dia_l, mes_l, anio_l = str_lic.split('/')
                fecha_licencia = date(int(anio_l), int(mes_l), int(dia_l))

                email = input('Introduce tu email: ')

                clientes[dni] = Cliente(dni, nombre, apellidos, tipo_licencia, fecha_nacimiento, fecha_licencia, email)
                print(f"Cliente {nombre} registrado correctamente.")
                guardar_datos(flota, clientes, reservas, contador_reservas, contador_flota)
                usuario_registrado=True
            except DniValido as e:
                print(f"Error de registro: {e}")
            except ValueError:
                print("Error: Formato de fecha incorrecto. Asegúrate de usar números DD/MM/AAAA.")

    seguir = True
    while seguir:
        print(30*'~')
        print('🚗Menú de gestión de alquileres🚗')
        print('1. Mostrar flota de coches disponibles.')
        print('2. Mostrar flota de coches alquilados.')
        print('3. Añadir un nuevo coche a la flota.')
        print('4. Crear nuevo contrato de alquiler.')
        print('5. Devolver vehículo')
        print('6. Mostrar ficha técnica cliente.')
        print('7. Salir.')
        print(30*'~')
        opc = input('Introduce una opción: ')
        if opc == '1':
            for clave, valor in flota.items():
                if  valor.disponible == True:
                    print(f'{clave},{valor}')

        elif opc == '2':
            hay_alquilados=False
            for clave, valor in flota.items():
                if not valor.disponible:
                    hay_alquilados = True
                    print(f"Coche ID {clave}: {valor.matricula}")
                    # Buscar en las reservas quién lo tiene
                    for res in reservas.values():
                        # Si la reserva tiene este vehículo y la fecha de fin aún no ha pasado (o asumiendo la última reserva)
                        if res.vehiculo.matricula == valor.matricula:
                            print(f" -> Alquilado por DNI: {res.dni_cliente} hasta el {res.fecha_fin}")
            if not hay_alquilados:
                print("No hay ningún coche alquilado ahora mismo.")
        elif opc == '3':
            print('Tipos de Vehículo:')
            print('1.Turismo')
            print('2.Eléctrico')
            print('3.Furgoneta')
            tipo = input('Introduce el tipo de Vehículo: ')
            contador_flota += 1
            if tipo == '1':
                matricula = pedir_matricula('Introduce la matrícula del vehículo: ')
                num_plazas = pedir_entero('Introduce el número de plazas')
                flota[str(contador_flota)] = Turismo(matricula, 50, num_plazas,True)
                print(f"Turismo con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")
            elif tipo == '3':
                matricula = pedir_matricula('Introduce la matrícula del vehículo: ')
                num_plazas = pedir_entero('Introduce el número de plazas')
                carga = pedir_entero('Introduce la carga de la Furgoneta:')
                flota[str(contador_flota)] = Furgoneta(matricula, 50,carga, num_plazas,True)
                print(f"Furgoneta con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")
            elif tipo == '2':
                matricula = pedir_matricula('Introduce la matrícula del vehículo: ')
                num_plazas = pedir_entero('Introduce el número de plazas')
                autonomia_maxima = pedir_entero('Introduce la autonomía máxima: ')
                flota[str(contador_flota)] = Electrico(matricula, 50, 100, autonomia_maxima, num_plazas,True)
                print(f"Eléctrico con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")
            guardar_datos(flota, clientes, reservas, contador_reservas, contador_flota)

        elif opc == '4':
            try:
                vehiculo = input('Introduce el índice del coche: ')
                if vehiculo not in flota:
                    raise ValueError("El vehículo seleccionado no existe en la flota.")

                dni_cliente = dni_cliente_actual

                str_inicio = input('Introduce la fecha de inicio (DD/MM/AAAA): ')
                dia_i, mes_i, anio_i = str_inicio.split('/')
                fecha_inicio = date(int(anio_i), int(mes_i), int(dia_i))
                if fecha_inicio < date.today():
                    raise FechasInvalidasExcepcion("No puedes iniciar una reserva en una fecha pasada.")

                str_fin = input('Introduce la fecha de fin (DD/MM/AAAA): ')
                dia_f, mes_f, anio_f = str_fin.split('/')
                fecha_fin = date(int(anio_f), int(mes_f), int(dia_f))
                if fecha_inicio >= fecha_fin:
                    raise FechasInvalidasExcepcion("La fecha de inicio no puede ser igual o posterior a la de fin.")

                tipo_licencia = input('Introduce el tipo de licencia: ')
                destino = input('Introduce el destino')
                # Extraemos el objeto vehículo y lo intentamos alquilar
                vehiculo_obj = flota[str(vehiculo)]

                apto, mensaje = clientes[dni_cliente].puede_alquilar()
                if apto:
                    vehiculo_obj.alquilar()
                    reserva = Reserva(f"RES-00{contador_reservas}", vehiculo_obj, dni_cliente, fecha_inicio, fecha_fin,
                                      tipo_licencia, destino)
                    reserva.generar_contrato_txt()
                    reservas[reserva.id_reserva] = reserva
                    contador_reservas += 1
                    clientes[dni_cliente].historial_reservas.append(reserva.id_reserva)
                    guardar_datos(flota, clientes, reservas, contador_reservas, contador_flota)
                    print("Reserva hecha correctamente.")
                else:
                    print(f"Error: No se puede alquilar. {mensaje}")

            except (UsuarioNoEncontrado, FechasInvalidasExcepcion, SolapeExcepcion, VehiculoEnRevisionExcepcion) as e:
                print(f"Error al crear la reserva: {e}")
            except ValueError:
                print("Error: Por favor, introduce datos válidos (ej: fechas correctas o índices numéricos).")

        elif opc == '5':
            try:
                vehiculo_idx = input('Introduce el índice del vehículo a devolver: ')
                if vehiculo_idx not in flota:
                    raise ValueError("El vehículo seleccionado no existe en la flota.")

                vehiculo_obj = flota[str(vehiculo_idx)]

                km_recorridos = pedir_float('Introduce los kilómetros recorridos durante el alquiler: ')

                if isinstance(vehiculo_obj, Electrico):
                    vehiculo_obj = vehiculo_obj + km_recorridos
                    vehiculo_obj.devolver(0)  # Si es eléctrico pasamos 0 ya ha sumado el operador +
                else:
                    vehiculo_obj.devolver(km_recorridos)  # Si es turismo o furgoneta, se lo pasamos normal
                print(f"Vehículo {vehiculo_obj.matricula} devuelto correctamente.")
                coste_extra = pedir_float("¿El vehículo se ha devuelto con daños o sucio? Introduce el coste extra (o 0 si está todo bien): ")
                if coste_extra > 0:
                    # Buscamos la última reserva de este cliente
                    id_ultima_reserva = clientes[dni_cliente_actual].historial_reservas[-1]
                    reserva_afectada = reservas[id_ultima_reserva]
                    reserva_afectada = reserva_afectada + coste_extra
                    print(f"Recargo de {coste_extra}€ aplicado a la reserva {reserva_afectada.id_reserva}.")
                guardar_datos(flota, clientes, reservas, contador_reservas, contador_flota)

            except SolapeExcepcion as e:
                print(f"Error: {e}")
            except ValueError:
                print("Error: Por favor, introduce kilómetros numéricos válidos.")



        elif opc == '6':
            print("Mi Perfil")
            # Como en el inicio de sesión guardamos el DNI en la variable `cliente_actual_dni`
            mi_usuario = clientes[dni_cliente_actual]
            mi_usuario.mostrar_ficha_tecnica()
            print("Mis Reservas")
            if not mi_usuario.historial_reservas:
                print("Todavía no tienes reservas hechas.")
            else:
                for id_res in mi_usuario.historial_reservas:
                    res = reservas[id_res]
                    print(f"[{res.id_reserva}] Vehículo: {res.vehiculo.matricula} | Fechas: {res.fecha_inicio} a {res.fecha_fin} | Total: {res._Reserva__precio_total}€")

        elif opc == '7':
            print("Guardando datos y cerrando el sistema...")
            guardar_datos(flota, clientes, reservas, contador_reservas, contador_flota)
            seguir = False

ARCHIVO_DATOS = "DATOS/datos_rentacar.pkl"

def guardar_datos(flota, clientes, reservas, contador_reservas, contador_flota):
    #Aquí guardamos los datos en el archivo pickle
    if not os.path.exists("DATOS"):
        os.makedirs("DATOS")
    datos = {"flota": flota,"clientes": clientes,"reservas": reservas,"contador_reservas": contador_reservas,"contador_flota": contador_flota}
    try:
        with open(ARCHIVO_DATOS, "wb") as datos_alquiler_coches:
            pickle.dump(datos, datos_alquiler_coches)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")


def cargar_datos():
    #Aquí leemos el archivo pickle para cargar los datos localmente
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, "rb") as datos_alquiler_coches:
                return pickle.load(datos_alquiler_coches)
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
    return None

if __name__ == "__main__":
 main()
