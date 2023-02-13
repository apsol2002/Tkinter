def funcionDecoradora(funcion_parametro):

    """ este es el """

    def funcionInterna(*args, **kwargs):
        print("Se va a realizar una operacion")

        funcion_parametro(*args, **kwargs)

        print("Ya se realizó la operación XD ")

    return funcionInterna


@funcionDecoradora
def suma(a, b):
    print(a + b)


@funcionDecoradora
def resta(a, b):
    print(a - b)


@funcionDecoradora
def potencia(base, exponente):
    print(pow(base,exponente))

suma(10,12)

resta(12, 43)

potencia(base=5,exponente=3)
