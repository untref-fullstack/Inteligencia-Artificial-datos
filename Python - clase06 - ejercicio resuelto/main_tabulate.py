from tabulate import tabulate
from data.productos import productos

# EJEMPLO RESUELTO: PARA COMPARTIR CON ESTUDIANTES EN LA CLASE 07

# Función 1: Buscar producto por nombre
def buscar_producto_por_nombre(nombre):
    nombre = nombre.strip().lower()                 # Normaliza el nombre (sin espacios y en minúsculas)
    for producto in productos:
        if nombre in producto["nombre"].lower():    # Compara el nombre en minúsculas
            return tabulate([producto], headers="keys", tablefmt="github")
    return "Producto no encontrado."

# Función 2: Filtrar productos por categoría
def filtrar_por_categoria(categoria):
    categoria = categoria.strip().lower()           # Normaliza la categoría
    productos_filtrados = [producto for producto in productos if categoria in producto["categoria"].lower()]
    if productos_filtrados:
        return tabulate(productos_filtrados, headers="keys", tablefmt="github")
    return "No se encontraron productos con esa categoría."

# Función 3: Filtrar productos por precio
def filtrar_por_precio(precio):
    productos_filtrados = [producto for producto in productos if producto["importe"] >= precio]
    if productos_filtrados:
        return tabulate(productos_filtrados, headers="keys", tablefmt="github")
    return "No se encontraron productos con un precio igual o superior."

# Búsquedas sobre las funciones creadas
producto_buscado = buscar_producto_por_nombre("smartphone samsung")
print('Buscar por nombre: \n', producto_buscado)

productos_categoria = filtrar_por_categoria("celulares")
print('Filtrar por categoría: \n', productos_categoria)

productos_precio = filtrar_por_precio(5000)
print('Filtrar por precio: \n', productos_precio)
