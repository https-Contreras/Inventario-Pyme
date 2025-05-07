from abc import ABC, abstractmethod
from datetime import datetime

class Movimientos(ABC):
    def __init__(self, producto_codigo, cantidad, fecha=None):
        self.producto_codigo=producto_codigo
        self.cantidad=cantidad
        self.fecha=fecha or datetime.now()
        
    @abstractmethod
    def tipo(self):
        pass