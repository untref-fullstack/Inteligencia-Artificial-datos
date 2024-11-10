# PROFE: Ejemplo práctico (diapo 59), para que lo realices en vivo.
# OBJETIVO: Combinar el uso de map, filter, reduce, en un mismo caso de uso.

from functools import reduce

precios = [1500, 1800, 2200, 8100, 4500, 5400, 7100, 2500, 5800, 3100]

descuento = 1.15    # 15% de descuento
iva = 1.20          # 20% de iva
stock = 400         # unidades de stock físico de cada producto
precio_base = 5000  # El precio base de un producto considerado caro

def aplicar_descuento(x):
  return x / descuento
  # return round(x / descuento, 2) # aplicalo luego, con la diapositiva 66
  
def calcular_preciofinal(x):
  return x * iva
  # return round(x * iva, 2)       # aplicalo luego, con la diapositiva 66

def obtener_precios_elevados(x):
  return x > precio_base

def calcular_stock_valorizado(acc, x):
  return acc + (x * 400)

precios_con_descuento = map(aplicar_descuento, precios)
precios_finales = map(calcular_preciofinal, precios)
precios_altos = filter(obtener_precios_elevados, precios)
resultado_stock = reduce(calcular_stock_valorizado, precios)

print(list(precios_con_descuento))
print(list(precios_finales))
print(f'Precio superior a 5K: {list(precios_altos)}')
print(f'Stock valorizado: {resultado_stock}')