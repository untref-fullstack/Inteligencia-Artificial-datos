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

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            conexion.autocommit = True  # Activar autocommit
            return conexion, conexion.cursor()
        
    except mysql.connector.Error as err:
        print(f"⛔️ Error al conectar a MySQL: {err}")
        return None, None

def solicitar_datos_categoria():
    print("📝 Ingreso de nueva categoría")
    nombre = input("Ingrese el nombre de la categoría: ")
    descripcion = input("Ingrese la descripción de la categoría: ")
    return nombre, descripcion

def insertar_categoria(nombre, descripcion):
    conexion, cursor = conectar_mysql()
    if not conexion or not cursor:
        return

    try:
        sql = "INSERT INTO Categories (CategoryName, Description) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, descripcion))
        print("✅ Categoría agregada correctamente.")

    except mysql.connector.Error as err:
        print(f"⛔️ Error al insertar los datos: {err}")
        
    finally:
        cursor.close()
        conexion.close()

if __name__ == "__main__":
    nombre, descripcion = solicitar_datos_categoria()
    insertar_categoria(nombre, descripcion)