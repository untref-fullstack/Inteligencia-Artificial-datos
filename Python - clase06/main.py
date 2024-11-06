from lists.productos import productos
from logic.utils import buscar_producto, filtrar_productos_precio


resultado = buscar_producto('nombre', 'Notebook i5', productos)
filtrados = filtrar_productos_precio(1100, productos)

print('Producto encontrado: ', resultado)

if len(filtrados):
    print('Productos filtrados: \n', filtrados)

# print(productos)