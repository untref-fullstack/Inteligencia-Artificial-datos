import datetime

entrada = input("Ingrese una fecha (dd/mm/yyyy): ")

try:
    fecha = datetime.datetime.strptime(entrada, "%d/%m/%Y")
    print("🗓️ Fecha válida:", fecha.date())
except ValueError:
    print("⛔️ Formato incorrecto. Use dd/mm/yyyy")