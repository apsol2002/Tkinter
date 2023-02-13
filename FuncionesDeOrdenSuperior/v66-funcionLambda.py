def invertir_cadena(cadena):
    return cadena[::-1]

''' Después me avivé de que podia usar 
nombre = "carlos"
nombre_al_reves = str(list(reversed(list(nombre))))
'''

def formatearMoneda(valor):

    """
    Esta funcion nos permite pasarle un numero por parametro valor
    y lo muestra en pantalla formateado de la forma x.xxx.xxx
    llegando solamente a poner el punto del millón
    """

    numero_formateado = ""
    for c in range(1, len(valor)+1):
        numero_formateado = numero_formateado + valor[-c]
        if c == 3:
            numero_formateado = numero_formateado + "." + valor[-c]
        elif c == 5:
            numero_formateado = numero_formateado + "." + valor[-c]
        elif c == 7:
            numero_formateado = numero_formateado + "." + valor[-c]

    print(invertir_cadena(numero_formateado))



''' Forma clasica en la que se declara y usa una función
def area_triangulo(base, altura):

    return (base*altura)/2


print(area_triangulo(5,8))
print(area_triangulo(2,3))
'''

area_triangulo = lambda base, altura: (base * altura) / 2

print(area_triangulo(5, 8))

triangulo1 = area_triangulo(2, 2)

print(triangulo1)

# al_cubo = lambda numero: numero ** numero

al_cubo = lambda numero: pow(numero, 3)  # n * n * n

print(al_cubo(9))

destacar_valor = lambda comision: "¡{}! $".format(comision)

print(destacar_valor(150))

print(destacar_valor(230))

formatearMoneda(input("Ingresael valor -> "))

help(formatearMoneda)

