# Variables globales para almacenar los datos del usuario
nombre_apellido = ""
edad = 0

def solicitar_nombre_apellido():
    global nombre_apellido
    try:
        nombre_apellido = input("Por favor, ingresa tu nombre y apellido: ")
        if not nombre_apellido.strip():
            raise ValueError("⛔️ El nombre y apellido no pueden estar vacíos.")
        
    except Exception as e:
        print("⛔️ Error: " + str(e))

def solicitar_edad():
    global edad
    try:
        edad = int(input("⛔️ Por favor, ingresa tu edad: "))
        if edad < 0:
            raise ValueError("⛔️ La edad no puede ser negativa.")
        
    except ValueError:
        print("⛔️ Por favor, ingresa un número válido para la edad.")
    except Exception as e:
        print("⛔️ Error: " + str(e))

def recopilar_datos():
    solicitar_nombre_apellido()
    solicitar_edad()
    
    try:
        anio_actual = 2024 
        anio_nacimiento = anio_actual - edad
        
        print("\n¡Bienvenido, " + nombre_apellido + "!")
        print("Tienes " + str(edad) + " años, lo que indica que naciste aproximadamente en " + str(anio_nacimiento) + ".")

    except Exception as e:
        print("⛔️ Error al mostrar los datos: " + str(e))


recopilar_datos() # Llamo a la función principal


'''
Variables Globales:

    Se definen nombre_apellido y edad como variables globales para almacenar los datos ingresados por el usuario.

Funciones:

    solicitar_nombre_apellido(): Pide al usuario su nombre y apellido. Se utiliza un bloque try-except para manejar posibles errores, como ingresar un valor vacío.

    solicitar_edad(): Pide la edad y verifica que sea un número positivo. Se manejan excepciones para asegurar que el input sea válido.

    recopilar_datos(): Llama a las funciones anteriores y calcula el año de nacimiento basado en la edad ingresada. Muestra un mensaje de bienvenida con los datos recogidos.

Ejecución:

    Al final del script, se llama a recopilar_datos() para iniciar el proceso.
'''