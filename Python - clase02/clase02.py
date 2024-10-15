# is digit y condicional if
edad = input("Ingresa tu edad: ")

if edad.isdigit():
    print("Has ingresado un valor numérico: " + str(edad))

nombre = input("Ingresa tu nombre: ")

if nombre:
    print("Has ingresado una cadena de texto: " + nombre)

# isdigit e isnumeric
edad = input("Ingresa tu edad: ")

if edad.isdigit():
    print("Has ingresado un valor numérico: " + str(edad))

if edad.isnumeric():
    print("Has ingresado un valor numérico: " + str(edad))


nombre = input("Ingresa tu nombre: ")

if nombre:      
    print("Has ingresado una cadena de texto: " + nombre)


nombre = input("Ingresa tu nombre: ")

if nombre.strip().title() == "Cameron Howe":
    print("Bienvenid@: " + nombre.strip().title())

# condicional if - elif - else 
temperatura = float(input("Ingresa la temperatura actual: "))

# Evaluar la temperatura con condicionales múltiples if - elif - else 
if temperatura < 10:
    print("Está frío. ❄️")
elif temperatura >= 10 and temperatura < 20:
    print("Está fresco. 🧤")
elif temperatura <= 20 and temperatura < 30:
    print("Está templado. ⛅️")
else:
    print("Está caluroso. 🔥")

# Evaluar la temperatura con expresiones lógicas simplificadas
if temperatura < 10:
    print("Está frío. ❄️")
elif 10 <= temperatura < 20:
    print("Está fresco. 🧤")
elif 20 <= temperatura < 30:
    print("Está templado. ⛅️")
else:
    print("Está caluroso. 🔥")

