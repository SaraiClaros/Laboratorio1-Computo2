import tkinter as tk
from tkinter import ttk, messagebox

def actualizar_campos(mascota_seleccionada):
    """ Actualiza los campos de entrada según la mascota seleccionada. """
    index = mascotas_opciones.index(mascota_seleccionada)
    nombre_var.set(entry_nombre[index].get())
    edad_var.set(entry_edad[index].get())
    tipo_var.set(entry_tipo[index].get())

def guardar_datos():
    """ Guarda los datos ingresados para la mascota seleccionada. """
    mascota_seleccionada = combobox_mascota.get()
    index = mascotas_opciones.index(mascota_seleccionada)
    entry_nombre[index].set(nombre_var.get())
    entry_edad[index].set(edad_var.get())
    entry_tipo[index].set(tipo_var.get())
    messagebox.showinfo("Información Guardada", f"Datos guardados para {mascota_seleccionada}.")

def mostrar_datos():
    """ Muestra los datos actuales de la mascota seleccionada. """
    mascota_seleccionada = combobox_mascota.get()
    if mascota_seleccionada in mascotas_opciones:
        index = mascotas_opciones.index(mascota_seleccionada)
        nombre = entry_nombre[index].get()
        edad = entry_edad[index].get()
        tipo = entry_tipo[index].get()
        messagebox.showinfo("Datos de la Mascota", f"Nombre: {nombre}\nEdad: {edad}\nTipo: {tipo}")

def mostrar_todos_los_datos():
    """ Muestra los datos de todas las mascotas. """
    datos = []
    for i, mascota in enumerate(mascotas_opciones):
        nombre = entry_nombre[i].get()
        edad = entry_edad[i].get()
        tipo = entry_tipo[i].get()
        datos.append(f"{mascota}:\n  Nombre: {nombre}\n  Edad: {edad}\n  Tipo: {tipo}\n")
    messagebox.showinfo("Datos de Todas las Mascotas", "\n".join(datos))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de Datos de Mascotas")

# Crear un marco para contener los campos de entrada
frame = tk.Frame(ventana, padx=10, pady=10)
frame.pack(padx=20, pady=20)

# Opciones para el combobox de selección de mascota
mascotas_opciones = ["Mascota 1", "Mascota 2", "Mascota 3"]

# Crear el combobox para seleccionar la mascota
tk.Label(frame, text="Seleccionar Mascota:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
combobox_mascota = ttk.Combobox(frame, values=mascotas_opciones, width=20)
combobox_mascota.grid(row=0, column=1, padx=5, pady=5)
combobox_mascota.set("Seleccionar Mascota")

# Crear variables para los campos de entrada
nombre_var = tk.StringVar()
edad_var = tk.StringVar()
tipo_var = tk.StringVar()

# Crear etiquetas y campos de entrada para los datos de las mascotas
tk.Label(frame, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=nombre_var, width=30).grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Edad:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=edad_var, width=30).grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Raza:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=tipo_var, width=30).grid(row=3, column=1, padx=5, pady=5)

# Botón para guardar los datos
boton_guardar = tk.Button(frame, text="Guardar Datos", command=guardar_datos, bg="lightblue")
boton_guardar.grid(row=4, column=0, columnspan=2, pady=10)

# Botón para mostrar los datos actuales
boton_mostrar = tk.Button(frame, text="Mostrar Datos", command=mostrar_datos, bg="lightgreen")
boton_mostrar.grid(row=5, column=0, columnspan=2, pady=10)

# Botón para mostrar todos los datos
boton_mostrar_todos = tk.Button(frame, text="Mostrar Todos los Datos", command=mostrar_todos_los_datos, bg="lightcoral")
boton_mostrar_todos.grid(row=6, column=0, columnspan=2, pady=10)

# Función para manejar el evento de selección en el combobox
def seleccionar_mascota(event):
    mascota_seleccionada = combobox_mascota.get()
    if mascota_seleccionada in mascotas_opciones:
        actualizar_campos(mascota_seleccionada)

# Asociar el evento de selección del combobox
combobox_mascota.bind("<<ComboboxSelected>>", seleccionar_mascota)

# Variables para almacenar los datos de las mascotas
entry_nombre = [tk.StringVar(value=""), tk.StringVar(value=""), tk.StringVar(value="")]
entry_edad = [tk.StringVar(value=""), tk.StringVar(value=""), tk.StringVar(value="")]
entry_tipo = [tk.StringVar(value=""), tk.StringVar(value=""), tk.StringVar(value="")]

# Inicializar los campos con datos predeterminados para la primera mascota
actualizar_campos(mascotas_opciones[0])

# Ejecutar el bucle principal
ventana.mainloop()
