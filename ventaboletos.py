import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QSpinBox

class VentaBoletos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Venta de Boletos")
        self.setGeometry(100, 100, 500, 350)
        self.num_boletos = 0
        self.precio_total = 0

        layout = QVBoxLayout()

        self.label = QLabel('Comprar boletos ')
        layout.addWidget(self.label)
        #self.precio_total = QLabel(f'{self.num_boletos * 5000}')

        self.boletos = QLabel('¿Cuántos boletos deseas comprar?')
        self.num_boletos_spinbox = QSpinBox()
        self.num_boletos_spinbox.valueChanged.connect(self.prevew_precios)

        self.button_comprar = QPushButton('Comprar')

        layout.addWidget(self.boletos)
        layout.addWidget(self.num_boletos_spinbox)
        layout.addWidget(self.button_comprar, alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignRight)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def prevew_precios(self):
        self.num_boletos = self.num_boletos_spinbox.value()
        self.label.setText(f'Total a pagar es de ${self.num_boletos * 5000}')

    
    def comprar_boletos(self):
        #aca irá que abre otra pestaña que estará vinculada a viewasientos.py

if __name__ == "__main__":
    app = QApplication([])
    venta_boletos = VentaBoletos()
    venta_boletos.show()
    sys.exit(app.exec())