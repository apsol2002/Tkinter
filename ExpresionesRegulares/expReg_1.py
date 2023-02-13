import re

cadena = '''Vamos a aprender  expresiones regulares en Python.
Python es un lenguaje muy sensillo para programar.
Aguante Python.'''

textoBuscar = "Python"

''' EJ - 1
print(re.search(textoBuscar, cadena)) # retorna None en caso de no estar
'''

''' EJ - 2 
if re.search(textoBuscar, cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")
'''

''' EJ - 3  si el texto está mas de una vez muestra el ultimo..
textoEncontrado = re.search(textoBuscar, cadena)

print(textoEncontrado.start())

print(textoEncontrado.end())

print(textoEncontrado.span())
'''

'''  EJ  - 4 '''
# print(re.findall(textoBuscar,cadena))

resultado = re.findall(textoBuscar,cadena)

print("la palabra está {} veces".format(len(resultado)))
