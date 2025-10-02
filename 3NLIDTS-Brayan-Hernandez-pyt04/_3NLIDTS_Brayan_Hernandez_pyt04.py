import tkinter as tk
from tkinter import messagebox
import re

def guardar_datos():

    nombres = entry_nombres.get()  
    apellidos = entry_apellidos.get()
    edad = entry_edad.get()
    estatura = entry_estatura.get()
    telefono = entry_telefono.get()

    genero = ""
    if var_genero.get() == 1:
        genero = "Masculino"
    elif var_genero.get() == 2:
        genero = "Femenino"

    if (es_entero_valido(edad) and es_decimal_valido(estatura) and
        es_entero_valido_de_10_digitos(telefono) and es_texto_valido(nombres) and es_texto_valido(apellidos)):

        datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad} a�os\nEstatura: {estatura} cm\nTelefono: {telefono}\nGenero: {genero}"

        with open("datos_usuario.txt", "a") as archivo:
            archivo.write(datos + "\n\n")
        messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n" + datos)

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

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))


ventana = tk.Tk()
ventana.title("Formulario de Datos Personales")

var_genero = tk.IntVar()

label_nombres = tk.Label(ventana, text="Nombres:")
label_nombres.pack()
entry_nombres = tk.Entry(ventana)
entry_nombres.pack()

label_apellidos = tk.Label(ventana, text="Apellidos:")
label_apellidos.pack()
entry_apellidos = tk.Entry(ventana)
entry_apellidos.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

label_estatura = tk.Label(ventana, text="Estatura (cm):")
label_estatura.pack()
entry_estatura = tk.Entry(ventana)
entry_estatura.pack()

label_telefono = tk.Label(ventana, text="Telefono:")
label_telefono.pack()
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

label_genero = tk.Label(ventana, text="Genero:")
label_genero.pack()

rbHombre = tk.Radiobutton(ventana, text="Masculino", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Femenino", variable=var_genero, value=2)
rbMujer.pack()

btn_guardar = tk.Button(ventana, text="Guardar Datos", command=guardar_datos)
btn_guardar.pack()

btn_limpiar = tk.Button(ventana, text="Limpiar Campos", command=limpiar_campos)
btn_limpiar.pack()


ventana.mainloop()