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
            
    def ListarProductos(self):
        conexion=Miconexion.obtener_conexion()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor=conexion.cursor()
            cursor.execute("SELECT codigo, nombre, stock, stock_minimo, precio FROM productos WHERE activo = 1")
            productos=cursor.fetchall()
            for p in productos:
                codigo, nombre, stock, minimo, precio = p
                print(f"Código: {codigo} | Nombre: {nombre} | Stock: {stock} | Mínimo: {minimo} | Precio: ${precio:.2f}")
        except Exception as e:
            print("Error en listar los productos", e)
        finally:
            cursor.close()
            conexion.close()
    
    def BuscarProductos(self, criterio, valor):
        conexion = Miconexion.obtener_conexion()
        if not conexion:
            print("Error al conectarse a la base de datos")
            return None
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
                print("Criterio inválido. Usa 'codigo' o 'nombre'.")
                return None

            cursor.execute(sql, (valor,))
            resultado = cursor.fetchone()

            if resultado:
                producto = Producto(*resultado)
                return producto
            else:
                print("Producto no encontrado o dado de baja.")
                return None
        except Exception as e:
            print("Error al buscar el producto:", e)
            return None
        finally:
            cursor.close()
            conexion.close()

            
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
        print("Entró a funcion listar productos")
        productos = []
        
        conexion = Miconexion.obtener_conexion()
        print("Despues de conexion.")
        if not conexion:
            print("❌ No se pudo establecer conexión con la base de datos")
            return productos

        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT Nombre FROM productos WHERE Activo = 1")
            productos = [fila[0] for fila in cursor.fetchall()]
            print(" Productos recibidos:", productos)
        except Exception as e:
            print("❌ Error al consultar productos:", e)
        finally:
            cursor.close()
            conexion.close()

        return productos
