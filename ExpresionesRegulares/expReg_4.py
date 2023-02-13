import re

n1 = "Sandra López"
n2 = "Carlos Gómez"
n3 = " er e 12345678 er ter "

if re.search("*\d", n2, re.IGNORECASE):
    print("Se encontó la coincidencia")
else:
    print("No se encontró la coinciden")


'''
".dra"  NO ME FUNCIONA ...

"\d" permite buscar un numero el inicio con MATCH


'''