import mysql.connector
# Configuración de la conexión
config = {
    "host": "localhost",  # Dirección del servidor MySQL (puede ser una IP o dominio)
    "user": "root",       # Usuario de MySQL
    "password": "Fluna.2103",   # Contraseña del usuario
    "database": "northwind"  # Nombre de la base de datos (opcional)
}

try:
    # Establecer la conexión
    conexion = mysql.connector.connect(**config)

    if conexion.is_connected():
        print("Conexión exitosa a MySQL:", conexion.database)

except mysql.connector.Error as err:
    print(f"Error al conectar: {err}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")