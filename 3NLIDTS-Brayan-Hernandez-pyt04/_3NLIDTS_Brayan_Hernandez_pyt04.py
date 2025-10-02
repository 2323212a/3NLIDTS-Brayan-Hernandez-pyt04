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

    nombres = entry_nombres.get()  
    apellidos = entry_apellidos.get()
    edad = entry_edad.get()
    estatura = entry_estatura.get()
    telefono = entry_telefono.get()

def guardar_valores():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    if var_genero.get() == 1:
        genero = "Masculino"
    elif var_genero.get() == 2:
        genero = "Femenino"
    else:
        genero = "No especificado"

    datos = (
        f"Nombres: {nombres}\n"
        f"Apellidos: {apellidos}\n"
        f"Edad: {edad}\n"
        f"Estatura: {estatura}\n"
        f"Telefono: {telefono}\n"
        f"Genero: {genero}"
    )

    with open("302024Datos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")

    messagebox.showinfo("Guardado", "Los datos han sido guardados exitosamente.\n\n" + datos)
    limpiar_campos()
    else:
        messagebox.showerror("Error", "Por favor, ingrese datos validos en todos los campos.")


def limpiar_campos():
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    var_genero.set(0)


def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

ventana = tk.Tk()
ventana.geometry("520x580")
ventana.title("Formulario de Datos Personales")

var_genero = tk.IntVar()

lbNombre = tk.Label(ventana, text="Nombres:")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Telefono:")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura (m):")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Genero:")
lbGenero.pack()
rbHombre = tk.Radiobutton(ventana, text="Masculino", variable=var_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton(ventana, text="Femenino", variable=var_genero, value=2)
rbMujer.pack()

btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_fun)
btnBorrar.pack()

btnGuardar = tk.Button(ventana, "Guardar valores", command=guardar_valores)
btnGuardar.pack()

ventana.mainloop()
