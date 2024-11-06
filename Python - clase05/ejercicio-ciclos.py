paises = ['Argentina', 'Venezuela', 'Uruguay', 'Perú', 'Chile', 'Paraguay', 'Bolivia', 'Colombia', 'Brasil', 'Ecuador', 'Guyana']

def limpiar_pantalla():
    import os

    if (os.system.__name__ == 'MacOS' or 'Linux'): # si estamos en Mac o Linux
        os.system('clear')
    else: # Sino (es asumimos que estamos en Windows)
        os.system('cls')

def mostrar_lista():
    limpiar_pantalla()
    print(str(paises))

mostrar_lista() # Función Principal