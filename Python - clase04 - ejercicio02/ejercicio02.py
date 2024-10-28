# importar módulos instalados
from tabulate import tabulate

# Lista inicial de países
paises = ['Argentina', 'Venezuela', 'Uruguay', 'Chile', 'Paraguay']

def listar_paises():
    tabla = [[idx + 1, paises] for idx, paises in enumerate(paises)]

    print("")
    print("Lista de países:")
    print(tabulate(tabla, headers=["Id", "Países"], tablefmt="github"))
    print("")

def normalizar_pais(pais):
    return pais.strip().capitalize()

def agregar_pais():
    nuevo_pais = input("🌎 Ingresa el nuevo país: ")
    if nuevo_pais:
        nuevo_pais = normalizar_pais(nuevo_pais)
    
    if not nuevo_pais:
        print("✋ ingresa un nombre de país válido.")
        return
    
    if nuevo_pais in paises:
        print("✋ " + nuevo_pais + " ya existe en la lista.")
    else:
        paises.append(nuevo_pais)
        print("✅ " + nuevo_pais + " ha sido agregado a la lista.")

def quitar_pais():
    pais_a_eliminar = input("🌎 Ingresa el nombre del país a eliminar: ")
    pais_a_eliminar = normalizar_pais(pais_a_eliminar)
    
    if not pais_a_eliminar:
        print("✋ Ingresa un nombre de país válido.")
        return
    
    if pais_a_eliminar in paises:
        paises.remove(pais_a_eliminar)
        print("✅ " + pais_a_eliminar + " ha sido eliminado de la lista.")
    else:
        print("⛔️ " + pais_a_eliminar + " no se encuentra en la lista.")

def ordenar_paises():
    paises.sort()
    # paises.reverse()
    print(str(paises))

listar_paises()

# # ordenar_paises()

# # Agregar un país
# agregar_pais()  # Solicita el país a agregar

# # Listar países nuevamente
# listar_paises()

# # Quitar un país
# quitar_pais()   # Solicita el país a eliminar

# # Listar países finales
# listar_paises()
