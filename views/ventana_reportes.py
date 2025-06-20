import os
from PyQt6.QtWidgets import QWidget, QSizeGrip
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QPixmap
from ui.ventana_reportes_ui import Ui_Form
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QHeaderView
from Backend.conexion import  Miconexion
from PyQt6.QtCore import QSortFilterProxyModel, Qt


class VentanaReportes(QWidget):
    def __init__(self, controlador):# constructor de la clase VentanaPrincipal
        self.controlador = controlador
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.resize(870, 650)  # Esto asegura que la ventana tenga el tamaño correcto inicial

        self.ui.frame_barra.setMinimumWidth(0)         
        self.ui.frame_barra.setMaximumWidth(260)     

        self.ui.frame_barrafiltro.setMaximumWidth(0)

        self.cargar_iconos()
        
        self.inicializar_animaciones()
        self.eventos()
        
        #EVENTOS
        self.proxy_movimientos = QSortFilterProxyModel()
        self.proxy_movimientos.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.tableInventario.setModel(self.proxy_movimientos)
        self.ui.tableInventario.setSortingEnabled(True)
        self.ui.bt_ocultar.clicked.connect(self.mostrar_movimientos)
        self.ui.btn_actual_a_antiguo.clicked.connect(self.ordenar_recientes)
        self.ui.btn_antiguo_a_actual.clicked.connect(self.ordenar_antiguos)
        self.ui.btn_entradas_2.clicked.connect(lambda: self.filtrar_tipo("Entrada"))
        self.ui.btn_salidas_2.clicked.connect(lambda: self.filtrar_tipo("Salida"))
        self.ui.btn_restablecer.clicked.connect(lambda: self.proxy_movimientos.setFilterFixedString(""))
        
    def inicializar_animaciones(self): # metodo para inicializar las animaciones y configuraciones de la ventana principal

        self.ui.bt_ocultar.clicked.connect(self.animacion_barra)
        self.ui.bt_mostrar.clicked.connect(self.animacion_barra)
        self.ui.btn_filtrar.clicked.connect(self.animacion_barra_filtro)
        # Ocultar el botón al inicio
        self.ui.btn_achicar.hide()
        self.ui.bt_mostrar.hide()
        # Dando sombra a los frames
        
        self.sombra_frame(self.ui.btn_filtrar)
        self.sombra_frame(self.ui.btn_antiguo_a_actual)
        self.sombra_frame(self.ui.btn_actual_a_antiguo)
        self.sombra_frame(self.ui.btn_entradas_2)
        self.sombra_frame(self.ui.btn_salidas_2)
        self.sombra_frame(self.ui.btn_restablecer)

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
        ruta_minimizar = os.path.join(root_dir, "models", "minimizar.svg")
        ruta_reportes = os.path.join(root_dir, "models", "reportes.svg")
        ruta_salidas = os.path.join(root_dir, "models", "salida.svg")
        ruta_filtrar = os.path.join(root_dir, "models", "filtrar.svg")
        ruta_exportar = os.path.join(root_dir, "models", "exportar.svg")
        ruta_calendario = os.path.join(root_dir, "models", "calendario.svg")
        ruta_stock = os.path.join(root_dir, "models", "stock.svg")
        ruta_mayor_a_menor = os.path.join(root_dir, "models", "mayor_a_menor.svg")
        ruta_menor_a_mayor = os.path.join(root_dir, "models", "menor_a_mayor.svg")
        ruta_restablecer = os.path.join(root_dir, "models", "restablecer.svg")


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
        self.ui.btn_exportar.setIcon(QtGui.QIcon(ruta_exportar))
        self.ui.label_3.setPixmap(QPixmap(ruta_calendario))
        self.ui.label_6.setPixmap(QPixmap(ruta_stock))
        self.ui.btn_antiguo_a_actual.setIcon(QtGui.QIcon(ruta_mayor_a_menor))
        self.ui.btn_actual_a_antiguo.setIcon(QtGui.QIcon(ruta_menor_a_mayor))
        self.ui.btn_entradas_2.setIcon(QtGui.QIcon(ruta_entrada))
        self.ui.btn_salidas_2.setIcon(QtGui.QIcon(ruta_salidas))
        self.ui.btn_graficar.setIcon(QtGui.QIcon(ruta_stock))
        self.ui.btn_restablecer.setIcon(QtGui.QIcon(ruta_restablecer))

    def eventos(self): # metodo para conectar los eventos de los botones
        #ventanas principales
        self.ui.btn_resumen.clicked.connect(lambda: self.controlador.mostrar_ventana_principal())
        self.ui.btn_entradas.clicked.connect(lambda: self.controlador.mostrar_ventana_entradas())
        self.ui.btn_salidas.clicked.connect(lambda: self.controlador.mostrar_ventana_salidas())
        self.ui.btn_alertas.clicked.connect(lambda: self.controlador.mostrar_ventana_alertas())
        self.ui.btn_configuracion.clicked.connect(lambda: self.controlador.mostrar_ventana_configuracion())
        self.ui.btn_inventario.clicked.connect(lambda: self.controlador.mostrar_ventana_inventario())



    def mostrar_movimientos(self):
        conexion = Miconexion.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = """
                    SELECT tipo, producto, cantidad, fecha, observacion
                    FROM movimientos 
                    ORDER BY fecha DESC
                """
                cursor.execute(sql)
                resultados = cursor.fetchall()

            # Crear el modelo de la tabla
            modelo = QStandardItemModel()
            modelo.setHorizontalHeaderLabels(["Tipo de movimiento", "Producto", "Cantidad", "Fecha", "Observaciones"])

            for fila in resultados:
                items = [QStandardItem(str(dato)) for dato in fila]
                modelo.appendRow(items)

            # Asignar el modelo a la QTableView
            self.proxy_movimientos.setSourceModel(modelo)
            self.ui.tableInventario.resizeColumnsToContents()
            self.ui.tableInventario.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        except Exception as e:
            print("❌ Error al mostrar movimientos:", e)
        finally:
            conexion.close()
            
    def ordenar_recientes(self):
        self.ui.tableInventario.sortByColumn(3, Qt.SortOrder.DescendingOrder)
    
        
    def ordenar_antiguos(self):
        self.ui.tableInventario.sortByColumn(3, Qt.SortOrder.AscendingOrder)
        
    def filtrar_tipo(self, tipo):
        self.proxy_movimientos.setFilterKeyColumn(0)  # Columna "Tipo de movimiento"
        self.proxy_movimientos.setFilterFixedString(tipo)

    
        