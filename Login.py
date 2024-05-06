import tkinter as tk

def iniciar_sesion():
    
    print("Iniciar sesión:")

window = tk.Tk()
window.title("Login")
window.geometry("800x500")
window.resizable(0,0)


frame_izquierda = tk.Frame(window, width=200, height=200, bg="lightblue")
frame_izquierda.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame_derecha = tk.Frame(window, width=200, height=200, bg="lightgrey")
frame_derecha.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

logo_label = tk.Label(frame_izquierda, text="Logo de la aplicación")
logo_label.pack(padx=10, pady=10)


titulo_label = tk.Label(frame_derecha, text="Inicio de Sesión", font=("Arial", 16))
titulo_label.grid(row=0, column=0, columnspan=2, padx=35, pady=25)

usuario_label = tk.Label(frame_derecha, text="Usuario:")
usuario_label.grid(row=1, column=0, padx=35, pady=25)
usuario_entry = tk.Entry(frame_derecha)
usuario_entry.grid(row=1, column=1, padx=35, pady=25)

clave_label = tk.Label(frame_derecha, text="Clave:")
clave_label.grid(row=2, column=0, padx=35, pady=25)
clave_entry = tk.Entry(frame_derecha, show="*")
clave_entry.grid(row=2, column=1, padx=35, pady=25)

btn_ingresar = tk.Button(frame_derecha, text="Ingresar", command=iniciar_sesion)
btn_ingresar.grid(row=3, column=0, columnspan=2, padx=35, pady=25)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)

window.mainloop()