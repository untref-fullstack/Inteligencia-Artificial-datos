import csv
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='usuario',
    password='contraseña',
    database='ecommerce'
)
cursor = conn.cursor()

query = """
    INSERT INTO productos (nombreProducto, importe, idCategoria)
    VALUES (%(nombreProducto)s, %(importe)s, %(idCategoria)s)
"""

with open('productos.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(query, row)

conn.commit()
cursor.close()
conn.close()
