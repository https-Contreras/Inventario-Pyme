from modelos.claseMovimientos import Movimientos

class Salidas(Movimientos):
    def _init_(self, codigo_producto, cantidad, fecha, observaciones=""):
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.observaciones = observaciones
        
    def tipo(self):
        return "Salida"