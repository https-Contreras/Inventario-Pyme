# Form implementation generated from reading ui file 'ventana_editareliminar.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 600)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
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
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_regresar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_regresar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../models/regresar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_regresar.setIcon(icon)
        self.btn_regresar.setIconSize(QtCore.QSize(40, 40))
        self.btn_regresar.setObjectName("btn_regresar")
        self.horizontalLayout.addWidget(self.btn_regresar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(parent=self.frame_superior)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(262, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_minimizar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_minimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../models/minimizar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QtCore.QSize(40, 40))
        self.btn_minimizar.setObjectName("btn_minimizar")
        self.horizontalLayout.addWidget(self.btn_minimizar)
        self.btn_achicar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_achicar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../models/hacerchico.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_achicar.setIcon(icon2)
        self.btn_achicar.setIconSize(QtCore.QSize(40, 40))
        self.btn_achicar.setObjectName("btn_achicar")
        self.horizontalLayout.addWidget(self.btn_achicar)
        self.btn_agrandar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_agrandar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../models/hacergrande.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_agrandar.setIcon(icon3)
        self.btn_agrandar.setIconSize(QtCore.QSize(40, 40))
        self.btn_agrandar.setObjectName("btn_agrandar")
        self.horizontalLayout.addWidget(self.btn_agrandar)
        self.btn_cerrar = QtWidgets.QPushButton(parent=self.frame_superior)
        self.btn_cerrar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../models/cerrar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QtCore.QSize(40, 40))
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout.addWidget(self.btn_cerrar)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_superior)
        self.frame_busqueda = QtWidgets.QFrame(parent=self.frame)
        self.frame_busqueda.setStyleSheet("QFrame {\n"
"    background-color: #60B0C3\n"
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
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    font: 20pt \"Swis721 BlkCn BT\";\n"
"}\n"
"")
        self.frame_busqueda.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_busqueda.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_busqueda.setObjectName("frame_busqueda")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_busqueda)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_buscar = QtWidgets.QLabel(parent=self.frame_busqueda)
        self.label_buscar.setObjectName("label_buscar")
        self.horizontalLayout_4.addWidget(self.label_buscar)
        self.LnEdit_buscar = QtWidgets.QLineEdit(parent=self.frame_busqueda)
        self.LnEdit_buscar.setObjectName("LnEdit_buscar")
        self.horizontalLayout_4.addWidget(self.LnEdit_buscar)
        self.btn_buscar = QtWidgets.QPushButton(parent=self.frame_busqueda)
        self.btn_buscar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../models/buscar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_buscar.setIcon(icon5)
        self.btn_buscar.setIconSize(QtCore.QSize(50, 50))
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_4.addWidget(self.btn_buscar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_busqueda)
        self.frame_cuerpo = QtWidgets.QFrame(parent=self.frame)
        self.frame_cuerpo.setStyleSheet("background-color: #99D8DD")
        self.frame_cuerpo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cuerpo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cuerpo.setObjectName("frame_cuerpo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_cuerpo)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_labels = QtWidgets.QFrame(parent=self.frame_cuerpo)
        self.frame_labels.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame_labels.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    font: 20pt \"Swis721 BlkCn BT\";\n"
"    text-align: right;\n"
"}")
        self.frame_labels.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_labels.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_labels.setObjectName("frame_labels")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_labels)
        self.verticalLayout_3.setContentsMargins(3, 0, 0, 5)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_labels)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_labels)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_labels)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_labels)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_labels)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        spacerItem10 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_3.addItem(spacerItem10)
        self.btn_eliminar = QtWidgets.QPushButton(parent=self.frame_labels)
        self.btn_eliminar.setStyleSheet("QPushButton{\n"
"    background-color: red;       \n"
"    color: #FFFFFF;                    /* Texto blanco */\n"
"    border: none;                    /* Sin borde de línea */\n"
"    border-radius: 12px;             /* Bordes redondeados */\n"
"    padding: 10px 20px;              /* Relleno interno */\n"
"    font: bold 12pt \"Arial\"; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5DADE2;       /* Color cuando el mouse pasa encima */\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../models/basura.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_eliminar.setIcon(icon6)
        self.btn_eliminar.setIconSize(QtCore.QSize(30, 30))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.verticalLayout_3.addWidget(self.btn_eliminar)
        self.horizontalLayout_3.addWidget(self.frame_labels)
        self.frame_llenado = QtWidgets.QFrame(parent=self.frame_cuerpo)
        self.frame_llenado.setStyleSheet("QFrame{\n"
"    background-color: #C0E4E5\n"
"}\n"
"QLineEdit{\n"
"    background-color: rgb(232, 232, 232);\n"
"    border-radius: 10px;\n"
"    height: 30px;\n"
"    font: 20pt \"Swis721 BlkCn BT\";\n"
"    \n"
"}")
        self.frame_llenado.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_llenado.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_llenado.setObjectName("frame_llenado")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_llenado)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.LnEdit_id_edit = QtWidgets.QLineEdit(parent=self.frame_llenado)
        self.LnEdit_id_edit.setObjectName("LnEdit_id_edit")
        self.verticalLayout_4.addWidget(self.LnEdit_id_edit)
        spacerItem11 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.LnEdit_producto_edit = QtWidgets.QLineEdit(parent=self.frame_llenado)
        self.LnEdit_producto_edit.setObjectName("LnEdit_producto_edit")
        self.verticalLayout_4.addWidget(self.LnEdit_producto_edit)
        spacerItem12 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.LnEdit_descripcion_edit = QtWidgets.QLineEdit(parent=self.frame_llenado)
        self.LnEdit_descripcion_edit.setObjectName("LnEdit_descripcion_edit")
        self.verticalLayout_4.addWidget(self.LnEdit_descripcion_edit)
        spacerItem13 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.LnEdit_stockactual_edit = QtWidgets.QLineEdit(parent=self.frame_llenado)
        self.LnEdit_stockactual_edit.setObjectName("LnEdit_stockactual_edit")
        self.verticalLayout_4.addWidget(self.LnEdit_stockactual_edit)
        spacerItem14 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        self.LnEdit_stockminimo_edit = QtWidgets.QLineEdit(parent=self.frame_llenado)
        self.LnEdit_stockminimo_edit.setObjectName("LnEdit_stockminimo_edit")
        self.verticalLayout_4.addWidget(self.LnEdit_stockminimo_edit)
        spacerItem15 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_4.addItem(spacerItem15)
        self.btn_agregar = QtWidgets.QPushButton(parent=self.frame_llenado)
        self.btn_agregar.setStyleSheet("QPushButton{\n"
"    background-color: #0068BC;       \n"
"    color: #FFFFFF;                    /* Texto blanco */\n"
"    border: none;                    /* Sin borde de línea */\n"
"    border-radius: 12px;             /* Bordes redondeados */\n"
"    padding: 10px 20px;              /* Relleno interno */\n"
"    font: bold 12pt \"Arial\"; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5DADE2;       /* Color cuando el mouse pasa encima */\n"
"}\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../models/agregar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_agregar.setIcon(icon7)
        self.btn_agregar.setIconSize(QtCore.QSize(30, 30))
        self.btn_agregar.setObjectName("btn_agregar")
        self.verticalLayout_4.addWidget(self.btn_agregar)
        self.horizontalLayout_3.addWidget(self.frame_llenado)
        self.verticalLayout.addWidget(self.frame_cuerpo)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 7)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ventana Editar/Eliminar producto"))
        self.label_buscar.setText(_translate("Form", "Editar producto por ID o nombre"))
        self.LnEdit_buscar.setPlaceholderText(_translate("Form", "Buscar producto a editar/eliminar"))
        self.label_2.setText(_translate("Form", "ID del producto"))
        self.label_3.setText(_translate("Form", "Nombre del producto"))
        self.label_4.setText(_translate("Form", "Precio del producto"))
        self.label_6.setText(_translate("Form", "Stock actual"))
        self.label_7.setText(_translate("Form", "Stock minimo"))
        self.btn_eliminar.setText(_translate("Form", "Eliminar"))
        self.LnEdit_id_edit.setPlaceholderText(_translate("Form", "ID..."))
        self.LnEdit_producto_edit.setPlaceholderText(_translate("Form", "Nombre..."))
        self.LnEdit_descripcion_edit.setPlaceholderText(_translate("Form", "Precio..."))
        self.LnEdit_stockactual_edit.setPlaceholderText(_translate("Form", "Stock (positivo)..."))
        self.LnEdit_stockminimo_edit.setPlaceholderText(_translate("Form", "Stock (minimo)..."))
        self.btn_agregar.setText(_translate("Form", "Editar"))
