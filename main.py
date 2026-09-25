
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QRadioButton, QButtonGroup

app = QApplication([])
window = QWidget()
window.setWindowTitle('Mi primera aplicación')
window.resize(400, 300)
window.move(0, 0)

texto = QLabel("Es un milagro")
def mostrar_mensaje():
    main_layout.addWidget(texto, alignment=Qt.AlignCenter)

button = QPushButton("Boton con un secreto")
button.clicked.connect(mostrar_mensaje)
main_layout = QVBoxLayout()
main_layout.addWidget(button, alignment=Qt.AlignCenter)
window.setLayout(main_layout)
window.show()
app.exec_()

print("Hola")

