def calcular(nro1, nro2, ope):
    try:
        if ope == "suma":
            res = nro1 + nro2
        elif ope == "resta":
            res = nro1 - nro2
        elif ope == "multiplica":
            res = nro1 * nro2
        elif ope == "divide":
            res = nro1 / nro2
        else:
            res = "⛔️ Algo falló. No deberías estar aquí."

        print("🔢: " + str(res))

    except Exception as e:
        print("⛔️ Se ha producido un error inesperado al intentar calcular.")



# calcular(12, "Untref", "resta")





### NameError

# try:
#     numero_a = 15

#     resultado = numero_a * numero_b

# except NameError:
#     print("Se ha producido un error: variable no definida.")


