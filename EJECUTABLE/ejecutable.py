from datetime import date
from ENTIDADES.vehiculos import  Vehiculo
from ENTIDADES.turismo import Turismo
from ENTIDADES.furgoneta import Furgoneta
from ENTIDADES.electrico import Electrico
from SERVICIOS.reserva import Reserva
from ENTIDADES.clientes import Cliente

def crear_flota(): #Creamos una flota inicial de vehículos
  flota = {"1": Turismo("1111-AAA", precio_base_dia=50, num_plazas=5,disponible = True),
          "2": Furgoneta("2222-BBB", precio_base_dia=60, carga=1000, num_plazas=3,disponible=True),
          "3": Electrico("3333-CCC", precio_base_dia=80, nivel_bateria=100, autonomia_maxima=400, num_plazas=5,disponible=True)}
  return flota

def crear_clientes_iniciales():
    # Diccionario usando el DNI como clave
    return {
        "12345678A": Cliente("12345678A", "Pepe", "Pérez", "B", "600112233", "606060060", "pepe@gmail.com")
    }

def main():
 flota = crear_flota()
 clientes= crear_clientes_iniciales()
 contador_reservas = 4 # Inicializamos el contador de reservas a 4, que son las iniciales para que empiece a generar ID RES-004
 contador_flota = 3
 flota["1"].alquilar()
 seguir = True

 while seguir:
  print(20*'~')
  print('Menú de gestión de alquileres')
  print('1. Mostrar flota de coches disponibles.')
  print('2. Mostrar flota de coches alquilados.')
  print('3. Añadir un nuevo coche a la flota.')
  print('4. Crear nuevo contrato de alquiler.')
  print('5. Iniciar sesión o registrar nuevo cliente.')
  print('6. Salir.')
  print(20*'~')
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
          flota[str(contador_flota)] = Turismo(matricula, 50, num_plazas)
          print(f"Turismo con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")
      elif tipo == '3':
          matricula = input('Introduce la matrícula del vehículo: ')
          num_plazas = int(input('Introduce el número de plazas: '))
          carga = int(input('Introduce la carga de la Furgoneta: '))
          flota[str(contador_flota)] = Furgoneta(matricula, 50,carga, num_plazas)
          print(f"Furgoneta con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")
      elif tipo == '2':
          matricula = input('Introduce la matrícula del vehículo: ')
          num_plazas = int(input('Introduce el número de plazas: '))
          autonomia_maxima = int(input('Introduce la autonomía máxima: '))
          flota[str(contador_flota)] = Electrico(matricula, 50, 100, autonomia_maxima, num_plazas)
          print(f"Eléctrico con matrícula {matricula} añadido a la flota correctamente con ID {contador_flota}")

  elif opc == '4':
     vehiculo = input('Introduce el índice del coche: ')
     dni_cliente = input('Introduce el Dni del cliente: ')

     str_inicio = input('Introduce la fecha de inicio (DD/MM/AAAA): ')
     dia_i, mes_i, anio_i = str_inicio.split('/')
     fecha_inicio = date(int(anio_i), int(mes_i), int(dia_i))

     str_fin = input('Introduce la fecha de fin (DD/MM/AAAA): ')
     dia_f, mes_f, anio_f = str_fin.split('/')
     fecha_fin = date(int(anio_f), int(mes_f), int(dia_f))

     tipo_licencia = input('Introduce el tipo de licencia: ')
     destino = input('Introduce el destino')
     reserva = Reserva(contador_reservas,flota[str(vehiculo)],dni_cliente, fecha_inicio, fecha_fin, tipo_licencia, destino)

  elif opc == '5':
      continuar = True
      while continuar == True:
          print('Usuario:')
          print('1.Iniciar Sesión:')
          print('2.Registrarse: ')
          elec = input('Escoja una opción: ')
          if elec == '1':
              dni = input('Introduce el dni: ')
              if dni in clientes:
                  print('Bienvenido {clientes[dni]}')
                  continuar = False
              else:  # Meter excepcion
                  print("Este cliente no está registrado.")
          elif elec == '2':
              print("--- Registro de Cliente ---")
              dni = input('Introduce el dni: ')
              if dni not in clientes:
                  #Excepcion
                  nombre = input('Introduce el nombre: ')
                  apellidos = input('Introduce el apellidos: ')
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
                  continuar = False
              else:  # Meter excepcion
                  print("Este cliente ya está registrado.")


  elif opc == '6':
      print("\n--- Consulta de Ficha Técnica ---")
      dni_consulta = input("Introduce el DNI del cliente: ")

      if dni_consulta in clientes:
          # Llamamos al método que creamos en la clase Cliente
          clientes[dni_consulta].mostrar_ficha_tecnica()
      else:
          print(f"Error: No existe ningún cliente registrado con el DNI {dni_consulta}.")

  elif opc == '7':
   seguir = False
if __name__ == "__main__":
 main()

