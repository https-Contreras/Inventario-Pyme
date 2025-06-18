from PyQt6.QtWidgets import QApplication
from views.ventana_principal import VentanaPrincipal
from views.ventana_inventario import VentanaInventario
from views.ventana_agregar import VentanaAgregar

class Controlador:
    def __init__(self):
        self.ventana_principal = VentanaPrincipal(self)
        self.ventana_principal.show()

    def mostrar_ventana_inventario(self):
        self.ventana_anterior = self.ventana_principal  # Guardar anterior
        self.ventana_inventario = VentanaInventario(self)
        self.ventana_anterior.hide()
        self.ventana_inventario.show()

    def mostrar_ventana_agregar(self):
        self.ventana_anterior = self.ventana_inventario  # Guardar anterior
        self.ventana_agregar = VentanaAgregar(self)
        self.ventana_anterior.hide()
        self.ventana_agregar.show()

    def volver_a_anterior(self, ventana_actual):
        ventana_actual.hide()
        self.ventana_anterior.show()

