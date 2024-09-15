import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QDialog
from PyQt5.QtCore import Qt

# Función para mostrar la ventana con el nombre completo y la edad
def mostrar_datos(nombre, edad):
    ventana = QDialog()  # Usamos QDialog para la nueva ventana
    ventana.setWindowTitle('Datos Ingresados')

    # Crear un layout vertical para la ventana de salida
    layout = QVBoxLayout()

    # Crear las etiquetas con el nombre y la edad centrados
    nombre_label = QLabel(f'Nombre Completo: {nombre}')
    edad_label = QLabel(f'Edad: {edad} años')

    nombre_label.setAlignment(Qt.AlignCenter)
    edad_label.setAlignment(Qt.AlignCenter)

    # Agregar las etiquetas al layout
    layout.addWidget(nombre_label)
    layout.addWidget(edad_label)

    ventana.setLayout(layout)
    ventana.resize(400, 200)
    ventana.exec_()  # Mostrar la nueva ventana como un diálogo modal

# Función principal para la ventana de entrada de datos
def ventana_principal():
    # Crear la aplicación
    app = QApplication(sys.argv)

    # Crear la ventana principal
    ventana = QWidget()
    ventana.setWindowTitle('Ingreso de Datos')

    # Crear el layout principal
    layout = QVBoxLayout()

    # Crear los campos de entrada de texto
    nombre_input = QLineEdit()
    nombre_input.setPlaceholderText('Ingrese su nombre completo')

    edad_input = QLineEdit()
    edad_input.setPlaceholderText('Ingrese su edad')

    # Crear el botón para enviar los datos
    boton = QPushButton('Mostrar Datos')

    # Definir la acción del botón
    def on_click():
        nombre = nombre_input.text()
        edad = edad_input.text()
        if nombre and edad:  # Verificar que los campos no estén vacíos
            mostrar_datos(nombre, edad)

    boton.clicked.connect(on_click)

    # Agregar los widgets al layout
    layout.addWidget(nombre_input)
    layout.addWidget(edad_input)
    layout.addWidget(boton)

    # Establecer el layout en la ventana
    ventana.setLayout(layout)

    # Ajustar el tamaño de la ventana y mostrarla
    ventana.resize(400, 200)
    ventana.show()

    # Iniciar el bucle de la aplicación
    sys.exit(app.exec_())

# Llamar a la función principal
if __name__ == '__main__':
    ventana_principal()
