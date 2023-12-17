import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QStackedWidget

from ventaboletos import VentaBoletos

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CINEMA PM')
        self.resize(500, 350)

        # Crear instancias de pages

        layout = QVBoxLayout()

        # Widgets
        self.btn_ir_a_ventaboletos = QPushButton("Ir a Venta de Boletos", self)
        self.btn_ir_a_ventaboletos.setGeometry(50, 50, 200, 50)
        self.btn_ir_a_ventaboletos.clicked.connect(self.mostrar_ventaboletos)

    def mostrar_ventaboletos(self):
        self.venta_boletos = VentaBoletos()
        self.venta_boletos.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MyApp()
    ventana.show()
    app.exec()