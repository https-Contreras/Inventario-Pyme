from Backend.conexion import Miconexion
from Backend.modelos.claseProducto import Producto


class Inventario():
    def agregar_producto(self, producto):
        conexion=Miconexion.obtener_conexion()
        if not conexion:
            print("No se pudo conectar para agregar el producto.")
            return
        try:
            cursor=conexion.cursor()
            sql="INSERT INTO productos (Codigo, Nombre, Stock, Stock_minimo, Precio) VALUES (%s, %s, %s, %s, %s)"
            datos=(producto.codigo, producto.nombre, producto.stock, producto.stock_minimo, producto.precio)
            cursor.execute(sql,datos)
            conexion.commit()
            print("Producto agregado correctamente")
        except Exception as e:
            print("Error al agregar producto: ", e)
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


            
    def BajaProducto(self, codigo_producto):
        conexion=Miconexion.obtener_conexion()
        if not conexion:
            print("No se pudo enlazar a la base de datos.")
            return 
        try:
            cursor=conexion.cursor()
            cursor.execute("SELECT * FROM productos WHERE codigo = %s AND activo = 1", (codigo_producto,))
            resultado=cursor.fetchone()
            if resultado:
                cursor.execute("UPDATE productos SET activo = 0 WHERE codigo = %s", (codigo_producto,))
                conexion.commit()
                print(f"Producto con codigo {codigo_producto} dado de baja exitosamente")
            else:
                print("Producto no encontrado o ya esta dado de baja")
        except Exception as e:
            print("Error al dar de b aja el producto. ",e)
        finally:
            cursor.close()
            conexion.close()
            
            
        

    def obtener_lista_productos():
        conexion = Miconexion.obtener_conexion()
        productos = []
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT Nombre, Stock, Precio FROM productos WHERE Activo = 1")
                resultados = cursor.fetchall()
                # Construir textos amigables para la lista
                productos = [
                    f"{nombre.ljust(35)} | Stock: {str(stock).ljust(20)} | Precio unitario:  ${precio:>7.2f}"
                    for nombre, stock, precio in resultados
                ]
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
                cursor.execute("SELECT Nombre, Stock, Stock_minimo FROM productos WHERE Stock < Stock_minimo AND Activo = 1")
                resultados = cursor.fetchall()
                productos_stock_bajo = [
                    f"{nombre.ljust(25)} | Stock: {str(stock).ljust(25)} | Mínimo requerido: {stock_minimo}"
                    for nombre, stock, stock_minimo in resultados
                ]
        except Exception as e:
            print("❌ Error al obtener productos con stock bajo:", e)
        finally:
            conexion.close()

        return productos_stock_bajo

