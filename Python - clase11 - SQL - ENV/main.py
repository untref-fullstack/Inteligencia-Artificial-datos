import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de la conexión
config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

try:
    # Establecer la conexión
    conexion = mysql.connector.connect(**config)

    if conexion.is_connected():
        print("Conexión exitosa a MySQL:", conexion.database)
        cursor = conexion.cursor()

        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()

        for tabla in tablas:
            print(tabla[0])

except mysql.connector.Error as err:
    print(f"Error al conectar: {err}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")