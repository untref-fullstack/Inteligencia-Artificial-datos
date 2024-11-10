lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista_anidada[1])     # salida: [4, 5, 6]
print(lista_anidada[2][0])  # salida: 7


# AGREGAR UN ELEMENTO
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_anidada[1].append(10) 

print(lista_anidada)


# MODIFICAR UN ELEMENTO
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_anidada[2][2] = 10

print(lista_anidada[2]) # Salida: [7, 8, 10]


# ELIMINAR UN ELEMENTO DE UNA SUBLISTA, POR SU VALOR
lista_anidada = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]
lista_anidada[1].remove(6)

print(lista_anidada[1]) # Salida: [4, 5, 10]


# ELIMINAR UN ELEMENTO DE UNA SUBLISTA, A PARTIR DE SU ÍNDICE
lista_anidada = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]
del lista_anidada[1][3]

print(lista_anidada[1]) # Salida: [4, 5, 6]


# COMPRENSIÓN DE LISTAS EN PYTHON

# Recorrer listas anidadas con un bucle for python
for sublista in lista_anidada:
    for elemento in sublista:
        print(elemento)


# Simplificando el doble bucle for anterior, a una sola línea de código
lista_aplanada = [elem for sublista in lista_anidada for elem in sublista]
print(lista_aplanada)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9]



# contenido generado a partir del CASO DE USO realizado en clase

semana_1 = [21.0, 25.0, 22.0, 24.0, 23.0, 25.0, 25.0]
semana_2 = [26.0, 25.0, 26.0, 27.0, 27.0, 28.0, 25.0]
semana_3 = [29.0, 27.0, 28.0, 29.0, 29.0, 31.0, 30.0]
semana_4 = [29.0, 27.0, 29.0, 30.0, 29.0, 29.0, 32.0]

temperaturas_mensuales = [semana_1, semana_2, semana_3, semana_4]

# FUNCIONES DE ORDEN SUPERIOR

## ejemplo con map()

def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4]
resultados = filter(cuadrado, numeros)

print(list(resultados))


## ejemplo con filter()

def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7]
pares = filter(es_par, numeros)

print(list(pares))  # Salida: [2, 4, 6]


## ejemplo con reduce()
from functools import reduce

def suma(x, y):
    return x + y

numeros = [1, 2, 3, 4]

resultado = reduce(suma, numeros)