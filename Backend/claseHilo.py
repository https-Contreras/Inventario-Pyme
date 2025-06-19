from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtCore import QDateTime
import time
import pymysql

class RelojThread(QThread):
    nueva_fecha = pyqtSignal(QDateTime)

    def run(self):
        while True:
            fecha_actual = QDateTime.currentDateTime()
            self.nueva_fecha.emit(fecha_actual)
            time.sleep(1)
            
            
            
class NotificacionesThread(QThread):
    nuevas_alertas = pyqtSignal(int)

    def run(self):
        while True:
            try:
                # Conexión a la BD
                conexion = pymysql.connect(
                    host="localhost",
                    user="root",
                    database="inventario_pymes",
                    password="Jadac03s",
                    charset='utf8mb4'
                )
                with conexion.cursor() as cursor:
                    cursor.execute("""
                        SELECT COUNT(*) FROM productos
                        WHERE Activo = 1 AND Stock < Stock_minimo
                    """)
                    resultado = cursor.fetchone()
                    total = resultado[0]
                    self.nuevas_alertas.emit(total)
            except Exception as e:
                print("❌ Error en hilo de notificaciones:", e)
            finally:
                try:
                    conexion.close()
                except:
                    pass
            time.sleep(10)  # Actualiza cada 10 segundos