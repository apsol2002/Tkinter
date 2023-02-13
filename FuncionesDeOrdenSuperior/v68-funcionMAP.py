class Empleado:
    def __init__(self, nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        datos = self.nombre, self.cargo, self.salario
        return f"{datos[0]} que trabaja como {datos[1]} tiene un salario de $ {datos[2]} uruguayos"



lista_empleados = [
    Empleado("Carlos", "IA Ingenier", 99999),
    Empleado("Maria", "Diseñadora", 60001),
    Empleado("José", "Programador", 58000),
    Empleado("Pepe", "Reponedor", 36000),
]

def calculo_comision(empleado):

    if empleado.salario < 60000:

        empleado.salario = empleado.salario*1.3

    return empleado

lista_empleados_comision = map(calculo_comision,lista_empleados)

for e in lista_empleados_comision:
    print(e)