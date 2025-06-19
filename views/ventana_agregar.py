import os
from PyQt6.QtWidgets import QWidget, QSizeGrip
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QPixmap
from ui.ventana_agregar_ui import Ui_Form
from PyQt6 import QtWidgets, QtGui
from Backend.conexion import Miconexion

class VentanaAgregar(QWidget):
    def __init__(self, controlador):# constructor de la clase VentanaPrincipal
        super().__init__()
        self.controlador = controlador
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.resize(780, 600)  # Esto asegura que la ventana tenga el tamaño correcto inicial

        self.cargar_iconos()
        
        self.inicializar_animaciones()
        
        self.eventos()

    def inicializar_animaciones(self): # metodo para inicializar las animaciones y configuraciones de la ventana principal

        # Ocultar el botón al inicio
        self.ui.btn_achicar.hide()
        # Dando sombra a los frames
        self.sombra_frame(self.ui.frame_cuerpo)
        self.sombra_frame(self.ui.LnEdit_id)
        self.sombra_frame(self.ui.LnEdit_producto)
        self.sombra_frame(self.ui.LnEdit_descripcion)
        self.sombra_frame(self.ui.LnEdit_categoria)
        self.sombra_frame(self.ui.LnEdit_stockactual)
        self.sombra_frame(self.ui.LnEdit_stockminimo)
        self.sombra_frame(self.ui.btn_agregar)

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
        
        # Establecer íconos
        self.ui.btn_regresar.setIcon(QtGui.QIcon(ruta_regresar))
        self.ui.btn_agregar.setIcon(QtGui.QIcon(ruta_agregar))
        self.ui.btn_cerrar.setIcon(QtGui.QIcon(ruta_cerrar))
        self.ui.btn_achicar.setIcon(QtGui.QIcon(ruta_hacerchico))
        self.ui.btn_agrandar.setIcon(QtGui.QIcon(ruta_hacergrande))
        self.ui.btn_minimizar.setIcon(QtGui.QIcon(ruta_minimizar))

    def eventos(self): # metodo para conectar los eventos de los botones
        self.ui.btn_regresar.clicked.connect(lambda: self.controlador.volver_a_anterior(self))
    
    
    def agregar_producto(self):
        