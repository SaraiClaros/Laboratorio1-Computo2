import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QRadioButton, QPushButton, QLabel, QMessageBox

class GestionCompraApp(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializar los widgets
        self.init_ui()

    def init_ui(self):
        # Crear el layout principal
        layout = QVBoxLayout()

        # Crear el layout de formulario
        form_layout = QFormLayout()

        # Crear widgets para el formulario
        self.nombre_cliente_input = QLineEdit()
        self.nombre_producto_input = QLineEdit()
        self.cantidad_spinbox = QSpinBox()
        self.cantidad_spinbox.setRange(1, 100)  # Establecer el rango de cantidad
        self.precio_unitario_input = QDoubleSpinBox()
        self.precio_unitario_input.setRange(0.01, 10000)  # Establecer el rango de precio
        self.precio_unitario_input.setDecimals(2)  # Dos decimales para el precio
        self.tipo_producto_combobox = QComboBox()
        self.garantia_opcional = QRadioButton("Garantía Extendida")
        self.sin_garantia = QRadioButton("Sin Garantía")

        # Agregar opciones al combobox
        self.tipo_producto_combobox.addItems(["Electrodomésticos", "Ropa", "Accesorios", "Muebles", "Otros"])

        # Crear el botón para mostrar los datos
        mostrar_datos_btn = QPushButton("Mostrar Resumen")
        mostrar_datos_btn.clicked.connect(self.mostrar_datos)

        # Agregar widgets al formulario
        form_layout.addRow("Nombre del Cliente:", self.nombre_cliente_input)
        form_layout.addRow("Nombre del Producto:", self.nombre_producto_input)
        form_layout.addRow("Cantidad:", self.cantidad_spinbox)
        form_layout.addRow("Precio Unitario:", self.precio_unitario_input)
        form_layout.addRow("Tipo de Producto:", self.tipo_producto_combobox)
        form_layout.addRow("Opciones Adicionales:", self.garantia_opcional)
        form_layout.addWidget(self.sin_garantia)
        
        # Agregar el botón al layout principal
        layout.addLayout(form_layout)
        layout.addWidget(mostrar_datos_btn)

        # Configurar la ventana principal
        self.setLayout(layout)
        self.setWindowTitle("Gestión de Compras en la Tienda")
        self.show()

    def mostrar_datos(self):
        """Muestra el resumen de la compra en un mensaje emergente."""
        nombre_cliente = self.nombre_cliente_input.text()
        nombre_producto = self.nombre_producto_input.text()
        cantidad = self.cantidad_spinbox.value()
        precio_unitario = self.precio_unitario_input.value()
        tipo_producto = self.tipo_producto_combobox.currentText()
        garantia = "Garantía Extendida" if self.garantia_opcional.isChecked() else "Sin Garantía"
        total = cantidad * precio_unitario

        mensaje = (f"Nombre del Cliente: {nombre_cliente}\n"
                   f"Nombre del Producto: {nombre_producto}\n"
                   f"Cantidad: {cantidad}\n"
                   f"Precio Unitario: ${precio_unitario:.2f}\n"
                   f"Tipo de Producto: {tipo_producto}\n"
                   f"Opción Adicional: {garantia}\n"
                   f"Total a Pagar: ${total:.2f}")

        QMessageBox.information(self, "Resumen de la Compra", mensaje)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = GestionCompraApp()
    sys.exit(app.exec_())
