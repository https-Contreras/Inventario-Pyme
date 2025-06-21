import os
from PyQt6.QtWidgets import QWidget, QSizeGrip, QHeaderView, QTableWidgetItem
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QDateTime
from PyQt6.QtGui import QColor, QIcon, QPixmap
from ui.ventana_principal_ui import Ui_Form
from views.ventana_inventario import VentanaInventario
from PyQt6 import QtWidgets, QtGui
from Backend.inventario import Inventario
from Backend.claseHilo import RelojThread, NotificacionesThread
from Backend.conexion import Miconexion

class VentanaPrincipal(QWidget):
    def __init__(self, controlador):# constructor de la clase VentanaPrincipal
        super().__init__()
        self.controlador = controlador
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.resize(870, 650)  # Esto asegura que la ventana tenga el tamaño correcto inicial

        self.ui.frame_barra.setMinimumWidth(0)         
        self.ui.frame_barra.setMaximumWidth(260)     
    

        self.cargar_iconos()
        
        self.inicializar_animaciones()
    
    
        #EVENTOS DE BOTONES
        
        self.ui.toolBox.currentChanged.connect(self.seccion_toolbox)
        
        self.inicializar_reloj()
        self.inicializar_hilo_alertas()

            
        self.eventos()

    def inicializar_animaciones(self): # metodo para inicializar las animaciones y configuraciones de la ventana principal

        self.ui.bt_ocultar.clicked.connect(self.animacion_barra)
        self.ui.bt_mostrar.clicked.connect(self.animacion_barra)
        # Ocultar el botón al inicio
        self.ui.btn_achicar.hide()
        self.ui.bt_mostrar.hide()
        # Dando sombra a los frames
        self.sombra_frame(self.ui.frame_cuerpo)
        self.sombra_frame(self.ui.toolBox)
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
        self.setLayout(layout)  # ⛔ ESTA LÍNEA CIERRA TU APP SI YA HAY LAYOUT

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
        self.ui.logo_letras.setPixmap(QPixmap(ruta_logo2))
        self.ui.btn_minimizar.setIcon(QtGui.QIcon(ruta_minimizar))
        self.ui.toolBox.setItemIcon(0, QIcon(ruta_paginas))
        self.ui.toolBox.setItemIcon(1, QIcon(ruta_paginas))
        self.ui.toolBox.setItemIcon(2, QIcon(ruta_paginas))
        self.ui.btn_reportes.setIcon(QtGui.QIcon(ruta_reportes))
        self.ui.btn_salidas.setIcon(QtGui.QIcon(ruta_salidas))
        

        
    
    
    #Esto es para las listas de la ventana principal
    def seccion_toolbox(self, index):
        try:
            if index == 0:
                self.ui.tableWidget_3.clear()
                self.ui.tableWidget_3.setColumnCount(3)
                self.ui.tableWidget_3.setHorizontalHeaderLabels(["Nombre", "Stock", "Precio"])
                self.ui.tableWidget_3.setRowCount(0)

                productos = Inventario.obtener_lista_productos()  

                for fila_idx, (nombre, stock, precio) in enumerate(productos):
                    self.ui.tableWidget_3.insertRow(fila_idx)
                    self.ui.tableWidget_3.setItem(fila_idx, 0, QTableWidgetItem(nombre))
                    self.ui.tableWidget_3.setItem(fila_idx, 1, QTableWidgetItem(str(stock)))
                    self.ui.tableWidget_3.setItem(fila_idx, 2, QTableWidgetItem(f"${precio:.2f}"))

                self.ui.tableWidget_3.resizeColumnsToContents()
                self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            elif index == 1:
                self.ui.tableWidget_2.clear()
                self.ui.tableWidget_2.setColumnCount(3)
                self.ui.tableWidget_2.setHorizontalHeaderLabels(["Nombre", "Stock actual", "Stock mínimo"])
                self.ui.tableWidget_2.setRowCount(0)

                productos_stock_bajo = Inventario.prod_stock_bajo()

                for fila_idx, (nombre, stock, stock_minimo) in enumerate(productos_stock_bajo):
                    self.ui.tableWidget_2.insertRow(fila_idx)
                    self.ui.tableWidget_2.setItem(fila_idx, 0, QTableWidgetItem(nombre))
                    self.ui.tableWidget_2.setItem(fila_idx, 1, QTableWidgetItem(str(stock)))
                    self.ui.tableWidget_2.setItem(fila_idx, 2, QTableWidgetItem(str(stock_minimo)))

                self.ui.tableWidget_2.resizeColumnsToContents()
                self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            elif index == 2:
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setColumnCount(4)
                self.ui.tableWidget.setHorizontalHeaderLabels(["Tipo de movimiento", "Artículo", "Stock", "Fecha"])
                self.ui.tableWidget.setRowCount(0)

                try:
                    conexion = Miconexion.obtener_conexion()
                    with conexion.cursor() as cursor:
                        cursor.execute("""
                                SELECT tipo, producto, cantidad, fecha 
                                FROM movimientos 
                                ORDER BY fecha DESC 
                                LIMIT 10
                            """)
                        resultados = cursor.fetchall()

                    for fila_idx, fila in enumerate(resultados):
                        self.ui.tableWidget.insertRow(fila_idx)
                        for col_idx, valor in enumerate(fila):
                            item = QTableWidgetItem(str(valor))
                            self.ui.tableWidget.setItem(fila_idx, col_idx, item)

                    self.ui.tableWidget.resizeColumnsToContents()
                    self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                    self.ui.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
                except Exception as e:
                        print("❌ Error al cargar movimientos recientes:", e)
                finally:
                    if conexion:
                        conexion.close()
        except Exception as e:
            print("❌ Excepción atrapada:", e)
            
            
    #Esto es para mostrar ventana de inventario
    def eventos(self): # metodo para conectar los eventos de los botones
        #vetanas principales
        self.ui.btn_inventario.clicked.connect(self.controlador.mostrar_ventana_inventario)
        self.ui.btn_entradas.clicked.connect(self.controlador.mostrar_ventana_entradas)
        self.ui.btn_salidas.clicked.connect(self.controlador.mostrar_ventana_salidas)
        self.ui.btn_reportes.clicked.connect(self.controlador.mostrar_ventana_reportes)
        self.ui.btn_alertas.clicked.connect(self.controlador.mostrar_ventana_alertas)
        self.ui.btn_configuracion.clicked.connect(self.controlador.mostrar_ventana_configuracion)
    
    
    def inicializar_reloj(self):
        self.reloj = RelojThread()
        self.reloj.nueva_fecha.connect(self.actualizar_fecha)
        self.reloj.start()

    def actualizar_fecha(self, fecha):
        self.ui.dateTimeEdit_tiempo.setDateTime(fecha)  # Suponiendo que tu QDateTimeEdit se llama así
        
    def inicializar_hilo_alertas(self):
        self.hilo_alertas = NotificacionesThread()
        self.hilo_alertas.nuevas_alertas.connect(self.actualizar_label_alertas)
        self.hilo_alertas.start()
        
    def actualizar_label_alertas(self, cantidad):
        self.ui.label_notificaciones.setText(f"🔔 {cantidad} productos con stock bajo")
        
    