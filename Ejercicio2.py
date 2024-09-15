import tkinter as tk
from tkinter import messagebox

# tkinter es el módulo de Python para la creación de interfaces gráficas.
# messagebox se usa para mostrar cuadros de mensaje emergentes.

# Recupera el texto ingresado en el campo de entrada (entry_clave) usando el método get().
# Muestra un cuadro de mensaje emergente con la clave ingresada
def mostrar_clave():
    clave = entry_clave.get()
    messagebox.showinfo("Clave Secreta", f"La clave es: {clave}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de Clave Secreta")

# Crear un label para la clave
label_clave = tk.Label(ventana, text="Ingrese la clave secreta:")
label_clave.pack(padx=10, pady=5)

# Crear un campo de entrada para la clave (con tipo de texto "password")
entry_clave = tk.Entry(ventana, show="*")
entry_clave.pack(padx=10, pady=5)

# Crear un botón para mostrar la clave (opcional, para pruebas)
boton_mostrar = tk.Button(ventana, text="Mostrar Clave", command=mostrar_clave)
boton_mostrar.pack(padx=10, pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
