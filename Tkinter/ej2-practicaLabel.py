from tkinter import *

mensaje = input('Ingresa un texto a mostrar')

root = Tk()

miFrame = Frame(root, width=500, height=400)
miFrame.pack()

''' --------------  FORMA 1 de trabajar con etiquetas..

miLabel = Label(miFrame, text="Hola como estás Python?")
miLabel.place(x='100',y='200')
'''

'''  -------------- FORMA 2 de trabajar con etiquetas.'''
# Solo valido si tenemos una sola etiqueta..
Label(miFrame, text=mensaje, fg='red', font=('Comic Sans MS', 18)).place(x='100',y='200')

root.mainloop()

