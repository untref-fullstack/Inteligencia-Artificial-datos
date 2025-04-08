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
            return conexion, conexion.cursor()
        
    except mysql.connector.Error as err:
        print(f"⛔️ Error al conectar a MySQL: {err}")
        return None, None

def solicitar_categoria_a_eliminar():
    print("🗑️ Eliminación de categoría")
    nombre = input("Ingrese el nombre de la categoría a eliminar: ")
    return nombre

def eliminar_categoria(nombre):
    conexion, cursor = conectar_mysql()
    if not conexion or not cursor:
        return

    try:
        sql = "DELETE FROM Categories WHERE CategoryName = %s"
        cursor.execute(sql, (nombre,))
        conexion.commit()

        if cursor.rowcount > 0:
            print(f"✅ Categoría '{nombre}' eliminada correctamente.")
        else:
            print(f"⚠️ No se encontró una categoría con el nombre '{nombre}'.")

    except mysql.connector.Error as err:
        print(f"⛔️ Error al eliminar la categoría: {err}")
        conexion.rollback()

    finally:
        cursor.close()
        conexion.close()


if __name__ == "__main__":
    nombre_categoria = solicitar_categoria_a_eliminar()
    eliminar_categoria(nombre_categoria)
