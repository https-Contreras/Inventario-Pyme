import os
from PyQt6.QtWidgets import QWidget, QSizeGrip
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QPixmap
from ui.ventana_inventario_ui import Ui_Form
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from Backend.inventario import Inventario
from PyQt6.QtWidgets import QHeaderView
class VentanaInventario(QWidget):
    def __init__(self, ventana_principal):# constructor de la clase VentanaPrincipal
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.resize(870, 650)  # Esto asegura que la ventana tenga el tamaño correcto inicial

        self.ui.frame_barra.setMinimumWidth(0)         
        self.ui.frame_barra.setMaximumWidth(260)     

        self.ui.frame_barrafiltro.setMaximumWidth(0)

        self.cargar_iconos()
        
        self.inicializar_animaciones()
        #Guardando referencias de ventanas
        self.ventana_principal = ventana_principal
        self.eventos()
        
        #Eventos
        self.ui.btn_inventario.clicked.connect(self.mostrar_inventario)
        self.ui.Linedit_busqueda.returnPressed.connect(self.buscar_producto)
        self.ui.btn_busqueda.clicked.connect(self.buscar_producto)
        
        
    def inicializar_animaciones(self): # metodo para inicializar las animaciones y configuraciones de la ventana principal

        self.ui.bt_ocultar.clicked.connect(self.animacion_barra)
        self.ui.bt_mostrar.clicked.connect(self.animacion_barra)
        self.ui.btn_filtrar.clicked.connect(self.animacion_barra_filtro)
        # Ocultar el botón al inicio
        self.ui.btn_achicar.hide()
        self.ui.bt_mostrar.hide()
        # Dando sombra a los frames
        self.sombra_frame(self.ui.btn_busqueda)
        self.sombra_frame(self.ui.btn_filtrar)
        self.sombra_frame(self.ui.Linedit_busqueda)
        self.sombra_frame(self.ui.btn_alfabeticamente)
        self.sombra_frame(self.ui.btn_mayoramenor)
        self.sombra_frame(self.ui.btn_menormayor)

        self.sombra_frame(self.ui.frame_cuerpo)
        self.sombra_frame(self.ui.btn_alertas)
        self.sombra_frame(self.ui.btn_configuracion)
        self.sombra_frame(self.ui.btn_entradas)
        self.sombra_frame(self.ui.btn_inventario)
        self.sombra_frame(self.ui.btn_resumen)
        self.sombra_frame(self.ui.btn_reportes)
        self.sombra_frame(self.ui.btn_salidas)
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

    def animacion_barra(self): 
        width = self.ui.frame_barra.width()
        normal = 0
        extender = 260

        if width == 0:
            self.ui.bt_mostrar.hide()
            self.ui.bt_ocultar.show()
            final_width = extender
        else:
            self.ui.bt_mostrar.show()
            self.ui.bt_ocultar.hide()
            final_width = normal

        self.animacion = QPropertyAnimation(self.ui.frame_barra, b"maximumWidth")
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(final_width)
        self.animacion.setDuration(400)
        self.animacion.setEasingCurve(QEasingCurve.Type.InQuad)
        self.animacion.start()

    def animacion_barra_filtro(self):
        # Asegurarse de que el frame esté visible para poder animarlo
        self.ui.frame_barrafiltro.show()

        width = self.ui.frame_barrafiltro.maximumWidth()
        normal = 0
        extender = 260

        if width == 0:
            final_width = extender
        else:
            final_width = normal

        self.animacion = QPropertyAnimation(self.ui.frame_barrafiltro, b"maximumWidth")
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(final_width)
        self.animacion.setDuration(400)
        self.animacion.setEasingCurve(QEasingCurve.Type.InQuad)
        self.animacion.start()

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
        ruta_alertas = os.path.join(root_dir, "models", "alertas.svg")
        ruta_cerrar = os.path.join(root_dir, "models", "cerrar.svg")
        ruta_config = os.path.join(root_dir, "models", "configuracion.svg")
        ruta_derecha = os.path.join(root_dir, "models", "derecha.svg")
        ruta_entrada = os.path.join(root_dir, "models", "entrada.svg")
        ruta_hacerchico = os.path.join(root_dir, "models", "hacerchico.svg")
        ruta_hacergrande = os.path.join(root_dir, "models", "hacergrande.svg")
        ruta_inventario = os.path.join(root_dir, "models", "inventario.svg")
        ruta_izquierda = os.path.join(root_dir, "models", "izquierda.svg")
        ruta_logo1 = os.path.join(root_dir, "models", "logoIMSreduce.png")
        ruta_logo2 = os.path.join(root_dir, "models", "logoIMSreduce2.png")
        ruta_minimizar = os.path.join(root_dir, "models", "minimizar.svg")
        ruta_paginas = os.path.join(root_dir, "models", "paginas.svg")
        ruta_reportes = os.path.join(root_dir, "models", "reportes.svg")
        ruta_salidas = os.path.join(root_dir, "models", "salida.svg")
        ruta_filtrar = os.path.join(root_dir, "models", "filtrar.svg")
        ruta_buscar = os.path.join(root_dir, "models", "buscar.svg")
        ruta_alfabeticamente = os.path.join(root_dir, "models", "alfabeticamente.svg")
        ruta_mayor_a_menor = os.path.join(root_dir, "models", "mayor_a_menor.svg")
        ruta_menor_a_mayor = os.path.join(root_dir, "models", "menor_a_mayor.svg")
        
        # Establecer íconos
        self.ui.btn_alertas.setIcon(QtGui.QIcon(ruta_alertas))
        self.ui.btn_cerrar.setIcon(QtGui.QIcon(ruta_cerrar))
        self.ui.btn_configuracion.setIcon(QtGui.QIcon(ruta_config))
        self.ui.bt_mostrar.setIcon(QtGui.QIcon(ruta_derecha))
        self.ui.btn_entradas.setIcon(QtGui.QIcon(ruta_entrada))
        self.ui.btn_achicar.setIcon(QtGui.QIcon(ruta_hacerchico))
        self.ui.btn_agrandar.setIcon(QtGui.QIcon(ruta_hacergrande))
        self.ui.btn_inventario.setIcon(QtGui.QIcon(ruta_inventario))
        self.ui.bt_ocultar.setIcon(QtGui.QIcon(ruta_izquierda))
        self.ui.btn_resumen.setIcon(QtGui.QIcon(ruta_logo1))
        self.ui.btn_minimizar.setIcon(QtGui.QIcon(ruta_minimizar))
        self.ui.btn_reportes.setIcon(QtGui.QIcon(ruta_reportes))
        self.ui.btn_salidas.setIcon(QtGui.QIcon(ruta_salidas))
        self.ui.btn_filtrar.setIcon(QtGui.QIcon(ruta_filtrar))
        self.ui.btn_busqueda.setIcon(QtGui.QIcon(ruta_buscar))
        self.ui.btn_alfabeticamente.setIcon(QtGui.QIcon(ruta_alfabeticamente))
        self.ui.btn_mayoramenor.setIcon(QtGui.QIcon(ruta_mayor_a_menor))
        self.ui.btn_menormayor.setIcon(QtGui.QIcon(ruta_menor_a_mayor))

    def eventos(self): # metodo para conectar los eventos de los botones
        self.ui.btn_resumen.clicked.connect(self.volver_a_ventana_principal)
        
    
    def volver_a_ventana_principal(self): # metodo para mostrar la ventana de inventario
        self.hide()  # Oculta esta ventana
        self.ventana_principal.show()  # Muestra la principal
        
        
        
    #Esto es para mostrar el inventario en la ventana de inventario:
    def mostrar_inventario(self):
        productos = Inventario.ListarProductos()

        # Crear el modelo
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Código", "Nombre", "Stock", "Stock mínimo", "Precio en pesos"])

        # Agregar filas
        for fila in productos:
            items = [QStandardItem(str(campo)) for campo in fila]
            model.appendRow(items)

            # Asignar el modelo a la tabla
            self.ui.tableInventario.setModel(model)
            # Ajustar columnas
            self.ui.tableInventario.resizeColumnsToContents()
            self.ui.tableInventario.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    def buscar_producto(self):
        #funcion para la barra de busqueda del inventario
        texto=self.ui.Linedit_busqueda.text().strip()
        
        
        if not texto:
            self.mostrar_inventario()
            
        # Determinar el criterio
        if texto.isdigit():
            criterio = "codigo"
        else:
            criterio = "nombre"
        
        productos = Inventario.BuscarProductos(criterio,texto)
        # Crear modelo para la tabla
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Código", "Nombre", "Stock", "Stock mínimo", "Precio en pesos"])
        
        if productos:
            for fila in productos:
                items = [QStandardItem(str(campo)) for campo in fila]
                model.appendRow(items)
        else:
            model.appendRow([QStandardItem("NINGUNA COINCIDENCIA")])

        self.ui.tableInventario.setModel(model)
        self.ui.tableInventario.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)