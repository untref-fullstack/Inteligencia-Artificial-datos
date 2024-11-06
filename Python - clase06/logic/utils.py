def buscar_producto(key, valor, list):

    if len(list) > 0:
        for producto in list:
            if producto[key] == valor:
                return producto
            return '⛔️ No se encontró producto con el valor indicado.'

def filtrar_productos_precio(valor, list):
    
    resultado = []
    if len(list) > 0:
        for producto in list:
            if producto['importe'] >= float(valor):
                resultado.append(producto)
        return resultado

