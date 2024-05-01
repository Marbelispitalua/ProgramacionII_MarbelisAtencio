import tkinter as tkinter
from tkinter import messagebox

ventana = tkinter.Tk()

def registrar():
    nombre = cnombre.get()
    apellido = capellido.get()
    edad = cedad.get()
    direccion = cdireccion.get()
    telefono = ctelefono.get()
    ciudad = ciudad_listbox.get(tkinter.ACTIVE) 

    sexo = "Masculino" if var_masculino.get() == 1 else "Femenino"

    mensaje = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nCiudad: {ciudad}"
    messagebox.showwarning(title="Registro", message=mensaje)

ventana.title("MI PROGRAMITA")
ventana.geometry("400x400")
ventana.resizable(True, True)

lnombre = tkinter.Label(ventana, text="Nombre:")
lnombre.place(x=10, y=10)
cnombre = tkinter.Entry(ventana, width=30)
cnombre.place(x=70, y=10)

lapellido = tkinter.Label(ventana, text="Apellido:")
lapellido.place(x=10, y=60)
capellido = tkinter.Entry(ventana, width=30)
capellido.place(x=70, y=60)

ledad = tkinter.Label(ventana, text="Edad:")
ledad.place(x=10, y=110)
cedad = tkinter.Entry(ventana, width=30)
cedad.place(x=70, y=110)

ldireccion = tkinter.Label(ventana, text="Dirección:")
ldireccion.place(x=10, y=160)
cdireccion = tkinter.Entry(ventana, width=30)
cdireccion.place(x=70, y=160)

ltelefono = tkinter.Label(ventana, text="Teléfono:")
ltelefono.place(x=10, y=210)
ctelefono = tkinter.Entry(ventana, width=30)
ctelefono.place(x=70, y=210)

lciudad = tkinter.Label(ventana, text="Ciudad:")
lciudad.place(x=10, y=260)

ciudades = ["Cartagena", "Bogota", "Lorica"] 
ciudad_listbox = tkinter.Listbox(ventana, selectmode=tkinter.SINGLE, height=3)
for ciudad in ciudades:
    ciudad_listbox.insert(tkinter.END, ciudad)
ciudad_listbox.place(x=70, y=260)

lsexo = tkinter.Label(ventana, text="Sexo:")
lsexo.place(x=200, y=260)

var_masculino = tkinter.IntVar()
var_femenino = tkinter.IntVar()

lsexo_m = tkinter.Radiobutton(ventana, text="M", value=1, variable=var_masculino)
lsexo_m.place(x=250, y=260)
lsexo_f = tkinter.Radiobutton(ventana, text="F", value=1, variable=var_femenino)
lsexo_f.place(x=300, y=260)

registrar_b = tkinter.Button(ventana, text="Registrar", command=registrar)
registrar_b.place(x=150, y=340)

ventana.mainloop()