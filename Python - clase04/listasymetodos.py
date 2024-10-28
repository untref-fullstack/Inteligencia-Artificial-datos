paises = ['Argentina', 'Venezuela', 'Uruguay', 'Chile', 'Paraguay']
# Bolivia, Perú, Colombia, Guyana

def limpiar_pantalla():
    import os

    if (os.system.__name__ == 'MacOS' or 'Linux'): # si estamos en Mac o Linux
        os.system('clear')
    else: # Sino (es asumimos que estamos en Windows)
        os.system('cls')

def mostrar_lista():
    # limpiar_pantalla()
    print(str(paises))

def agregar_pais():
    nuevo_pais = input('🌎 Ingresa un nuevo país: ')
    paises.append(nuevo_pais)
    mostrar_lista()

def quitar_pais():
    a_quitar = input('🌎 Ingresa el país a quitar: ')
    paises.remove(a_quitar.strip())
    print(a_quitar + ' ha sido quitado de la lista.')

def encontrar_pais():
    a_buscar = input('🔎 Ingresa el país a buscar: ')
    indice = paises.index(a_buscar)
    print('El país ' + a_buscar + ' fue encontrado en la posición: ' + str(indice))



mostrar_lista() # Función Principal