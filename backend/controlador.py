from PyQt6.QtWidgets import QApplication
from views.ventana_principal import VentanaPrincipal
from views.ventana_inventario import VentanaInventario
from views.ventana_agregar import VentanaAgregar
from views.ventana_editareliminar import VentanaEditarEliminar
from views.ventana_entradas import VentanaEntradas
#from views.ventana_reportes import VentanaReportes 

class Controlador:
    def __init__(self):
        # Creamos todas las ventanas principales al inicio
        self.ventana_principal = VentanaPrincipal(self)
        self.ventana_inventario = VentanaInventario(self)
        self.ventana_entradas = VentanaEntradas(self)
        #self.ventana_reportes = VentanaReportes(self)
        
        # Ventanas secundarias (se crean cuando se necesitan)
        self.ventana_agregar = None
        self.ventana_editareliminar = None
        
        # Mostramos la ventana principal inicial
        self.ventana_actual = self.ventana_principal
        self.ventana_actual.show()

    def mostrar_ventana_inventario(self):
        self._cambiar_ventana_principal(self.ventana_inventario)

    def mostrar_ventana_entradas(self):
        self._cambiar_ventana_principal(self.ventana_entradas)

    def mostrar_ventana_principal(self):
        self._cambiar_ventana_principal(self.ventana_principal)
        
    #def mostrar_ventana_reportes(self):
        #self._cambiar_ventana_principal(self.ventana_reportes)

    def mostrar_ventana_agregar(self):
        if not self.ventana_agregar:
            self.ventana_agregar = VentanaAgregar(self)
        self._cambiar_ventana(self.ventana_agregar)

    def mostrar_ventana_editareliminar(self):
        if not self.ventana_editareliminar:
            self.ventana_editareliminar = VentanaEditarEliminar(self)
        self._cambiar_ventana(self.ventana_editareliminar)

    def _cambiar_ventana_principal(self, nueva_ventana):
        """Para cambiar entre ventanas principales (barra izquierda)"""
        if self.ventana_actual != nueva_ventana:
            self.ventana_actual.hide()
            self.ventana_actual = nueva_ventana
            self.ventana_actual.show()

    def _cambiar_ventana(self, nueva_ventana):
        """Para cambiar a ventanas secundarias"""
        self.ventana_actual.hide()
        nueva_ventana.show()

    def volver_a_anterior(self, ventana_actual):
        """Para volver desde ventanas secundarias"""
        ventana_actual.hide()
        self.ventana_actual.show()