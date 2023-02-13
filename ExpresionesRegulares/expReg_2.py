import re

lista_nombres = ['Ana Gómez','Andrea Trueno','Mariano Martinez','Jose Dodera','Cacho Martinez']

for elemento in lista_nombres:
    # if re.findall("^An", elemento): que comiencen con An
    if re.findall("z$", elemento) and re.findall("^An", elemento): # que terminen en z
        print(elemento)

'''
Anclas de inicio y fin
"^An"
"z$"

Patrones de busueda 
"[ñ]"
"niñ[ao]s" - retorna tanto niñas como niños
"cami[oó]n" - encuentra la palabra con y sin tilde. 

'''



