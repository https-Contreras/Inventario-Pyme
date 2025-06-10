import pymysql

class Miconexion():
    def obtener_conexion():
        return pymysql.connect(
            host="localhost",
            user="root",
            password="",  # tu contraseña si aplica
            database="inventario_pymes"
        )
