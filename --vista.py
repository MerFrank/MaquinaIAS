import tkinter as tk
from tkinter import ttk, filedialog

# Crear ventana principal
root = tk.Tk()
root.title("Simulador de Instrucciones")
root.geometry("800x600")

# Sección de tabla de instrucciones
frame_instrucciones = tk.LabelFrame(root, text="Tabla de Instrucciones", padx=10, pady=10)
frame_instrucciones.pack(fill="both", expand=True, padx=10, pady=10)

# Tabla para las instrucciones
tabla_instrucciones = ttk.Treeview(frame_instrucciones, columns=("Linea", "Instrucción HEX", "Instrucción"), show="headings")
tabla_instrucciones.heading("Linea", text="Línea")
tabla_instrucciones.heading("Instrucción HEX", text="Instrucción (HEX)")
tabla_instrucciones.heading("Instrucción", text="Instrucción")
tabla_instrucciones.pack(fill="both", expand=True)

# Sección de tabla de datos
frame_datos = tk.LabelFrame(root, text="Datos de Memoria", padx=10, pady=10)
frame_datos.pack(fill="both", expand=True, padx=10, pady=10)

# Tabla para los datos
tabla_datos = ttk.Treeview(frame_datos, columns=("Dirección", "Dato"), show="headings")
tabla_datos.heading("Dirección", text="Dirección")
tabla_datos.heading("Dato", text="Dato")
tabla_datos.pack(fill="both", expand=True)

# Sección de datos del sistema
frame_sistema = tk.LabelFrame(root, text="Datos del Sistema", padx=10, pady=10)
frame_sistema.pack(fill="both", expand=True, padx=10, pady=10)

# Etiquetas para mostrar datos del sistema
etiqueta_acumulador = tk.Label(frame_sistema, text="Acumulador: 0")
etiqueta_acumulador.pack(anchor="w")

etiqueta_mq = tk.Label(frame_sistema, text="MQ: 0")
etiqueta_mq.pack(anchor="w")

etiqueta_ciclos = tk.Label(frame_sistema, text="Ciclos de ejecución: 0")
etiqueta_ciclos.pack(anchor="w")

# Función para cargar instrucciones
def cargar_instrucciones():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo de instrucciones", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "r") as f:
            instrucciones = f.readlines()
            for i, instruccion in enumerate(instrucciones):
                tabla_instrucciones.insert("", "end", values=(i+1, instruccion.strip(), ""))

# Botón para cargar instrucciones
boton_cargar = tk.Button(root, text="Cargar Instrucciones", command=cargar_instrucciones)
boton_cargar.pack(pady=10)

# Iniciar aplicación
root.mainloop()