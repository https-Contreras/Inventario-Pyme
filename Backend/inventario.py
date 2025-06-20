from Backend.conexion import Miconexion
from PyQt6.QtWidgets import QMessageBox
from Backend.modelos.claseProducto import Producto


class Inventario():
    def agregar_producto(self, codigo, nombre, stock, stock_minimo, precio):
        conexion = Miconexion.obtener_conexion()
        if not conexion:
            print("No se pudo conectar para agregar el producto.")
            return
        try:
            cursor = conexion.cursor()
            sql = """
                INSERT INTO productos (Codigo, Nombre, Stock, Stock_minimo, Precio)
                VALUES (%s, %s, %s, %s, %s)
            """
            datos = (codigo, nombre, stock, stock_minimo, precio)
            cursor.execute(sql, datos)
            conexion.commit()
            print("✅ Producto agregado correctamente")
        except Exception as e:
            print("❌ Error al agregar producto:", e)
        finally:
            cursor.close()
            conexion.close()

            
    def ListarProductos():
        conexion = Miconexion.obtener_conexion()
        productos = []
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT Codigo, Nombre, Stock, Stock_minimo, Precio FROM productos WHERE Activo = 1")
                productos = cursor.fetchall()
        except Exception as e:
            print("❌ Error al obtener productos:", e)
        finally:
            conexion.close()
        return productos
        
    def BuscarProductos( criterio, valor):
        conexion = Miconexion.obtener_conexion()
        productos = []

        if not conexion:
            print("Error al conectarse a la base de datos")
            return productos

        try:
            cursor = conexion.cursor()
            if criterio == "codigo":
                sql = """
                    SELECT codigo, nombre, stock, stock_minimo, precio 
                    FROM productos 
                    WHERE codigo = %s AND activo = 1
                """
            elif criterio == "nombre":
                sql = """
                    SELECT codigo, nombre, stock, stock_minimo, precio 
                    FROM productos 
                    WHERE nombre LIKE %s AND activo = 1
                """
                valor = f"%{valor}%"
            else:
                return productos

            cursor.execute(sql, (valor,))
            productos = cursor.fetchall()

        except Exception as e:
            print("Error al buscar el producto:", e)
        finally:
            cursor.close()
            conexion.close()

        return productos


            
    def BajaProducto(self, criterio):
        conexion = Miconexion.obtener_conexion()
        if not conexion:
            return "conexion_fallida"

        try:
            cursor = conexion.cursor()

            if criterio.isdigit():
                sql_check = "SELECT * FROM productos WHERE Codigo = %s AND Activo = 1"
                sql_baja = "UPDATE productos SET Activo = 0 WHERE Codigo = %s"
            else:
                sql_check = "SELECT * FROM productos WHERE Nombre = %s AND Activo = 1"
                sql_baja = "UPDATE productos SET Activo = 0 WHERE Nombre = %s"

            cursor.execute(sql_check, (criterio,))
            resultado = cursor.fetchone()

            if resultado:
                cursor.execute(sql_baja, (criterio,))
                conexion.commit()
                return "exito"
            else:
                return "no_encontrado"
        except Exception as e:
            return f"error:{e}"
        finally:
            cursor.close()
            conexion.close()

            

    def EditarProducto(self, codigo, nombre, stock, stock_minimo, precio):
        conexion = Miconexion.obtener_conexion()
        if not conexion:
            return "conexion_fallida"

        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos WHERE Codigo = %s AND Activo = 1", (codigo,))
            resultado = cursor.fetchone()

            if resultado:
                sql = """
                    UPDATE productos 
                    SET Nombre = %s, Stock = %s, Stock_minimo = %s, Precio = %s 
                    WHERE Codigo = %s
                """
                cursor.execute(sql, (nombre, stock, stock_minimo, precio, codigo))
                conexion.commit()
                return "exito"
            else:
                return "no_encontrado"
        except Exception as e:
            return f"error:{e}"
        finally:
            cursor.close()
            conexion.close()

    def obtener_lista_productos():
        conexion = Miconexion.obtener_conexion()
        productos = []
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT Nombre, Stock, Precio FROM productos WHERE Activo = 1")
                productos = cursor.fetchall()  # ya son tuplas: (nombre, stock, precio)
        except Exception as e:
            print("❌ Error:", e)
        finally:
            conexion.close()
        return productos



    def prod_stock_bajo():
        conexion = Miconexion.obtener_conexion()
        productos_stock_bajo = []

        try:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT Nombre, Stock, Stock_minimo
                    FROM productos
                    WHERE Stock < Stock_minimo AND Activo = 1
                """)
                productos_stock_bajo = cursor.fetchall()  # Lista de tuplas
        except Exception as e:
            print("❌ Error al obtener productos con stock bajo:", e)
        finally:
            conexion.close()

        return productos_stock_bajo
