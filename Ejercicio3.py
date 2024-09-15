import tkinter as tk
from tkinter import messagebox

def mostrar_info():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    messagebox.showinfo("Información Ingresada", f"Número de Cédula: {cedula}\nNombre Completo: {nombre}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de Información")

# Crear un label y campo de entrada para el número de cédula
label_cedula = tk.Label(ventana, text="Número de Cédula:")
label_cedula.pack(padx=10, pady=5)

entry_cedula = tk.Entry(ventana)
entry_cedula.pack(padx=10, pady=5)

# Crear un label y campo de entrada para el nombre completo
label_nombre = tk.Label(ventana, text="Nombre Completo:")
label_nombre.pack(padx=10, pady=5)

entry_nombre = tk.Entry(ventana)
entry_nombre.pack(padx=10, pady=5)

# Crear un botón para mostrar la información ingresada
boton_mostrar = tk.Button(ventana, text="Mostrar Información", command=mostrar_info)
boton_mostrar.pack(padx=10, pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
