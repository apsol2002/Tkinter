import tkinter
from tkinter import *

root = Tk()

miFrame = Frame(root)
miFrame.pack()

# ------------------------------------------------------------
textoCaja = StringVar()
valor1 = 0
valor2 = 0
operador = ''

# ------------------------------------------------------------

def codigoBoton(valor):
    texto = textoCaja.get()
    textoCaja.set(texto + valor)

def suma():
    global valor1
    valor1 = int(textoCaja.get())

    textoCaja.set('')

    global operador
    operador = 'suma'

    print(f"Valor 1 {valor1} y operador es {operador}")

def igual():
        global valor2
        valor2 = int(textoCaja.get())

        global operador

        print(f"Valor 1 {valor1},  valor 2 {valor2} y operador es {operador}")
        algo = valor1 + valor2
        textoCaja.set(str(algo))


# ---------------PANTALLA-----------------
pantalla = Entry(miFrame, textvariable=textoCaja)
pantalla.grid(row=1, column=1, pady=10, padx=10, columnspan=4)
pantalla.config(background='black', fg='#03f943', justify=tkinter.RIGHT)

# ---------------FILA 1-----------------

boton7 = Button(miFrame, text='7', width=3, command=lambda:codigoBoton('7'))
boton7.grid(row=2, column=1)

boton8 = Button(miFrame, text='8', width=3, command=lambda:codigoBoton('8'))
boton8.grid(row=2, column=2)

boton9 = Button(miFrame, text='9', width=3, command=lambda:codigoBoton('9'))
boton9.grid(row=2, column=3)

botonDiv = Button(miFrame, text='/', width=3)
botonDiv.grid(row=2, column=4)

# ---------------Fila 2 -----------------

boton4 = Button(miFrame, text='4', width=3, command=lambda:codigoBoton('4'))
boton4.grid(row=3, column=1)

boton5 = Button(miFrame, text='5', width=3, command=lambda:codigoBoton('5'))
boton5.grid(row=3, column=2)

boton6 = Button(miFrame, text='6', width=3, command=lambda:codigoBoton('6'))
boton6.grid(row=3, column=3)

botonMult = Button(miFrame, text='*', width=3)
botonMult.grid(row=3, column=4)

# ---------------Fila 3-----------------

boton1 = Button(miFrame, text='1', width=3, command=lambda:codigoBoton('1'))
boton1.grid(row=4, column=1)

boton2 = Button(miFrame, text='2', width=3, command=lambda:codigoBoton('2'))
boton2.grid(row=4, column=2)

boton3 = Button(miFrame, text='3', width=3, command=lambda:codigoBoton('3'))
boton3.grid(row=4, column=3)

botonMenos = Button(miFrame, text='-', width=3)
botonMenos.grid(row=4, column=4)

# ---------------PANTALLA-----------------

boton0 = Button(miFrame, text='0', width=3, command=lambda:codigoBoton('0'))
boton0.grid(row=5, column=1)

botonIgual = Button(miFrame, text='=', width=8, command=igual)
botonIgual.grid(row=5, column=2, columnspan=2, )

botonMas = Button(miFrame, text='+', width=3, command=suma)
botonMas.grid(row=5, column=4)

# ---------------PANTALLA-----------------
root.mainloop()
