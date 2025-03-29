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

def actualizar_precios_categoria():
    categoria_id = input("Ingresa el ID de la categoría a actualizar: ")
    porcentaje = float(input("Ingresa el '%' de aumento (Ej: 10 para 10%): "))

    sql = """
             UPDATE productos
             SET precio = precio * (1 + %s / 100)
             WHERE categoria_id = %s
          """

    valores = (porcentaje, categoria_id)

    if ejecutar_consulta(sql, valores) is None:
        print(f"Precios de Categoría: {categoria_id} incrementados un {porcentaje}%.")
    else:
        print("No se pudo actualizar los precios.")

def ejecutar_consulta(sql, valores = None):
    conexion, cursor = conectar_mysql()

    if not conexion or not cursor:
        return None

    try:
        cursor.execute(sql, valores) if valores else cursor.execute(sql)

        if sql.strip().lower().startswith("select"):
            resultado = cursor.fetchall()
        else:
            conexion.commit()
            resultado = None

        return resultado
    
    except mysql.connector.Error as err:
        print(f"⛔️ Error ejecutando la consulta: {err}")
        return None
    
    finally:
        cursor.close()
        conexion.close()

def visualizar_categorias():
    sql = "SELECT * FROM categories;"
    resultado = ejecutar_consulta(sql)

    if resultado is not None:
        print("\n📌 Categorías registradas en la base de datos:")
        for fila in resultado:
            print(fila)
    else:
        print("⚠️ No se pudo ejecutar la consulta.")

def visualizar_productos():
    sql = "SELECT productId, productName, unitPrice FROM products;"
    resultado = ejecutar_consulta(sql)

    if resultado is not None:
        print("\n📌 Listado de Productos en Northwind:")
        for fila in resultado:
            print(fila)
    else:
        print("⚠️ No se pudo ejecutar la consulta.")

def actualizar_precio_producto():
    conexion, cursor = conectar_mysql()
    if not conexion:
        return
    
    codigo_producto = input("Ingrese el código del producto: ")
    nuevo_precio = input("Ingrese el nuevo precio del producto: ")
    
    try:
        nuevo_precio = float(nuevo_precio)
        query = """
            UPDATE products 
            SET UnitPrice = %s 
            WHERE ProductID = %s
        """
        cursor.execute(query, (nuevo_precio, codigo_producto))
        conexion.commit()
        print("✅ Precio actualizado correctamente.")

    except ValueError:
        print("❌ Error: El precio ingresado no es un número válido.")

    except mysql.connector.Error as err:
        print(f"❌ Error al actualizar: {err}")

    finally:
        cursor.close()
        conexion.close()

conexion, cursor = conectar_mysql()

if conexion:
    print("✅ Conexión exitosa a MySQL")
    conexion.close()
else:
    print("❌ Error al conectar a MySQL")

# actualizar_precio_producto()