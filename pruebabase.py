from Backend.conexion import Miconexion

def obtener_productos():
    conexion =Miconexion.obtener_conexion()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT Codigo, Nombre, Stock, Stock_minimo, Precio FROM productos WHERE Activo = 1")
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"🟢 Producto: {fila}")
    except Error as e:
        print("❌ Error al consultar:", e)
    finally:
        cursor.close()
        conexion.close()
        
        
if __name__ == "__main__":
    obtener_productos()