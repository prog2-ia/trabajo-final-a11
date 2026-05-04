from datetime import date
from ENTIDADES.vehiculos import  Vehiculo
from ENTIDADES.turismo import Turismo
from ENTIDADES.furgoneta import Furgoneta
from ENTIDADES.electrico import Electrico
from SERVICIOS.reserva import Reserva

def crear_flota(): #Creamos una flota inicial de vehículos
  flota = {"1": Turismo("1111-AAA", precio_base_dia=50, num_plazas=5,disponible = True),
          "2": Furgoneta("2222-BBB", precio_base_dia=60, carga=1000, num_plazas=3,disponible=True),
          "3": Electrico("3333-CCC", precio_base_dia=80, nivel_bateria=100, autonomia_maxima=400, num_plazas=5,disponible=True)}
  return flota


def main():
 flota = crear_flota()
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
  print('5. Salir.')
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
     reserva = ''
     vehiculo = input('Introduce el índice del coche: ')
     #dni_cliente = input('Introduce el Dni del cliente: ')
     fecha_inicio = date(input('Introduce la fecha de inicio: '))
     fecha_fin = date(input('Introduce la fecha de fin:  '))
     tipo_licencia = input('Introduce el tipo de licencia: ')
     destino = input('Introduce el destino')
     reserva = Reserva(contador_reservas,flota[str(vehiculo)],dni_cliente, fecha_inicio, fecha_fin, tipo_licencia, destino)
     reserva.generar_contrato_txt()
     flota[str(vehiculo)].alquilar()



  elif opc == '5':
   seguir = False
if __name__ == "__main__":
 main()
