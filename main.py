import sys
from PyQt6.QtWidgets import QApplication
from Backend.controlador import Controlador

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controlador = Controlador()
    sys.exit(app.exec())
