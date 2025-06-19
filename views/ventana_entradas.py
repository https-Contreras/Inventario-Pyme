import os
from PyQt6.QtWidgets import QWidget, QSizeGrip, QHeaderView, QMessageBox
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor, QIcon, QPixmap
from ui.ventana_entradas_ui import Ui_Form
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from Backend.inventario import Inventario
from Backend.conexion import Miconexion
from datetime import datetime

class VentanaEntradas(QWidget):
    def __init__(self, controlador):# constructor de la clase VentanaPrincipal
        self.controlador = controlador
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.resize(870, 650)  # Esto asegura que la ventana tenga el tamaño correcto inicial

        self.ui.frame_barra.setMinimumWidth(0)         
        self.ui.frame_barra.setMaximumWidth(260)     

        self.cargar_iconos()
        
        self.inicializar_animaciones()
        self.eventos()
        self.ui.btn_busqueda.clicked.connect(self.buscar_producto)
        self.ui.btn_registrar_entrada.clicked.connect(self.registrar_entrada)
        
    def inicializar_animaciones(self): # metodo para inicializar las animaciones y configuraciones de la ventana principal

        self.ui.bt_ocultar.clicked.connect(self.animacion_barra)
        self.ui.bt_mostrar.clicked.connect(self.animacion_barra)
        # Ocultar el botón al inicio
        self.ui.btn_achicar.hide()
        self.ui.bt_mostrar.hide()
        # Dando sombra a los frames
        self.sombra_frame(self.ui.btn_busqueda)
        self.sombra_frame(self.ui.Linedit_busqueda)

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
        ruta_minimizar = os.path.join(root_dir, "models", "minimizar.svg")
        ruta_reportes = os.path.join(root_dir, "models", "reportes.svg")
        ruta_salidas = os.path.join(root_dir, "models", "salida.svg")
        ruta_filtrar = os.path.join(root_dir, "models", "filtrar.svg")
        ruta_buscar = os.path.join(root_dir, "models", "buscar.svg")
        ruta_logo1 = os.path.join(root_dir, "models", "logoIMSreduce.png")
        
        ruta_like = os.path.join(root_dir, "models", "like.svg")
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
        self.ui.btn_busqueda.setIcon(QtGui.QIcon(ruta_buscar))
        self.ui.btn_registrar_entrada.setIcon(QtGui.QIcon(ruta_like))

    def eventos(self): # metodo para conectar los eventos de los botones
        self.ui.btn_resumen.clicked.connect(lambda: self.controlador.mostrar_ventana_principal())
        self.ui.btn_inventario.clicked.connect(lambda: self.controlador.mostrar_ventana_inventario())
        self.ui.btn_salidas.clicked.connect(lambda: self.controlador.mostrar_ventana_salidas())
        self.ui.btn_reportes.clicked.connect(lambda: self.controlador.mostrar_ventana_reportes())
        self.ui.btn_salidas.clicked.connect(lambda: self.controlador.mostrar_ventana_salidas())
        self.ui.btn_configuracion.clicked.connect(lambda: self.controlador.mostrar_ventana_configuracion())


    def buscar_producto(self):
            #funcion para la barra de busqueda del inventario
            texto=self.ui.Linedit_busqueda.text().strip()
            
                
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

            self.ui.tbView_actualProducto.setModel(model)
            self.ui.tbView_actualProducto.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    
    def registrar_entrada(self):
        codigo = self.ui.Linedit_busqueda.text().strip()
        cantidad = self.ui.LnEdit_entrada.text().strip()
        fecha = self.ui.LnEdit_fecha.text().strip()
        observaciones = self.ui.LnEdit_observaciones.text().strip()
        if not codigo or not cantidad:
            QMessageBox.warning(self,"Campos vacios", "Debe ingresar codigo o cantidad")
            return
        
        # Validar formato de fecha
        try:
            datetime.strptime(fecha, "%Y-%m-%d")  # Si falla, lanza ValueError
        except ValueError:
            QMessageBox.warning(self, "Fecha inválida", "La fecha debe estar en formato YYYY-MM-DD.")
            return
        
        try:
            cantidad = int(cantidad)
            if cantidad <=0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self,"Cantidad inválida","La cantidad debe ser mayor a 0")
            
        conexion=Miconexion.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                #Buscar producto por nombre o codigo
                sql_buscar = """
                        SELECT Stock, Nombre FROM productos 
                        WHERE Activo = 1 AND (codigo = %s OR nombre = %s)
                    """
                
                cursor.execute(sql_buscar, (codigo, codigo))
                resultado = cursor.fetchone()
                
                if not resultado:
                    QMessageBox.warning(self, "No encontrado", "El producto no existe o esta dado de baja")
                    return

                stock_actual, nombre = resultado
                nuevo_stock= stock_actual+cantidad
                
                #Actualizar stock
                sql_actualizar = "UPDATE productos SET Stock = %s WHERE Codigo = %s OR Nombre = %s"
                
                cursor.execute(sql_actualizar, (nuevo_stock, codigo, codigo))

                cursor.execute(sql_actualizar, (nuevo_stock, codigo, codigo))
                
                #Registrar movimiento
                sql_movimiento = """
                        INSERT INTO movimientos (tipo, producto, cantidad, fecha, observacion)
                        VALUES (%s, %s, %s, %s, %s)
                        """
                        
                cursor.execute(sql_movimiento, ("Entrada", nombre, cantidad, fecha, observaciones))
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Entrada registrada y stock actualizado.")
                self.ui.LnEdit_entrada.clear()
                self.ui.LnEdit_fecha.clear()
                self.ui.LnEdit_observaciones.clear()
        except Exception as e:
            conexion.rollback()
            
            QMessageBox.critical(self, "Error", f"Falló la operación:\n{e}")
        finally:
            conexion.close()