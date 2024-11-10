temperaturas_mensuales = []     # Lista principal

def cargar_temperaturas(semana):
    print(f'Ingresa las temperaturas para {semana}:')
    temperaturas = []

    for i in range(7):          # 7 temperaturas por cada semana
        while True:
            try:
                temp = input(f'Ingresa la temperatura del día {i + 1}: ')
                temp = temp = float(temp)
                temperaturas.append(temp)
                break
            except ValueError:
                print('⛔️ Ingresa un valor numérico válido para la temperatura.')
    return temperaturas

# Cargamos las temperaturas diarias, para cada semana
semana_1 = cargar_temperaturas('Semana 1')
semana_2 = cargar_temperaturas('Semana 2')
semana_3 = cargar_temperaturas('Semana 3')
semana_4 = cargar_temperaturas('Semana 4')

# Agregamos cada sublista a la lista principal
temperaturas_mensuales.append(semana_1)
temperaturas_mensuales.append(semana_2)
temperaturas_mensuales.append(semana_3)
temperaturas_mensuales.append(semana_4)

# Mostrar la lista de sublistas
print('\nTemperaturas mensuales registradas:')
for i, semana in enumerate(temperaturas_mensuales, start=1):
    print(f'Semana {i}: {semana}')

'''
    PROFE: dejo por aquí un ejemplo ya completo, por si querés usarlo en otro ejercicio
    Será útil para compartir con estudiantes cuando vayan a elaborar el segundo ejercicio

    Semana 1: [21.0, 25.0, 22.0, 24.0, 23.0, 25.0, 25.0]
    Semana 2: [26.0, 25.0, 26.0, 27.0, 27.0, 28.0, 25.0]
    Semana 3: [29.0, 27.0, 28.0, 29.0, 29.0, 31.0, 30.0]
    Semana 4: [29.0, 27.0, 29.0, 30.0, 29.0, 29.0, 32.0]
'''