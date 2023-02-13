from tkinter import *

root = Tk()

varRadio = IntVar()
varCheckUruguay = IntVar()
varCheckArgentina = IntVar()
varCheckBrazil = IntVar()

varPaises = StringVar()


def usoRadio():
    if varRadio.get() == 1:
        print("Masculino")
    elif varRadio.get() == 2:
        print("Femenino")
    else:
        print("Otro")


def usoCheck():
    texto = ""
    if varCheckUruguay.get() == 1:
        texto += " Uruguay "
    if varCheckArgentina.get() == 1:
        texto += " Argentina "
    if varCheckBrazil.get() == 1:
        texto += " Brazil "

    varPaises.set(texto)

Label(root, text="Selecciona una opción").pack()

Radiobutton(root, text="Masculino", variable=varRadio, value=1, command=usoRadio).pack()
Radiobutton(root, text="Femenino", variable=varRadio, value=2, command=usoRadio).pack()
Radiobutton(root, text="Otro", variable=varRadio, value=3, command=usoRadio).pack()

Label(root, text="").pack()

Label(root, text="Selecciona un Pais.").pack()

Checkbutton(root, text="Uruguay", variable=varCheckUruguay, onvalue=1, offvalue=0, command=usoCheck).pack()
Checkbutton(root, text="Argentina", variable=varCheckArgentina, onvalue=1, offvalue=0, command=usoCheck).pack()
Checkbutton(root, text="Brazil", variable=varCheckBrazil, onvalue=1, offvalue=0, command=usoCheck).pack()

Label(root, text="").pack()
textoFinal = Label(root, textvariable=varPaises)
textoFinal.pack()
Label(root, text="").pack()

mainloop()
