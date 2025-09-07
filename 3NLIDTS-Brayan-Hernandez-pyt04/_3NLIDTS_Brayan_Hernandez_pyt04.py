import tkinter as tk
from tkinter import messagebox

# Funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def guardar_valores():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    genero = {
        1: "Masculino",
        2: "Femenino"
    }.get(var_genero.get(), "No especificado")

    datos = (
        f"Nombres: {nombres}\n"
        f"Apellidos: {apellidos}\n"
        f"Edad: {edad}\n"
        f"Estatura: {estatura}\n"
        f"Teléfono: {telefono}\n"
        f"Género: {genero}"
    )

    with open("302024Datos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(datos + "\n\n")

    messagebox.showinfo("Guardado", "Los datos han sido guardados exitosamente.\n\n" + datos)
    limpiar_campos()

ventana = tk.Tk()
ventana.title("Formulario de Datos Personales")

var_genero = tk.IntVar()

# Estilo general
fuente_label = ("Segoe UI", 11)
fuente_titulo = ("Segoe UI", 16, "bold")
fuente_entry = ("Segoe UI", 11)

# Título
titulo = tk.Label(ventana, text="Formulario de Datos Personales", font=fuente_titulo)
titulo.grid(row=0, column=0, columnspan=2, pady=20)

# Función para crear campos
def crear_label_entry(fila, texto):
    label = tk.Label(ventana, text=texto, font=fuente_label)
    label.grid(row=fila, column=0, sticky="e", padx=10, pady=5)
    entry = tk.Entry(ventana, font=fuente_entry, width=30)
    entry.grid(row=fila, column=1, padx=10, pady=5)
    return entry

# Crear entradas
tbNombre = crear_label_entry(1, "Nombres:")
tbApellidos = crear_label_entry(2, "Apellidos:")
tbTelefono = crear_label_entry(3, "Teléfono:")
tbEdad = crear_label_entry(4, "Edad:")
tbEstatura = crear_label_entry(5, "Estatura (m):")

# Género
lbGenero = tk.Label(ventana, text="Género:", font=fuente_label)
lbGenero.grid(row=6, column=0, sticky="e", padx=10, pady=5)

frame_genero = tk.Frame(ventana)
frame_genero.grid(row=6, column=1, sticky="w")

rbHombre = tk.Radiobutton(frame_genero, text="Masculino", variable=var_genero, value=1, font=fuente_label)
rbHombre.pack(side="left", padx=5)
rbMujer = tk.Radiobutton(frame_genero, text="Femenino", variable=var_genero, value=2, font=fuente_label)
rbMujer.pack(side="left", padx=5)

# Botones
estilo_btn = {"font": ("Segoe UI", 11, "bold"), "width": 18}

btnBorrar = tk.Button(ventana, text="Borrar valores", command=limpiar_campos, **estilo_btn)
btnBorrar.grid(row=7, column=0, pady=25)

btnGuardar = tk.Button(ventana, text="Guardar valores", command=guardar_valores, **estilo_btn)
btnGuardar.grid(row=7, column=1)

# Botón para cambiar tema
btnTema = tk.Button(ventana, text="Cambiar a Modo Oscuro", command=cambiar_tema, **estilo_btn)
btnTema.grid(row=8, column=0, columnspan=2, pady=10)

# Aplicar tema por primera vez
aplicar_tema()

ventana.mainloop()
