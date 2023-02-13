from tkinter import *
from tkinter import filedialog

root = Tk()


def abreFichero():
    fichero = filedialog.askopenfilename(title='Abrir', filetypes=(('Excel','*.xlsx'), ('Archivos PDF','*.pdf'), ('Todos los archivos','*.*')))

    print(fichero)


Button(root, text='Abre fichero', command=abreFichero).pack()

root.mainloop()
