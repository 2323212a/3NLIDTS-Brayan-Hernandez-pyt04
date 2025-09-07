import tkinter as tk
from tkinter import messagebox
import os

# ---------- Configuracion de colores ----------
modo_oscuro = False

color_claro = {
    "bg": "#f0f4f7",
    "fg": "#2c3e50",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000",
    "btn_bg": "#3498db",
    "btn_fg": "#ffffff"
}

color_oscuro = {
    "bg": "#1e1e1e",
    "fg": "#dcdcdc",
    "entry_bg": "#2b2b2b",
    "entry_fg": "#ffffff",
    "btn_bg": "#3a8fd4",
    "btn_fg": "#ffffff"
}


# ---------- Funciones ----------
def centrar_ventana(win, ancho, alto):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - ancho) // 2
    y = (screen_height - alto) // 2
    win.geometry(f"{ancho}x{alto}+{x}+{y}")


def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)


def campos_vacios():
    return (
        not tbNombre.get().strip() or
        not tbApellidos.get().strip() or
        not tbEdad.get().strip() or
        not tbEstatura.get().strip() or
        not tbTelefono.get().strip()
    )


def guardar_valores():
    if campos_vacios():
        messagebox.showwarning("Campos vacios", "Por favor complete todos los campos antes de guardar.")
        return

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
        f"Telefono: {telefono}\n"
        f"Genero: {genero}"
    )

    confirmar = messagebox.askyesno("Confirmar", "Desea guardar los siguientes datos?\n\n" + datos)

    if confirmar:
        with open("302024Datos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n\n")

        messagebox.showinfo("Guardado", "Datos guardados correctamente.")
        limpiar_campos()


def mostrar_datos_guardados():
    if not os.path.exists("302024Datos.txt"):
        messagebox.showinfo("Sin datos", "Aun no hay datos guardados.")
        return

    with open("302024Datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read().strip()

    if contenido:
        messagebox.showinfo("Datos guardados", contenido)
    else:
        messagebox.showinfo("Sin datos", "Aun no hay datos guardados.")


def cambiar_tema():
    global modo_oscuro
    modo_oscuro = not modo_oscuro
    aplicar_tema()
    btnTema.config(text="Modo Claro" if modo_oscuro else "Modo Oscuro")

def aplicar_tema():
    colores = color_oscuro if modo_oscuro else color_claro
    ventana.configure(bg=colores["bg"])

    for widget in ventana.winfo_children():
        # Aplica bg y fg solo a widgets que lo soportan
        if isinstance(widget, (tk.Label, tk.Radiobutton)):
            widget.configure(bg=colores["bg"], fg=colores["fg"])
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=colores["entry_bg"], fg=colores["entry_fg"], insertbackground=colores["entry_fg"])
        elif isinstance(widget, tk.Button):
            widget.configure(bg=colores["btn_bg"], fg=colores["btn_fg"], activebackground=colores["btn_bg"])
        elif isinstance(widget, tk.Frame):
            widget.configure(bg=colores["bg"])  # Solo cambia el fondo


# ---------- Interfaz ----------
ventana = tk.Tk()
ventana.title("Formulario de Datos Personales")
centrar_ventana(ventana, 500, 620)

var_genero = tk.IntVar()

fuente_label = ("Segoe UI", 11)
fuente_titulo = ("Segoe UI", 16, "bold")
fuente_entry = ("Segoe UI", 11)

# Titulo
titulo = tk.Label(ventana, text="Formulario de Datos Personales", font=fuente_titulo)
titulo.grid(row=0, column=0, columnspan=2, pady=20)


def crear_label_entry(fila, texto):
    label = tk.Label(ventana, text=texto, font=fuente_label)
    label.grid(row=fila, column=0, sticky="e", padx=10, pady=5)
    entry = tk.Entry(ventana, font=fuente_entry, width=30)
    entry.grid(row=fila, column=1, padx=10, pady=5)
    return entry


# Entradas
tbNombre = crear_label_entry(1, "Nombres:")
tbApellidos = crear_label_entry(2, "Apellidos:")
tbTelefono = crear_label_entry(3, "Telefono:")
tbEdad = crear_label_entry(4, "Edad:")
tbEstatura = crear_label_entry(5, "Estatura (m):")

# Genero
lbGenero = tk.Label(ventana, text="Genero:", font=fuente_label)
lbGenero.grid(row=6, column=0, sticky="e", padx=10, pady=5)

frame_genero = tk.Frame(ventana)
frame_genero.grid(row=6, column=1, sticky="w")

rbHombre = tk.Radiobutton(frame_genero, text="Masculino", variable=var_genero, value=1, font=fuente_label)
rbHombre.pack(side="left", padx=5)
rbMujer = tk.Radiobutton(frame_genero, text="Femenino", variable=var_genero, value=2, font=fuente_label)
rbMujer.pack(side="left", padx=5)

# Botones
estilo_btn = {"font": ("Segoe UI", 11, "bold"), "width": 18}

btnBorrar = tk.Button(ventana, text="Borrar Valores", command=limpiar_campos, **estilo_btn)
btnBorrar.grid(row=7, column=0, pady=20)

btnGuardar = tk.Button(ventana, text="Guardar Valores", command=guardar_valores, **estilo_btn)
btnGuardar.grid(row=7, column=1)

btnTema = tk.Button(ventana, text="Modo Oscuro", command=cambiar_tema, **estilo_btn)
btnTema.grid(row=8, column=0, columnspan=2, pady=5)

btnMostrar = tk.Button(ventana, text="Mostrar Datos Guardados", command=mostrar_datos_guardados, **estilo_btn)
btnMostrar.grid(row=9, column=0, columnspan=2, pady=10)

# Aplicar tema inicial
aplicar_tema()

ventana.mainloop()
