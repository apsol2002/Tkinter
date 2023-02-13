from tkinter import *

raiz = Tk()

raiz.title('Primer ventana en Python')

raiz.resizable(True,True)

# raiz.iconbitmap('la ruta al icono . ICO')

# raiz.geometry("800x600")
# la raiz se adapta al tama;o del FRAME

# raiz.config(bg='blue')

# ---------FRAME ---------------------------------------------------
miFrame = Frame()
# se crea el frame pero no tiene tamano y esta volando

# miFrame.pack(side="left", anchor="n")
# con esto se manda dentro de la raiz
# a la izquierda a la derecha.
miFrame.pack(fill="both", expand="True")

miFrame.config(bg="blue")

miFrame.config(width=800,height=600)

# --------------------------------------------------------------------
raiz.mainloop()