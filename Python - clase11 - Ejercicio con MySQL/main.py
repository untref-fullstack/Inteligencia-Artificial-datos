import mysql.connector
import os
import dotenv
from tabulate import tabulate

dotenv.load_dotenv()

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database="northwind"
        )
        cursor = conexion.cursor()
        return conexion, cursor
    except mysql.connector.Error as err:
        print(f"❌ Error al conectar a MySQL: {err}")
        return None, None

def probar_conexion():
    conexion, cursor = conectar_mysql()
    if conexion:
        print("✅ Conexión exitosa a MySQL")
        conexion.close()
    else:
        print("❌ Error al conectar a MySQL")

def seleccionar_datos(tabla):
    conexion, cursor = conectar_mysql()
    if not conexion:
        return
    
    try:
        query = f"SELECT * FROM {tabla}"
        cursor.execute(query)
        resultados = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        print(tabulate(resultados, headers=columnas, tablefmt="grid"))
    except mysql.connector.Error as err:
        print(f"❌ Error al ejecutar la consulta: {err}")
    finally:
        cursor.close()
        conexion.close()

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    limpiar_consola()
    probar_conexion()
    tabla = input("Ingrese el nombre de la tabla a consultar: ")
    seleccionar_datos(tabla)
