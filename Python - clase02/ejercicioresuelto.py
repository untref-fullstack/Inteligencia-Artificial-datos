# Inicializar las variables
temp_diciembre = 0
temp_enero = 0
temp_febrero = 0
temp_marzo = 0

# Solicitar al usuario que ingrese las temps
temp_diciembre = float(input("Ingresa la temp mínima promedio del mes de diciembre: "))
temp_enero = float(input("Ingresa la temp mínima promedio del mes de enero: "))
temp_febrero = float(input("Ingresa la temp mínima promedio del mes de febrero: "))
temp_marzo = float(input("Ingresa la temp mínima promedio del mes de marzo: "))

# Calcular el promedio
resultado = (temp_diciembre + temp_enero + temp_febrero + temp_marzo) / 4

# Validar el clima según el promedio
if resultado < 10:
    mensaje = "El clima es frío. 🥶"
elif 10 <= resultado <= 15:
    mensaje = "El clima es fresco. ❄️"
elif 16 <= resultado <= 22:
    mensaje = "El clima es templado. ⛅️"
else:
    mensaje = "El clima es caluroso. 🌞 ¡Prepárate para disfrutar del sol!"

# Imprimir el mensaje resultante
print(mensaje)