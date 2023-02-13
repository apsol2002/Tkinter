from tkinter import *
from tkinter import messagebox

root = Tk()


# -----  Funciones para AYUDA
def salirAplicacion():
    # alor = messagebox.askquestion('Salir', 'Seguro que quieres salir del programa?') retorna yes o no
    valor = messagebox.askokcancel('Salir', 'Seguro que quieres salir del programa?')  # retorna True o False
    # if valor == 'yes':
    if valor:
        root.destroy()


def cerrarDocumento():
    valor = messagebox.askretrycancel('Reintenar', 'En éste momento no es posible cerrar el documento')
    if valor:
        cerrarDocumento()


# -----  Funciones para AYUDA
def infoAdicional():
    messagebox.showinfo("Ventana de AVISO", "Procesador de textos version 2018")


def avisoLicencia():
    messagebox.showwarning("Ventana de ALERTA", "Software bajo licencia GNU-APS")


# ----------------------------

barraMenu = Menu(root)

root.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar Ccomo')
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar', command=cerrarDocumento)
archivoMenu.add_command(label='Salir', command=salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Cortar')
archivoEdicion.add_command(label='Pegar')

archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label='Licencia', command=avisoLicencia)
archivoAyuda.add_command(label='Acerca de...', command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda, )

root.mainloop()
