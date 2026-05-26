# ***Sistema de Gestión de Alquiler de Vehículos***
## Creadores
* **Máximo Gil Carcaño** - [maximogil11]
* **Hugo Sánchez Recio** - [hugosanchez13]

## Propósito del Proyecto:
Esta aplicación es un sistema de gestión para una flota de vehículos de alquiler. Está diseñada utilizando los principios de la Programación Orientada a objetos en Python que hemos visto en clase hasta ahora
El programa permite administrar diferentes tipos de vehículos jerarquizados (Turismos, Furgonetas y Eléctricos), aplicando políticas de precios específicas y penalizaciones. Además, gestiona reservas normales, genera contratos en formato texto (`.txt`)

El proyecto cumple con requerimientos avanzados como:
* Uso de herencia, polimorfismo y clases abstractas (`ABC`).
* Encapsulamiento de atributos privados.
* Manejo de excepciones.
* Modularidad (separación en diferentes archivos `.py`).

## Estructura del Proyecto
El código está dividido en módulos para facilitar su mantenimiento y escalabilidad:

* `main.py`: Punto de entrada principal de la aplicación.
* `EJECUTABLE/`: Contiene `menu.py`, que maneja toda interfaz de usuario y los bucles del programa.
* `ENTIDADES/`: Contiene las clases principales (`vehiculos.py`, `turismo.py`, `furgoneta.py`, `electrico.py`, `clientes.py`).
* `SERVICIOS/`: Contiene la lógica de operaciones y facturación (`reserva.py`).
* `EXCEPCIONES/`: Define errores personalizados (`excepciones.py`) para evitar que el programa colapse.
* `CONTRATOS/`: Carpeta autogenerada donde se guardan los "recibos" de alquiler en formato `.txt`.
* `DATOS/`: Carpeta autogenerada donde se almacena la base de datos local.

# Archivos Pickle
Este proyecto guarda los datos, es decir, no pierdes la información al cerrar la consola.
Todo el estado de la aplicación (la flota de vehículos, los clientes registrados y el historial de reservas) se guarda automáticamente en el archivo **`DATOS/datos_rentacar.pkl`** mediante la librería  `pickle` de Python. 

* **Autoguardado:** El sistema guarda los datos cada vez que se hace un cambio importante (registrar cliente, añadir coche, alquilar, devolver) y al salir del programa correctamente.
* **Reinicio de la base de datos:** Si en algún momento necesitas hacer pruebas desde cero o la base de datos se corrompe, simplemente **borra el archivo `datos_rentacar.pkl`** y la aplicación volverá a sus valores por defecto en el próximo arranque.

## Instalación

Para hacer funcionar este proyecto en tu entorno local descarga los archivos del proyecto en una carpeta local. Deberías tener los archivos `vehiculos.py`, `reserva.py` , `ejecutable.py` y `requirements.txt`.
1. Crea y activa un entorno virtual:
   bash
   python -m venv env
   # En Windows: env\Scripts\activate
   # En macOS/Linux: source env/bin/activate

2. Instala las dependencias necesarias ejecutando el siguiente comando:
 bash
 pip install -r requirements.txt

## Uso en caso de descargar todo el proyecto
El proyecto está modularizado, pero cuenta con un archivo principal de pruebas llamado ejecutable.py.
Para iniciar el programa y ver la simulación completa del sistema de reservas, simplemente ejecuta el siguiente comando en tu terminal:
Bash
python main.py

## Si no quieres descargar el código fuente ni instalar dependencias, puedes usar la versión del programa generada con PyInstaller:
**Para Linux:**
1. Abre tu terminal en la carpeta `dist/` donde se encuentra el archivo **`RentACar`**.
2. Utilizar el comando `chmod +x RentACar`
3. Ejecútalo escribiendo: `./RentACar`


Al hacerlo, el programa interactuará con las clases de vehiculos.py y reserva.py para crear objetos, calcular las tarifas correspondientes y generar automáticamente los archivos de texto (.txt) con los contratos en tu misma carpeta.


El archivo ejecutable.py funciona de la siguiente manera:

## Ejemplos de Funcionamiento
El código es capaz de procesar diferentes casuísticas. A continuación, se muestra un ejemplo de cómo funciona internamente la creación de una reserva:

1.Creación de un vehículo:
Python
from vehiculos import Turismo
# Crea un turismo con matrícula 1111-AAA, 50€/día base y 5 plazas
mi_coche = Turismo("1111-AAA", precio_base_dia=50, num_plazas=5)


2. Creación de una reserva (Ejemplo con 10% de descuento por más de 7 días):
Python
from reserva import Reserva
from datetime import date


fecha_inicio = date(2026, 3, 15)
fecha_fin = date(2026, 3, 25) # 10 días de alquiler


# El sistema calcula el precio automáticamente y aplica descuentos
mi_reserva = Reserva("RES-001", mi_coche, "12345678A", fecha_inicio, fecha_fin, "B", "Madrid")
mi_reserva.vehiculo.alquilar()
mi_reserva.generar_contrato_txt()


3. Resultado (Contrato generado en .txt): El sistema creará un archivo llamado contrato_RES-001.txt con este contenido generado dinámicamente:
Plaintext
       --- CONTRATO DE ALQUILER ---
        Reserva ID: RES-001
        DNI Cliente: 12345678A
        Vehículo: Turismo Matricula: 1111-AAA, Plazas: 5
        Fechas: 2026-03-15 a 2026-03-25
        Precio Total: 450.0 €
        ----------------------------
