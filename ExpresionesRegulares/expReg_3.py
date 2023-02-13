import re

lista_nombres = ['Ana','Pedro','María','Rosa','Sandra','Celia']

lista_codigos= ['Ma1', 'Se1', 'Ma2', 'Va1', 'MaA','MaB', 'MaC',  'Va2', 'Va3', 'Ma4', 'Ma5']

for elemento in lista_codigos:
    if re.findall('^Ma*[^2-4A-B]$', elemento):
        print(elemento)


'''

'[o-t]'
'^[O-T]'
'[o-t]$'

'^Ma[2-4]$'
'^Ma*[2-4]$'

'^Ma[^2-4]$' NEGACION DE RANGO. el que no cumple con ser de 2 a 4
'^Ma[^2-4A-B]$'
'^Ma[2-4A-B]$'

'^Ma[.:]' el tercer elemento puede ser tanto un punto como una coma.

'''