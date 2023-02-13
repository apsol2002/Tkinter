class Empleado:
    def __init__(self, nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        datos = self.nombre, self.cargo, self.salario
        return f"{datos[0]} que trabaja como {datos[1]} tiene un salario de $ {datos[2]} uruguayos"
'''
def numero_par(num):

    if (num % 2) == 0:

        return True


numeros = [10, 23, 15, 13, 47, 48, 49, 65, 60]

# cuando se pasa una funcion como parametro en este caso no lleva parentesis. sino se ejecutaría
print(list(filter(numero_par, numeros)))

'''
# --- EJEMPLO BASICO -----------------------------------------------------
numeros = [10, 23, 15, 13, 47, 48, 49, 65, 60]

print(list(filter(lambda numero_par : (numero_par % 2)==0, numeros)))

# --- EJEMPLO FILTRAR OBJETOS --------------------------------------------

lista_empleados = [
    Empleado("Carlos", "IA Ingenier", 99999),
    Empleado("Maria", "Diseñadora", 60001),
    Empleado("José", "Programador", 58000),
    Empleado("Pepe", "Reponedor", 36000),
]

salarios_altos = filter(lambda e: e.salario>60000, lista_empleados)

for e in salarios_altos:
    print(e)