import json

with open('productos.json', 'r', encoding='utf-8') as f:
    productos = json.load(f)

print(productos[0]["nombreProducto"])  # Accedemos como a cualquier diccionario

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='usuario',
    password='contraseña',
    database='northwind'
)
cursor = conn.cursor()

query = """
INSERT INTO productos (
    nombreProducto, 
    importe, 
    idCategoria
) VALUES (
    %(nombreProducto)s, 
    %(importe)s, 
    %(idCategoria)s
)
"""

for producto in productos:
    cursor.execute(query, producto)

conn.commit()
cursor.close()
conn.close()
