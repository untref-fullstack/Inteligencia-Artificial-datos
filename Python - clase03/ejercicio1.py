def calcular(nro_a, nro_b, ope):

    print(str(ope or 'error'))

    if (ope == 'suma'):
        resultado = nro_a + nro_b
    elif (ope == 'resta'):
        resultado = nro_a - nro_b
    elif (ope == 'multiplica'):
        resultado = nro_a * nro_b
    elif (ope == 'divide'):
        resultado = nro_a / nro_b
    else: 
        resultado = "⛔️ Error en la operación."

    print("Resultado: " + str(resultado))

calcular(21, 22, "multiplica")