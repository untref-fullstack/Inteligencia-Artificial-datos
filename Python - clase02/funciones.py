def nombre_de_la_funcion():
    # Cuerpo de la función
    print("Hola, soy una función simple.")

def saludar():
    nombre = input("Ingresa tu nombre:")
    if nombre:
      print("Benvenid@: " + nombre)
      mostrar_clave()
    else:
      print("Ingresa un nombre válido. ⛔️")
   
   
def mostrar_clave():
    token = "f51b02b8-7d40-469c-8d14-db347443ad5d"
    print("Su token es: " + token)

# saludar() # Llamamos a la función 

import datetime

def mostrar_fecha():
    fecha_actual = datetime.datetime.now()
    print("La fecha y hora actual es:", fecha_actual)

# Llamamos a la función
mostrar_fecha()


## ESPACIO DE TRABAJO FINAL
# posible resolución de la consigna propuesta

# Variables globales
temp_diciembre = 0
temp_enero = 0
temp_febrero = 0
temp_marzo = 0
promedio = 0
mensaje = ""

def solicitar_temperaturas():
    """Solicita las temperaturas mínimas promedio de los meses."""
    global temp_diciembre, temp_enero, temp_febrero, temp_marzo
    temp_diciembre = float(input("Ingresa la temp mínima promedio del mes de diciembre: "))
    temp_enero = float(input("Ingresa la temp mínima promedio del mes de enero: "))
    temp_febrero = float(input("Ingresa la temp mínima promedio del mes de febrero: "))
    temp_marzo = float(input("Ingresa la temp mínima promedio del mes de marzo: "))

def calcular_promedio():
    """Calcula el promedio de las temperaturas."""
    global promedio
    promedio = (temp_diciembre + temp_enero + temp_febrero + temp_marzo) / 4

def validar_clima():
    """Valida el clima según el promedio y asigna un mensaje."""
    global mensaje
    if promedio < 10:
        mensaje = "El clima es frío. 🥶"
    elif 10 <= promedio <= 15:
        mensaje = "El clima es fresco. ❄️"
    elif 16 <= promedio <= 22:
        mensaje = "El clima es templado. ⛅️"
    else:
        mensaje = "El clima es caluroso. 🌞 ¡Prepárate para disfrutar del sol!"

def imprimir_mensaje():
    """Imprime el mensaje resultante."""
    print(mensaje)

def ejecutar_aplicacion():
    """Función principal que coordina todo el proceso."""
    solicitar_temperaturas()
    calcular_promedio()
    validar_clima()
    imprimir_mensaje()

# Invocamos la función principal
ejecutar_aplicacion()

