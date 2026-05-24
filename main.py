# main.py
from EJECUTABLE.menu import main as iniciar_aplicacion

if __name__ == "__main__":
    try:
        iniciar_aplicacion()
    except KeyboardInterrupt:
        print("Saliendo del programa...")