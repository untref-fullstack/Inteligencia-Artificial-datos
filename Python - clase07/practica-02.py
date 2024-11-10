# COMPLEMENTO DEL EJERCICIO, PARTE 2
from functools import reduce

# listas de temperaturas por semana
semana_1 = [21.0, 25.0, 22.0, 24.0, 23.0, 25.0, 25.0]
semana_2 = [26.0, 25.0, 26.0, 27.0, 27.0, 28.0, 25.0]
semana_3 = [29.0, 27.0, 28.0, 29.0, 29.0, 31.0, 30.0]
semana_4 = [29.0, 27.0, 29.0, 30.0, 29.0, 29.0, 32.0]

semanas = [semana_1, semana_2, semana_3, semana_4]

# Función para sumar elementos de la lista
def sumar(x, y):
    return x + y

# Calculamos promedio de una lista con reduce()
def promedio(lista):
    total = reduce(sumar, lista)    # Usamos reduce con la función sumar
    return total / len(lista)       # Dividimos por la cantidad de elementos

# Calculamos promedio de cada semana
promedios_semanales = [promedio(semana) for semana in semanas]

# Imprimimos promedios semanales
for i, promedio_semana in enumerate(promedios_semanales, 1):
    print(f'Promedio semana {i}: {round(promedio_semana, 2)}')

# Calculamos e Imprimimos promedio mensual
promedio_mensual = promedio(promedios_semanales)

print(f'\nPromedio mensual: {round(promedio_mensual, 2)}')