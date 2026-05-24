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
        print('Usuario:')
        print('1.Iniciar Sesión:')
        print('2.Registrarse: ')
        elec = input('Escoja una opción: ')
        if elec == '1':
            try:
                dni = input('Introduce el dni: ')
                if dni not in clientes:
                    raise UsuarioNoEncontrado("Este cliente no está registrado.")  # Excepción lanzada
                print('Bienvenido {clientes[dni]}')
                dni_cliente_actual = dni
                usuario_registrado = True
            except UsuarioNoEncontrado as e:
                print(f"Error: {e}")
        elif elec == '2':
            try:
                print("--- Registro de Cliente ---")
                dni = input('Introduce el dni: ')
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
                continuar = False
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
        print('5. Iniciar sesión o registrar nuevo cliente.')
        print('6. Mostrar ficha técnica cliente.')
        print('7. Salir.')
        print(30*'~')
        opc = input('Introduce una opción: ')
        if opc == '1':
            for clave, valor in flota.items():
                if  valor.disponible == True:
                    print(f'{clave},{valor}')

        elif opc == '2':
            for clave, valor in flota.items():
                if valor.disponible == False:
                    print(f'{clave},{valor}')
        elif opc == '3':
            print('Tipos de Vehículo:')
            print('1.Turismo')
            print('2.Eléctrico')
            print('3.Furgoneta')
            tipo = input('Introduce el tipo de Vehículo: ')
            contador_flota += 1
            if tipo == '1':
                matricula = input('Introduce la matrícula del vehículo: ')
                num_plazas = int(input('Introduce el número de plazas: '))
                flota[str(contador_flota)] = Turismo(matricula, 50, num_plazas,True)
                print(f"Turismo con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")
            elif tipo == '3':
                matricula = input('Introduce la matrícula del vehículo: ')
                num_plazas = int(input('Introduce el número de plazas: '))
                carga = int(input('Introduce la carga de la Furgoneta: '))
                flota[str(contador_flota)] = Furgoneta(matricula, 50,carga, num_plazas,True)
                print(f"Furgoneta con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")
            elif tipo == '2':
                matricula = input('Introduce la matrícula del vehículo: ')
                num_plazas = int(input('Introduce el número de plazas: '))
                autonomia_maxima = int(input('Introduce la autonomía máxima: '))
                flota[str(contador_flota)] = Electrico(matricula, 50, 100, autonomia_maxima, num_plazas,True)
                print(f"Eléctrico con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")
            guardar_datos(flota, clientes, reservas, contador_reservas, contador_flota)

        elif opc == '4':
            try:
                vehiculo = input('Introduce el índice del coche: ')
                if vehiculo not in flota:
                    raise ValueError("El vehículo seleccionado no existe en la flota.")
                dni_cliente = input('Introduce el Dni del cliente: ')
                if dni_cliente not in clientes:
                    raise UsuarioNoEncontrado("Este cliente no está registrado en el sistema. Regístralo primero.")

                str_inicio = input('Introduce la fecha de inicio (DD/MM/AAAA): ')
                dia_i, mes_i, anio_i = str_inicio.split('/')
                fecha_inicio = date(int(anio_i), int(mes_i), int(dia_i))

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
                    guardar_datos(flota, clientes, reservas, contador_reservas, contador_flota)
                    print("Reserva hecha correctamente.")
                else:
                    print(f"Error: No se puede alquilar. {mensaje}")

            except (UsuarioNoEncontrado, FechasInvalidasExcepcion, SolapeExcepcion, VehiculoEnRevisionExcepcion) as e:
                print(f"Error al crear la reserva: {e}")
            except ValueError:
                print("Error: Por favor, introduce datos válidos (ej: fechas correctas o índices numéricos).")

        elif opc == '6':
            print("\n--- Consulta de Ficha Técnica ---")
            try:
                dni_consulta = input("Introduce el DNI del cliente: ")
                if dni_consulta not in clientes:
                    raise UsuarioNoEncontrado(f"No existe ningún cliente registrado con el DNI {dni_consulta}.")

                clientes[dni_consulta].mostrar_ficha_tecnica()
            except UsuarioNoEncontrado as e:
                print(f"Error: {e}")

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
