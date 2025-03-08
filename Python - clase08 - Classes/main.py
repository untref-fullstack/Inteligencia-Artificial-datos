from res.productos import productos
from res.Producto import Producto
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def buscar_producto_por_codigo(codigo):
    for prod in productos:
        if prod["codigo"] == codigo:
            return prod
    return None

def main():
    limpiar_pantalla()

    codigo = input("Ingrese el código del producto: ")
    datos_producto = buscar_producto_por_codigo(codigo)
    
    if datos_producto:
        producto = Producto(datos_producto)
        print(f"{producto.nombre} Precio de lista: $ {producto.precio:.2f}. Con IVA: $ {producto.precio_con_iva():.2f}")
    else:
        print("Producto no encontrado.")

if __name__ == "__main__":
    main()