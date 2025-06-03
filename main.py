from PyQt6.QtWidgets import QApplication
from views.ventana_principal import VentanaPrincipal
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())