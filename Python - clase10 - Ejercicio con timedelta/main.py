from facturas import facturas
from datetime import datetime, timedelta
from tabulate import tabulate

def calcular_fechas_cobro(facturas):
    for factura in facturas:
        fecha_factura = datetime.strptime(factura["fechaFactura"], "%Y-%m-%d")
        vencimiento = factura["vencimiento"]
        fecha_cobro = fecha_factura + timedelta(days=vencimiento)
        factura["fechaCobro"] = fecha_cobro.strftime("%Y-%m-%d")

# Ejecutar la función
calcular_fechas_cobro(facturas)

# Mostrar resultados en formato tabular
headers = ["Cliente", "Nro Factura", "Importe", "Fecha Factura", "Fecha Cobro", "Vencimiento"]
tabla = [[f["cliente"], f["nroFactura"], f["importe"], f["fechaFactura"], f["fechaCobro"], f["vencimiento"]] for f in facturas]

print(tabulate(tabla, headers=headers, tablefmt="grid"))
