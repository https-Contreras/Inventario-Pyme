# Form implementation generated from reading ui file 'ventana_alertas.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(870, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(parent=self.frame)
        self.frame_superior.setStyleSheet("QFrame{\n"
"    background-color: #0068BC;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    font: 20pt \"Swis721 BlkCn BT\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover { \n"
"    background-color:#5DADE2; \n"
"    \n"
"}\n"
"")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.frame_superior)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(365, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_minimizar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_minimizar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../models/minimizar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_minimizar.setIcon(icon)
        self.btn_minimizar.setIconSize(QtCore.QSize(40, 40))
        self.btn_minimizar.setObjectName("btn_minimizar")
        self.horizontalLayout.addWidget(self.btn_minimizar)
        self.btn_achicar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_achicar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../models/hacerchico.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_achicar.setIcon(icon1)
        self.btn_achicar.setIconSize(QtCore.QSize(40, 40))
        self.btn_achicar.setObjectName("btn_achicar")
        self.horizontalLayout.addWidget(self.btn_achicar)
        self.btn_agrandar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_agrandar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../models/hacergrande.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_agrandar.setIcon(icon2)
        self.btn_agrandar.setIconSize(QtCore.QSize(40, 40))
        self.btn_agrandar.setObjectName("btn_agrandar")
        self.horizontalLayout.addWidget(self.btn_agrandar)
        self.btn_cerrar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_cerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../models/cerrar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_cerrar.setIcon(icon3)
        self.btn_cerrar.setIconSize(QtCore.QSize(40, 40))
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout.addWidget(self.btn_cerrar)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_cuerpo = QtWidgets.QFrame(parent=self.frame)
        self.frame_cuerpo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cuerpo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cuerpo.setObjectName("frame_cuerpo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_cuerpo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_barra = QtWidgets.QFrame(parent=self.frame_cuerpo)
        self.frame_barra.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_barra.setStyleSheet("QFrame {\n"
"    background-color: #60B0C3\n"
"}\n"
"QPushButton{\n"
"    background-color: #0068BC;       \n"
"    color: #FFFFFF;                    /* Texto blanco */\n"
"    border: none;                    /* Sin borde de línea */\n"
"    border-radius: 12px;             /* Bordes redondeados */\n"
"    padding: 10px 20px;              /* Relleno interno */\n"
"    font: bold 12pt \"Arial\"; \n"
"}\n"
"QPushButton#btn_resumen{\n"
"background-color: #ffffff\n"
"}\n"
"QPushButton#btn_resumen:hover{\n"
"background-color: #5DADE2;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5DADE2;       /* Color cuando el mouse pasa encima */\n"
"}\n"
"")
        self.frame_barra.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_barra.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_barra.setObjectName("frame_barra")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_barra)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_resumen = QtWidgets.QPushButton(parent=self.frame_barra)
        self.btn_resumen.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../models/logoIMSreduce.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_resumen.setIcon(icon4)
        self.btn_resumen.setIconSize(QtCore.QSize(120, 120))
        self.btn_resumen.setObjectName("btn_resumen")
        self.verticalLayout_3.addWidget(self.btn_resumen)
        self.btn_inventario = QtWidgets.QPushButton(parent=self.frame_barra)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../models/inventario.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_inventario.setIcon(icon5)
        self.btn_inventario.setIconSize(QtCore.QSize(30, 30))
        self.btn_inventario.setObjectName("btn_inventario")
        self.verticalLayout_3.addWidget(self.btn_inventario)
        self.btn_entradas = QtWidgets.QPushButton(parent=self.frame_barra)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../models/entrada.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_entradas.setIcon(icon6)
        self.btn_entradas.setIconSize(QtCore.QSize(30, 30))
        self.btn_entradas.setObjectName("btn_entradas")
        self.verticalLayout_3.addWidget(self.btn_entradas)
        self.btn_salidas = QtWidgets.QPushButton(parent=self.frame_barra)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../models/salida.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_salidas.setIcon(icon7)
        self.btn_salidas.setIconSize(QtCore.QSize(30, 30))
        self.btn_salidas.setObjectName("btn_salidas")
        self.verticalLayout_3.addWidget(self.btn_salidas)
        self.btn_reportes = QtWidgets.QPushButton(parent=self.frame_barra)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../models/reportes.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_reportes.setIcon(icon8)
        self.btn_reportes.setIconSize(QtCore.QSize(30, 30))
        self.btn_reportes.setObjectName("btn_reportes")
        self.verticalLayout_3.addWidget(self.btn_reportes)
        self.btn_alertas = QtWidgets.QPushButton(parent=self.frame_barra)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../models/alertas.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_alertas.setIcon(icon9)
        self.btn_alertas.setIconSize(QtCore.QSize(30, 30))
        self.btn_alertas.setObjectName("btn_alertas")
        self.verticalLayout_3.addWidget(self.btn_alertas)
        self.btn_configuracion = QtWidgets.QPushButton(parent=self.frame_barra)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../models/configuracion.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_configuracion.setIcon(icon10)
        self.btn_configuracion.setIconSize(QtCore.QSize(30, 30))
        self.btn_configuracion.setObjectName("btn_configuracion")
        self.verticalLayout_3.addWidget(self.btn_configuracion)
        self.horizontalLayout_2.addWidget(self.frame_barra)
        self.frame_contenido = QtWidgets.QFrame(parent=self.frame_cuerpo)
        self.frame_contenido.setStyleSheet("background-color: #99D8DD")
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_contenido)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_busqueda = QtWidgets.QFrame(parent=self.frame_contenido)
        self.frame_busqueda.setStyleSheet("QFrame{\n"
"    background-color: #ffffff\n"
"}\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover { \n"
"    background-color:#5DADE2; \n"
"    min-width: 60px;\n"
"    min-height: 60px;\n"
"    border-radius: 30px; \n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid #000000;\n"
"    border-radius:10px;\n"
"    height:40px;\n"
"    font: 20pt \"Swis721 BlkCn BT\";\n"
"}\n"
"QLabel {\n"
"    color: black;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    font: 20pt \"Swis721 BlkCn BT\";\n"
"}")
        self.frame_busqueda.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_busqueda.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_busqueda.setObjectName("frame_busqueda")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_busqueda)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_ocultar = QtWidgets.QPushButton(parent=self.frame_busqueda)
        self.bt_ocultar.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../models/izquierda.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_ocultar.setIcon(icon11)
        self.bt_ocultar.setIconSize(QtCore.QSize(50, 50))
        self.bt_ocultar.setObjectName("bt_ocultar")
        self.horizontalLayout_3.addWidget(self.bt_ocultar)
        self.bt_mostrar = QtWidgets.QPushButton(parent=self.frame_busqueda)
        self.bt_mostrar.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../models/derecha.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_mostrar.setIcon(icon12)
        self.bt_mostrar.setIconSize(QtCore.QSize(50, 50))
        self.bt_mostrar.setObjectName("bt_mostrar")
        self.horizontalLayout_3.addWidget(self.bt_mostrar)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_busqueda)
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_4.addWidget(self.frame_busqueda)
        self.frame_informacion = QtWidgets.QFrame(parent=self.frame_contenido)
        self.frame_informacion.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_informacion.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_informacion.setObjectName("frame_informacion")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_informacion)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_productos = QtWidgets.QFrame(parent=self.frame_informacion)
        self.frame_productos.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_productos.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_productos.setObjectName("frame_productos")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_productos)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableproductostock = QtWidgets.QTableWidget(parent=self.frame_productos)
        self.tableproductostock.setObjectName("tableproductostock")
        self.tableproductostock.setColumnCount(0)
        self.tableproductostock.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableproductostock)
        self.verticalLayout_5.addWidget(self.frame_productos)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_informacion)
        self.frame_3.setStyleSheet("QFrame{\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: black;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    font: 18pt \"Swis721 BlkCn BT\";\n"
"}\n"
"QSpinBox::up-button { width: 0px; height: 0px; border: none; }\n"
"QSpinBox::down-button { width: 0px; height: 0px; border: none; }\n"
"QSpinBox{\n"
"    background-color:#ffffff;\n"
"    color: black;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    font: 18pt \"Swis721 BlkCn BT\";\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.spinBox_sinstock = QtWidgets.QSpinBox(parent=self.frame_3)
        self.spinBox_sinstock.setEnabled(False)
        self.spinBox_sinstock.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.spinBox_sinstock.setObjectName("spinBox_sinstock")
        self.horizontalLayout_5.addWidget(self.spinBox_sinstock)
        spacerItem6 = QtWidgets.QSpacerItem(126, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.spinBox_bajostock = QtWidgets.QSpinBox(parent=self.frame_3)
        self.spinBox_bajostock.setEnabled(False)
        self.spinBox_bajostock.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.spinBox_bajostock.setWrapping(False)
        self.spinBox_bajostock.setObjectName("spinBox_bajostock")
        self.horizontalLayout_5.addWidget(self.spinBox_bajostock)
        spacerItem7 = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_5.setStretch(0, 7)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.frame_informacion)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 6)
        self.horizontalLayout_2.addWidget(self.frame_contenido)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.addWidget(self.frame_cuerpo)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ventana Alertas"))
        self.btn_inventario.setText(_translate("Form", "Inventario"))
        self.btn_entradas.setText(_translate("Form", "Entradas"))
        self.btn_salidas.setText(_translate("Form", "Salidas"))
        self.btn_reportes.setText(_translate("Form", "Reportes"))
        self.btn_alertas.setText(_translate("Form", "Alertas"))
        self.btn_configuracion.setText(_translate("Form", "Configuracion"))
        self.label_4.setText(_translate("Form", "Productos con stock bajo o sin stock"))
        self.label_2.setText(_translate("Form", "Productos sin stock"))
        self.label_3.setText(_translate("Form", "Productos con stock bajo"))
