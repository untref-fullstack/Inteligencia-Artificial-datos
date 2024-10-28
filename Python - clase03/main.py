# Buscamos que el usuario ingrese su nombre, para poder saludarlo

nombre = ""

def saludar(): 
    nombre = input("Ingresa tu nombre: ")

    if nombre:
        print("Bienvenid@, " + nombre)


# saludar()

####################################################################

# Validación utilizando los métodos de variables

def saludar(): 
    nombre = input("Ingresa tu nombre: ")

    if not nombre.isspace() and len(nombre.strip()) > 0:
        print("Bienvenid@, " + nombre.strip().title())
    else:
        print("⛔️ Ingresa un nombre válido.")
    

# saludar()

####################################################################

# Funciones con parámetro(s)

def saludar(nombre):
    print("Hola, " + nombre + "!")

# parámetros múltiples

def sumar(a, b):
    resultado = a + b
    print("Resultado: " + str(resultado))

# sumar(21, 75)

# parámetros múltiples y retorno
def sumar(a, b):
    return a + b

# resultado = sumar(5, 3)  # resultado: 8
# print(resultado)

####################################################################

# Ejemplo de parámetros y retorno para realizar un cálculo

def calcular(num1, num2, ope):
    if ope == 'suma':
        return num1 + num2
    elif ope == 'resta':
        return num1 - num2
    elif ope == 'multiplica':
        return num1 * num2
    elif ope == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "⛔️ Error: División por cero"
    else:
        return "⛔️ Error: Operación no válida"

# Ejemplo de uso
resultado = calcular(10, 5, 'suma')
print(resultado)

resultado = calcular(1240, 550, 'resta')
print(resultado)

resultado = calcular(1975, 49, 'multiplica')
print(resultado)

resultado = calcular(1984, 14, 'divide')
print(resultado)

