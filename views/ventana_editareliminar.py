import os
from PyQt6.QtWidgets import QWidget, QSizeGrip,  QMessageBox
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QPixmap
from ui.ventana_editareliminar_ui import Ui_Form
from PyQt6 import QtWidgets, QtGui
from Backend.inventario import Inventario

class VentanaEditarEliminar(QWidget):
    def __init__(self, controlador):# constructor de la clase VentanaPrincipal
        super().__init__()
        self.controlador = controlador
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.resize(780, 600)  # Esto asegura que la ventana tenga el tamaño correcto inicial

        self.cargar_iconos()
        
        self.inicializar_animaciones()
        
        self.eventos()
        self.ui.btn_eliminar.clicked.connect(self.eliminar_producto)
        self.ui.btn_agregar.clicked.connect(self.editar_producto)
        self.ui.btn_buscar.clicked.connect(self.llenar_datos_producto)
        self.ui.LnEdit_buscar.returnPressed.connect(self.llenar_datos_producto)

    def inicializar_animaciones(self): # metodo para inicializar las animaciones y configuraciones de la ventana principal

        # Ocultar el botón al inicio
        self.ui.btn_achicar.hide()
        # Dando sombra a los frames
        self.sombra_frame(self.ui.frame_cuerpo)
        self.sombra_frame(self.ui.LnEdit_id_edit)
        self.sombra_frame(self.ui.LnEdit_producto_edit)
        self.sombra_frame(self.ui.LnEdit_descripcion_edit)
        self.sombra_frame(self.ui.LnEdit_stockactual_edit)
        self.sombra_frame(self.ui.LnEdit_stockminimo_edit)
        self.sombra_frame(self.ui.btn_agregar)
        self.sombra_frame(self.ui.btn_eliminar)


        #control barra de titulos
        self.ui.btn_minimizar.clicked.connect(self.control_bt_minimizar)
        self.ui.btn_agrandar.clicked.connect(self.control_bt_agrandar)
        self.ui.btn_achicar.clicked.connect(self.control_bt_normal)
        self.ui.btn_cerrar.clicked.connect(self.close)
        #eliminar barra y titulo -opacidad
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        #SizeGrip
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.grip, 0, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.evento_mover_desde_frame()

    def sombra_frame(self, frame): #metodo para dar sombra a los frames
        sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(18)
        sombra.setXOffset(4)
        sombra.setYOffset(4)
        sombra.setColor(QColor(0, 0, 0, 100))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self): #metodo para minimizar la ventana
        self.showMinimized()

    def control_bt_normal(self): #metodo para maximizar la ventana
        self.showNormal()
        self.ui.btn_achicar.hide()
        self.ui.btn_agrandar.show()
    
    def control_bt_agrandar(self): #metodo para maximizar la ventana
        self.showMaximized()
        self.ui.btn_agrandar.hide()
        self.ui.btn_achicar.show()
 
    def evento_mover_desde_frame(self):
        self.ui.frame_superior.mousePressEvent = self.frame_mouse_press_event
        self.ui.frame_superior.mouseMoveEvent = self.frame_mouse_move_event

    def frame_mouse_press_event(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    def frame_mouse_move_event(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and not self.isMaximized():
            self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    def cargar_iconos(self):# metodo para cargar los íconos desde la carpeta /models
        # Carpeta raíz del proyecto
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # Ruta a los íconos en /models
        
        ruta_cerrar = os.path.join(root_dir, "models", "cerrar.svg")
        ruta_hacerchico = os.path.join(root_dir, "models", "hacerchico.svg")
        ruta_hacergrande = os.path.join(root_dir, "models", "hacergrande.svg")
        ruta_minimizar = os.path.join(root_dir, "models", "minimizar.svg")
        ruta_regresar = os.path.join(root_dir, "models", "regresar.svg")
        ruta_agregar = os.path.join(root_dir, "models", "agregar.svg")
        ruta_buscar = os.path.join(root_dir, "models", "buscar.svg")
        ruta_eliminar = os.path.join(root_dir, "models", "basura.svg")
        # Establecer íconos
        self.ui.btn_regresar.setIcon(QtGui.QIcon(ruta_regresar))
        self.ui.btn_agregar.setIcon(QtGui.QIcon(ruta_agregar))
        self.ui.btn_cerrar.setIcon(QtGui.QIcon(ruta_cerrar))
        self.ui.btn_achicar.setIcon(QtGui.QIcon(ruta_hacerchico))
        self.ui.btn_agrandar.setIcon(QtGui.QIcon(ruta_hacergrande))
        self.ui.btn_minimizar.setIcon(QtGui.QIcon(ruta_minimizar))
        self.ui.btn_buscar.setIcon(QtGui.QIcon(ruta_buscar))
        self.ui.btn_eliminar.setIcon(QtGui.QIcon(ruta_eliminar))

    def eventos(self): # metodo para conectar los eventos de los botones
        self.ui.btn_regresar.clicked.connect(lambda: self.controlador.volver_a_anterior(self))
    
    

    def eliminar_producto(self):
        codigo = self.ui.LnEdit_id_edit.text().strip()
        nombre = self.ui.LnEdit_producto_edit.text().strip()

        criterio = codigo if codigo else nombre
        if not criterio:
            QMessageBox.warning(self, "Campo requerido", "⚠️ Ingresa el código o el nombre del producto.")
            return

        resultado = Inventario().BajaProducto(criterio)

        if resultado == "conexion_fallida":
            QMessageBox.critical(self, "Error de conexión", "❌ No se pudo conectar a la base de datos.")
        elif resultado == "exito":
            QMessageBox.information(self, "Éxito", "✅ Producto dado de baja correctamente.")
            self.ui.LnEdit_id_edit.clear()
            self.ui.LnEdit_producto_edit.clear()
            self.ui.LnEdit_stockactual_edit.clear()
            self.ui.LnEdit_stockminimo_edit.clear()
            self.ui.LnEdit_descripcion_edit.clear()
        elif resultado == "no_encontrado":
            QMessageBox.warning(self, "No encontrado", "⚠️ Producto no encontrado o ya inactivo.")
        elif resultado.startswith("error:"):
            error_msg = resultado.split(":", 1)[1]
            QMessageBox.critical(self, "Error inesperado", f"❌ Error: {error_msg}")
        
    def editar_producto(self):
        try:
            codigo = int(self.ui.LnEdit_id_edit.text())
            nombre = self.ui.LnEdit_producto_edit.text().strip()
            stock = int(self.ui.LnEdit_stockactual_edit.text())
            stock_minimo = int(self.ui.LnEdit_stockminimo_edit.text())
            precio = float(self.ui.LnEdit_descripcion_edit.text())

            if not nombre:
                QMessageBox.warning(self, "Campo requerido", "⚠️ El nombre no puede estar vacío.")
                return

            resultado = Inventario().EditarProducto(codigo, nombre, stock, stock_minimo, precio)

            if resultado == "conexion_fallida":
                QMessageBox.critical(self, "Error de conexión", "❌ No se pudo conectar a la base de datos.")
            elif resultado == "exito":
                QMessageBox.information(self, "Éxito", "✅ Producto editado correctamente.")
            elif resultado == "no_encontrado":
                QMessageBox.warning(self, "No encontrado", "⚠️ Producto no encontrado o está inactivo.")
            elif resultado.startswith("error:"):
                error_msg = resultado.split(":", 1)[1]
                QMessageBox.critical(self, "Error inesperado", f"❌ Error: {error_msg}")

        except ValueError:
            QMessageBox.critical(self, "Error de formato", "❌ Todos los campos deben tener valores válidos.")
            
    def llenar_datos_producto(self):
        #Funcion para llenar los lineedits de los campos mas rapido
        texto = self.ui.LnEdit_buscar.text().strip()

        if not texto:
            QMessageBox.warning(self, "Campo vacío", "⚠️ Ingresa el código o nombre del producto.")
            return

        criterio = "codigo" if texto.isdigit() else "nombre"
        productos = Inventario.BuscarProductos(criterio, texto)

        if not productos:
            QMessageBox.information(self, "No encontrado", "❌ No se encontró ningún producto con ese criterio.")
            return

        # Tomamos el primer resultado
        codigo, nombre, stock, stock_minimo, precio = productos[0]

        self.ui.LnEdit_id_edit.setText(str(codigo))
        self.ui.LnEdit_producto_edit.setText(nombre)
        self.ui.LnEdit_stockactual_edit.setText(str(stock))
        self.ui.LnEdit_stockminimo_edit.setText(str(stock_minimo))
        self.ui.LnEdit_descripcion_edit.setText(f"{precio:.2f}")