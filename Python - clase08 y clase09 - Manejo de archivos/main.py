import json
from tabulate import tabulate

ruta_base = 'res/'

def leer_archivo_txt():
    with open(ruta_base + 'empleados.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)


# leer_archivo_txt()

def leer_empleados_json():

    try:
        with open(ruta_base + 'empleados.json', "r", encoding="utf-8") as archivo:
            empleados = json.load(archivo)
        
        if isinstance(empleados, list):
            print(tabulate(empleados, headers="keys", tablefmt="grid"))
        else:
            print("⛔️ El archivo JSON no contiene una lista de empleados válida.")

    except FileNotFoundError:
        print(f"⛔️ Error: No se encontró el archivo en {ruta_base}")

    except json.JSONDecodeError:
        print("⛔️ Error: El archivo JSON tiene un formato incorrecto.")


# leer_empleados_json()