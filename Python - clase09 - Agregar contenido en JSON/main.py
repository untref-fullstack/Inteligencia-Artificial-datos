import json
from tabulate import tabulate

def leer_y_agregar_empleado():
    ruta_archivo = "res/empleados.json"
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            empleados = json.load(archivo)
        
        if not isinstance(empleados, list):
            print("El archivo JSON no contiene una lista válida de empleados.")
            return
        
        # Mostrar empleados actuales
        print("Empleados actuales:")
        print(tabulate(empleados, headers="keys", tablefmt="grid"))
        
        # Solicitar datos del nuevo empleado
        nuevo_empleado = {
            "ID": int(input("Ingrese ID del nuevo empleado: ")),
            "Nombre": input("Ingrese Nombre: "),
            "Cargo": input("Ingrese Cargo: "),
            "Salario": float(input("Ingrese Salario: "))
        }
        
        empleados.append(nuevo_empleado)
        
        # Guardar la lista actualizada en el archivo JSON
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(empleados, archivo, indent=4, ensure_ascii=False)
        
        print("Empleado agregado exitosamente.")
        print("Lista actualizada de empleados:")
        print(tabulate(empleados, headers="keys", tablefmt="grid"))
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato incorrecto.")
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar datos correctos.")

# Llamada a la función
leer_y_agregar_empleado()
