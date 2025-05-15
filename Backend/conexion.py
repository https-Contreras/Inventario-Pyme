import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inventario_pymes"
        )
        if conexion.is_connected():
            print("Conexion exitosa a la BD")
            return conexion
    except Error as e:
        print("Error al conectarse a la BD", e)
        return None