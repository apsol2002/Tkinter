import tkinter
from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=400)
miFrame.pack()

# ------------------------------------------------------------
miNombre = StringVar()
# ------------------------------------------------------------

labelNombre = Label(miFrame, text="Nombre")
labelNombre.grid(row=0, column=0, padx=10, pady=10)

labelPass = Label(miFrame, text="Password")
labelPass.grid(row=1, column=0, padx=10, pady=10)

labelApellido = Label(miFrame, text="Apellido")
labelApellido.grid(row=2, column=0, padx=10, pady=10)

labelDireccion = Label(miFrame, text="Direccion")
labelDireccion.grid(row=3, column=0, padx=10, pady=10)

labelComentarios = Label(miFrame, text="Cometarios")
labelComentarios.grid(row=4, column=0, padx=10, pady=10)

# ------------------------------------------------------------

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg='red', justify=tkinter.CENTER)

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=1, column=1, padx=10, pady=10)
cuadroPassword.config(show='*', justify=tkinter.CENTER)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(justify=tkinter.CENTER)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)
cuadroDireccion.config(justify=tkinter.CENTER)

# ------------------------------------------------------------

textoComentarios = Text(miFrame, width=16, height=5)
textoComentarios.grid(row=4, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textoComentarios.yview())
scrollVert.grid(row=4, column=2, sticky='nsew', padx=10, pady=10)

textoComentarios.config(yscrollcommand=scrollVert.set)  # se pone abajo porque sino no es accesible ...


# ------------------------------------------------------------

def codigoBoton():
    miNombre.set("Carlos")


botonEnvío = Button(root, text="Enviar", command=codigoBoton)
botonEnvío.pack()

root.mainloop()
