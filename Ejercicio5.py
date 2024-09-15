import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    """ Guarda los datos ingresados y muestra un mensaje de confirmación. """
    datos = {
        "Nombre": nombre_var.get(),
        "Apellido": apellido_var.get(),
        "Edad": edad_var.get(),
        "Estatura": estatura_var.get(),
        "Ocupación": ocupacion_var.get(),
        "Dirección": direccion_var.get(),
        "Teléfono": telefono_var.get(),
        "Nacionalidad": nacionalidad_var.get(),
        "Fecha de Nacimiento": fecha_nacimiento_var.get(),
        "Estado Civil": estado_civil_var.get()
    }
    
    mensaje = "\n".join([f"{key}: {value}" for key, value in datos.items()])
    messagebox.showinfo("Datos Guardados", mensaje)

def mostrar_datos():
    """ Muestra los datos actuales ingresados. """
    datos = {
        "Nombre": nombre_var.get(),
        "Apellido": apellido_var.get(),
        "Edad": edad_var.get(),
        "Estatura": estatura_var.get(),
        "Ocupación": ocupacion_var.get(),
        "Dirección": direccion_var.get(),
        "Teléfono": telefono_var.get(),
        "Nacionalidad": nacionalidad_var.get(),
        "Fecha de Nacimiento": fecha_nacimiento_var.get(),
        "Estado Civil": estado_civil_var.get()
    }
    
    mensaje = "\n".join([f"{key}: {value}" for key, value in datos.items()])
    messagebox.showinfo("Datos Ingresados", mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Datos Personales")

# Crear un marco para contener los campos de entrada
frame = tk.Frame(ventana, padx=10, pady=10)
frame.pack(padx=20, pady=20)

# Título en la parte superior
titulo = tk.Label(frame, text="Datos Personales", font=("Helvetica", 16, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Crear variables para los campos de entrada
nombre_var = tk.StringVar()
apellido_var = tk.StringVar()
edad_var = tk.StringVar()
estatura_var = tk.StringVar()
ocupacion_var = tk.StringVar()
direccion_var = tk.StringVar()
telefono_var = tk.StringVar()
nacionalidad_var = tk.StringVar()
fecha_nacimiento_var = tk.StringVar()
estado_civil_var = tk.StringVar()

# Crear etiquetas y campos de entrada para los datos de la persona
tk.Label(frame, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=nombre_var, width=40).grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Apellido:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=apellido_var, width=40).grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Edad:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=edad_var, width=40).grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Estatura (cm):").grid(row=4, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=estatura_var, width=40).grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame, text="Ocupación:").grid(row=5, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=ocupacion_var, width=40).grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame, text="Dirección:").grid(row=6, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=direccion_var, width=40).grid(row=6, column=1, padx=5, pady=5)

tk.Label(frame, text="Teléfono:").grid(row=7, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=telefono_var, width=40).grid(row=7, column=1, padx=5, pady=5)

tk.Label(frame, text="Nacionalidad:").grid(row=8, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=nacionalidad_var, width=40).grid(row=8, column=1, padx=5, pady=5)

tk.Label(frame, text="Fecha de Nacimiento:").grid(row=9, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=fecha_nacimiento_var, width=40).grid(row=9, column=1, padx=5, pady=5)

tk.Label(frame, text="Estado Civil:").grid(row=10, column=0, padx=5, pady=5, sticky='e')
tk.Entry(frame, textvariable=estado_civil_var, width=40).grid(row=10, column=1, padx=5, pady=5)

# Botón para guardar los datos
boton_guardar = tk.Button(frame, text="Guardar Datos", command=guardar_datos, bg="lightblue")
boton_guardar.grid(row=11, column=0, columnspan=2, pady=10)

# Botón para mostrar los datos actuales
boton_mostrar = tk.Button(frame, text="Mostrar Datos", command=mostrar_datos, bg="lightgreen")
boton_mostrar.grid(row=12, column=0, columnspan=2, pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
