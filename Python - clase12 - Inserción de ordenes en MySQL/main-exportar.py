import mysql.connector
import csv

# Conexión a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='usuario',
    password='contraseña',
    database='ecommerce'
)
cursor = conn.cursor()

# Ejecutamos la consulta
cursor.execute("SELECT * FROM categorias;")

# Obtenemos todos los registros
rows = cursor.fetchall()

# Obtenemos los nombres de columnas desde cursor.description
column_names = [desc[0] for desc in cursor.description]

# Escribimos en el archivo CSV
with open('categorias.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Escribimos el encabezado
    writer.writerow(column_names)
    
    # Escribimos los datos
    for row in rows:
        writer.writerow(row)

# Cerramos la conexión
cursor.close()
conn.close()
